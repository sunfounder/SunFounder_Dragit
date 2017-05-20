###SpeakPython

This App is originally written by matthew3 on [bitbucket](https://bitbucket.org/matthew3/speakpython/wiki/Home)

We modified this to use with a USB microphone on Raspberry Pi.

####Diffrences:
file: SpeakPythonRecognizer.py

----  169|		self.pipeline = gst.parse_launch(' ! '.join(['autoaudiosrc',
++++  169|		self.pipeline = gst.parse_launch(' ! '.join(['alsasrc device=hw:1',


This version of SpeakPython is also on GNU GPL V3 licences, detials in file LICENCES.TXT