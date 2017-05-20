from abc import ABCMeta, abstractmethod;

class BaseResult(object):
	__metaclass__ = ABCMeta;

	@abstractmethod
	def getResultString(varList):
		print "base result";
		pass;
