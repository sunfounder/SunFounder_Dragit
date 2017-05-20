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

class Match(object):

	exp = ''; #the regex describing the desired string
	testCases = [];
	results = []; #list of Result() objects 
	keywords = [];
	kGroupRegexes = [];

	def __init__(self, exp, testCases, keywords, kGroupRegexes, results):
		self.exp = exp;
		self.testCases = testCases;
		self.keywords = keywords;
		self.kGroupRegexes = kGroupRegexes;
		self.results = results;

#this function is for matching "?P<*>" to insert actual group numbers into the named groups 
class GroupCounter():
	count = -1;

	def __init__(self, start=0):
		self.count = start-1;

	def __call__(self, match):
		self.count += 1;
		return "?P<{}>".format("g_" + str(self.count));
