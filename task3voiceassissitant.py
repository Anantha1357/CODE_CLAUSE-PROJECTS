import pyttsx3
import wikipedia
voice=pyttsx3.init()
In = input(" matter to search and voice assisstant")
result=wikipedia.summary(In,sentences=12)
print(result)
voice.say(result)
voice.runAndWait()
