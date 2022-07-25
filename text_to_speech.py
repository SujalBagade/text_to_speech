import pyttsx3
s = input("type something")
engine = pyttsx3.init('sapi5')
engine.say(s)
engine.runAndWait()

