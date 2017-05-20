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
grammar SpeakPython;

options
{
	language=Python;
	backtrack=true;
}

@header
{
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
}

@members
{
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
	self.optionVals['wordDelim'] = '[ ,/]';

	self.defaultOptionVals = self.optionVals.copy();
}
	: s EOF {}
	;

s
@init
{
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
}
	: alias { self.aliases[self.aliasWord] = $alias.aliasR; } s 
	| mat { self.matches.append($mat.matR); } s 
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
	self.keywords = [];
	self.regexCount = 0;
	self.regexes = {};
}
	: (localOptions)? exps
			{ self.optionVals = self.optionValsBackup; }
		statementFields
			{ $matR = Match($exps.expsR, self.statementFieldDict['testCases'], self.keywords, self.kGroupRegexes, self.statementFieldDict['results']); }
	;

statementFields
	: AT_RESULTS mResults AT statementFields
		{ self.statementFieldDict['results'] = $mResults.mResultsR; }
	| AT_TESTS testCases AT statementFields
		{ self.statementFieldDict['testCases'] = $testCases.testCasesR; }
	| {}
	;

alias returns [aliasR]
	: HASH_NAME
			{ self.aliasWord = $HASH_NAME.text[1:]; }
		LR_BR RR_BR EQ exps
			//save the state of what keyword variables were when we finished parsing expression
			{ self.aliasKeywordState[self.aliasWord] = (self.isKeyword, self.finishedKeywords); }
			//save list of alias keywords for use in later matches
			{ self.aliasKeywords[self.aliasWord] = self.keywords; }
		statementFields
			//compile result of alias
			{ $aliasR = Function(self.aliasWord, $exps.expsR, self.statementFieldDict['testCases'], self.kGroupRegexes, self.statementFieldDict['results']); }
	;

exps returns [expsR='']
	: expVal SEMI { $expsR = sub(r"\?P<\*>", GroupCounter(), $expVal.expValR); }
	;

//returns an expression derivative
expVal returns [expValR='']
	: LS_BR
			{ self.bracketCount += 1; }
		e1=expVal RS_BR
			{ self.bracketCount -= 1; }
		opt
			{ if (self.bracketCount == 0 and ($opt.optR[1] not in "?*" or len($opt.optR[1]) == 0)): self.finishedKeywords = True; self.wordAtBracket = 0; }
			{ if self.isKleene: self.kGroupRegexes[str(self.kGroupCount)] = $e1.expValR; self.kGroupCount += 1; self.isKleene = False; }
		subExp
			{ $expValR = $opt.optR[0] + "(?P<*>" + $e1.expValR + ")" + $opt.optR[1] + $subExp.subExpR; }

	| LR_BR
			{ self.bracketCount += 1; }
		e2=expVal RR_BR
			{ self.bracketCount -= 1; }
		opt
			/*Finish keywords if past word was not optional*/
			{ if (self.bracketCount == 0 and ($opt.optR[1] not in "?*" or len($opt.optR[1]) == 0)): self.finishedKeywords = True; self.wordAtBracket = 0; }
			/*Perform kleene-specific operations*/
			{ if self.isKleene: self.kGroupRegexes[str(self.kGroupCount)] = $e2.expValR; self.kGroupCount += 1; self.isKleene = False; }

		subExp
			/*Build result*/
			{ $expValR = $opt.optR[0] + "(?:" + $e2.expValR + ")" + $opt.optR[1] + $subExp.subExpR; }

	| w1=WORD
			{ if (self.isKeyword and not self.finishedKeywords): self.keywords.append(w1.text.lower()); self.isKeyword = False; self.wordAtBracket = self.bracketCount; } { if (self.bracketCount == 0): self.finishedKeywords = True; }
		subExp
			{ $expValR = "(?:" + $w1.text.lower() + ")" + $subExp.subExpR; }

	| VAR_NAME
			{ if (self.isKeyword and not self.finishedKeywords): self.keywords.append("*"); self.isKeyword = False; self.wordAtBracket = self.bracketCount; } { if (self.bracketCount == 0): self.finishedKeywords = True; }
		subExp
			{ $expValR = "(?P<" + $VAR_NAME.text[1:] + ">" + self.optionVals['varRegex'] + ")" + $subExp.subExpR; }

	| HASH_NAME
			{ name = $HASH_NAME.text[1:]; self.aliasUseCount[name] = 0 if (name not in self.aliasUseCount) else self.aliasUseCount[name] + 1; }
			{ aliasUseCount = self.aliasUseCount[name]; }

			{ if (self.isKeyword and not self.finishedKeywords): self.keywords.extend(self.aliasKeywords[name]); self.isKeyword = self.aliasKeywordState[name][0]; self.wordAtBracket = self.bracketCount; }
			{ if (self.bracketCount == 0): self.finishedKeywords = self.aliasKeywordState[name][1]; }
		subExp
			{ retVal = $subExp.subExpR; }
			{ retVal = "(?P<" + "_" + name + "_" + str(aliasUseCount) + "_>" + sub(r"<([^>]+)>", "<_" + name + "_" + str(aliasUseCount) + r"_\g<1>" + ">", self.aliases[name].getExp()) + ")" + $subExp.subExpR; }
			{ $expValR = retVal; }

	| REGEX
			{ if (self.isKeyword and not self.finishedKeywords): self.keywords.append("*"); self.isKeyword = False; self.wordAtBracket = self.bracketCount; }
			//make regex a python regex if not already one, and make all numbered capture groups non-capture
			{ reg = $REGEX.text[1:-2]; reg = sub(r"\(\?<([^>]+)>", r"(?P<\1>", reg); reg = sub(r"\([^\?]", r"(?:", reg); self.regexes[str(self.regexCount)] = reg; regexString = "(?P<r_" + str(self.regexCount) + ">" + reg + ")"; self.regexCount += 1; }
		subExp
			{ $expValR = regexString + $subExp.subExpR; }
	;

//this subExp handles OR properly so that we can't have OR OR OR expVal
subExp returns [subExpR='']
	: expVal
			{ $subExpR = self.optionVals['wordDelim'] + "*" + $expVal.expValR; }
	| OR 
			{ if (self.bracketCount <= self.wordAtBracket): self.isKeyword = True; self.finishedKeywords = False; }
		 expVal
			{ $subExpR = "|" + $expVal.expValR; }
	
	| {}
	; 

//returns a prefix, and a suffix to attach to the expression
opt returns [optR=('','')]
	: QSTN
		{ if (self.bracketCount < self.wordAtBracket): self.isKeyword = True; }
		{ $optR=("","?"); }
	| STAR
		{ self.isKleene = True; }
		{ if (self.bracketCount < self.wordAtBracket): self.isKeyword = True; } { $optR=("(?P<k_" + str(self.kGroupCount) + ">(?:", self.optionVals['wordDelim'] + "+)*)"); }
	| PLUS
		{ self.isKleene = True; }
		{ $optR=("(?P<k_" + str(self.kGroupCount) + ">(?:", self.optionVals['wordDelim'] + "+)+)"); }
	| {}
	;

testCases returns [testCasesR=[\]]
	: testCase ts=testCases
			{ $ts.testCasesR.append($testCase.testCaseR); $testCasesR = $ts.testCasesR; }
	| {}
	;

testCase returns [testCaseR='']
	: q1=QUOTE_STRING EQ (RA_BR)? q2=QUOTE_STRING { self.globalTests[$q1.text[1:-1]] = $q2.text[1:-1]; $testCaseR = $q1.text[1:-1]; }
	| q3=QUOTE_STRING
		{ $testCaseR = $q3.text[1:-1]; }
	;

/*Returns a list of Result() objects*/
mResults returns [mResultsR=[\]]
	: m1=mResult ms=mResults { $ms.mResultsR.append($m1.mResultR); $mResultsR = $ms.mResultsR; }
	| { $mResultsR = []; }
	;

/*Returns a Result() object*/
mResult returns [mResultR]
	: ls=labels LC_BR resultant RC_BR { $mResultR = Result($ls.labelsR, $resultant.resultantR); }
	;

/*Returns a list of numeric labels*/
labels returns [labelsR]
	: l1=label labelsRest { $labelsRest.labelsRestR.append($label.labelR); $labelsR = $labelsRest.labelsRestR; }
	| l2=label { $labelsR = [$l2.labelR] }
	;

labelsRest returns [labelsRestR]
	: COMMA labels { $labelsRestR = $labels.labelsR; }
	;
	
/*Returns a numeric label*/
label returns [labelR]
	: VAR_NAME { $labelR = $VAR_NAME.text[1:]; }
	| NUM { $labelR = $NUM.text; }
	| HASH_NAME UNDERSCORE_NUM { $labelR = $HASH_NAME.text[1:] + $UNDERSCORE_NUM.text; }
	| HASH_NAME { $labelR = $HASH_NAME.text[1:]; }
	| KLEENE NUM { $labelR = $KLEENE.text + $NUM.text; }
	| REGEX_LABEL NUM { $labelR = $REGEX_LABEL.text + $NUM.text; }
	| WORD { $labelR = $WORD.text; }
	;

//Parse result list
resultant returns [resultantR]
	: results { $resultantR = $results.resultsR; }
	;

results returns [resultsR=[\]]
	: result rs=results { $rs.resultsR.insert(0, $result.resultR); $resultsR = $rs.resultsR; }
	| {}
	;

result returns [resultR]
	: QUOTE_STRING { $resultR = StringResult($QUOTE_STRING.text[1:-1]); }
	| VAR_NAME { $resultR = VarResult($VAR_NAME.text[1:]); }
	| HASH_NAME UNDERSCORE_NUM { $resultR = FunctionResult($HASH_NAME.text[1:] + $UNDERSCORE_NUM.text); }
	| HASH_NAME { $resultR = FunctionResult($HASH_NAME.text[1:]); }
	| KLEENE NUM LA_BR r1=results RA_BR LR_BR r2=results RR_BR
		{ $resultR = KleeneResult($KLEENE.text + $NUM.text, $r1.resultsR, $r2.resultsR); }
	| REGEX_LABEL NUM LR_BR QUOTE_STRING RR_BR { $resultR = RegexResult(self.regexes[$NUM.text], $NUM.text, $QUOTE_STRING.text[1:-1]); }
	| REGEX_LABEL NUM { $resultR = RegexResult(self.regexes[$NUM.text], $NUM.text); }
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
