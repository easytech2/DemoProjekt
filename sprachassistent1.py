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
	    command =myCommand()

    return command
def assistent(command):
    # if statments, um Kommandos auszuführen
    if 'öffne Seite' in command: 
	    reg_ex= re.search('öffne seite(.*), command')  
	    if reg_ex:
		    domain = reg_ex.group(1) 	#befehl nach Öffne Seite wird als domain genutzt
		    url= 'https://www.'+ domain
		    webbrowser.open(url)
		    print('Fertig!')
    elif 'Wer ist Micha' in command:
	    talkToMe('Micha ist ein Individuum das öffters seine Tage bekommen kann als Frauen.')

    elif 'Was bedeutet schlechter Verlierer' in command:
	    talkToMe('Die Difinition dafür lautet "Micha".')

    elif 'Wer ist Radwan' in command:
	    talkToMe('Radwan ist mein Programmierer und Der collste Teakwondo kämpfer den es gibt aber er ist und bleibt der beste Typ den es gibt vor allem gewinnt er immer gegen Micha!')


    elif 'Wer ist besser Micha oder Radwan?' in command:
	    talkToMe('Bei dieser Frage muss ich lachen Ha Ha Ha Ha  Radwan Natürlich')

    elif 'Erzähl mir ein Witz' in command:
	    talkToMe('Geht ein kleiner Micha zu Radwan nach ein paar minuten kommt er heulend zurück warum?  Weil er wieder Verloren hat!')

    elif 'Was geht' in command:
	    talkToMe('Schau gerade wie Micha verliert!')

    talkToMe('Mein Name ist Kayle und ich bin bereit für die Befehle')
while True:
	# hier kann man mehrere Befehle ausführen.
    assistent(myCommand())
