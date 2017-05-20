from BaseResult import BaseResult;

class VarResult(BaseResult):

	varName = '';

	def __init__(self, varName):
		self.varName = varName;

	def getResultString(self, varList):
		if not self.varName in varList:
			print "Error (VarResult): variable (" + self.varName + ") is not in the variable list.";
			return '';

		#if list, pop first item, if empty, return None
		if isinstance(varList[self.varName], list):
                        #print varList;
			if len(varList[self.varName]) > 0:
				return varList[self.varName].pop(0);
			else:
				return None;
		else:
			pass;

		#return an ordinary variable value
		return varList[self.varName];
