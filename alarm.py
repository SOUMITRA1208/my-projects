import datetime
import winsound

message=input('Enter your alarm message ')
alarmhour=int(input('At what hour do you want to wake up '))
alarmminute=int(input('At what minute do you want to wake up '))
ampm=str(input("am or pm ? "))
if ampm=='pm':
	alarmhour=alarmhour+12

while(1==1): 
    if (alarmhour == datetime.datetime.now().hour and alarmminute == datetime.datetime.now().minute):
    	print(message)
    	
    	winsound.PlaySound("song of your choice in Wav format",winsound.SND_FILENAME)
