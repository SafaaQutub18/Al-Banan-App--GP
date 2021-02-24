
from Moropholgical_Analyzer import tokenizeText
import azure.cognitiveservices.speech as speechsdk
import socket
import time

host, port = "127.0.0.1", 25001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

def convertSpeechToText():
        global sock
        speech_config = speechsdk.SpeechConfig(subscription="1fda37b270004643b89af5621d9902a2", region="eastasia", )
        speech_config.speech_recognition_language="ar-SA"
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
        speech_recognizer.recognized.connect(lambda evt:tokenizeText(evt.result.text ,sock))                    

        speech_recognizer.start_continuous_recognition()
        
        
        time.sleep(190)
        speech_recognizer.stop_continuous_recognition()

convertSpeechToText()
   

    
    
