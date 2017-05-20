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

import re;

class Result(object):

	labels = [];
	results = [];
	variables = {}

	def __init__(self, labels, results):
		self.labels = labels;
		self.results = results;

	def getResult(self, captureGroupDict=None):
		#use default variables if none defined (allows for user-altered variables)
		if captureGroupDict == None:
			captureGroupDict = self.variables;
		else:
			self.setVariables(captGroupDict);
	
		#form result out of the list of results
		r = '';
		for result in self.results:
				r += result.getResultString(self.variables);

		return r;

	#returns true if each dictionary
	def isCoveredBy(self, captGroupDict):
		for l in self.labels:
			if (not (l in captGroupDict)):
				return False;

		return True;

	def getVariables(self):
		return self.variables;
	
	#set re-defined variables to their new values	
	def setVariables(self, varDict):
		self.variables = varDict;
