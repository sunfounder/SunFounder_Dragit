/*
#SpeakPython allows developers to add speech recognition support to their Python applications
#Copyright (C) 2015  Eric Matthews

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by 
#the Free Software Foundation, either version 3 of the License, or 
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of 
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

grammar SpeakPythonJSGF;

options
{
	language=Python;
	backtrack=true;
}

@members
{
optionVals = {};
optionValsBackup = optionVals;

rules = [];
aliasRules = {};

parseFailed = False;
messages = {'regex': "We're sorry, regex is not supported in JSGF at this time",
		'variable': "We're sorry, variables are not supported in JSGF at this time"};
}

@lexer::members
{
commentMode = False;
multiCommentMode = False;
stringMode = False;
}

prog
@init
{
self.optionVals['wordRegex'] = '[a-zA-Z0-9_\\+\\.\\-]+';
self.optionVals['varRegex'] = '[a-zA-Z0-9_\\+\\.\\-]+';
self.optionVals['wordDelim'] = '[ ,/]+';
}
	: s EOF {}
	;

s
@init
{
}
	: alias { } s 
	| mat { self.rules.append($mat.matR); } s 
	| globalOptions s
	| {}
	;

globalOptions
	: AT_GLOBAL_OPTIONS myOptions AT
	;

localOptions
	: AT_OPTIONS { self.optionValsBackup = self.optionVals; self.optionVals = self.optionValsBackup.copy(); } myOptions AT
	;

myOptions
	: myOption myOptions
	| {}
	;

myOption
	: WORD EQ (RA_BR)? REGEX (SEMI)? { self.optionVals[$WORD.text] = $REGEX.text[1:-2]; }
	;

/*Returns a Match() object*/
mat returns [matR]
@init
{
}
	: (localOptions)? exps
			{ self.optionVals = self.optionValsBackup; }
		statementFields
			{ $matR = $exps.expsR; }
	;

statementFields
	: AT_RESULTS mResults AT statementFields
		{ }
	| AT_TESTS testCases AT statementFields
		{ }
	| {}
	;

alias returns [aliasR]
	: HASH_NAME LR_BR RR_BR EQ exps statementFields
		{ self.aliasRules[$HASH_NAME.text[1:]] = $exps.expsR; }
	;

exps returns [expsR='']
	: expVal SEMI { $expsR = $expVal.expValR + ";"; }
	;

//returns an expression derivative
expVal returns [expValR='']
	: LS_BR e1=expVal RS_BR opt subExp
			{ $expValR = $opt.optR[0] + $e1.expValR + $opt.optR[1] + $subExp.subExpR; }

	| LR_BR e2=expVal RR_BR opt subExp
			{ $expValR = $opt.optR[0] + $e2.expValR + $opt.optR[1] + $subExp.subExpR; }

	| w1=WORD subExp
			{ $expValR = $w1.text + $subExp.subExpR; }

	| VAR_NAME subExp
			{ if (self.messages['variable'] != None): print self.messages['variable']; self.messages['variable'] = None; self.parseFailed = True; $expValR = $subExp.subExpR; }

	| HASH_NAME subExp
			{ name = $HASH_NAME.text[1:]; }
			{ if (name not in self.aliasRules): print "The rule <" + name + "> does not exist before it is referenced."; }
			{ $expValR = "<" + name + ">" + $subExp.subExpR; }

	| REGEX	subExp
			{ if (self.messages['regex'] != None): print self.messages['regex']; self.messages['regex'] = None; self.parseFailed = True; $expValR = $subExp.subExpR; }
	;

//this subExp handles OR properly so that we can't have OR OR OR expVal
subExp returns [subExpR='']
	: expVal
			{ $subExpR = " " + $expVal.expValR; }
	| OR expVal { $subExpR = " | " + $expVal.expValR; }
	| {}
	; 

//returns a prefix, and a suffix to attach to the expression
opt returns [optR=('(',')')]
	: QSTN { $optR=("[", "]"); }
	| STAR { $optR=("(", ")*"); }
	| PLUS { $optR=("(", ")+"); }
	| {}
	;

testCases returns [testCasesR=[\]]
	: testCase ts=testCases { }
	| { }
	;

testCase returns [testCaseR='']
	: q1=QUOTE_STRING EQ (RA_BR)? q2=QUOTE_STRING { }
	| q3=QUOTE_STRING
		{ }
	;

/*Returns a list of Result() objects*/
mResults
	: m1=mResult ms=mResults { }
	| { }
	;

/*Returns a Result() object*/
mResult
	: ls=labels LC_BR resultant RC_BR { }
	;

/*Returns a list of numeric labels*/
labels
	: l1=label labelsRest { }
	| l2=label { }
	;

labelsRest
	: COMMA labels { }
	;
	
/*Returns a numeric label*/
label
	: VAR_NAME { }
	| NUM { }
	| HASH_NAME UNDERSCORE_NUM { }
	| HASH_NAME { }
	| KLEENE NUM { }
	| REGEX_LABEL NUM { }
	| WORD { }
	;

//Parse result list
resultant
	: results { }
	;

results
	: result results {}
	| {}
	;

result
	: QUOTE_STRING { }
	| VAR_NAME { }
	| HASH_NAME UNDERSCORE_NUM { }
	| HASH_NAME { }
	| KLEENE NUM LA_BR results RA_BR LR_BR results RR_BR { }
	| REGEX_LABEL NUM LR_BR QUOTE_STRING RR_BR {}
	| REGEX_LABEL NUM {}
	;

/*Single line comment*/
COMMENT: '||' (~('\r'|'\n'))* { $channel = HIDDEN; };

/*multi-line comment*/
/*
START_MULTI_COMMENT:{not self.stringMode}?=> '|{' { $channel = HIDDEN; self.multiCommentMode = True; };
INSIDE_MULTI_COMMENT:{self.multiCommentMode}?=> .* '}|' { $channel = HIDDEN; self.multiCommentMode = False; };
*/

/*string rules*/
fragment START_SQUOTE_STRING:{not (self.commentMode or self.multiCommentMode)}?=> '\'' { self.stringMode = True; };
fragment START_DQUOTE_STRING:{not (self.commentMode or self.multiCommentMode)}?=> '"' { self.stringMode = True; };

fragment INSIDE_SQUOTE_STRING:{self.stringMode}?=> ~('\'')*;
fragment INSIDE_DQUOTE_STRING:{self.stringMode}?=> ~('"')*;

fragment END_SQUOTE_STRING:{self.stringMode}?=> '\'' { self.stringMode = False; };
fragment END_DQUOTE_STRING:{self.stringMode}?=> '"' { self.stringMode = False; };

QUOTE_STRING: (START_SQUOTE_STRING INSIDE_SQUOTE_STRING END_SQUOTE_STRING)
		| (START_DQUOTE_STRING INSIDE_DQUOTE_STRING END_DQUOTE_STRING);
/*end of string rules*/

NEWLINE: ('\r')?'\n' { $channel = HIDDEN; };
WHITE_SPACE: (' '|'\t')+ { $channel = HIDDEN; };

REGEX:{not self.stringMode}?=> '/'.+'/r';

QSTN: '?';
TILDE: '~';
B_ARROW: '<-';
ARROW: '->';
LS_BR: '[';
RS_BR: ']';
LC_BR: '{';
RC_BR: '}';
LR_BR: '(';
RR_BR: ')';
LA_BR: '<';
RA_BR: '>';
OR: '|';
COMMA: ',';
SEMI: ';';
EQ: '=';
AT_TESTS: '@tests';
AT_RESULTS: '@results';
AT_GLOBAL_OPTIONS: '@globalOptions';
AT_OPTIONS: '@options';
AT: '@';
PLUS: '+';
STAR: '*';
UNDERSCORE_NUM: '_' ('0'..'9')+;
KLEENE: 'k_';
REGEX_LABEL: 'r_';

VAR_NAME: '$'('a'..'z'|'A'..'Z')('a'..'z'|'A'..'Z')*;
HASH_NAME: '#'('a'..'z'|'A'..'Z')('a'..'z'|'A'..'Z'|'0'..'9')*;
NUM: ('0'..'9')+;
WORD: ('a'..'z'|'A'..'Z')+;
