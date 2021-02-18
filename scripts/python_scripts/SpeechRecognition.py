import azure.cognitiveservices.speech as speechsdk

from Moropholgical_Analyzer import tokenizeText
    
def convertSpeechToText(stop_recognition):
    global speech_recognizer
    
    if stop_recognition == True:    
        speech_recognizer.stop_continuous_recognition()
        
        
    else:   
        speech_config = speechsdk.SpeechConfig(subscription="1fda37b270004643b89af5621d9902a2", region="eastasia", )
        speech_config.speech_recognition_language="ar-SA"
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
        speech_recognizer.recognized.connect(lambda evt: tokenizeText(evt.result.text))
        speech_recognizer.start_continuous_recognition()
        
        

   

    
    
