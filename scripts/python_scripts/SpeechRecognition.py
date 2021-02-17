import azure.cognitiveservices.speech as speechsdk
    
def speechToText(x):
    global speech_recognizer
    
    if x==1:    
        speech_recognizer.stop_continuous_recognition()
    else:   
        speech_config = speechsdk.SpeechConfig(subscription="1fda37b270004643b89af5621d9902a2", region="eastasia", )
        speech_config.speech_recognition_language="ar-SA"
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
        
        speech_recognizer.recognized.connect(lambda evt: print('RECOGNIZED: {}'.format(evt.result.text)))
        speech_recognizer.start_continuous_recognition()
   
  
    
    
