
import azure.cognitiveservices.speech as speechsdk
import socket
import time

host, port = "127.0.0.1", 25001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

from Moropholgical_Analyzer import extractMorphologicalFeatures
    
def convertSpeechToText(stop_recognition):
    global speech_recognizer
    
    if stop_recognition == True:    
        speech_recognizer.stop_continuous_recognition()
        
        
    else:   
        speech_config = speechsdk.SpeechConfig(subscription="1fda37b270004643b89af5621d9902a2", region="eastasia", )
        speech_config.speech_recognition_language="ar-SA"
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
        speech_recognizer.recognized.connect(lambda evt:(sock.sendall(evt.result.text.encode("UTF-8"))))
        speech_recognizer.start_continuous_recognition()
        
        

   

    
    
