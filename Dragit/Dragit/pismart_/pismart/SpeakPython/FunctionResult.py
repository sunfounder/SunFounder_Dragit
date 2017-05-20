from BaseResult import BaseResult;

class FunctionResult(BaseResult):

	funcName = '';

	def __init__(self, funcName):
		self.funcName = funcName;

	def getResultString(self, varList):
		if not self.funcName in varList:
			print "FuncResult Error: variable (" + self.funcName + ") is not in the variable list.";
			return None;

		#if list, pop first item, if empty, return None 
                if isinstance(varList[self.funcName], list): 
                        #print varList; 
                        if len(varList[self.funcName]) > 0: 
                                return varList[self.funcName].pop(0); 
                        else: 
                                return None; 
                else: 
                        pass;

		return varList[self.funcName];
