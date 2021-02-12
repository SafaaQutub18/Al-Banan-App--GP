import speech_recognition as sr


r  = sr.Recognizer()
mic = sr.Microphone()
for x in range(20):
    print(x)
    with mic as source:
        print('speak Anything: ')
        audio = r.listen(source, 20, 20)
        try: 
            text= r.recognize_google(audio, language='ar-SA')
            print('you said: {​​​​}​​​​'.format(text))
        except:
            print('sorry')

