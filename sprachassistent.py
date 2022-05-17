#Installieurng der Bibliotehken
import speech_recongnition as sr
import os
import re
import webbrowser


#Funktion bauen
def talkToMe(audio):
	#schreibt das nieder, was als "audio" eingeschriben wurde
	print(audio)
	os.system("say" + audio)



def myCommand():
	# Hört auf die Kommandos
	r= sr.Recognizer()
	with sr.Microphone() as source:
		print("Bereit....")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration=1) #Hier werden die geräusche vom Mikrophone unterdrückt damit der Assistent die stimme besser aufnehmen kann.
		audio=r.listen(source)

	try:
		command=r.recognize_google(audio, language='de-DE').lower()
		print('Du hast gesagt: ' + command + ('\n'))


	except sr.UnknownValueError:
		print('Dein letztes Kommando konnte nicht verstanden werden.')
		command =myComman()

	return command
def assistent(command):
	# if statments, um Kommandos auszuführen
	if 'öffne Seite' in command: 
	     reg_ex= re.serach('offne seite(.*), command')  
	if reg_ex:
			domain = reg_ex.group(1) 	#befehl nach Öffne Seite wird als domain genutzt
			url= 'https://www.'+ domain
			webbrowser.open(url)
			print('Fertig!')

	elif 'Wer ist Micha' in command:
		talkToMe('Micha ist ein Individuum.')


	elif 'Was bedeutet schlechter Verlierer' in command:
		talkToMe('Die Difinition dafür lautet "Micha".')

	elif 'Wer ist Radwan' in command:
		talkToMe('Radwan ist ein Programmierer!')


	elif 'Ist Micha besser als Radwan' in command:
		talkToMe('Bei dieser Frage muss ich lachen Ha Ha Ha Ha ')


	elif 'Erzähl mir ein Witz' in command:
		talkToMe('Warum Leben Haie in Salzwasser? Weil sie in Pfefferwasser niesen müssen.')


	elif 'Was geht' in command:
		talkToMe('Alles was zwei beine hat!')


talkToMe('Mein Name ist Charwice und ich bin bereit für die Befehle')
while True:
	# hier kann man mehrere Befehle ausführen.
	assistent(myCommand())



