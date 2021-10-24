from gtts import gTTS
import playsound
tts = gTTS(text=' Привет,приятно познакомится', lang='ru')
tts.save("hello.mp3")
playsound.playsound('hello.mp3')