from gtts import gTTS
from playsound import playsound
x = 'hello'
test = gTTS('hello')
test = open('H:/CSP/docs/hello.mp3', 'w')
test.close()
playsound('H:/CSP/docs/hello.mp3')