from BaseResult import BaseResult;

class StringResult(BaseResult):

	string = '';

	def __init__(self, string):
		self.string = string;

	def getResultString(self, varList):
		return self.string;
