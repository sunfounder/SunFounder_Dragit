# $ANTLR 3.4 SpeakPythonJSGF.g 2015-09-25 20:19:04

import sys
from antlr3 import *
from antlr3.compat import set, frozenset



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
ARROW=4
AT=5
AT_GLOBAL_OPTIONS=6
AT_OPTIONS=7
AT_RESULTS=8
AT_TESTS=9
B_ARROW=10
COMMA=11
COMMENT=12
END_DQUOTE_STRING=13
END_SQUOTE_STRING=14
EQ=15
HASH_NAME=16
INSIDE_DQUOTE_STRING=17
INSIDE_SQUOTE_STRING=18
KLEENE=19
LA_BR=20
LC_BR=21
LR_BR=22
LS_BR=23
NEWLINE=24
NUM=25
OR=26
PLUS=27
QSTN=28
QUOTE_STRING=29
RA_BR=30
RC_BR=31
REGEX=32
REGEX_LABEL=33
RR_BR=34
RS_BR=35
SEMI=36
STAR=37
START_DQUOTE_STRING=38
START_SQUOTE_STRING=39
TILDE=40
UNDERSCORE_NUM=41
VAR_NAME=42
WHITE_SPACE=43
WORD=44

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ARROW", "AT", "AT_GLOBAL_OPTIONS", "AT_OPTIONS", "AT_RESULTS", "AT_TESTS", 
    "B_ARROW", "COMMA", "COMMENT", "END_DQUOTE_STRING", "END_SQUOTE_STRING", 
    "EQ", "HASH_NAME", "INSIDE_DQUOTE_STRING", "INSIDE_SQUOTE_STRING", "KLEENE", 
    "LA_BR", "LC_BR", "LR_BR", "LS_BR", "NEWLINE", "NUM", "OR", "PLUS", 
    "QSTN", "QUOTE_STRING", "RA_BR", "RC_BR", "REGEX", "REGEX_LABEL", "RR_BR", 
    "RS_BR", "SEMI", "STAR", "START_DQUOTE_STRING", "START_SQUOTE_STRING", 
    "TILDE", "UNDERSCORE_NUM", "VAR_NAME", "WHITE_SPACE", "WORD"
]




class SpeakPythonJSGFParser(Parser):
    grammarFileName = "SpeakPythonJSGF.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(SpeakPythonJSGFParser, self).__init__(input, state, *args, **kwargs)




        self.delegates = []





    optionVals = {};
    optionValsBackup = optionVals;

    rules = [];
    aliasRules = {};

    parseFailed = False;
    messages = {'regex': "We're sorry, regex is not supported in JSGF at this time",
    		'variable': "We're sorry, variables are not supported in JSGF at this time"};



    # $ANTLR start "prog"
    # SpeakPythonJSGF.g:47:1: prog : s EOF ;
    def prog(self, ):

        self.optionVals['wordRegex'] = '[a-zA-Z0-9_\\+\\.\\-]+';
        self.optionVals['varRegex'] = '[a-zA-Z0-9_\\+\\.\\-]+';
        self.optionVals['wordDelim'] = '[ ,/]+';

        try:
            try:
                # SpeakPythonJSGF.g:54:2: ( s EOF )
                # SpeakPythonJSGF.g:54:4: s EOF
                pass 
                self._state.following.append(self.FOLLOW_s_in_prog51)
                self.s()

                self._state.following.pop()

                self.match(self.input, EOF, self.FOLLOW_EOF_in_prog53)

                if self._state.backtracking == 0:
                    pass






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "prog"



    # $ANTLR start "s"
    # SpeakPythonJSGF.g:57:1: s : ( alias s | mat s | globalOptions s |);
    def s(self, ):
        mat1 = None




        try:
            try:
                # SpeakPythonJSGF.g:61:2: ( alias s | mat s | globalOptions s |)
                alt1 = 4
                LA1 = self.input.LA(1)
                if LA1 == HASH_NAME:
                    LA1_1 = self.input.LA(2)

                    if (LA1_1 == LR_BR) :
                        LA1_5 = self.input.LA(3)

                        if (LA1_5 == RR_BR) :
                            alt1 = 1
                        elif (LA1_5 == HASH_NAME or (LR_BR <= LA1_5 <= LS_BR) or LA1_5 == REGEX or LA1_5 == VAR_NAME or LA1_5 == WORD) :
                            alt1 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 1, 5, self.input)

                            raise nvae


                    elif (LA1_1 == HASH_NAME or LA1_1 == LS_BR or LA1_1 == OR or LA1_1 == REGEX or LA1_1 == SEMI or LA1_1 == VAR_NAME or LA1_1 == WORD) :
                        alt1 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 1, 1, self.input)

                        raise nvae


                elif LA1 == AT_OPTIONS or LA1 == LR_BR or LA1 == LS_BR or LA1 == REGEX or LA1 == VAR_NAME or LA1 == WORD:
                    alt1 = 2
                elif LA1 == AT_GLOBAL_OPTIONS:
                    alt1 = 3
                elif LA1 == EOF:
                    alt1 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 1, 0, self.input)

                    raise nvae


                if alt1 == 1:
                    # SpeakPythonJSGF.g:61:4: alias s
                    pass 
                    self._state.following.append(self.FOLLOW_alias_in_s71)
                    self.alias()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass



                    self._state.following.append(self.FOLLOW_s_in_s75)
                    self.s()

                    self._state.following.pop()


                elif alt1 == 2:
                    # SpeakPythonJSGF.g:62:4: mat s
                    pass 
                    self._state.following.append(self.FOLLOW_mat_in_s81)
                    mat1 = self.mat()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        self.rules.append(mat1); 



                    self._state.following.append(self.FOLLOW_s_in_s85)
                    self.s()

                    self._state.following.pop()


                elif alt1 == 3:
                    # SpeakPythonJSGF.g:63:4: globalOptions s
                    pass 
                    self._state.following.append(self.FOLLOW_globalOptions_in_s91)
                    self.globalOptions()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_s_in_s93)
                    self.s()

                    self._state.following.pop()


                elif alt1 == 4:
                    # SpeakPythonJSGF.g:64:4: 
                    pass 
                    if self._state.backtracking == 0:
                        pass





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "s"



    # $ANTLR start "globalOptions"
    # SpeakPythonJSGF.g:67:1: globalOptions : AT_GLOBAL_OPTIONS myOptions AT ;
    def globalOptions(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:68:2: ( AT_GLOBAL_OPTIONS myOptions AT )
                # SpeakPythonJSGF.g:68:4: AT_GLOBAL_OPTIONS myOptions AT
                pass 
                self.match(self.input, AT_GLOBAL_OPTIONS, self.FOLLOW_AT_GLOBAL_OPTIONS_in_globalOptions109)

                self._state.following.append(self.FOLLOW_myOptions_in_globalOptions111)
                self.myOptions()

                self._state.following.pop()

                self.match(self.input, AT, self.FOLLOW_AT_in_globalOptions113)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "globalOptions"



    # $ANTLR start "localOptions"
    # SpeakPythonJSGF.g:71:1: localOptions : AT_OPTIONS myOptions AT ;
    def localOptions(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:72:2: ( AT_OPTIONS myOptions AT )
                # SpeakPythonJSGF.g:72:4: AT_OPTIONS myOptions AT
                pass 
                self.match(self.input, AT_OPTIONS, self.FOLLOW_AT_OPTIONS_in_localOptions124)

                if self._state.backtracking == 0:
                    pass
                    self.optionValsBackup = self.optionVals; self.optionVals = self.optionValsBackup.copy(); 



                self._state.following.append(self.FOLLOW_myOptions_in_localOptions128)
                self.myOptions()

                self._state.following.pop()

                self.match(self.input, AT, self.FOLLOW_AT_in_localOptions130)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "localOptions"



    # $ANTLR start "myOptions"
    # SpeakPythonJSGF.g:75:1: myOptions : ( myOption myOptions |);
    def myOptions(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:76:2: ( myOption myOptions |)
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == WORD) :
                    alt2 = 1
                elif (LA2_0 == EOF or LA2_0 == AT) :
                    alt2 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae


                if alt2 == 1:
                    # SpeakPythonJSGF.g:76:4: myOption myOptions
                    pass 
                    self._state.following.append(self.FOLLOW_myOption_in_myOptions141)
                    self.myOption()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_myOptions_in_myOptions143)
                    self.myOptions()

                    self._state.following.pop()


                elif alt2 == 2:
                    # SpeakPythonJSGF.g:77:4: 
                    pass 
                    if self._state.backtracking == 0:
                        pass





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "myOptions"



    # $ANTLR start "myOption"
    # SpeakPythonJSGF.g:80:1: myOption : WORD EQ ( RA_BR )? REGEX ( SEMI )? ;
    def myOption(self, ):
        WORD2 = None
        REGEX3 = None

        try:
            try:
                # SpeakPythonJSGF.g:81:2: ( WORD EQ ( RA_BR )? REGEX ( SEMI )? )
                # SpeakPythonJSGF.g:81:4: WORD EQ ( RA_BR )? REGEX ( SEMI )?
                pass 
                WORD2 = self.match(self.input, WORD, self.FOLLOW_WORD_in_myOption159)

                self.match(self.input, EQ, self.FOLLOW_EQ_in_myOption161)

                # SpeakPythonJSGF.g:81:12: ( RA_BR )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == RA_BR) :
                    alt3 = 1
                if alt3 == 1:
                    # SpeakPythonJSGF.g:81:13: RA_BR
                    pass 
                    self.match(self.input, RA_BR, self.FOLLOW_RA_BR_in_myOption164)




                REGEX3 = self.match(self.input, REGEX, self.FOLLOW_REGEX_in_myOption168)

                # SpeakPythonJSGF.g:81:27: ( SEMI )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == SEMI) :
                    alt4 = 1
                if alt4 == 1:
                    # SpeakPythonJSGF.g:81:28: SEMI
                    pass 
                    self.match(self.input, SEMI, self.FOLLOW_SEMI_in_myOption171)




                if self._state.backtracking == 0:
                    pass
                    self.optionVals[WORD2.text] = REGEX3.text[1:-2]; 






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "myOption"



    # $ANTLR start "mat"
    # SpeakPythonJSGF.g:85:1: mat returns [matR] : ( localOptions )? exps statementFields ;
    def mat(self, ):
        matR = None


        exps4 = None




        try:
            try:
                # SpeakPythonJSGF.g:89:2: ( ( localOptions )? exps statementFields )
                # SpeakPythonJSGF.g:89:4: ( localOptions )? exps statementFields
                pass 
                # SpeakPythonJSGF.g:89:4: ( localOptions )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == AT_OPTIONS) :
                    alt5 = 1
                if alt5 == 1:
                    # SpeakPythonJSGF.g:89:5: localOptions
                    pass 
                    self._state.following.append(self.FOLLOW_localOptions_in_mat198)
                    self.localOptions()

                    self._state.following.pop()




                self._state.following.append(self.FOLLOW_exps_in_mat202)
                exps4 = self.exps()

                self._state.following.pop()

                if self._state.backtracking == 0:
                    pass
                    self.optionVals = self.optionValsBackup; 



                self._state.following.append(self.FOLLOW_statementFields_in_mat211)
                self.statementFields()

                self._state.following.pop()

                if self._state.backtracking == 0:
                    pass
                    matR =  exps4 






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return matR

    # $ANTLR end "mat"



    # $ANTLR start "statementFields"
    # SpeakPythonJSGF.g:95:1: statementFields : ( AT_RESULTS mResults AT statementFields | AT_TESTS testCases AT statementFields |);
    def statementFields(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:96:2: ( AT_RESULTS mResults AT statementFields | AT_TESTS testCases AT statementFields |)
                alt6 = 3
                LA6 = self.input.LA(1)
                if LA6 == AT_RESULTS:
                    alt6 = 1
                elif LA6 == AT_TESTS:
                    alt6 = 2
                elif LA6 == EOF or LA6 == AT_GLOBAL_OPTIONS or LA6 == AT_OPTIONS or LA6 == HASH_NAME or LA6 == LR_BR or LA6 == LS_BR or LA6 == REGEX or LA6 == VAR_NAME or LA6 == WORD:
                    alt6 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae


                if alt6 == 1:
                    # SpeakPythonJSGF.g:96:4: AT_RESULTS mResults AT statementFields
                    pass 
                    self.match(self.input, AT_RESULTS, self.FOLLOW_AT_RESULTS_in_statementFields227)

                    self._state.following.append(self.FOLLOW_mResults_in_statementFields229)
                    self.mResults()

                    self._state.following.pop()

                    self.match(self.input, AT, self.FOLLOW_AT_in_statementFields231)

                    self._state.following.append(self.FOLLOW_statementFields_in_statementFields233)
                    self.statementFields()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass




                elif alt6 == 2:
                    # SpeakPythonJSGF.g:98:4: AT_TESTS testCases AT statementFields
                    pass 
                    self.match(self.input, AT_TESTS, self.FOLLOW_AT_TESTS_in_statementFields242)

                    self._state.following.append(self.FOLLOW_testCases_in_statementFields244)
                    self.testCases()

                    self._state.following.pop()

                    self.match(self.input, AT, self.FOLLOW_AT_in_statementFields246)

                    self._state.following.append(self.FOLLOW_statementFields_in_statementFields248)
                    self.statementFields()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass




                elif alt6 == 3:
                    # SpeakPythonJSGF.g:100:4: 
                    pass 
                    if self._state.backtracking == 0:
                        pass





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "statementFields"



    # $ANTLR start "alias"
    # SpeakPythonJSGF.g:103:1: alias returns [aliasR] : HASH_NAME LR_BR RR_BR EQ exps statementFields ;
    def alias(self, ):
        aliasR = None


        HASH_NAME5 = None
        exps6 = None


        try:
            try:
                # SpeakPythonJSGF.g:104:2: ( HASH_NAME LR_BR RR_BR EQ exps statementFields )
                # SpeakPythonJSGF.g:104:4: HASH_NAME LR_BR RR_BR EQ exps statementFields
                pass 
                HASH_NAME5 = self.match(self.input, HASH_NAME, self.FOLLOW_HASH_NAME_in_alias272)

                self.match(self.input, LR_BR, self.FOLLOW_LR_BR_in_alias274)

                self.match(self.input, RR_BR, self.FOLLOW_RR_BR_in_alias276)

                self.match(self.input, EQ, self.FOLLOW_EQ_in_alias278)

                self._state.following.append(self.FOLLOW_exps_in_alias280)
                exps6 = self.exps()

                self._state.following.pop()

                self._state.following.append(self.FOLLOW_statementFields_in_alias282)
                self.statementFields()

                self._state.following.pop()

                if self._state.backtracking == 0:
                    pass
                    self.aliasRules[HASH_NAME5.text[1:]] = exps6; 






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return aliasR

    # $ANTLR end "alias"



    # $ANTLR start "exps"
    # SpeakPythonJSGF.g:108:1: exps returns [expsR=''] : expVal SEMI ;
    def exps(self, ):
        expsR = ''


        expVal7 = None


        try:
            try:
                # SpeakPythonJSGF.g:109:2: ( expVal SEMI )
                # SpeakPythonJSGF.g:109:4: expVal SEMI
                pass 
                self._state.following.append(self.FOLLOW_expVal_in_exps301)
                expVal7 = self.expVal()

                self._state.following.pop()

                self.match(self.input, SEMI, self.FOLLOW_SEMI_in_exps303)

                if self._state.backtracking == 0:
                    pass
                    expsR =  expVal7 + ""; 






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return expsR

    # $ANTLR end "exps"



    # $ANTLR start "expVal"
    # SpeakPythonJSGF.g:113:1: expVal returns [expValR=''] : ( LS_BR e1= expVal RS_BR opt subExp | LR_BR e2= expVal RR_BR opt subExp |w1= WORD subExp | VAR_NAME subExp | HASH_NAME subExp | REGEX subExp );
    def expVal(self, ):
        expValR = ''


        w1 = None
        HASH_NAME14 = None
        e1 = None

        e2 = None

        opt8 = None

        subExp9 = None

        opt10 = None

        subExp11 = None

        subExp12 = None

        subExp13 = None

        subExp15 = None

        subExp16 = None


        try:
            try:
                # SpeakPythonJSGF.g:114:2: ( LS_BR e1= expVal RS_BR opt subExp | LR_BR e2= expVal RR_BR opt subExp |w1= WORD subExp | VAR_NAME subExp | HASH_NAME subExp | REGEX subExp )
                alt7 = 6
                LA7 = self.input.LA(1)
                if LA7 == LS_BR:
                    alt7 = 1
                elif LA7 == LR_BR:
                    alt7 = 2
                elif LA7 == WORD:
                    alt7 = 3
                elif LA7 == VAR_NAME:
                    alt7 = 4
                elif LA7 == HASH_NAME:
                    alt7 = 5
                elif LA7 == REGEX:
                    alt7 = 6
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae


                if alt7 == 1:
                    # SpeakPythonJSGF.g:114:4: LS_BR e1= expVal RS_BR opt subExp
                    pass 
                    self.match(self.input, LS_BR, self.FOLLOW_LS_BR_in_expVal321)

                    self._state.following.append(self.FOLLOW_expVal_in_expVal325)
                    e1 = self.expVal()

                    self._state.following.pop()

                    self.match(self.input, RS_BR, self.FOLLOW_RS_BR_in_expVal327)

                    self._state.following.append(self.FOLLOW_opt_in_expVal329)
                    opt8 = self.opt()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_subExp_in_expVal331)
                    subExp9 = self.subExp()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        expValR =  opt8[0] + e1 + opt8[1] + subExp9 




                elif alt7 == 2:
                    # SpeakPythonJSGF.g:117:4: LR_BR e2= expVal RR_BR opt subExp
                    pass 
                    self.match(self.input, LR_BR, self.FOLLOW_LR_BR_in_expVal342)

                    self._state.following.append(self.FOLLOW_expVal_in_expVal346)
                    e2 = self.expVal()

                    self._state.following.pop()

                    self.match(self.input, RR_BR, self.FOLLOW_RR_BR_in_expVal348)

                    self._state.following.append(self.FOLLOW_opt_in_expVal350)
                    opt10 = self.opt()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_subExp_in_expVal352)
                    subExp11 = self.subExp()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        expValR =  opt10[0] + e2 + opt10[1] + subExp11 




                elif alt7 == 3:
                    # SpeakPythonJSGF.g:120:4: w1= WORD subExp
                    pass 
                    w1 = self.match(self.input, WORD, self.FOLLOW_WORD_in_expVal365)

                    self._state.following.append(self.FOLLOW_subExp_in_expVal367)
                    subExp12 = self.subExp()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        expValR =  w1.text + subExp12 




                elif alt7 == 4:
                    # SpeakPythonJSGF.g:123:4: VAR_NAME subExp
                    pass 
                    self.match(self.input, VAR_NAME, self.FOLLOW_VAR_NAME_in_expVal378)

                    self._state.following.append(self.FOLLOW_subExp_in_expVal380)
                    subExp13 = self.subExp()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        if (self.messages['variable'] != None): print self.messages['variable']; self.messages['variable'] = None; self.parseFailed = True; expValR =  subExp13 




                elif alt7 == 5:
                    # SpeakPythonJSGF.g:126:4: HASH_NAME subExp
                    pass 
                    HASH_NAME14 = self.match(self.input, HASH_NAME, self.FOLLOW_HASH_NAME_in_expVal391)

                    self._state.following.append(self.FOLLOW_subExp_in_expVal393)
                    subExp15 = self.subExp()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        name = HASH_NAME14.text[1:]; 



                    if self._state.backtracking == 0:
                        pass
                        if (name not in self.aliasRules): print "The rule <" + name + "> does not exist before it is referenced."; 



                    if self._state.backtracking == 0:
                        pass
                        expValR =  "<" + name + ">" + subExp15 




                elif alt7 == 6:
                    # SpeakPythonJSGF.g:131:4: REGEX subExp
                    pass 
                    self.match(self.input, REGEX, self.FOLLOW_REGEX_in_expVal414)

                    self._state.following.append(self.FOLLOW_subExp_in_expVal416)
                    subExp16 = self.subExp()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        if (self.messages['regex'] != None): print self.messages['regex']; self.messages['regex'] = None; self.parseFailed = True; expValR =  subExp16 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return expValR

    # $ANTLR end "expVal"



    # $ANTLR start "subExp"
    # SpeakPythonJSGF.g:136:1: subExp returns [subExpR=''] : ( expVal | OR expVal |);
    def subExp(self, ):
        subExpR = ''


        expVal17 = None

        expVal18 = None


        try:
            try:
                # SpeakPythonJSGF.g:137:2: ( expVal | OR expVal |)
                alt8 = 3
                LA8 = self.input.LA(1)
                if LA8 == HASH_NAME or LA8 == LR_BR or LA8 == LS_BR or LA8 == REGEX or LA8 == VAR_NAME or LA8 == WORD:
                    alt8 = 1
                elif LA8 == OR:
                    alt8 = 2
                elif LA8 == EOF or LA8 == RR_BR or LA8 == RS_BR or LA8 == SEMI:
                    alt8 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae


                if alt8 == 1:
                    # SpeakPythonJSGF.g:137:4: expVal
                    pass 
                    self._state.following.append(self.FOLLOW_expVal_in_subExp437)
                    expVal17 = self.expVal()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        subExpR =  " " + expVal17 




                elif alt8 == 2:
                    # SpeakPythonJSGF.g:139:4: OR expVal
                    pass 
                    self.match(self.input, OR, self.FOLLOW_OR_in_subExp447)

                    self._state.following.append(self.FOLLOW_expVal_in_subExp449)
                    expVal18 = self.expVal()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        subExpR =  " | " + expVal18 




                elif alt8 == 3:
                    # SpeakPythonJSGF.g:140:4: 
                    pass 
                    if self._state.backtracking == 0:
                        pass





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return subExpR

    # $ANTLR end "subExp"



    # $ANTLR start "opt"
    # SpeakPythonJSGF.g:144:1: opt returns [optR=('(',')')] : ( QSTN | STAR | PLUS |);
    def opt(self, ):
        optR = ('(',')')


        try:
            try:
                # SpeakPythonJSGF.g:145:2: ( QSTN | STAR | PLUS |)
                alt9 = 4
                LA9 = self.input.LA(1)
                if LA9 == QSTN:
                    alt9 = 1
                elif LA9 == STAR:
                    alt9 = 2
                elif LA9 == PLUS:
                    alt9 = 3
                elif LA9 == EOF or LA9 == HASH_NAME or LA9 == LR_BR or LA9 == LS_BR or LA9 == OR or LA9 == REGEX or LA9 == RR_BR or LA9 == RS_BR or LA9 == SEMI or LA9 == VAR_NAME or LA9 == WORD:
                    alt9 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 9, 0, self.input)

                    raise nvae


                if alt9 == 1:
                    # SpeakPythonJSGF.g:145:4: QSTN
                    pass 
                    self.match(self.input, QSTN, self.FOLLOW_QSTN_in_opt473)

                    if self._state.backtracking == 0:
                        pass
                        optR = ("[", "]") 




                elif alt9 == 2:
                    # SpeakPythonJSGF.g:146:4: STAR
                    pass 
                    self.match(self.input, STAR, self.FOLLOW_STAR_in_opt480)

                    if self._state.backtracking == 0:
                        pass
                        optR = ("(", ")*") 




                elif alt9 == 3:
                    # SpeakPythonJSGF.g:147:4: PLUS
                    pass 
                    self.match(self.input, PLUS, self.FOLLOW_PLUS_in_opt487)

                    if self._state.backtracking == 0:
                        pass
                        optR = ("(", ")+") 




                elif alt9 == 4:
                    # SpeakPythonJSGF.g:148:4: 
                    pass 
                    if self._state.backtracking == 0:
                        pass





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return optR

    # $ANTLR end "opt"



    # $ANTLR start "testCases"
    # SpeakPythonJSGF.g:151:1: testCases returns [testCasesR=[]] : ( testCase ts= testCases |);
    def testCases(self, ):
        testCasesR = []


        ts = None


        try:
            try:
                # SpeakPythonJSGF.g:152:2: ( testCase ts= testCases |)
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == QUOTE_STRING) :
                    alt10 = 1
                elif (LA10_0 == EOF or LA10_0 == AT) :
                    alt10 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae


                if alt10 == 1:
                    # SpeakPythonJSGF.g:152:4: testCase ts= testCases
                    pass 
                    self._state.following.append(self.FOLLOW_testCase_in_testCases509)
                    self.testCase()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_testCases_in_testCases513)
                    ts = self.testCases()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass




                elif alt10 == 2:
                    # SpeakPythonJSGF.g:153:4: 
                    pass 
                    if self._state.backtracking == 0:
                        pass





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return testCasesR

    # $ANTLR end "testCases"



    # $ANTLR start "testCase"
    # SpeakPythonJSGF.g:156:1: testCase returns [testCaseR=''] : (q1= QUOTE_STRING EQ ( RA_BR )? q2= QUOTE_STRING |q3= QUOTE_STRING );
    def testCase(self, ):
        testCaseR = ''


        q1 = None
        q2 = None
        q3 = None

        try:
            try:
                # SpeakPythonJSGF.g:157:2: (q1= QUOTE_STRING EQ ( RA_BR )? q2= QUOTE_STRING |q3= QUOTE_STRING )
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == QUOTE_STRING) :
                    LA12_1 = self.input.LA(2)

                    if (LA12_1 == EQ) :
                        alt12 = 1
                    elif (LA12_1 == EOF or LA12_1 == AT or LA12_1 == QUOTE_STRING) :
                        alt12 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 12, 1, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae


                if alt12 == 1:
                    # SpeakPythonJSGF.g:157:4: q1= QUOTE_STRING EQ ( RA_BR )? q2= QUOTE_STRING
                    pass 
                    q1 = self.match(self.input, QUOTE_STRING, self.FOLLOW_QUOTE_STRING_in_testCase537)

                    self.match(self.input, EQ, self.FOLLOW_EQ_in_testCase539)

                    # SpeakPythonJSGF.g:157:23: ( RA_BR )?
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == RA_BR) :
                        alt11 = 1
                    if alt11 == 1:
                        # SpeakPythonJSGF.g:157:24: RA_BR
                        pass 
                        self.match(self.input, RA_BR, self.FOLLOW_RA_BR_in_testCase542)




                    q2 = self.match(self.input, QUOTE_STRING, self.FOLLOW_QUOTE_STRING_in_testCase548)

                    if self._state.backtracking == 0:
                        pass




                elif alt12 == 2:
                    # SpeakPythonJSGF.g:158:4: q3= QUOTE_STRING
                    pass 
                    q3 = self.match(self.input, QUOTE_STRING, self.FOLLOW_QUOTE_STRING_in_testCase557)

                    if self._state.backtracking == 0:
                        pass





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return testCaseR

    # $ANTLR end "testCase"



    # $ANTLR start "mResults"
    # SpeakPythonJSGF.g:163:1: mResults : (m1= mResult ms= mResults |);
    def mResults(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:164:2: (m1= mResult ms= mResults |)
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == HASH_NAME or LA13_0 == KLEENE or LA13_0 == NUM or LA13_0 == REGEX_LABEL or LA13_0 == VAR_NAME or LA13_0 == WORD) :
                    alt13 = 1
                elif (LA13_0 == EOF or LA13_0 == AT) :
                    alt13 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae


                if alt13 == 1:
                    # SpeakPythonJSGF.g:164:4: m1= mResult ms= mResults
                    pass 
                    self._state.following.append(self.FOLLOW_mResult_in_mResults576)
                    self.mResult()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_mResults_in_mResults580)
                    self.mResults()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass




                elif alt13 == 2:
                    # SpeakPythonJSGF.g:165:4: 
                    pass 
                    if self._state.backtracking == 0:
                        pass





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "mResults"



    # $ANTLR start "mResult"
    # SpeakPythonJSGF.g:169:1: mResult : ls= labels LC_BR resultant RC_BR ;
    def mResult(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:170:2: (ls= labels LC_BR resultant RC_BR )
                # SpeakPythonJSGF.g:170:4: ls= labels LC_BR resultant RC_BR
                pass 
                self._state.following.append(self.FOLLOW_labels_in_mResult602)
                self.labels()

                self._state.following.pop()

                self.match(self.input, LC_BR, self.FOLLOW_LC_BR_in_mResult604)

                self._state.following.append(self.FOLLOW_resultant_in_mResult606)
                self.resultant()

                self._state.following.pop()

                self.match(self.input, RC_BR, self.FOLLOW_RC_BR_in_mResult608)

                if self._state.backtracking == 0:
                    pass






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "mResult"



    # $ANTLR start "labels"
    # SpeakPythonJSGF.g:174:1: labels : (l1= label labelsRest |l2= label );
    def labels(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:175:2: (l1= label labelsRest |l2= label )
                alt14 = 2
                LA14 = self.input.LA(1)
                if LA14 == VAR_NAME:
                    LA14_1 = self.input.LA(2)

                    if (LA14_1 == COMMA) :
                        alt14 = 1
                    elif (LA14_1 == EOF or LA14_1 == LC_BR) :
                        alt14 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 14, 1, self.input)

                        raise nvae


                elif LA14 == NUM:
                    LA14_2 = self.input.LA(2)

                    if (LA14_2 == COMMA) :
                        alt14 = 1
                    elif (LA14_2 == EOF or LA14_2 == LC_BR) :
                        alt14 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 14, 2, self.input)

                        raise nvae


                elif LA14 == HASH_NAME:
                    LA14 = self.input.LA(2)
                    if LA14 == UNDERSCORE_NUM:
                        LA14_9 = self.input.LA(3)

                        if (LA14_9 == COMMA) :
                            alt14 = 1
                        elif (LA14_9 == EOF or LA14_9 == LC_BR) :
                            alt14 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 14, 9, self.input)

                            raise nvae


                    elif LA14 == COMMA:
                        alt14 = 1
                    elif LA14 == EOF or LA14 == LC_BR:
                        alt14 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 14, 3, self.input)

                        raise nvae


                elif LA14 == KLEENE:
                    LA14_4 = self.input.LA(2)

                    if (LA14_4 == NUM) :
                        LA14_10 = self.input.LA(3)

                        if (LA14_10 == COMMA) :
                            alt14 = 1
                        elif (LA14_10 == EOF or LA14_10 == LC_BR) :
                            alt14 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 14, 10, self.input)

                            raise nvae


                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 14, 4, self.input)

                        raise nvae


                elif LA14 == REGEX_LABEL:
                    LA14_5 = self.input.LA(2)

                    if (LA14_5 == NUM) :
                        LA14_11 = self.input.LA(3)

                        if (LA14_11 == COMMA) :
                            alt14 = 1
                        elif (LA14_11 == EOF or LA14_11 == LC_BR) :
                            alt14 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 14, 11, self.input)

                            raise nvae


                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 14, 5, self.input)

                        raise nvae


                elif LA14 == WORD:
                    LA14_6 = self.input.LA(2)

                    if (LA14_6 == COMMA) :
                        alt14 = 1
                    elif (LA14_6 == EOF or LA14_6 == LC_BR) :
                        alt14 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 14, 6, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae


                if alt14 == 1:
                    # SpeakPythonJSGF.g:175:4: l1= label labelsRest
                    pass 
                    self._state.following.append(self.FOLLOW_label_in_labels625)
                    self.label()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_labelsRest_in_labels627)
                    self.labelsRest()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass




                elif alt14 == 2:
                    # SpeakPythonJSGF.g:176:4: l2= label
                    pass 
                    self._state.following.append(self.FOLLOW_label_in_labels636)
                    self.label()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "labels"



    # $ANTLR start "labelsRest"
    # SpeakPythonJSGF.g:179:1: labelsRest : COMMA labels ;
    def labelsRest(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:180:2: ( COMMA labels )
                # SpeakPythonJSGF.g:180:4: COMMA labels
                pass 
                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_labelsRest649)

                self._state.following.append(self.FOLLOW_labels_in_labelsRest651)
                self.labels()

                self._state.following.pop()

                if self._state.backtracking == 0:
                    pass






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "labelsRest"



    # $ANTLR start "label"
    # SpeakPythonJSGF.g:184:1: label : ( VAR_NAME | NUM | HASH_NAME UNDERSCORE_NUM | HASH_NAME | KLEENE NUM | REGEX_LABEL NUM | WORD );
    def label(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:185:2: ( VAR_NAME | NUM | HASH_NAME UNDERSCORE_NUM | HASH_NAME | KLEENE NUM | REGEX_LABEL NUM | WORD )
                alt15 = 7
                LA15 = self.input.LA(1)
                if LA15 == VAR_NAME:
                    alt15 = 1
                elif LA15 == NUM:
                    alt15 = 2
                elif LA15 == HASH_NAME:
                    LA15_3 = self.input.LA(2)

                    if (LA15_3 == UNDERSCORE_NUM) :
                        alt15 = 3
                    elif (LA15_3 == EOF or LA15_3 == COMMA or LA15_3 == LC_BR) :
                        alt15 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 15, 3, self.input)

                        raise nvae


                elif LA15 == KLEENE:
                    alt15 = 5
                elif LA15 == REGEX_LABEL:
                    alt15 = 6
                elif LA15 == WORD:
                    alt15 = 7
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae


                if alt15 == 1:
                    # SpeakPythonJSGF.g:185:4: VAR_NAME
                    pass 
                    self.match(self.input, VAR_NAME, self.FOLLOW_VAR_NAME_in_label667)

                    if self._state.backtracking == 0:
                        pass




                elif alt15 == 2:
                    # SpeakPythonJSGF.g:186:4: NUM
                    pass 
                    self.match(self.input, NUM, self.FOLLOW_NUM_in_label674)

                    if self._state.backtracking == 0:
                        pass




                elif alt15 == 3:
                    # SpeakPythonJSGF.g:187:4: HASH_NAME UNDERSCORE_NUM
                    pass 
                    self.match(self.input, HASH_NAME, self.FOLLOW_HASH_NAME_in_label681)

                    self.match(self.input, UNDERSCORE_NUM, self.FOLLOW_UNDERSCORE_NUM_in_label683)

                    if self._state.backtracking == 0:
                        pass




                elif alt15 == 4:
                    # SpeakPythonJSGF.g:188:4: HASH_NAME
                    pass 
                    self.match(self.input, HASH_NAME, self.FOLLOW_HASH_NAME_in_label690)

                    if self._state.backtracking == 0:
                        pass




                elif alt15 == 5:
                    # SpeakPythonJSGF.g:189:4: KLEENE NUM
                    pass 
                    self.match(self.input, KLEENE, self.FOLLOW_KLEENE_in_label697)

                    self.match(self.input, NUM, self.FOLLOW_NUM_in_label699)

                    if self._state.backtracking == 0:
                        pass




                elif alt15 == 6:
                    # SpeakPythonJSGF.g:190:4: REGEX_LABEL NUM
                    pass 
                    self.match(self.input, REGEX_LABEL, self.FOLLOW_REGEX_LABEL_in_label706)

                    self.match(self.input, NUM, self.FOLLOW_NUM_in_label708)

                    if self._state.backtracking == 0:
                        pass




                elif alt15 == 7:
                    # SpeakPythonJSGF.g:191:4: WORD
                    pass 
                    self.match(self.input, WORD, self.FOLLOW_WORD_in_label715)

                    if self._state.backtracking == 0:
                        pass





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "label"



    # $ANTLR start "resultant"
    # SpeakPythonJSGF.g:195:1: resultant : results ;
    def resultant(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:196:2: ( results )
                # SpeakPythonJSGF.g:196:4: results
                pass 
                self._state.following.append(self.FOLLOW_results_in_resultant729)
                self.results()

                self._state.following.pop()

                if self._state.backtracking == 0:
                    pass






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "resultant"



    # $ANTLR start "results"
    # SpeakPythonJSGF.g:199:1: results : ( result results |);
    def results(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:200:2: ( result results |)
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == HASH_NAME or LA16_0 == KLEENE or LA16_0 == QUOTE_STRING or LA16_0 == REGEX_LABEL or LA16_0 == VAR_NAME) :
                    alt16 = 1
                elif (LA16_0 == EOF or (RA_BR <= LA16_0 <= RC_BR) or LA16_0 == RR_BR) :
                    alt16 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae


                if alt16 == 1:
                    # SpeakPythonJSGF.g:200:4: result results
                    pass 
                    self._state.following.append(self.FOLLOW_result_in_results742)
                    self.result()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_results_in_results744)
                    self.results()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass




                elif alt16 == 2:
                    # SpeakPythonJSGF.g:201:4: 
                    pass 
                    if self._state.backtracking == 0:
                        pass





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "results"



    # $ANTLR start "result"
    # SpeakPythonJSGF.g:204:1: result : ( QUOTE_STRING | VAR_NAME | HASH_NAME UNDERSCORE_NUM | HASH_NAME | KLEENE NUM LA_BR results RA_BR LR_BR results RR_BR | REGEX_LABEL NUM LR_BR QUOTE_STRING RR_BR | REGEX_LABEL NUM );
    def result(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:205:2: ( QUOTE_STRING | VAR_NAME | HASH_NAME UNDERSCORE_NUM | HASH_NAME | KLEENE NUM LA_BR results RA_BR LR_BR results RR_BR | REGEX_LABEL NUM LR_BR QUOTE_STRING RR_BR | REGEX_LABEL NUM )
                alt17 = 7
                LA17 = self.input.LA(1)
                if LA17 == QUOTE_STRING:
                    alt17 = 1
                elif LA17 == VAR_NAME:
                    alt17 = 2
                elif LA17 == HASH_NAME:
                    LA17_3 = self.input.LA(2)

                    if (LA17_3 == UNDERSCORE_NUM) :
                        alt17 = 3
                    elif (LA17_3 == EOF or LA17_3 == HASH_NAME or LA17_3 == KLEENE or (QUOTE_STRING <= LA17_3 <= RC_BR) or (REGEX_LABEL <= LA17_3 <= RR_BR) or LA17_3 == VAR_NAME) :
                        alt17 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 17, 3, self.input)

                        raise nvae


                elif LA17 == KLEENE:
                    alt17 = 5
                elif LA17 == REGEX_LABEL:
                    LA17_5 = self.input.LA(2)

                    if (LA17_5 == NUM) :
                        LA17_8 = self.input.LA(3)

                        if (LA17_8 == LR_BR) :
                            alt17 = 6
                        elif (LA17_8 == EOF or LA17_8 == HASH_NAME or LA17_8 == KLEENE or (QUOTE_STRING <= LA17_8 <= RC_BR) or (REGEX_LABEL <= LA17_8 <= RR_BR) or LA17_8 == VAR_NAME) :
                            alt17 = 7
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 17, 8, self.input)

                            raise nvae


                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 17, 5, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae


                if alt17 == 1:
                    # SpeakPythonJSGF.g:205:4: QUOTE_STRING
                    pass 
                    self.match(self.input, QUOTE_STRING, self.FOLLOW_QUOTE_STRING_in_result762)

                    if self._state.backtracking == 0:
                        pass




                elif alt17 == 2:
                    # SpeakPythonJSGF.g:206:4: VAR_NAME
                    pass 
                    self.match(self.input, VAR_NAME, self.FOLLOW_VAR_NAME_in_result769)

                    if self._state.backtracking == 0:
                        pass




                elif alt17 == 3:
                    # SpeakPythonJSGF.g:207:4: HASH_NAME UNDERSCORE_NUM
                    pass 
                    self.match(self.input, HASH_NAME, self.FOLLOW_HASH_NAME_in_result776)

                    self.match(self.input, UNDERSCORE_NUM, self.FOLLOW_UNDERSCORE_NUM_in_result778)

                    if self._state.backtracking == 0:
                        pass




                elif alt17 == 4:
                    # SpeakPythonJSGF.g:208:4: HASH_NAME
                    pass 
                    self.match(self.input, HASH_NAME, self.FOLLOW_HASH_NAME_in_result785)

                    if self._state.backtracking == 0:
                        pass




                elif alt17 == 5:
                    # SpeakPythonJSGF.g:209:4: KLEENE NUM LA_BR results RA_BR LR_BR results RR_BR
                    pass 
                    self.match(self.input, KLEENE, self.FOLLOW_KLEENE_in_result792)

                    self.match(self.input, NUM, self.FOLLOW_NUM_in_result794)

                    self.match(self.input, LA_BR, self.FOLLOW_LA_BR_in_result796)

                    self._state.following.append(self.FOLLOW_results_in_result798)
                    self.results()

                    self._state.following.pop()

                    self.match(self.input, RA_BR, self.FOLLOW_RA_BR_in_result800)

                    self.match(self.input, LR_BR, self.FOLLOW_LR_BR_in_result802)

                    self._state.following.append(self.FOLLOW_results_in_result804)
                    self.results()

                    self._state.following.pop()

                    self.match(self.input, RR_BR, self.FOLLOW_RR_BR_in_result806)

                    if self._state.backtracking == 0:
                        pass




                elif alt17 == 6:
                    # SpeakPythonJSGF.g:210:4: REGEX_LABEL NUM LR_BR QUOTE_STRING RR_BR
                    pass 
                    self.match(self.input, REGEX_LABEL, self.FOLLOW_REGEX_LABEL_in_result813)

                    self.match(self.input, NUM, self.FOLLOW_NUM_in_result815)

                    self.match(self.input, LR_BR, self.FOLLOW_LR_BR_in_result817)

                    self.match(self.input, QUOTE_STRING, self.FOLLOW_QUOTE_STRING_in_result819)

                    self.match(self.input, RR_BR, self.FOLLOW_RR_BR_in_result821)

                    if self._state.backtracking == 0:
                        pass




                elif alt17 == 7:
                    # SpeakPythonJSGF.g:211:4: REGEX_LABEL NUM
                    pass 
                    self.match(self.input, REGEX_LABEL, self.FOLLOW_REGEX_LABEL_in_result828)

                    self.match(self.input, NUM, self.FOLLOW_NUM_in_result830)

                    if self._state.backtracking == 0:
                        pass





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "result"



 

    FOLLOW_s_in_prog51 = frozenset([])
    FOLLOW_EOF_in_prog53 = frozenset([1])
    FOLLOW_alias_in_s71 = frozenset([6, 7, 16, 22, 23, 32, 42, 44])
    FOLLOW_s_in_s75 = frozenset([1])
    FOLLOW_mat_in_s81 = frozenset([6, 7, 16, 22, 23, 32, 42, 44])
    FOLLOW_s_in_s85 = frozenset([1])
    FOLLOW_globalOptions_in_s91 = frozenset([6, 7, 16, 22, 23, 32, 42, 44])
    FOLLOW_s_in_s93 = frozenset([1])
    FOLLOW_AT_GLOBAL_OPTIONS_in_globalOptions109 = frozenset([5, 44])
    FOLLOW_myOptions_in_globalOptions111 = frozenset([5])
    FOLLOW_AT_in_globalOptions113 = frozenset([1])
    FOLLOW_AT_OPTIONS_in_localOptions124 = frozenset([5, 44])
    FOLLOW_myOptions_in_localOptions128 = frozenset([5])
    FOLLOW_AT_in_localOptions130 = frozenset([1])
    FOLLOW_myOption_in_myOptions141 = frozenset([44])
    FOLLOW_myOptions_in_myOptions143 = frozenset([1])
    FOLLOW_WORD_in_myOption159 = frozenset([15])
    FOLLOW_EQ_in_myOption161 = frozenset([30, 32])
    FOLLOW_RA_BR_in_myOption164 = frozenset([32])
    FOLLOW_REGEX_in_myOption168 = frozenset([1, 36])
    FOLLOW_SEMI_in_myOption171 = frozenset([1])
    FOLLOW_localOptions_in_mat198 = frozenset([16, 22, 23, 32, 42, 44])
    FOLLOW_exps_in_mat202 = frozenset([8, 9])
    FOLLOW_statementFields_in_mat211 = frozenset([1])
    FOLLOW_AT_RESULTS_in_statementFields227 = frozenset([5, 16, 19, 25, 33, 42, 44])
    FOLLOW_mResults_in_statementFields229 = frozenset([5])
    FOLLOW_AT_in_statementFields231 = frozenset([8, 9])
    FOLLOW_statementFields_in_statementFields233 = frozenset([1])
    FOLLOW_AT_TESTS_in_statementFields242 = frozenset([5, 29])
    FOLLOW_testCases_in_statementFields244 = frozenset([5])
    FOLLOW_AT_in_statementFields246 = frozenset([8, 9])
    FOLLOW_statementFields_in_statementFields248 = frozenset([1])
    FOLLOW_HASH_NAME_in_alias272 = frozenset([22])
    FOLLOW_LR_BR_in_alias274 = frozenset([34])
    FOLLOW_RR_BR_in_alias276 = frozenset([15])
    FOLLOW_EQ_in_alias278 = frozenset([16, 22, 23, 32, 42, 44])
    FOLLOW_exps_in_alias280 = frozenset([8, 9])
    FOLLOW_statementFields_in_alias282 = frozenset([1])
    FOLLOW_expVal_in_exps301 = frozenset([36])
    FOLLOW_SEMI_in_exps303 = frozenset([1])
    FOLLOW_LS_BR_in_expVal321 = frozenset([16, 22, 23, 32, 42, 44])
    FOLLOW_expVal_in_expVal325 = frozenset([35])
    FOLLOW_RS_BR_in_expVal327 = frozenset([16, 22, 23, 26, 27, 28, 32, 37, 42, 44])
    FOLLOW_opt_in_expVal329 = frozenset([16, 22, 23, 26, 32, 42, 44])
    FOLLOW_subExp_in_expVal331 = frozenset([1])
    FOLLOW_LR_BR_in_expVal342 = frozenset([16, 22, 23, 32, 42, 44])
    FOLLOW_expVal_in_expVal346 = frozenset([34])
    FOLLOW_RR_BR_in_expVal348 = frozenset([16, 22, 23, 26, 27, 28, 32, 37, 42, 44])
    FOLLOW_opt_in_expVal350 = frozenset([16, 22, 23, 26, 32, 42, 44])
    FOLLOW_subExp_in_expVal352 = frozenset([1])
    FOLLOW_WORD_in_expVal365 = frozenset([16, 22, 23, 26, 32, 42, 44])
    FOLLOW_subExp_in_expVal367 = frozenset([1])
    FOLLOW_VAR_NAME_in_expVal378 = frozenset([16, 22, 23, 26, 32, 42, 44])
    FOLLOW_subExp_in_expVal380 = frozenset([1])
    FOLLOW_HASH_NAME_in_expVal391 = frozenset([16, 22, 23, 26, 32, 42, 44])
    FOLLOW_subExp_in_expVal393 = frozenset([1])
    FOLLOW_REGEX_in_expVal414 = frozenset([16, 22, 23, 26, 32, 42, 44])
    FOLLOW_subExp_in_expVal416 = frozenset([1])
    FOLLOW_expVal_in_subExp437 = frozenset([1])
    FOLLOW_OR_in_subExp447 = frozenset([16, 22, 23, 32, 42, 44])
    FOLLOW_expVal_in_subExp449 = frozenset([1])
    FOLLOW_QSTN_in_opt473 = frozenset([1])
    FOLLOW_STAR_in_opt480 = frozenset([1])
    FOLLOW_PLUS_in_opt487 = frozenset([1])
    FOLLOW_testCase_in_testCases509 = frozenset([29])
    FOLLOW_testCases_in_testCases513 = frozenset([1])
    FOLLOW_QUOTE_STRING_in_testCase537 = frozenset([15])
    FOLLOW_EQ_in_testCase539 = frozenset([29, 30])
    FOLLOW_RA_BR_in_testCase542 = frozenset([29])
    FOLLOW_QUOTE_STRING_in_testCase548 = frozenset([1])
    FOLLOW_QUOTE_STRING_in_testCase557 = frozenset([1])
    FOLLOW_mResult_in_mResults576 = frozenset([16, 19, 25, 33, 42, 44])
    FOLLOW_mResults_in_mResults580 = frozenset([1])
    FOLLOW_labels_in_mResult602 = frozenset([21])
    FOLLOW_LC_BR_in_mResult604 = frozenset([16, 19, 29, 33, 42])
    FOLLOW_resultant_in_mResult606 = frozenset([31])
    FOLLOW_RC_BR_in_mResult608 = frozenset([1])
    FOLLOW_label_in_labels625 = frozenset([11])
    FOLLOW_labelsRest_in_labels627 = frozenset([1])
    FOLLOW_label_in_labels636 = frozenset([1])
    FOLLOW_COMMA_in_labelsRest649 = frozenset([16, 19, 25, 33, 42, 44])
    FOLLOW_labels_in_labelsRest651 = frozenset([1])
    FOLLOW_VAR_NAME_in_label667 = frozenset([1])
    FOLLOW_NUM_in_label674 = frozenset([1])
    FOLLOW_HASH_NAME_in_label681 = frozenset([41])
    FOLLOW_UNDERSCORE_NUM_in_label683 = frozenset([1])
    FOLLOW_HASH_NAME_in_label690 = frozenset([1])
    FOLLOW_KLEENE_in_label697 = frozenset([25])
    FOLLOW_NUM_in_label699 = frozenset([1])
    FOLLOW_REGEX_LABEL_in_label706 = frozenset([25])
    FOLLOW_NUM_in_label708 = frozenset([1])
    FOLLOW_WORD_in_label715 = frozenset([1])
    FOLLOW_results_in_resultant729 = frozenset([1])
    FOLLOW_result_in_results742 = frozenset([16, 19, 29, 33, 42])
    FOLLOW_results_in_results744 = frozenset([1])
    FOLLOW_QUOTE_STRING_in_result762 = frozenset([1])
    FOLLOW_VAR_NAME_in_result769 = frozenset([1])
    FOLLOW_HASH_NAME_in_result776 = frozenset([41])
    FOLLOW_UNDERSCORE_NUM_in_result778 = frozenset([1])
    FOLLOW_HASH_NAME_in_result785 = frozenset([1])
    FOLLOW_KLEENE_in_result792 = frozenset([25])
    FOLLOW_NUM_in_result794 = frozenset([20])
    FOLLOW_LA_BR_in_result796 = frozenset([16, 19, 29, 30, 33, 42])
    FOLLOW_results_in_result798 = frozenset([30])
    FOLLOW_RA_BR_in_result800 = frozenset([22])
    FOLLOW_LR_BR_in_result802 = frozenset([16, 19, 29, 33, 34, 42])
    FOLLOW_results_in_result804 = frozenset([34])
    FOLLOW_RR_BR_in_result806 = frozenset([1])
    FOLLOW_REGEX_LABEL_in_result813 = frozenset([25])
    FOLLOW_NUM_in_result815 = frozenset([22])
    FOLLOW_LR_BR_in_result817 = frozenset([29])
    FOLLOW_QUOTE_STRING_in_result819 = frozenset([34])
    FOLLOW_RR_BR_in_result821 = frozenset([1])
    FOLLOW_REGEX_LABEL_in_result828 = frozenset([25])
    FOLLOW_NUM_in_result830 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SpeakPythonJSGFLexer", SpeakPythonJSGFParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
