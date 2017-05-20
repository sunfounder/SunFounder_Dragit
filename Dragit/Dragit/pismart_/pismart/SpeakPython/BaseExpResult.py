from BaseResult import BaseResult;
from abc import ABCMeta, abstractmethod;

class BaseExpResult(BaseResult):
    __metaclass__ = ABCMeta;

    @abstractmethod
    def getResultString(varList):
        print "BaseExpResult";
        pass;

    @abstractmethod
    def getExpResult():
        print "Exp Result";
        pass;
