# $ANTLR 3.4 SpeakPython.g 2015-09-25 20:19:02

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


import re;
sub = re.sub;
from Match import Match;
from Match import GroupCounter;
from Result import Result;
from StringResult import StringResult;
from VarResult import VarResult;
from FunctionResult import FunctionResult;
from KleeneResult import KleeneResult;
from RegexResult import RegexResult;
from Function import Function;



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




class SpeakPythonParser(Parser):
    grammarFileName = "SpeakPython.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(SpeakPythonParser, self).__init__(input, state, *args, **kwargs)




        self.delegates = []





    optionVals = {};
    optionValsBackup = optionVals;
    statementFieldDict = {};
    isKeyword = True;
    wordEncountered = False;
    finishedKeywords = False;
    globalTests = {};
    upCount = 0;
    matches = [];
    aliases = {};
    aliasWord = '';
    aliasUseCount = {};
    aliasKeywords = {}
    aliasKeywordState = {};
    kGroupRegexes = {};
    isKleene = False;
    kGroupCount = 0;
    keywords = [];
    regexes = {};
    regexCount = 0;
    termNum = 0;



    # $ANTLR start "prog"
    # SpeakPython.g:76:1: prog : s EOF ;
    def prog(self, ):

        self.optionVals['wordRegex'] = '[a-zA-Z0-9_\\+\\.\\-]+';
        self.optionVals['varRegex'] = '[a-zA-Z0-9_\\+\\.\\-]+';
        self.optionVals['wordDelim'] = '[ ,/]';
        self.defaultOptionVals = self.optionVals.copy();

        try:
            try:
                # SpeakPython.g:85:2: ( s EOF )
                # SpeakPython.g:85:4: s EOF
                pass 
                self._state.following.append(self.FOLLOW_s_in_prog56)
                self.s()

                self._state.following.pop()

                self.match(self.input, EOF, self.FOLLOW_EOF_in_prog58)

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
    # SpeakPython.g:88:1: s : ( alias s | mat s | globalOptions s |);
    def s(self, ):
        alias1 = None

        mat2 = None



        self.statementFieldDict = {};
        self.statementFieldDict['testCases'] = [];
        self.statementFieldDict['results'] = [];
        self.upCount = 0;
        self.bracketCount = 0;
        self.wordEncountered = False;
        self.isKeyword = True;
        self.finishedKeywords = False;
        self.keywords = [];
        self.regexes = {};
        self.regexCount = 0;
        self.wordAtBracket = 0;
        self.kGroupCount = 0;
        self.isKleene = False;
        self.kGroupRegexes = {};
        self.aliasWord = '';
        self.aliasUseCount = {};

        try:
            try:
                # SpeakPython.g:112:2: ( alias s | mat s | globalOptions s |)
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
                    # SpeakPython.g:112:4: alias s
                    pass 
                    self._state.following.append(self.FOLLOW_alias_in_s76)
                    alias1 = self.alias()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        self.aliases[self.aliasWord] = alias1; 



                    self._state.following.append(self.FOLLOW_s_in_s80)
                    self.s()

                    self._state.following.pop()


                elif alt1 == 2:
                    # SpeakPython.g:113:4: mat s
                    pass 
                    self._state.following.append(self.FOLLOW_mat_in_s86)
                    mat2 = self.mat()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        self.matches.append(mat2); 



                    self._state.following.append(self.FOLLOW_s_in_s90)
                    self.s()

                    self._state.following.pop()


                elif alt1 == 3:
                    # SpeakPython.g:114:4: globalOptions s
                    pass 
                    self._state.following.append(self.FOLLOW_globalOptions_in_s96)
                    self.globalOptions()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_s_in_s98)
                    self.s()

                    self._state.following.pop()


                elif alt1 == 4:
                    # SpeakPython.g:115:4: 
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
    # SpeakPython.g:118:1: globalOptions : AT_GLOBAL_OPTIONS myOptions AT ;
    def globalOptions(self, ):
        try:
            try:
                # SpeakPython.g:119:2: ( AT_GLOBAL_OPTIONS myOptions AT )
                # SpeakPython.g:119:4: AT_GLOBAL_OPTIONS myOptions AT
                pass 
                self.match(self.input, AT_GLOBAL_OPTIONS, self.FOLLOW_AT_GLOBAL_OPTIONS_in_globalOptions114)

                self._state.following.append(self.FOLLOW_myOptions_in_globalOptions116)
                self.myOptions()

                self._state.following.pop()

                self.match(self.input, AT, self.FOLLOW_AT_in_globalOptions118)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "globalOptions"



    # $ANTLR start "localOptions"
    # SpeakPython.g:122:1: localOptions : AT_OPTIONS myOptions AT ;
    def localOptions(self, ):
        try:
            try:
                # SpeakPython.g:123:2: ( AT_OPTIONS myOptions AT )
                # SpeakPython.g:123:4: AT_OPTIONS myOptions AT
                pass 
                self.match(self.input, AT_OPTIONS, self.FOLLOW_AT_OPTIONS_in_localOptions129)

                if self._state.backtracking == 0:
                    pass
                    self.optionValsBackup = self.optionVals; self.optionVals = self.optionValsBackup.copy(); 



                self._state.following.append(self.FOLLOW_myOptions_in_localOptions133)
                self.myOptions()

                self._state.following.pop()

                self.match(self.input, AT, self.FOLLOW_AT_in_localOptions135)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "localOptions"



    # $ANTLR start "myOptions"
    # SpeakPython.g:126:1: myOptions : ( myOption myOptions |);
    def myOptions(self, ):
        try:
            try:
                # SpeakPython.g:127:2: ( myOption myOptions |)
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
                    # SpeakPython.g:127:4: myOption myOptions
                    pass 
                    self._state.following.append(self.FOLLOW_myOption_in_myOptions146)
                    self.myOption()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_myOptions_in_myOptions148)
                    self.myOptions()

                    self._state.following.pop()


                elif alt2 == 2:
                    # SpeakPython.g:128:4: 
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
    # SpeakPython.g:131:1: myOption : WORD EQ ( RA_BR )? REGEX ( SEMI )? ;
    def myOption(self, ):
        WORD3 = None
        REGEX4 = None

        try:
            try:
                # SpeakPython.g:132:2: ( WORD EQ ( RA_BR )? REGEX ( SEMI )? )
                # SpeakPython.g:132:4: WORD EQ ( RA_BR )? REGEX ( SEMI )?
                pass 
                WORD3 = self.match(self.input, WORD, self.FOLLOW_WORD_in_myOption164)

                self.match(self.input, EQ, self.FOLLOW_EQ_in_myOption166)

                # SpeakPython.g:132:12: ( RA_BR )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == RA_BR) :
                    alt3 = 1
                if alt3 == 1:
                    # SpeakPython.g:132:13: RA_BR
                    pass 
                    self.match(self.input, RA_BR, self.FOLLOW_RA_BR_in_myOption169)




                REGEX4 = self.match(self.input, REGEX, self.FOLLOW_REGEX_in_myOption173)

                # SpeakPython.g:132:27: ( SEMI )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == SEMI) :
                    alt4 = 1
                if alt4 == 1:
                    # SpeakPython.g:132:28: SEMI
                    pass 
                    self.match(self.input, SEMI, self.FOLLOW_SEMI_in_myOption176)




                if self._state.backtracking == 0:
                    pass
                    self.optionVals[WORD3.text] = REGEX4.text[1:-2]; 






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "myOption"



    # $ANTLR start "mat"
    # SpeakPython.g:136:1: mat returns [matR] : ( localOptions )? exps statementFields ;
    def mat(self, ):
        matR = None


        exps5 = None



        self.keywords = [];
        self.regexCount = 0;
        self.regexes = {};

        try:
            try:
                # SpeakPython.g:143:2: ( ( localOptions )? exps statementFields )
                # SpeakPython.g:143:4: ( localOptions )? exps statementFields
                pass 
                # SpeakPython.g:143:4: ( localOptions )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == AT_OPTIONS) :
                    alt5 = 1
                if alt5 == 1:
                    # SpeakPython.g:143:5: localOptions
                    pass 
                    self._state.following.append(self.FOLLOW_localOptions_in_mat203)
                    self.localOptions()

                    self._state.following.pop()




                self._state.following.append(self.FOLLOW_exps_in_mat207)
                exps5 = self.exps()

                self._state.following.pop()

                if self._state.backtracking == 0:
                    pass
                    self.optionVals = self.optionValsBackup; 



                self._state.following.append(self.FOLLOW_statementFields_in_mat216)
                self.statementFields()

                self._state.following.pop()

                if self._state.backtracking == 0:
                    pass
                    matR =  Match(exps5, self.statementFieldDict['testCases'], self.keywords, self.kGroupRegexes, self.statementFieldDict['results']) 






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return matR

    # $ANTLR end "mat"



    # $ANTLR start "statementFields"
    # SpeakPython.g:149:1: statementFields : ( AT_RESULTS mResults AT statementFields | AT_TESTS testCases AT statementFields |);
    def statementFields(self, ):
        mResults6 = None

        testCases7 = None


        try:
            try:
                # SpeakPython.g:150:2: ( AT_RESULTS mResults AT statementFields | AT_TESTS testCases AT statementFields |)
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
                    # SpeakPython.g:150:4: AT_RESULTS mResults AT statementFields
                    pass 
                    self.match(self.input, AT_RESULTS, self.FOLLOW_AT_RESULTS_in_statementFields232)

                    self._state.following.append(self.FOLLOW_mResults_in_statementFields234)
                    mResults6 = self.mResults()

                    self._state.following.pop()

                    self.match(self.input, AT, self.FOLLOW_AT_in_statementFields236)

                    self._state.following.append(self.FOLLOW_statementFields_in_statementFields238)
                    self.statementFields()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        self.statementFieldDict['results'] = mResults6; 




                elif alt6 == 2:
                    # SpeakPython.g:152:4: AT_TESTS testCases AT statementFields
                    pass 
                    self.match(self.input, AT_TESTS, self.FOLLOW_AT_TESTS_in_statementFields247)

                    self._state.following.append(self.FOLLOW_testCases_in_statementFields249)
                    testCases7 = self.testCases()

                    self._state.following.pop()

                    self.match(self.input, AT, self.FOLLOW_AT_in_statementFields251)

                    self._state.following.append(self.FOLLOW_statementFields_in_statementFields253)
                    self.statementFields()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        self.statementFieldDict['testCases'] = testCases7; 




                elif alt6 == 3:
                    # SpeakPython.g:154:4: 
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
    # SpeakPython.g:157:1: alias returns [aliasR] : HASH_NAME LR_BR RR_BR EQ exps statementFields ;
    def alias(self, ):
        aliasR = None


        HASH_NAME8 = None
        exps9 = None


        try:
            try:
                # SpeakPython.g:158:2: ( HASH_NAME LR_BR RR_BR EQ exps statementFields )
                # SpeakPython.g:158:4: HASH_NAME LR_BR RR_BR EQ exps statementFields
                pass 
                HASH_NAME8 = self.match(self.input, HASH_NAME, self.FOLLOW_HASH_NAME_in_alias277)

                if self._state.backtracking == 0:
                    pass
                    self.aliasWord = HASH_NAME8.text[1:]; 



                self.match(self.input, LR_BR, self.FOLLOW_LR_BR_in_alias286)

                self.match(self.input, RR_BR, self.FOLLOW_RR_BR_in_alias288)

                self.match(self.input, EQ, self.FOLLOW_EQ_in_alias290)

                self._state.following.append(self.FOLLOW_exps_in_alias292)
                exps9 = self.exps()

                self._state.following.pop()

                if self._state.backtracking == 0:
                    pass
                    self.aliasKeywordState[self.aliasWord] = (self.isKeyword, self.finishedKeywords); 



                if self._state.backtracking == 0:
                    pass
                    self.aliasKeywords[self.aliasWord] = self.keywords; 



                self._state.following.append(self.FOLLOW_statementFields_in_alias314)
                self.statementFields()

                self._state.following.pop()

                if self._state.backtracking == 0:
                    pass
                    aliasR =  Function(self.aliasWord, exps9, self.statementFieldDict['testCases'], self.kGroupRegexes, self.statementFieldDict['results']) 






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return aliasR

    # $ANTLR end "alias"



    # $ANTLR start "exps"
    # SpeakPython.g:170:1: exps returns [expsR=''] : expVal SEMI ;
    def exps(self, ):
        expsR = ''


        expVal10 = None


        try:
            try:
                # SpeakPython.g:171:2: ( expVal SEMI )
                # SpeakPython.g:171:4: expVal SEMI
                pass 
                self._state.following.append(self.FOLLOW_expVal_in_exps338)
                expVal10 = self.expVal()

                self._state.following.pop()

                self.match(self.input, SEMI, self.FOLLOW_SEMI_in_exps340)

                if self._state.backtracking == 0:
                    pass
                    expsR =  sub(r"\?P<\*>", GroupCounter(), expVal10) 






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return expsR

    # $ANTLR end "exps"



    # $ANTLR start "expVal"
    # SpeakPython.g:175:1: expVal returns [expValR=''] : ( LS_BR e1= expVal RS_BR opt subExp | LR_BR e2= expVal RR_BR opt subExp |w1= WORD subExp | VAR_NAME subExp | HASH_NAME subExp | REGEX subExp );
    def expVal(self, ):
        expValR = ''


        w1 = None
        VAR_NAME16 = None
        HASH_NAME18 = None
        REGEX20 = None
        e1 = None

        e2 = None

        opt11 = None

        subExp12 = None

        opt13 = None

        subExp14 = None

        subExp15 = None

        subExp17 = None

        subExp19 = None

        subExp21 = None


        try:
            try:
                # SpeakPython.g:176:2: ( LS_BR e1= expVal RS_BR opt subExp | LR_BR e2= expVal RR_BR opt subExp |w1= WORD subExp | VAR_NAME subExp | HASH_NAME subExp | REGEX subExp )
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
                    # SpeakPython.g:176:4: LS_BR e1= expVal RS_BR opt subExp
                    pass 
                    self.match(self.input, LS_BR, self.FOLLOW_LS_BR_in_expVal358)

                    if self._state.backtracking == 0:
                        pass
                        self.bracketCount += 1; 



                    self._state.following.append(self.FOLLOW_expVal_in_expVal369)
                    e1 = self.expVal()

                    self._state.following.pop()

                    self.match(self.input, RS_BR, self.FOLLOW_RS_BR_in_expVal371)

                    if self._state.backtracking == 0:
                        pass
                        self.bracketCount -= 1; 



                    self._state.following.append(self.FOLLOW_opt_in_expVal380)
                    opt11 = self.opt()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        if (self.bracketCount == 0 and (opt11[1] not in "?*" or len(opt11[1]) == 0)): self.finishedKeywords = True; self.wordAtBracket = 0; 



                    if self._state.backtracking == 0:
                        pass
                        if self.isKleene: self.kGroupRegexes[str(self.kGroupCount)] = e1; self.kGroupCount += 1; self.isKleene = False; 



                    self._state.following.append(self.FOLLOW_subExp_in_expVal394)
                    subExp12 = self.subExp()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        expValR =  opt11[0] + "(?P<*>" + e1 + ")" + opt11[1] + subExp12 




                elif alt7 == 2:
                    # SpeakPython.g:186:4: LR_BR e2= expVal RR_BR opt subExp
                    pass 
                    self.match(self.input, LR_BR, self.FOLLOW_LR_BR_in_expVal405)

                    if self._state.backtracking == 0:
                        pass
                        self.bracketCount += 1; 



                    self._state.following.append(self.FOLLOW_expVal_in_expVal416)
                    e2 = self.expVal()

                    self._state.following.pop()

                    self.match(self.input, RR_BR, self.FOLLOW_RR_BR_in_expVal418)

                    if self._state.backtracking == 0:
                        pass
                        self.bracketCount -= 1; 



                    self._state.following.append(self.FOLLOW_opt_in_expVal427)
                    opt13 = self.opt()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        if (self.bracketCount == 0 and (opt13[1] not in "?*" or len(opt13[1]) == 0)): self.finishedKeywords = True; self.wordAtBracket = 0; 



                    if self._state.backtracking == 0:
                        pass
                        if self.isKleene: self.kGroupRegexes[str(self.kGroupCount)] = e2; self.kGroupCount += 1; self.isKleene = False; 



                    self._state.following.append(self.FOLLOW_subExp_in_expVal452)
                    subExp14 = self.subExp()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        expValR =  opt13[0] + "(?:" + e2 + ")" + opt13[1] + subExp14 




                elif alt7 == 3:
                    # SpeakPython.g:200:4: w1= WORD subExp
                    pass 
                    w1 = self.match(self.input, WORD, self.FOLLOW_WORD_in_expVal470)

                    if self._state.backtracking == 0:
                        pass
                        if (self.isKeyword and not self.finishedKeywords): self.keywords.append(w1.text.lower()); self.isKeyword = False; self.wordAtBracket = self.bracketCount; 



                    if self._state.backtracking == 0:
                        pass
                        if (self.bracketCount == 0): self.finishedKeywords = True; 



                    self._state.following.append(self.FOLLOW_subExp_in_expVal481)
                    subExp15 = self.subExp()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        expValR =  "(?:" + w1.text.lower() + ")" + subExp15 




                elif alt7 == 4:
                    # SpeakPython.g:205:4: VAR_NAME subExp
                    pass 
                    VAR_NAME16 = self.match(self.input, VAR_NAME, self.FOLLOW_VAR_NAME_in_expVal492)

                    if self._state.backtracking == 0:
                        pass
                        if (self.isKeyword and not self.finishedKeywords): self.keywords.append("*"); self.isKeyword = False; self.wordAtBracket = self.bracketCount; 



                    if self._state.backtracking == 0:
                        pass
                        if (self.bracketCount == 0): self.finishedKeywords = True; 



                    self._state.following.append(self.FOLLOW_subExp_in_expVal503)
                    subExp17 = self.subExp()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        expValR =  "(?P<" + VAR_NAME16.text[1:] + ">" + self.optionVals['varRegex'] + ")" + subExp17 




                elif alt7 == 5:
                    # SpeakPython.g:210:4: HASH_NAME subExp
                    pass 
                    HASH_NAME18 = self.match(self.input, HASH_NAME, self.FOLLOW_HASH_NAME_in_expVal514)

                    if self._state.backtracking == 0:
                        pass
                        name = HASH_NAME18.text[1:]; self.aliasUseCount[name] = 0 if (name not in self.aliasUseCount) else self.aliasUseCount[name] + 1; 



                    if self._state.backtracking == 0:
                        pass
                        aliasUseCount = self.aliasUseCount[name]; 



                    if self._state.backtracking == 0:
                        pass
                        if (self.isKeyword and not self.finishedKeywords): self.keywords.extend(self.aliasKeywords[name]); self.isKeyword = self.aliasKeywordState[name][0]; self.wordAtBracket = self.bracketCount; 



                    if self._state.backtracking == 0:
                        pass
                        if (self.bracketCount == 0): self.finishedKeywords = self.aliasKeywordState[name][1]; 



                    self._state.following.append(self.FOLLOW_subExp_in_expVal539)
                    subExp19 = self.subExp()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        retVal = subExp19; 



                    if self._state.backtracking == 0:
                        pass
                        retVal = "(?P<" + "_" + name + "_" + str(aliasUseCount) + "_>" + sub(r"<([^>]+)>", "<_" + name + "_" + str(aliasUseCount) + r"_\g<1>" + ">", self.aliases[name].getExp()) + ")" + subExp19; 



                    if self._state.backtracking == 0:
                        pass
                        expValR =  retVal 




                elif alt7 == 6:
                    # SpeakPython.g:221:4: REGEX subExp
                    pass 
                    REGEX20 = self.match(self.input, REGEX, self.FOLLOW_REGEX_in_expVal560)

                    if self._state.backtracking == 0:
                        pass
                        if (self.isKeyword and not self.finishedKeywords): self.keywords.append("*"); self.isKeyword = False; self.wordAtBracket = self.bracketCount; 



                    if self._state.backtracking == 0:
                        pass
                        reg = REGEX20.text[1:-2]; reg = sub(r"\(\?<([^>]+)>", r"(?P<\1>", reg); reg = sub(r"\([^\?]", r"(?:", reg); self.regexes[str(self.regexCount)] = reg; regexString = "(?P<r_" + str(self.regexCount) + ">" + reg + ")"; self.regexCount += 1; 



                    self._state.following.append(self.FOLLOW_subExp_in_expVal578)
                    subExp21 = self.subExp()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        expValR =  regexString + subExp21 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return expValR

    # $ANTLR end "expVal"



    # $ANTLR start "subExp"
    # SpeakPython.g:230:1: subExp returns [subExpR=''] : ( expVal | OR expVal |);
    def subExp(self, ):
        subExpR = ''


        expVal22 = None

        expVal23 = None


        try:
            try:
                # SpeakPython.g:231:2: ( expVal | OR expVal |)
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
                    # SpeakPython.g:231:4: expVal
                    pass 
                    self._state.following.append(self.FOLLOW_expVal_in_subExp599)
                    expVal22 = self.expVal()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        subExpR =  self.optionVals['wordDelim'] + "*" + expVal22 




                elif alt8 == 2:
                    # SpeakPython.g:233:4: OR expVal
                    pass 
                    self.match(self.input, OR, self.FOLLOW_OR_in_subExp609)

                    if self._state.backtracking == 0:
                        pass
                        if (self.bracketCount <= self.wordAtBracket): self.isKeyword = True; self.finishedKeywords = False; 



                    self._state.following.append(self.FOLLOW_expVal_in_subExp620)
                    expVal23 = self.expVal()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        subExpR =  "|" + expVal23 




                elif alt8 == 3:
                    # SpeakPython.g:238:4: 
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
    # SpeakPython.g:242:1: opt returns [optR=('','')] : ( QSTN | STAR | PLUS |);
    def opt(self, ):
        optR = ('','')


        try:
            try:
                # SpeakPython.g:243:2: ( QSTN | STAR | PLUS |)
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
                    # SpeakPython.g:243:4: QSTN
                    pass 
                    self.match(self.input, QSTN, self.FOLLOW_QSTN_in_opt649)

                    if self._state.backtracking == 0:
                        pass
                        if (self.bracketCount < self.wordAtBracket): self.isKeyword = True; 



                    if self._state.backtracking == 0:
                        pass
                        optR = ("","?") 




                elif alt9 == 2:
                    # SpeakPython.g:246:4: STAR
                    pass 
                    self.match(self.input, STAR, self.FOLLOW_STAR_in_opt662)

                    if self._state.backtracking == 0:
                        pass
                        self.isKleene = True; 



                    if self._state.backtracking == 0:
                        pass
                        if (self.bracketCount < self.wordAtBracket): self.isKeyword = True; 



                    if self._state.backtracking == 0:
                        pass
                        optR = ("(?P<k_" + str(self.kGroupCount) + ">(?:", self.optionVals['wordDelim'] + "+)*)") 




                elif alt9 == 3:
                    # SpeakPython.g:249:4: PLUS
                    pass 
                    self.match(self.input, PLUS, self.FOLLOW_PLUS_in_opt677)

                    if self._state.backtracking == 0:
                        pass
                        self.isKleene = True; 



                    if self._state.backtracking == 0:
                        pass
                        optR = ("(?P<k_" + str(self.kGroupCount) + ">(?:", self.optionVals['wordDelim'] + "+)+)") 




                elif alt9 == 4:
                    # SpeakPython.g:252:4: 
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
    # SpeakPython.g:255:1: testCases returns [testCasesR=[]] : ( testCase ts= testCases |);
    def testCases(self, ):
        testCasesR = []


        ts = None

        testCase24 = None


        try:
            try:
                # SpeakPython.g:256:2: ( testCase ts= testCases |)
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
                    # SpeakPython.g:256:4: testCase ts= testCases
                    pass 
                    self._state.following.append(self.FOLLOW_testCase_in_testCases705)
                    testCase24 = self.testCase()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_testCases_in_testCases709)
                    ts = self.testCases()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        ts.append(testCase24); testCasesR =  ts 




                elif alt10 == 2:
                    # SpeakPython.g:258:4: 
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
    # SpeakPython.g:261:1: testCase returns [testCaseR=''] : (q1= QUOTE_STRING EQ ( RA_BR )? q2= QUOTE_STRING |q3= QUOTE_STRING );
    def testCase(self, ):
        testCaseR = ''


        q1 = None
        q2 = None
        q3 = None

        try:
            try:
                # SpeakPython.g:262:2: (q1= QUOTE_STRING EQ ( RA_BR )? q2= QUOTE_STRING |q3= QUOTE_STRING )
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
                    # SpeakPython.g:262:4: q1= QUOTE_STRING EQ ( RA_BR )? q2= QUOTE_STRING
                    pass 
                    q1 = self.match(self.input, QUOTE_STRING, self.FOLLOW_QUOTE_STRING_in_testCase736)

                    self.match(self.input, EQ, self.FOLLOW_EQ_in_testCase738)

                    # SpeakPython.g:262:23: ( RA_BR )?
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == RA_BR) :
                        alt11 = 1
                    if alt11 == 1:
                        # SpeakPython.g:262:24: RA_BR
                        pass 
                        self.match(self.input, RA_BR, self.FOLLOW_RA_BR_in_testCase741)




                    q2 = self.match(self.input, QUOTE_STRING, self.FOLLOW_QUOTE_STRING_in_testCase747)

                    if self._state.backtracking == 0:
                        pass
                        self.globalTests[q1.text[1:-1]] = q2.text[1:-1]; testCaseR =  q1.text[1:-1] 




                elif alt12 == 2:
                    # SpeakPython.g:263:4: q3= QUOTE_STRING
                    pass 
                    q3 = self.match(self.input, QUOTE_STRING, self.FOLLOW_QUOTE_STRING_in_testCase756)

                    if self._state.backtracking == 0:
                        pass
                        testCaseR =  q3.text[1:-1] 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return testCaseR

    # $ANTLR end "testCase"



    # $ANTLR start "mResults"
    # SpeakPython.g:268:1: mResults returns [mResultsR=[]] : (m1= mResult ms= mResults |);
    def mResults(self, ):
        mResultsR = []


        m1 = None

        ms = None


        try:
            try:
                # SpeakPython.g:269:2: (m1= mResult ms= mResults |)
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
                    # SpeakPython.g:269:4: m1= mResult ms= mResults
                    pass 
                    self._state.following.append(self.FOLLOW_mResult_in_mResults779)
                    m1 = self.mResult()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_mResults_in_mResults783)
                    ms = self.mResults()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        ms.append(m1); mResultsR =  ms 




                elif alt13 == 2:
                    # SpeakPython.g:270:4: 
                    pass 
                    if self._state.backtracking == 0:
                        pass
                        mResultsR =  [] 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return mResultsR

    # $ANTLR end "mResults"



    # $ANTLR start "mResult"
    # SpeakPython.g:274:1: mResult returns [mResultR] : ls= labels LC_BR resultant RC_BR ;
    def mResult(self, ):
        mResultR = None


        ls = None

        resultant25 = None


        try:
            try:
                # SpeakPython.g:275:2: (ls= labels LC_BR resultant RC_BR )
                # SpeakPython.g:275:4: ls= labels LC_BR resultant RC_BR
                pass 
                self._state.following.append(self.FOLLOW_labels_in_mResult809)
                ls = self.labels()

                self._state.following.pop()

                self.match(self.input, LC_BR, self.FOLLOW_LC_BR_in_mResult811)

                self._state.following.append(self.FOLLOW_resultant_in_mResult813)
                resultant25 = self.resultant()

                self._state.following.pop()

                self.match(self.input, RC_BR, self.FOLLOW_RC_BR_in_mResult815)

                if self._state.backtracking == 0:
                    pass
                    mResultR =  Result(ls, resultant25) 






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return mResultR

    # $ANTLR end "mResult"



    # $ANTLR start "labels"
    # SpeakPython.g:279:1: labels returns [labelsR] : (l1= label labelsRest |l2= label );
    def labels(self, ):
        labelsR = None


        l1 = None

        l2 = None

        labelsRest26 = None


        try:
            try:
                # SpeakPython.g:280:2: (l1= label labelsRest |l2= label )
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
                    # SpeakPython.g:280:4: l1= label labelsRest
                    pass 
                    self._state.following.append(self.FOLLOW_label_in_labels836)
                    l1 = self.label()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_labelsRest_in_labels838)
                    labelsRest26 = self.labelsRest()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        labelsRest26.append(l1); labelsR =  labelsRest26 




                elif alt14 == 2:
                    # SpeakPython.g:281:4: l2= label
                    pass 
                    self._state.following.append(self.FOLLOW_label_in_labels847)
                    l2 = self.label()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        labelsR = [l2] 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return labelsR

    # $ANTLR end "labels"



    # $ANTLR start "labelsRest"
    # SpeakPython.g:284:1: labelsRest returns [labelsRestR] : COMMA labels ;
    def labelsRest(self, ):
        labelsRestR = None


        labels27 = None


        try:
            try:
                # SpeakPython.g:285:2: ( COMMA labels )
                # SpeakPython.g:285:4: COMMA labels
                pass 
                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_labelsRest864)

                self._state.following.append(self.FOLLOW_labels_in_labelsRest866)
                labels27 = self.labels()

                self._state.following.pop()

                if self._state.backtracking == 0:
                    pass
                    labelsRestR =  labels27 






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return labelsRestR

    # $ANTLR end "labelsRest"



    # $ANTLR start "label"
    # SpeakPython.g:289:1: label returns [labelR] : ( VAR_NAME | NUM | HASH_NAME UNDERSCORE_NUM | HASH_NAME | KLEENE NUM | REGEX_LABEL NUM | WORD );
    def label(self, ):
        labelR = None


        VAR_NAME28 = None
        NUM29 = None
        HASH_NAME30 = None
        UNDERSCORE_NUM31 = None
        HASH_NAME32 = None
        KLEENE33 = None
        NUM34 = None
        REGEX_LABEL35 = None
        NUM36 = None
        WORD37 = None

        try:
            try:
                # SpeakPython.g:290:2: ( VAR_NAME | NUM | HASH_NAME UNDERSCORE_NUM | HASH_NAME | KLEENE NUM | REGEX_LABEL NUM | WORD )
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
                    # SpeakPython.g:290:4: VAR_NAME
                    pass 
                    VAR_NAME28 = self.match(self.input, VAR_NAME, self.FOLLOW_VAR_NAME_in_label886)

                    if self._state.backtracking == 0:
                        pass
                        labelR =  VAR_NAME28.text[1:] 




                elif alt15 == 2:
                    # SpeakPython.g:291:4: NUM
                    pass 
                    NUM29 = self.match(self.input, NUM, self.FOLLOW_NUM_in_label893)

                    if self._state.backtracking == 0:
                        pass
                        labelR =  NUM29.text 




                elif alt15 == 3:
                    # SpeakPython.g:292:4: HASH_NAME UNDERSCORE_NUM
                    pass 
                    HASH_NAME30 = self.match(self.input, HASH_NAME, self.FOLLOW_HASH_NAME_in_label900)

                    UNDERSCORE_NUM31 = self.match(self.input, UNDERSCORE_NUM, self.FOLLOW_UNDERSCORE_NUM_in_label902)

                    if self._state.backtracking == 0:
                        pass
                        labelR =  HASH_NAME30.text[1:] + UNDERSCORE_NUM31.text 




                elif alt15 == 4:
                    # SpeakPython.g:293:4: HASH_NAME
                    pass 
                    HASH_NAME32 = self.match(self.input, HASH_NAME, self.FOLLOW_HASH_NAME_in_label909)

                    if self._state.backtracking == 0:
                        pass
                        labelR =  HASH_NAME32.text[1:] 




                elif alt15 == 5:
                    # SpeakPython.g:294:4: KLEENE NUM
                    pass 
                    KLEENE33 = self.match(self.input, KLEENE, self.FOLLOW_KLEENE_in_label916)

                    NUM34 = self.match(self.input, NUM, self.FOLLOW_NUM_in_label918)

                    if self._state.backtracking == 0:
                        pass
                        labelR =  KLEENE33.text + NUM34.text 




                elif alt15 == 6:
                    # SpeakPython.g:295:4: REGEX_LABEL NUM
                    pass 
                    REGEX_LABEL35 = self.match(self.input, REGEX_LABEL, self.FOLLOW_REGEX_LABEL_in_label925)

                    NUM36 = self.match(self.input, NUM, self.FOLLOW_NUM_in_label927)

                    if self._state.backtracking == 0:
                        pass
                        labelR =  REGEX_LABEL35.text + NUM36.text 




                elif alt15 == 7:
                    # SpeakPython.g:296:4: WORD
                    pass 
                    WORD37 = self.match(self.input, WORD, self.FOLLOW_WORD_in_label934)

                    if self._state.backtracking == 0:
                        pass
                        labelR =  WORD37.text 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return labelR

    # $ANTLR end "label"



    # $ANTLR start "resultant"
    # SpeakPython.g:300:1: resultant returns [resultantR] : results ;
    def resultant(self, ):
        resultantR = None


        results38 = None


        try:
            try:
                # SpeakPython.g:301:2: ( results )
                # SpeakPython.g:301:4: results
                pass 
                self._state.following.append(self.FOLLOW_results_in_resultant952)
                results38 = self.results()

                self._state.following.pop()

                if self._state.backtracking == 0:
                    pass
                    resultantR =  results38 






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return resultantR

    # $ANTLR end "resultant"



    # $ANTLR start "results"
    # SpeakPython.g:304:1: results returns [resultsR=[]] : ( result rs= results |);
    def results(self, ):
        resultsR = []


        rs = None

        result39 = None


        try:
            try:
                # SpeakPython.g:305:2: ( result rs= results |)
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
                    # SpeakPython.g:305:4: result rs= results
                    pass 
                    self._state.following.append(self.FOLLOW_result_in_results969)
                    result39 = self.result()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_results_in_results973)
                    rs = self.results()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        rs.insert(0, result39); resultsR =  rs 




                elif alt16 == 2:
                    # SpeakPython.g:306:4: 
                    pass 
                    if self._state.backtracking == 0:
                        pass





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return resultsR

    # $ANTLR end "results"



    # $ANTLR start "result"
    # SpeakPython.g:309:1: result returns [resultR] : ( QUOTE_STRING | VAR_NAME | HASH_NAME UNDERSCORE_NUM | HASH_NAME | KLEENE NUM LA_BR r1= results RA_BR LR_BR r2= results RR_BR | REGEX_LABEL NUM LR_BR QUOTE_STRING RR_BR | REGEX_LABEL NUM );
    def result(self, ):
        resultR = None


        QUOTE_STRING40 = None
        VAR_NAME41 = None
        HASH_NAME42 = None
        UNDERSCORE_NUM43 = None
        HASH_NAME44 = None
        KLEENE45 = None
        NUM46 = None
        NUM47 = None
        QUOTE_STRING48 = None
        NUM49 = None
        r1 = None

        r2 = None


        try:
            try:
                # SpeakPython.g:310:2: ( QUOTE_STRING | VAR_NAME | HASH_NAME UNDERSCORE_NUM | HASH_NAME | KLEENE NUM LA_BR r1= results RA_BR LR_BR r2= results RR_BR | REGEX_LABEL NUM LR_BR QUOTE_STRING RR_BR | REGEX_LABEL NUM )
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
                    # SpeakPython.g:310:4: QUOTE_STRING
                    pass 
                    QUOTE_STRING40 = self.match(self.input, QUOTE_STRING, self.FOLLOW_QUOTE_STRING_in_result995)

                    if self._state.backtracking == 0:
                        pass
                        resultR =  StringResult(QUOTE_STRING40.text[1:-1]) 




                elif alt17 == 2:
                    # SpeakPython.g:311:4: VAR_NAME
                    pass 
                    VAR_NAME41 = self.match(self.input, VAR_NAME, self.FOLLOW_VAR_NAME_in_result1002)

                    if self._state.backtracking == 0:
                        pass
                        resultR =  VarResult(VAR_NAME41.text[1:]) 




                elif alt17 == 3:
                    # SpeakPython.g:312:4: HASH_NAME UNDERSCORE_NUM
                    pass 
                    HASH_NAME42 = self.match(self.input, HASH_NAME, self.FOLLOW_HASH_NAME_in_result1009)

                    UNDERSCORE_NUM43 = self.match(self.input, UNDERSCORE_NUM, self.FOLLOW_UNDERSCORE_NUM_in_result1011)

                    if self._state.backtracking == 0:
                        pass
                        resultR =  FunctionResult(HASH_NAME42.text[1:] + UNDERSCORE_NUM43.text) 




                elif alt17 == 4:
                    # SpeakPython.g:313:4: HASH_NAME
                    pass 
                    HASH_NAME44 = self.match(self.input, HASH_NAME, self.FOLLOW_HASH_NAME_in_result1018)

                    if self._state.backtracking == 0:
                        pass
                        resultR =  FunctionResult(HASH_NAME44.text[1:]) 




                elif alt17 == 5:
                    # SpeakPython.g:314:4: KLEENE NUM LA_BR r1= results RA_BR LR_BR r2= results RR_BR
                    pass 
                    KLEENE45 = self.match(self.input, KLEENE, self.FOLLOW_KLEENE_in_result1025)

                    NUM46 = self.match(self.input, NUM, self.FOLLOW_NUM_in_result1027)

                    self.match(self.input, LA_BR, self.FOLLOW_LA_BR_in_result1029)

                    self._state.following.append(self.FOLLOW_results_in_result1033)
                    r1 = self.results()

                    self._state.following.pop()

                    self.match(self.input, RA_BR, self.FOLLOW_RA_BR_in_result1035)

                    self.match(self.input, LR_BR, self.FOLLOW_LR_BR_in_result1037)

                    self._state.following.append(self.FOLLOW_results_in_result1041)
                    r2 = self.results()

                    self._state.following.pop()

                    self.match(self.input, RR_BR, self.FOLLOW_RR_BR_in_result1043)

                    if self._state.backtracking == 0:
                        pass
                        resultR =  KleeneResult(KLEENE45.text + NUM46.text, r1, r2) 




                elif alt17 == 6:
                    # SpeakPython.g:316:4: REGEX_LABEL NUM LR_BR QUOTE_STRING RR_BR
                    pass 
                    self.match(self.input, REGEX_LABEL, self.FOLLOW_REGEX_LABEL_in_result1052)

                    NUM47 = self.match(self.input, NUM, self.FOLLOW_NUM_in_result1054)

                    self.match(self.input, LR_BR, self.FOLLOW_LR_BR_in_result1056)

                    QUOTE_STRING48 = self.match(self.input, QUOTE_STRING, self.FOLLOW_QUOTE_STRING_in_result1058)

                    self.match(self.input, RR_BR, self.FOLLOW_RR_BR_in_result1060)

                    if self._state.backtracking == 0:
                        pass
                        resultR =  RegexResult(self.regexes[NUM47.text], NUM47.text, QUOTE_STRING48.text[1:-1]) 




                elif alt17 == 7:
                    # SpeakPython.g:317:4: REGEX_LABEL NUM
                    pass 
                    self.match(self.input, REGEX_LABEL, self.FOLLOW_REGEX_LABEL_in_result1067)

                    NUM49 = self.match(self.input, NUM, self.FOLLOW_NUM_in_result1069)

                    if self._state.backtracking == 0:
                        pass
                        resultR =  RegexResult(self.regexes[NUM49.text], NUM49.text) 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return resultR

    # $ANTLR end "result"



 

    FOLLOW_s_in_prog56 = frozenset([])
    FOLLOW_EOF_in_prog58 = frozenset([1])
    FOLLOW_alias_in_s76 = frozenset([6, 7, 16, 22, 23, 32, 42, 44])
    FOLLOW_s_in_s80 = frozenset([1])
    FOLLOW_mat_in_s86 = frozenset([6, 7, 16, 22, 23, 32, 42, 44])
    FOLLOW_s_in_s90 = frozenset([1])
    FOLLOW_globalOptions_in_s96 = frozenset([6, 7, 16, 22, 23, 32, 42, 44])
    FOLLOW_s_in_s98 = frozenset([1])
    FOLLOW_AT_GLOBAL_OPTIONS_in_globalOptions114 = frozenset([5, 44])
    FOLLOW_myOptions_in_globalOptions116 = frozenset([5])
    FOLLOW_AT_in_globalOptions118 = frozenset([1])
    FOLLOW_AT_OPTIONS_in_localOptions129 = frozenset([5, 44])
    FOLLOW_myOptions_in_localOptions133 = frozenset([5])
    FOLLOW_AT_in_localOptions135 = frozenset([1])
    FOLLOW_myOption_in_myOptions146 = frozenset([44])
    FOLLOW_myOptions_in_myOptions148 = frozenset([1])
    FOLLOW_WORD_in_myOption164 = frozenset([15])
    FOLLOW_EQ_in_myOption166 = frozenset([30, 32])
    FOLLOW_RA_BR_in_myOption169 = frozenset([32])
    FOLLOW_REGEX_in_myOption173 = frozenset([1, 36])
    FOLLOW_SEMI_in_myOption176 = frozenset([1])
    FOLLOW_localOptions_in_mat203 = frozenset([16, 22, 23, 32, 42, 44])
    FOLLOW_exps_in_mat207 = frozenset([8, 9])
    FOLLOW_statementFields_in_mat216 = frozenset([1])
    FOLLOW_AT_RESULTS_in_statementFields232 = frozenset([5, 16, 19, 25, 33, 42, 44])
    FOLLOW_mResults_in_statementFields234 = frozenset([5])
    FOLLOW_AT_in_statementFields236 = frozenset([8, 9])
    FOLLOW_statementFields_in_statementFields238 = frozenset([1])
    FOLLOW_AT_TESTS_in_statementFields247 = frozenset([5, 29])
    FOLLOW_testCases_in_statementFields249 = frozenset([5])
    FOLLOW_AT_in_statementFields251 = frozenset([8, 9])
    FOLLOW_statementFields_in_statementFields253 = frozenset([1])
    FOLLOW_HASH_NAME_in_alias277 = frozenset([22])
    FOLLOW_LR_BR_in_alias286 = frozenset([34])
    FOLLOW_RR_BR_in_alias288 = frozenset([15])
    FOLLOW_EQ_in_alias290 = frozenset([16, 22, 23, 32, 42, 44])
    FOLLOW_exps_in_alias292 = frozenset([8, 9])
    FOLLOW_statementFields_in_alias314 = frozenset([1])
    FOLLOW_expVal_in_exps338 = frozenset([36])
    FOLLOW_SEMI_in_exps340 = frozenset([1])
    FOLLOW_LS_BR_in_expVal358 = frozenset([16, 22, 23, 32, 42, 44])
    FOLLOW_expVal_in_expVal369 = frozenset([35])
    FOLLOW_RS_BR_in_expVal371 = frozenset([16, 22, 23, 26, 27, 28, 32, 37, 42, 44])
    FOLLOW_opt_in_expVal380 = frozenset([16, 22, 23, 26, 32, 42, 44])
    FOLLOW_subExp_in_expVal394 = frozenset([1])
    FOLLOW_LR_BR_in_expVal405 = frozenset([16, 22, 23, 32, 42, 44])
    FOLLOW_expVal_in_expVal416 = frozenset([34])
    FOLLOW_RR_BR_in_expVal418 = frozenset([16, 22, 23, 26, 27, 28, 32, 37, 42, 44])
    FOLLOW_opt_in_expVal427 = frozenset([16, 22, 23, 26, 32, 42, 44])
    FOLLOW_subExp_in_expVal452 = frozenset([1])
    FOLLOW_WORD_in_expVal470 = frozenset([16, 22, 23, 26, 32, 42, 44])
    FOLLOW_subExp_in_expVal481 = frozenset([1])
    FOLLOW_VAR_NAME_in_expVal492 = frozenset([16, 22, 23, 26, 32, 42, 44])
    FOLLOW_subExp_in_expVal503 = frozenset([1])
    FOLLOW_HASH_NAME_in_expVal514 = frozenset([16, 22, 23, 26, 32, 42, 44])
    FOLLOW_subExp_in_expVal539 = frozenset([1])
    FOLLOW_REGEX_in_expVal560 = frozenset([16, 22, 23, 26, 32, 42, 44])
    FOLLOW_subExp_in_expVal578 = frozenset([1])
    FOLLOW_expVal_in_subExp599 = frozenset([1])
    FOLLOW_OR_in_subExp609 = frozenset([16, 22, 23, 32, 42, 44])
    FOLLOW_expVal_in_subExp620 = frozenset([1])
    FOLLOW_QSTN_in_opt649 = frozenset([1])
    FOLLOW_STAR_in_opt662 = frozenset([1])
    FOLLOW_PLUS_in_opt677 = frozenset([1])
    FOLLOW_testCase_in_testCases705 = frozenset([29])
    FOLLOW_testCases_in_testCases709 = frozenset([1])
    FOLLOW_QUOTE_STRING_in_testCase736 = frozenset([15])
    FOLLOW_EQ_in_testCase738 = frozenset([29, 30])
    FOLLOW_RA_BR_in_testCase741 = frozenset([29])
    FOLLOW_QUOTE_STRING_in_testCase747 = frozenset([1])
    FOLLOW_QUOTE_STRING_in_testCase756 = frozenset([1])
    FOLLOW_mResult_in_mResults779 = frozenset([16, 19, 25, 33, 42, 44])
    FOLLOW_mResults_in_mResults783 = frozenset([1])
    FOLLOW_labels_in_mResult809 = frozenset([21])
    FOLLOW_LC_BR_in_mResult811 = frozenset([16, 19, 29, 33, 42])
    FOLLOW_resultant_in_mResult813 = frozenset([31])
    FOLLOW_RC_BR_in_mResult815 = frozenset([1])
    FOLLOW_label_in_labels836 = frozenset([11])
    FOLLOW_labelsRest_in_labels838 = frozenset([1])
    FOLLOW_label_in_labels847 = frozenset([1])
    FOLLOW_COMMA_in_labelsRest864 = frozenset([16, 19, 25, 33, 42, 44])
    FOLLOW_labels_in_labelsRest866 = frozenset([1])
    FOLLOW_VAR_NAME_in_label886 = frozenset([1])
    FOLLOW_NUM_in_label893 = frozenset([1])
    FOLLOW_HASH_NAME_in_label900 = frozenset([41])
    FOLLOW_UNDERSCORE_NUM_in_label902 = frozenset([1])
    FOLLOW_HASH_NAME_in_label909 = frozenset([1])
    FOLLOW_KLEENE_in_label916 = frozenset([25])
    FOLLOW_NUM_in_label918 = frozenset([1])
    FOLLOW_REGEX_LABEL_in_label925 = frozenset([25])
    FOLLOW_NUM_in_label927 = frozenset([1])
    FOLLOW_WORD_in_label934 = frozenset([1])
    FOLLOW_results_in_resultant952 = frozenset([1])
    FOLLOW_result_in_results969 = frozenset([16, 19, 29, 33, 42])
    FOLLOW_results_in_results973 = frozenset([1])
    FOLLOW_QUOTE_STRING_in_result995 = frozenset([1])
    FOLLOW_VAR_NAME_in_result1002 = frozenset([1])
    FOLLOW_HASH_NAME_in_result1009 = frozenset([41])
    FOLLOW_UNDERSCORE_NUM_in_result1011 = frozenset([1])
    FOLLOW_HASH_NAME_in_result1018 = frozenset([1])
    FOLLOW_KLEENE_in_result1025 = frozenset([25])
    FOLLOW_NUM_in_result1027 = frozenset([20])
    FOLLOW_LA_BR_in_result1029 = frozenset([16, 19, 29, 30, 33, 42])
    FOLLOW_results_in_result1033 = frozenset([30])
    FOLLOW_RA_BR_in_result1035 = frozenset([22])
    FOLLOW_LR_BR_in_result1037 = frozenset([16, 19, 29, 33, 34, 42])
    FOLLOW_results_in_result1041 = frozenset([34])
    FOLLOW_RR_BR_in_result1043 = frozenset([1])
    FOLLOW_REGEX_LABEL_in_result1052 = frozenset([25])
    FOLLOW_NUM_in_result1054 = frozenset([22])
    FOLLOW_LR_BR_in_result1056 = frozenset([29])
    FOLLOW_QUOTE_STRING_in_result1058 = frozenset([34])
    FOLLOW_RR_BR_in_result1060 = frozenset([1])
    FOLLOW_REGEX_LABEL_in_result1067 = frozenset([25])
    FOLLOW_NUM_in_result1069 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SpeakPythonLexer", SpeakPythonParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
