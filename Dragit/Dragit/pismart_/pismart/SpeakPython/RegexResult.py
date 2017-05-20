from BaseResult import BaseResult;

import re;

class RegexResult(BaseResult):

	regexNum = "0";
	regex = "";
	captureName = None;

	def __init__(self, regex, regexNum, captureName=None):
		self.regex = regex;
		self.regexNum = regexNum;
		self.captureName = captureName;

	def getResultString(self, varList):
		if varList == None:
			print "varList found as None in RegexResult";
			return "";

		key = "r_" + self.regexNum;

		if key in varList:
			#looking for entire capture, return entire result
			if self.captureName == None:
				return varList[key];
			#looking for specific captured sub-group, return sub-group result
			else:
				#use regex to collect capture groups
				matches = re.match(self.regex, varList[key]);
				regexMatchDict = matches.groupdict();

				#utilize the capture group specified in .sps
				#    ex. r_0('animal'), 'animal' is the capture group's name
				if self.captureName in regexMatchDict:
					return regexMatchDict[self.captureName];
				else:
					print "No group captured in regex /" + self.regex + "/r for capture group name " + self.captureName;
					return "";
		
		print key + " does not exist in varList";
		return "";
