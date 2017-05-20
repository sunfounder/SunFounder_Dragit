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

from BaseResult import BaseResult;

import copy;

class KleeneResult(BaseResult):

	kNum = '';
	delim = [];
	resultList = [];

        addExtraDelim = False;

	def __init__(self, kNum, delim, resultList):
		#allow delimiter to be a mix of vars, strings and functions
		self.kNum = kNum;
		self.delim = delim;
		self.resultList = resultList;

	def getResultString(self, varList):
		retStr = '';
		delimStr = '';

		finished = False;

                #copy kleene variables to allow recursive kleene results
                kleeneVars = copy.deepcopy(varList[self.kNum]);

                #add all variables outside of kleene that don't exist within kleene
                for var in varList:
                    if var not in kleeneVars:
                        if isinstance(varList[var], list) or isinstance(varList[var], dict):
                            kleeneVars[var] = copy.deepcopy(varList[var]);
                        else:
                            kleeneVars[var] = varList[var];
                
                #keep tacking on results until we reach a None result
		while not finished:

			delimStr = '';
                        #print kleeneVars;

			#form the result string from list of results
			for result in self.resultList:
#				print varList[self.kNum];	
				#try to get the result, stop if there's no more result
				r = result.getResultString(kleeneVars);
				if r != None:
					retStr += r;
				else:
					finished = True;
                                        break;

                        #recompute the delimiter because it's possible that the delimeter changes depending on if it uses up its results or not (like another kleene)
			for d in self.delim:
				retDelim = d.getResultString(kleeneVars);
				if retDelim != None:
					delimStr += retDelim;
				else:
					finished = True;
                                        break;

			#add the delim, then loop
			retStr += delimStr;

                removalCount = 2;
                if self.addExtraDelim:
                    removalCount = 1;

		retStr = retStr[:(-removalCount*len(delimStr))]; #remove the last added delim

		return retStr;
