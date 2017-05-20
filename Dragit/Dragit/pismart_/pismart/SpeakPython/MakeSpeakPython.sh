#!/bin/bash

echo "SP:Building lexer and parser from SpeakPython.g..."
if `java -jar ../../antlr-3.4-complete.jar -Dlanguage=Python "SpeakPython.g"`; then
	perl -0pi -e 's/el\s+if/elif/sg' SpeakPythonLexer.py
	echo "SP:Success."
fi

echo "SP:Building lexer and parser from SpeakPythonJSGF.g..."
if `java -jar ../../antlr-3.4-complete.jar -Dlanguage=Python "SpeakPythonJSGF.g"`; then
	perl -0pi -e 's/el\s+if/elif/sg' SpeakPythonJSGFLexer.py
	echo "SP:Success."
fi
