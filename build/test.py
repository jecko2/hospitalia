import pyttsx3
engine = pyttsx3.init()

# rate
rate = engine.getProperty("rate")
engine.setProperty("rate", 200)

# volume
volume = engine.getProperty("volume")
engine.setProperty("volume", 1.0)

# voice
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# speak
engine.say("Hello, welcome to jarvis")
engine.say("My current speaking rate is " + str(rate) + " you can however change this if you like")
engine.runAndWait()
engine.stop()

