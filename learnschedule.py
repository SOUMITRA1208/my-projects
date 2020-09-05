import datetime
import webbrowser
import playsound
from gtts import gTTS
def speak(text):
	tts=gTTS(text=text,lang="en")
	filename="voice.mp3"
	tts.save(filename)
	playsound.playsound(filename)

course_url='https://www.coursera.org/'
print("Welcome Soumitra")
print('')
coursehour=int(input('At what hour do you wish to start learning ?  '))
courseminute=int(input('At what minute do you wish to start learning ? '))
ampm=str(input('am or pm ? '))
if ampm=='pm':
	coursehour=coursehour+12

while(1==1):
	if (coursehour == datetime.datetime.now().hour and courseminute == datetime.datetime.now().minute):
		speak('start your learning now')
		webbrowser.open(course_url)
	