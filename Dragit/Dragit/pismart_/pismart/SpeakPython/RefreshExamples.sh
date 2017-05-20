#bin
cp * ../bin/SpeakPython/

rm ../bin/SpeakPython/RefreshExamples.sh
rm ../bin/SpeakPython/MakeSpeakPython.sh

mv ../bin/SpeakPython/MakeSpeechProject.py ../bin/
mv ../bin/SpeakPython/SpeakPythonMakeDB.py ../bin/

#examples
cp -r ../bin/* ../examples/WithoutSpeechRecognition/Calculator/
cp -r ../bin/* ../examples/WithoutSpeechRecognition/LinuxCommands/
cp -r ../bin/* ../examples/SpeechRecognition/HouseCommands/
cp -r ../bin/* ../examples/SpeechRecognition/RPi/4LED/
cp -r ../bin/* ../examples/unfinished/RGB-LED/
cp -r ../bin/* ../examples/unfinished/playground/
