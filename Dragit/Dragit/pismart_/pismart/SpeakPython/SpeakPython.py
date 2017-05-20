#SpeakPython allows developers to add speech recognition support to their Python applications
#Copyright (C) 2015  Eric Matthews

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by 
#the Free Software Foundation, either version 3 of the License, or 
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of 
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import re
import pickle
import sqlite3

import sys
import os.path

from Result import Result

class SpeakPython(object):

	db = '';
	functionNameStack = [];
	ruleID = 0;

	DEBUG_VAL = 3;

	def __init__(self, database, DEBUG=3):
		self.db = database;
		self.DEBUG_VAL = 3;
		self.DEBUG_VAL = DEBUG;

		if not os.path.isfile(self.db):
			self.debugMsg(self.db + " does not exist.", 10);

	def debugMsg(self, msg, severity):
		if self.DEBUG_VAL <= severity:
                    print "DEBUG(" + str(severity) + "): SpeakPython.py: " + str(msg) + "\n";

	#returns the best-matched result out of the labels of matched regexes
	def getBestResult(self, results, varDict):

		#for each result, find the first result that is covered by the variable dictionary (since results are sorted from longest set of labels to smallest)
		for result in results:
			if result.isCoveredBy(varDict):
				result.setVariables(varDict);
				return result;

		return None;

	#gets the value of a g_# variable if exists
	#input:
	#g - current variable
	#matchGroupDict - dictionary of variable matches from regex
	#output: string value of the g_# variable or None if not g_#
	def getExpandedNums(self, g, matchGroupDict):
		#check numbered groups
		m = re.match(r'g_([0-9]+)', g);
		if m != None:
			newG = m.group(1);
			return [(newG, matchGroupDict[g])];

		return [(g, None)];

	def getResultForFunction(self, cursor, g, groupDict, funcName):
		funcVarDict = {}

		#for each key in matchGroup that matches the current function	
		for key in groupDict:

			#get the expanded form of the variable (if it is another function, this will recurse to this function to find the result of that function)
			subResults = self.getExpandedForm(cursor, key, groupDict);
			for (subKey, subResult) in subResults:
				#if there aren't any recorded variables, pop recorded variables and continue
				if subResult == None:
					continue;
				else:
					funcVarDict[subKey] = subResult;

			#print "funcVarDict: " + str(funcVarDict);

		#load results from db by function name
		funcResults = cursor.execute("SELECT results FROM functions WHERE name=?", [funcName]);
		funcResults = pickle.loads(cursor.fetchone()[0]);

		#find the result based on the function's result coverage (just like a match) default to raw regex match
		resultStr = groupDict[g];

		#get the function result that best matches the labels
		result = self.getBestResult(funcResults, funcVarDict);

		if result != None:
			resultStr = result.getResult();

		return resultStr;

	#gets the value of a function variable if exists, returns the value
	#input:
	#cursor - allows query of function results
	#g - current variable
	#matchGroupDict - dictionary of variable matches from regex (with previous function paths removed)
	#		therefore, only variables relating to this function
	#
	#output: string value of the function variable after evaluation, None if not a function variable
	def getExpandedFunctions(self, cursor, g, matchGroupDict):
		#check function groups
		#find functions of the form "_{name}_{num}_" and simplify them for the result lists
		m = re.match(r'_([a-zA-Z]+)_([0-9]+)_(.*)', g);
		if m != None:
			funcName = m.group(1);
			funcNum = m.group(2);
			newG = m.group(3)

			localizedDict = {};

			#key is a function variable
			#create copy of dictionary terms prefixed by function
			#remove function prefix from those terms
			for key in matchGroupDict:
				#if key is function variable
				m = re.match('_' + funcName + '_' + funcNum + '_(.*)', key);
				if m != None:
					globalVarName = m.group(0);
					localVarName = m.group(1);
					localizedDict[localVarName] = matchGroupDict[globalVarName];

			#keep a stack record of function names
			self.functionNameStack.append(funcName);
	
			#get result of function
			functionResult = self.getResultForFunction(cursor, newG, localizedDict, funcName);

			#remove function name from stack
			self.functionNameStack.pop();

			#return so as not to record function as variable
			return [(funcName, functionResult), (funcName + "_" + funcNum, functionResult)];

		return [(g, None)];

	#gets the value of a variable if exists, returns the value
	#input:
	#g - current variable
	#matchGroupDict - dictionary of variable matches from regex (with previous function paths removed)
	#		therefore, only variables relating to current function in the stack matter
	#output: string value of the variable, None if not a variable
	def getExpandedVars(self, g, matchGroupDict):
		m = re.match('[a-zA-Z0-9]+', g);
		if m != None:
			return [(g, matchGroupDict[g])];

		return [(g, None)];

	#using a cursor and an index, we get the regex associated with the function or matchID from DB and return it
	def getKleeneRegex(self, c, index):
		kGroupRegexes = {};

		c.execute("SELECT regexes FROM kleene WHERE id=?", [(index)])
		kMatch = c.fetchone();
		if kMatch != None:
			kGroupRegexes = pickle.loads(kMatch[0]);
		else:
			kGroupRegexes = {};

		return kGroupRegexes;
	
	#gets the values of a kleene if exists, returns the value
	#input:
	#g - current variable
	#cursor - used to query database
	#matchGroupDict - dictionary of variable matches from regex (with previous function paths removed)
	#		therefore, only variables relating to current function in the stack matter
	#output: a dictionary containing all the localized variables within the kleene, None if not a kleene
	def getExpandedKleene(self, cursor, g, matchGroupDict):

		#see if it is a kleene variable
		m = re.match(r'k_([0-9]+)', g);
		if m != None:
			kNum = m.group(1);

			#get all that was matched by kleene in regex
			rawMatchStr = matchGroupDict[g];			

			#find the regex inside kleene, from database table kleene, that was used to get the rawMatchStr
			#see if we should use function kleene or match kleene and handle appropriately
			if len(self.functionNameStack) > 0:
				funcName = self.functionNameStack[-1];
				funcKleeneRegexes = self.getKleeneRegex(cursor, funcName);
				innerRegex = funcKleeneRegexes[kNum];
			else:
				innerRegex = self.getKleeneRegex(cursor, self.ruleID)[kNum];

			#use the inner regex multiple times to retrieve a list of results used for each variable
			retDict = {};
			if innerRegex != None:

				origInnerRegex = innerRegex;

				delim = " /,";

				#alter innerRegex to match spaces so as to get rid of them in next iteration
				innerRegex = origInnerRegex + "[" + delim + "]*";

				#search for the regex multiple times within the string
				#shorten the string each iteration by what was previously matched
				kMatch = re.match(innerRegex, rawMatchStr);
				while (kMatch != None):
					innerVars	= kMatch.groupdict();

					#get raw match string
					innerMatchStr = kMatch.group(0);

					#print "innerVars: " + str(innerVars);

					kleeneDict = {};

					#for each variable of the inner regex, expand it to its proper form (functions turn into function results, kleene are recursed, etc)
					for var in innerVars:
						keyValues = self.getExpandedForm(cursor, var, innerVars);
						for key, value in keyValues:
							kleeneDict[key] = value;

					#print "kleeneDict: " + str(kleeneDict);

					#accumulate each variable in the kleene into a list of those variables' values
					#this accumulation is retDict
					for var in kleeneDict:
						if var in retDict:
							retDict[var].append( kleeneDict[var] );
						else:
							retDict[var] = [ kleeneDict[var] ];

					#cut off previous match from string, and re-search the regex
					rawMatchStr = rawMatchStr[len(innerMatchStr):];
					kMatch = re.match(innerRegex, rawMatchStr);
	
			return [(g, retDict)];

		return [(g, None)];

	def getExpandedRegexes(self, g, matchGroupDict):
		#see if it is a regex variable
		m = re.match(r'r_([0-9]+)', g);
		if m != None:
			return [(g, matchGroupDict[g])];

		return [(g, None)];

	def validResult(self, ret):
		return len(ret) > 0 and ret[0][1];

	def getExpandedForm(self, cursor, g, matchGroupDict):

		#remove all None or empty regex group matches
		val = matchGroupDict[g];
		if val == '' or val == None:
			return [(g, None)];

		#expand and get result list
		ret = self.getExpandedNums(g, matchGroupDict);
		if self.validResult(ret):
			return ret;

		ret = self.getExpandedKleene(cursor, g, matchGroupDict);
		if self.validResult(ret):
			return ret;

		ret = self.getExpandedFunctions(cursor, g, matchGroupDict);
		if self.validResult(ret):
			return ret;

		ret = self.getExpandedVars(g, matchGroupDict);
		if self.validResult(ret):
			return ret;

		ret = self.getExpandedRegexes(g, matchGroupDict);
		if self.validResult(ret):
			return ret;

		return [(g, None)];

	def init(self):
		self.functionNameStack = [];

	#returns a result that best matches the regex
	def matchResult(self, inStr):
		self.init();

		conn = sqlite3.connect(self.db);
		c = conn.cursor();

		#parse out keyword to search in DB
		if ' ' in inStr:
			keyword = inStr[:(inStr.find(' '))];
		else:
			keyword = inStr;
		keyword = keyword.lower();

		self.debugMsg("Keyword: " + keyword, 2);

		matches = c.execute("SELECT order_id, regex, results FROM matches WHERE keywords LIKE '%'||?||'%' OR keywords LIKE '%*%' ORDER BY order_id", [keyword]);

		longestResult = None;
		longestResultLen = 0;

		#for each match, find the match result that covers the most labels of all match regexes that the input fits
		for match in matches:
			matchID = match[0];
			regex = match[1];

			self.ruleID = matchID;

			#match regex and get capture groups
			m = re.match(regex, inStr);
		
			#regex doesn't match, stop
			if m == None:
				continue;

			#regex matches, get groups
			self.debugMsg(regex, 1);

			matchGroupDict = m.groupdict();
			groupDict = {};

			self.debugMsg("raw matches: " + str(matchGroupDict), 1);

			#get the expanded form of a variable/function for use as a result label
			for g in matchGroupDict:
				keyValues = self.getExpandedForm(c, g, matchGroupDict);
				for (key, value) in keyValues:
					if value != None:
						groupDict[key] = value;

			results = match[2]; #load pickled results from db
			results = pickle.loads(results); #unpickle them

			self.debugMsg("processed variables: " + str(groupDict), 1)

			#for each result, see if match covers the label, find the match-result pair that covers the most labels
			bestResult = self.getBestResult(results, groupDict);

			#for each top-level match
			#see which phrase match result has the largest amount of labels. Keep that one.
			if bestResult != None:
				if longestResultLen < len(bestResult.labels):
					longestResult = bestResult;
					longestResultLen = len(bestResult.labels);

		return longestResult;
