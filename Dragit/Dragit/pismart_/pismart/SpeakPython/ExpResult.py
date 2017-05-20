from BaseResult import BaseResult;

class ExpResult(BaseResult):

    lexp = None;
    rexp = None;
    op = None;

    def __init__(self, lexp, op, rexp):
        self.lexp = lexp;
        self.op = op;
        self.rexp = rexp;

    def getResultString(varList):
        lval = int(self.lexp.getResultString(varList));
        rval = int(self.rexp.getResultString(varList));
        if op == '+':
            return str(lval + rval);
        elif op == '-':
            return str(lval - rval);
        elif op == '*':
            return str(lval * rval);
        elif op == '/':
            return str(lval / rval);

        print "Error, could not match operator.";
        return "Error: Could not match operator.";
            
