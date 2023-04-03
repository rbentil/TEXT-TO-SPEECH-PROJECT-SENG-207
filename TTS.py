import pyttsx3
import PySimpleGUI as sg

sg.theme('dark')
# initialize the text-to-speech engine
engine = pyttsx3.init()

# define a function to speak the given text with the specified voice
def speak(text, voice_id):
    # set the voice ID
    engine.setProperty('voice', voice_id)
    # speak the text
    engine.say(text)
    engine.runAndWait()

# create the GUI window
layout = [[sg.Text('Enter the text to speak:')],
          [sg.Input(key='-INPUT-')],
          [sg.Radio('Male', 'RADIO1', default=True, key='-MALE-'),
           sg.Radio('Female', 'RADIO1', key='-FEMALE-')],
          [sg.Button('Speak'), sg.Button('Exit')]]

window = sg.Window('Text to Speech', layout)

# event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == 'Speak':
        # get the text to speak and the selected voice
        text = values['-INPUT-']
        if values['-MALE-']:
            voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
        else:
            voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
        # speak the text with the selected voice
        speak(text, voice_id)

# close the window and the text-to-speech engine
window.close()
engine.stop()
