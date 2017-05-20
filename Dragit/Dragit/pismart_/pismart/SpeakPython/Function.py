from Result import Result;

class Function(object):

	funcName = '';
	testCases = [];
	exp = '';
	results = [];
	kGroupRegexes = [];

	def __init__(self, name, exp, testCases, kGroupRegexes, results):
		self.funcName = name;
		self.testCases = testCases;
		self.exp = exp;
		self.results = results;
		self.kGroupRegexes = kGroupRegexes;
		print kGroupRegexes;

	def getName(self):
		return self.funcName;

	def getExp(self):
		return self.exp;

	def getResults(self):
		return self.results;
