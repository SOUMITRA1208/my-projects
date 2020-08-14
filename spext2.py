import speech_recognition as sr 
r=sr.Recognizer()
x=int(input('enter the message duration in seconds '))
print('please talk !')
with sr.Microphone() as source:
	audio_data=r.record(source,duration=x)
	print('Recognizing...')
	text=r.recognize_google(audio_data)
	print(text)