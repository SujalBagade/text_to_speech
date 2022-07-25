import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
        print("speak...")
        r.pause_threshold = 1
        audio = r.listen(source)
MyText = r.recognize_google(audio)
print(MyText)



