# $ANTLR 3.4 SpeakPythonJSGF.g 2015-09-25 20:19:04

import sys
from antlr3 import *
#from antlr3.compat import set, frozenset
from sets import Set as set, ImmutableSet as frozenset


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


class SpeakPythonJSGFLexer(Lexer):

    grammarFileName = "SpeakPythonJSGF.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(SpeakPythonJSGFLexer, self).__init__(input, state)

        self.delegates = []




             
    commentMode = False;
    multiCommentMode = False;
    stringMode = False;



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):
        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:215:8: ( '||' (~ ( '\\r' | '\\n' ) )* )
            # SpeakPythonJSGF.g:215:10: '||' (~ ( '\\r' | '\\n' ) )*
            pass 
            self.match("||")


            # SpeakPythonJSGF.g:215:15: (~ ( '\\r' | '\\n' ) )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((0 <= LA1_0 <= 9) or (11 <= LA1_0 <= 12) or (14 <= LA1_0 <= 65535)) :
                    alt1 = 1


                if alt1 == 1:
                    # SpeakPythonJSGF.g:
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop1


            #action start
            _channel = HIDDEN; 
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "START_SQUOTE_STRING"
    def mSTART_SQUOTE_STRING(self, ):
        try:
            # SpeakPythonJSGF.g:224:29: ({...}? => '\\'' )
            # SpeakPythonJSGF.g:224:30: {...}? => '\\''
            pass 
            if not ((not (self.commentMode or self.multiCommentMode))):
                raise FailedPredicateException(self.input, "START_SQUOTE_STRING", "not (self.commentMode or self.multiCommentMode)")


            self.match(39)

            #action start
            self.stringMode = True; 
            #action end





        finally:
            pass

    # $ANTLR end "START_SQUOTE_STRING"



    # $ANTLR start "START_DQUOTE_STRING"
    def mSTART_DQUOTE_STRING(self, ):
        try:
            # SpeakPythonJSGF.g:225:29: ({...}? => '\"' )
            # SpeakPythonJSGF.g:225:30: {...}? => '\"'
            pass 
            if not ((not (self.commentMode or self.multiCommentMode))):
                raise FailedPredicateException(self.input, "START_DQUOTE_STRING", "not (self.commentMode or self.multiCommentMode)")


            self.match(34)

            #action start
            self.stringMode = True; 
            #action end





        finally:
            pass

    # $ANTLR end "START_DQUOTE_STRING"



    # $ANTLR start "INSIDE_SQUOTE_STRING"
    def mINSIDE_SQUOTE_STRING(self, ):
        try:
            # SpeakPythonJSGF.g:227:30: ({...}? => (~ ( '\\'' ) )* )
            # SpeakPythonJSGF.g:227:31: {...}? => (~ ( '\\'' ) )*
            pass 
            if not ((self.stringMode)):
                raise FailedPredicateException(self.input, "INSIDE_SQUOTE_STRING", "self.stringMode")


            # SpeakPythonJSGF.g:227:52: (~ ( '\\'' ) )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((0 <= LA2_0 <= 38) or (40 <= LA2_0 <= 65535)) :
                    alt2 = 1


                if alt2 == 1:
                    # SpeakPythonJSGF.g:
                    pass 
                    if (0 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop2





        finally:
            pass

    # $ANTLR end "INSIDE_SQUOTE_STRING"



    # $ANTLR start "INSIDE_DQUOTE_STRING"
    def mINSIDE_DQUOTE_STRING(self, ):
        try:
            # SpeakPythonJSGF.g:228:30: ({...}? => (~ ( '\"' ) )* )
            # SpeakPythonJSGF.g:228:31: {...}? => (~ ( '\"' ) )*
            pass 
            if not ((self.stringMode)):
                raise FailedPredicateException(self.input, "INSIDE_DQUOTE_STRING", "self.stringMode")


            # SpeakPythonJSGF.g:228:52: (~ ( '\"' ) )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((0 <= LA3_0 <= 33) or (35 <= LA3_0 <= 65535)) :
                    alt3 = 1


                if alt3 == 1:
                    # SpeakPythonJSGF.g:
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop3





        finally:
            pass

    # $ANTLR end "INSIDE_DQUOTE_STRING"



    # $ANTLR start "END_SQUOTE_STRING"
    def mEND_SQUOTE_STRING(self, ):
        try:
            # SpeakPythonJSGF.g:230:27: ({...}? => '\\'' )
            # SpeakPythonJSGF.g:230:28: {...}? => '\\''
            pass 
            if not ((self.stringMode)):
                raise FailedPredicateException(self.input, "END_SQUOTE_STRING", "self.stringMode")


            self.match(39)

            #action start
            self.stringMode = False; 
            #action end





        finally:
            pass

    # $ANTLR end "END_SQUOTE_STRING"



    # $ANTLR start "END_DQUOTE_STRING"
    def mEND_DQUOTE_STRING(self, ):
        try:
            # SpeakPythonJSGF.g:231:27: ({...}? => '\"' )
            # SpeakPythonJSGF.g:231:28: {...}? => '\"'
            pass 
            if not ((self.stringMode)):
                raise FailedPredicateException(self.input, "END_DQUOTE_STRING", "self.stringMode")


            self.match(34)

            #action start
            self.stringMode = False; 
            #action end





        finally:
            pass

    # $ANTLR end "END_DQUOTE_STRING"



    # $ANTLR start "QUOTE_STRING"
    def mQUOTE_STRING(self, ):
        try:
            _type = QUOTE_STRING
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:233:13: ( ( START_SQUOTE_STRING INSIDE_SQUOTE_STRING END_SQUOTE_STRING ) | ( START_DQUOTE_STRING INSIDE_DQUOTE_STRING END_DQUOTE_STRING ) )
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 39) and ((not (self.commentMode or self.multiCommentMode))):
                alt4 = 1
            elif (LA4_0 == 34) and ((not (self.commentMode or self.multiCommentMode))):
                alt4 = 2
            else:
                nvae = NoViableAltException("", 4, 0, self.input)

                raise nvae


            if alt4 == 1:
                # SpeakPythonJSGF.g:233:15: ( START_SQUOTE_STRING INSIDE_SQUOTE_STRING END_SQUOTE_STRING )
                pass 
                # SpeakPythonJSGF.g:233:15: ( START_SQUOTE_STRING INSIDE_SQUOTE_STRING END_SQUOTE_STRING )
                # SpeakPythonJSGF.g:233:16: START_SQUOTE_STRING INSIDE_SQUOTE_STRING END_SQUOTE_STRING
                pass 
                self.mSTART_SQUOTE_STRING()


                self.mINSIDE_SQUOTE_STRING()


                self.mEND_SQUOTE_STRING()






            elif alt4 == 2:
                # SpeakPythonJSGF.g:234:5: ( START_DQUOTE_STRING INSIDE_DQUOTE_STRING END_DQUOTE_STRING )
                pass 
                # SpeakPythonJSGF.g:234:5: ( START_DQUOTE_STRING INSIDE_DQUOTE_STRING END_DQUOTE_STRING )
                # SpeakPythonJSGF.g:234:6: START_DQUOTE_STRING INSIDE_DQUOTE_STRING END_DQUOTE_STRING
                pass 
                self.mSTART_DQUOTE_STRING()


                self.mINSIDE_DQUOTE_STRING()


                self.mEND_DQUOTE_STRING()






            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "QUOTE_STRING"



    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):
        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:237:8: ( ( '\\r' )? '\\n' )
            # SpeakPythonJSGF.g:237:10: ( '\\r' )? '\\n'
            pass 
            # SpeakPythonJSGF.g:237:10: ( '\\r' )?
            alt5 = 2
            LA5_0 = self.input.LA(1)

            if (LA5_0 == 13) :
                alt5 = 1
            if alt5 == 1:
                # SpeakPythonJSGF.g:237:11: '\\r'
                pass 
                self.match(13)




            self.match(10)

            #action start
            _channel = HIDDEN; 
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEWLINE"



    # $ANTLR start "WHITE_SPACE"
    def mWHITE_SPACE(self, ):
        try:
            _type = WHITE_SPACE
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:238:12: ( ( ' ' | '\\t' )+ )
            # SpeakPythonJSGF.g:238:14: ( ' ' | '\\t' )+
            pass 
            # SpeakPythonJSGF.g:238:14: ( ' ' | '\\t' )+
            cnt6 = 0
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 9 or LA6_0 == 32) :
                    alt6 = 1


                if alt6 == 1:
                    # SpeakPythonJSGF.g:
                    pass 
                    if self.input.LA(1) == 9 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt6 >= 1:
                        break #loop6

                    eee = EarlyExitException(6, self.input)
                    raise eee

                cnt6 += 1


            #action start
            _channel = HIDDEN; 
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WHITE_SPACE"



    # $ANTLR start "REGEX"
    def mREGEX(self, ):
        try:
            _type = REGEX
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:240:6: ({...}? => '/' ( . )+ '/r' )
            # SpeakPythonJSGF.g:240:7: {...}? => '/' ( . )+ '/r'
            pass 
            if not ((not self.stringMode)):
                raise FailedPredicateException(self.input, "REGEX", "not self.stringMode")


            self.match(47)

            # SpeakPythonJSGF.g:240:35: ( . )+
            cnt7 = 0
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == 47) :
                    LA7_1 = self.input.LA(2)

                    if (LA7_1 == 114) :
                        alt7 = 2
                    elif ((0 <= LA7_1 <= 113) or (115 <= LA7_1 <= 65535)) :
                        alt7 = 1


                elif ((0 <= LA7_0 <= 46) or (48 <= LA7_0 <= 65535)) :
                    alt7 = 1


                if alt7 == 1:
                    # SpeakPythonJSGF.g:240:35: .
                    pass 
                    self.matchAny()


                else:
                    if cnt7 >= 1:
                        break #loop7

                    eee = EarlyExitException(7, self.input)
                    raise eee

                cnt7 += 1


            self.match("/r")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "REGEX"



    # $ANTLR start "QSTN"
    def mQSTN(self, ):
        try:
            _type = QSTN
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:242:5: ( '?' )
            # SpeakPythonJSGF.g:242:7: '?'
            pass 
            self.match(63)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "QSTN"



    # $ANTLR start "TILDE"
    def mTILDE(self, ):
        try:
            _type = TILDE
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:243:6: ( '~' )
            # SpeakPythonJSGF.g:243:8: '~'
            pass 
            self.match(126)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TILDE"



    # $ANTLR start "B_ARROW"
    def mB_ARROW(self, ):
        try:
            _type = B_ARROW
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:244:8: ( '<-' )
            # SpeakPythonJSGF.g:244:10: '<-'
            pass 
            self.match("<-")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "B_ARROW"



    # $ANTLR start "ARROW"
    def mARROW(self, ):
        try:
            _type = ARROW
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:245:6: ( '->' )
            # SpeakPythonJSGF.g:245:8: '->'
            pass 
            self.match("->")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ARROW"



    # $ANTLR start "LS_BR"
    def mLS_BR(self, ):
        try:
            _type = LS_BR
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:246:6: ( '[' )
            # SpeakPythonJSGF.g:246:8: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LS_BR"



    # $ANTLR start "RS_BR"
    def mRS_BR(self, ):
        try:
            _type = RS_BR
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:247:6: ( ']' )
            # SpeakPythonJSGF.g:247:8: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RS_BR"



    # $ANTLR start "LC_BR"
    def mLC_BR(self, ):
        try:
            _type = LC_BR
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:248:6: ( '{' )
            # SpeakPythonJSGF.g:248:8: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LC_BR"



    # $ANTLR start "RC_BR"
    def mRC_BR(self, ):
        try:
            _type = RC_BR
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:249:6: ( '}' )
            # SpeakPythonJSGF.g:249:8: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RC_BR"



    # $ANTLR start "LR_BR"
    def mLR_BR(self, ):
        try:
            _type = LR_BR
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:250:6: ( '(' )
            # SpeakPythonJSGF.g:250:8: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LR_BR"



    # $ANTLR start "RR_BR"
    def mRR_BR(self, ):
        try:
            _type = RR_BR
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:251:6: ( ')' )
            # SpeakPythonJSGF.g:251:8: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RR_BR"



    # $ANTLR start "LA_BR"
    def mLA_BR(self, ):
        try:
            _type = LA_BR
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:252:6: ( '<' )
            # SpeakPythonJSGF.g:252:8: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LA_BR"



    # $ANTLR start "RA_BR"
    def mRA_BR(self, ):
        try:
            _type = RA_BR
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:253:6: ( '>' )
            # SpeakPythonJSGF.g:253:8: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RA_BR"



    # $ANTLR start "OR"
    def mOR(self, ):
        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:254:3: ( '|' )
            # SpeakPythonJSGF.g:254:5: '|'
            pass 
            self.match(124)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OR"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):
        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:255:6: ( ',' )
            # SpeakPythonJSGF.g:255:8: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "SEMI"
    def mSEMI(self, ):
        try:
            _type = SEMI
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:256:5: ( ';' )
            # SpeakPythonJSGF.g:256:7: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SEMI"



    # $ANTLR start "EQ"
    def mEQ(self, ):
        try:
            _type = EQ
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:257:3: ( '=' )
            # SpeakPythonJSGF.g:257:5: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EQ"



    # $ANTLR start "AT_TESTS"
    def mAT_TESTS(self, ):
        try:
            _type = AT_TESTS
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:258:9: ( '@tests' )
            # SpeakPythonJSGF.g:258:11: '@tests'
            pass 
            self.match("@tests")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AT_TESTS"



    # $ANTLR start "AT_RESULTS"
    def mAT_RESULTS(self, ):
        try:
            _type = AT_RESULTS
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:259:11: ( '@results' )
            # SpeakPythonJSGF.g:259:13: '@results'
            pass 
            self.match("@results")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AT_RESULTS"



    # $ANTLR start "AT_GLOBAL_OPTIONS"
    def mAT_GLOBAL_OPTIONS(self, ):
        try:
            _type = AT_GLOBAL_OPTIONS
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:260:18: ( '@globalOptions' )
            # SpeakPythonJSGF.g:260:20: '@globalOptions'
            pass 
            self.match("@globalOptions")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AT_GLOBAL_OPTIONS"



    # $ANTLR start "AT_OPTIONS"
    def mAT_OPTIONS(self, ):
        try:
            _type = AT_OPTIONS
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:261:11: ( '@options' )
            # SpeakPythonJSGF.g:261:13: '@options'
            pass 
            self.match("@options")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AT_OPTIONS"



    # $ANTLR start "AT"
    def mAT(self, ):
        try:
            _type = AT
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:262:3: ( '@' )
            # SpeakPythonJSGF.g:262:5: '@'
            pass 
            self.match(64)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AT"



    # $ANTLR start "PLUS"
    def mPLUS(self, ):
        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:263:5: ( '+' )
            # SpeakPythonJSGF.g:263:7: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "STAR"
    def mSTAR(self, ):
        try:
            _type = STAR
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:264:5: ( '*' )
            # SpeakPythonJSGF.g:264:7: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STAR"



    # $ANTLR start "UNDERSCORE_NUM"
    def mUNDERSCORE_NUM(self, ):
        try:
            _type = UNDERSCORE_NUM
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:265:15: ( '_' ( '0' .. '9' )+ )
            # SpeakPythonJSGF.g:265:17: '_' ( '0' .. '9' )+
            pass 
            self.match(95)

            # SpeakPythonJSGF.g:265:21: ( '0' .. '9' )+
            cnt8 = 0
            while True: #loop8
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if ((48 <= LA8_0 <= 57)) :
                    alt8 = 1


                if alt8 == 1:
                    # SpeakPythonJSGF.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt8 >= 1:
                        break #loop8

                    eee = EarlyExitException(8, self.input)
                    raise eee

                cnt8 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "UNDERSCORE_NUM"



    # $ANTLR start "KLEENE"
    def mKLEENE(self, ):
        try:
            _type = KLEENE
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:266:7: ( 'k_' )
            # SpeakPythonJSGF.g:266:9: 'k_'
            pass 
            self.match("k_")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KLEENE"



    # $ANTLR start "REGEX_LABEL"
    def mREGEX_LABEL(self, ):
        try:
            _type = REGEX_LABEL
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:267:12: ( 'r_' )
            # SpeakPythonJSGF.g:267:14: 'r_'
            pass 
            self.match("r_")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "REGEX_LABEL"



    # $ANTLR start "VAR_NAME"
    def mVAR_NAME(self, ):
        try:
            _type = VAR_NAME
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:269:9: ( '$' ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' )* )
            # SpeakPythonJSGF.g:269:11: '$' ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' )*
            pass 
            self.match(36)

            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # SpeakPythonJSGF.g:269:33: ( 'a' .. 'z' | 'A' .. 'Z' )*
            while True: #loop9
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if ((65 <= LA9_0 <= 90) or (97 <= LA9_0 <= 122)) :
                    alt9 = 1


                if alt9 == 1:
                    # SpeakPythonJSGF.g:
                    pass 
                    if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop9




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "VAR_NAME"



    # $ANTLR start "HASH_NAME"
    def mHASH_NAME(self, ):
        try:
            _type = HASH_NAME
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:270:10: ( '#' ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )* )
            # SpeakPythonJSGF.g:270:12: '#' ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )*
            pass 
            self.match(35)

            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # SpeakPythonJSGF.g:270:34: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )*
            while True: #loop10
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if ((48 <= LA10_0 <= 57) or (65 <= LA10_0 <= 90) or (97 <= LA10_0 <= 122)) :
                    alt10 = 1


                if alt10 == 1:
                    # SpeakPythonJSGF.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop10




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "HASH_NAME"



    # $ANTLR start "NUM"
    def mNUM(self, ):
        try:
            _type = NUM
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:271:4: ( ( '0' .. '9' )+ )
            # SpeakPythonJSGF.g:271:6: ( '0' .. '9' )+
            pass 
            # SpeakPythonJSGF.g:271:6: ( '0' .. '9' )+
            cnt11 = 0
            while True: #loop11
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if ((48 <= LA11_0 <= 57)) :
                    alt11 = 1


                if alt11 == 1:
                    # SpeakPythonJSGF.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt11 >= 1:
                        break #loop11

                    eee = EarlyExitException(11, self.input)
                    raise eee

                cnt11 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NUM"



    # $ANTLR start "WORD"
    def mWORD(self, ):
        try:
            _type = WORD
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:272:5: ( ( 'a' .. 'z' | 'A' .. 'Z' )+ )
            # SpeakPythonJSGF.g:272:7: ( 'a' .. 'z' | 'A' .. 'Z' )+
            pass 
            # SpeakPythonJSGF.g:272:7: ( 'a' .. 'z' | 'A' .. 'Z' )+
            cnt12 = 0
            while True: #loop12
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if ((65 <= LA12_0 <= 90) or (97 <= LA12_0 <= 122)) :
                    alt12 = 1


                if alt12 == 1:
                    # SpeakPythonJSGF.g:
                    pass 
                    if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt12 >= 1:
                        break #loop12

                    eee = EarlyExitException(12, self.input)
                    raise eee

                cnt12 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WORD"



    def mTokens(self):
        # SpeakPythonJSGF.g:1:8: ( COMMENT | QUOTE_STRING | NEWLINE | WHITE_SPACE | REGEX | QSTN | TILDE | B_ARROW | ARROW | LS_BR | RS_BR | LC_BR | RC_BR | LR_BR | RR_BR | LA_BR | RA_BR | OR | COMMA | SEMI | EQ | AT_TESTS | AT_RESULTS | AT_GLOBAL_OPTIONS | AT_OPTIONS | AT | PLUS | STAR | UNDERSCORE_NUM | KLEENE | REGEX_LABEL | VAR_NAME | HASH_NAME | NUM | WORD )
        alt13 = 35
        LA13_0 = self.input.LA(1)

        if (LA13_0 == 124) :
            LA13_1 = self.input.LA(2)

            if (LA13_1 == 124) :
                alt13 = 1
            else:
                alt13 = 18

        elif (LA13_0 == 34 or LA13_0 == 39) and ((not (self.commentMode or self.multiCommentMode))):
            alt13 = 2
        elif (LA13_0 == 10 or LA13_0 == 13) :
            alt13 = 3
        elif (LA13_0 == 9 or LA13_0 == 32) :
            alt13 = 4
        elif (LA13_0 == 47) and ((not self.stringMode)):
            alt13 = 5
        elif (LA13_0 == 63) :
            alt13 = 6
        elif (LA13_0 == 126) :
            alt13 = 7
        elif (LA13_0 == 60) :
            LA13_8 = self.input.LA(2)

            if (LA13_8 == 45) :
                alt13 = 8
            else:
                alt13 = 16

        elif (LA13_0 == 45) :
            alt13 = 9
        elif (LA13_0 == 91) :
            alt13 = 10
        elif (LA13_0 == 93) :
            alt13 = 11
        elif (LA13_0 == 123) :
            alt13 = 12
        elif (LA13_0 == 125) :
            alt13 = 13
        elif (LA13_0 == 40) :
            alt13 = 14
        elif (LA13_0 == 41) :
            alt13 = 15
        elif (LA13_0 == 62) :
            alt13 = 17
        elif (LA13_0 == 44) :
            alt13 = 19
        elif (LA13_0 == 59) :
            alt13 = 20
        elif (LA13_0 == 61) :
            alt13 = 21
        elif (LA13_0 == 64) :
            LA13 = self.input.LA(2)
            if LA13 == 116:
                alt13 = 22
            elif LA13 == 114:
                alt13 = 23
            elif LA13 == 103:
                alt13 = 24
            elif LA13 == 111:
                alt13 = 25
            else:
                alt13 = 26

        elif (LA13_0 == 43) :
            alt13 = 27
        elif (LA13_0 == 42) :
            alt13 = 28
        elif (LA13_0 == 95) :
            alt13 = 29
        elif (LA13_0 == 107) :
            LA13_24 = self.input.LA(2)

            if (LA13_24 == 95) :
                alt13 = 30
            else:
                alt13 = 35

        elif (LA13_0 == 114) :
            LA13_25 = self.input.LA(2)

            if (LA13_25 == 95) :
                alt13 = 31
            else:
                alt13 = 35

        elif (LA13_0 == 36) :
            alt13 = 32
        elif (LA13_0 == 35) :
            alt13 = 33
        elif ((48 <= LA13_0 <= 57)) :
            alt13 = 34
        elif ((65 <= LA13_0 <= 90) or (97 <= LA13_0 <= 106) or (108 <= LA13_0 <= 113) or (115 <= LA13_0 <= 122)) :
            alt13 = 35
        else:
            nvae = NoViableAltException("", 13, 0, self.input)

            raise nvae


        if alt13 == 1:
            # SpeakPythonJSGF.g:1:10: COMMENT
            pass 
            self.mCOMMENT()



        elif alt13 == 2:
            # SpeakPythonJSGF.g:1:18: QUOTE_STRING
            pass 
            self.mQUOTE_STRING()



        elif alt13 == 3:
            # SpeakPythonJSGF.g:1:31: NEWLINE
            pass 
            self.mNEWLINE()



        elif alt13 == 4:
            # SpeakPythonJSGF.g:1:39: WHITE_SPACE
            pass 
            self.mWHITE_SPACE()



        elif alt13 == 5:
            # SpeakPythonJSGF.g:1:51: REGEX
            pass 
            self.mREGEX()



        elif alt13 == 6:
            # SpeakPythonJSGF.g:1:57: QSTN
            pass 
            self.mQSTN()



        elif alt13 == 7:
            # SpeakPythonJSGF.g:1:62: TILDE
            pass 
            self.mTILDE()



        elif alt13 == 8:
            # SpeakPythonJSGF.g:1:68: B_ARROW
            pass 
            self.mB_ARROW()



        elif alt13 == 9:
            # SpeakPythonJSGF.g:1:76: ARROW
            pass 
            self.mARROW()



        elif alt13 == 10:
            # SpeakPythonJSGF.g:1:82: LS_BR
            pass 
            self.mLS_BR()



        elif alt13 == 11:
            # SpeakPythonJSGF.g:1:88: RS_BR
            pass 
            self.mRS_BR()



        elif alt13 == 12:
            # SpeakPythonJSGF.g:1:94: LC_BR
            pass 
            self.mLC_BR()



        elif alt13 == 13:
            # SpeakPythonJSGF.g:1:100: RC_BR
            pass 
            self.mRC_BR()



        elif alt13 == 14:
            # SpeakPythonJSGF.g:1:106: LR_BR
            pass 
            self.mLR_BR()



        elif alt13 == 15:
            # SpeakPythonJSGF.g:1:112: RR_BR
            pass 
            self.mRR_BR()



        elif alt13 == 16:
            # SpeakPythonJSGF.g:1:118: LA_BR
            pass 
            self.mLA_BR()



        elif alt13 == 17:
            # SpeakPythonJSGF.g:1:124: RA_BR
            pass 
            self.mRA_BR()



        elif alt13 == 18:
            # SpeakPythonJSGF.g:1:130: OR
            pass 
            self.mOR()



        elif alt13 == 19:
            # SpeakPythonJSGF.g:1:133: COMMA
            pass 
            self.mCOMMA()



        elif alt13 == 20:
            # SpeakPythonJSGF.g:1:139: SEMI
            pass 
            self.mSEMI()



        elif alt13 == 21:
            # SpeakPythonJSGF.g:1:144: EQ
            pass 
            self.mEQ()



        elif alt13 == 22:
            # SpeakPythonJSGF.g:1:147: AT_TESTS
            pass 
            self.mAT_TESTS()



        elif alt13 == 23:
            # SpeakPythonJSGF.g:1:156: AT_RESULTS
            pass 
            self.mAT_RESULTS()



        elif alt13 == 24:
            # SpeakPythonJSGF.g:1:167: AT_GLOBAL_OPTIONS
            pass 
            self.mAT_GLOBAL_OPTIONS()



        elif alt13 == 25:
            # SpeakPythonJSGF.g:1:185: AT_OPTIONS
            pass 
            self.mAT_OPTIONS()



        elif alt13 == 26:
            # SpeakPythonJSGF.g:1:196: AT
            pass 
            self.mAT()



        elif alt13 == 27:
            # SpeakPythonJSGF.g:1:199: PLUS
            pass 
            self.mPLUS()



        elif alt13 == 28:
            # SpeakPythonJSGF.g:1:204: STAR
            pass 
            self.mSTAR()



        elif alt13 == 29:
            # SpeakPythonJSGF.g:1:209: UNDERSCORE_NUM
            pass 
            self.mUNDERSCORE_NUM()



        elif alt13 == 30:
            # SpeakPythonJSGF.g:1:224: KLEENE
            pass 
            self.mKLEENE()



        elif alt13 == 31:
            # SpeakPythonJSGF.g:1:231: REGEX_LABEL
            pass 
            self.mREGEX_LABEL()



        elif alt13 == 32:
            # SpeakPythonJSGF.g:1:243: VAR_NAME
            pass 
            self.mVAR_NAME()



        elif alt13 == 33:
            # SpeakPythonJSGF.g:1:252: HASH_NAME
            pass 
            self.mHASH_NAME()



        elif alt13 == 34:
            # SpeakPythonJSGF.g:1:262: NUM
            pass 
            self.mNUM()



        elif alt13 == 35:
            # SpeakPythonJSGF.g:1:266: WORD
            pass 
            self.mWORD()








 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(SpeakPythonJSGFLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
