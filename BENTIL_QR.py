import PySimpleGUI as sg
import qrcode
from PIL import Image

sg.theme('Topanga')


# Define the window layout
layout = [
    [sg.Text('Enter Text:')],
    [sg.InputText()],
    [sg.Text('QR Code Size (px):')],
    [sg.InputText('300')],
    [sg.Text('QR Code Color:')],
    [sg.InputText('#000000')],
    [sg.Button('Create'), sg.Exit()],
    [sg.Image(key='-IMAGE-', size=(200, 150))]
]

# Create the window
window = sg.Window('QR Code Generator', layout)

# Event loop to process events and get input
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    # Get the input text
    input_text = values[0]

    # Get the size of the QR code
    try:
        qr_size = int(values[1])
    except ValueError:
        sg.popup('Invalid size value entered. Please enter a positive integer.')
        continue

    # Get the color of the QR code
    qr_color = values[2]

    # Generate the QR code
    qr = qrcode.QRCode(version=None, box_size=10, border=4)
    qr.add_data(input_text)
    qr.make(fit=True)
    img = qr.make_image(fill_color=qr_color, back_color="white")
    img = img.resize((qr_size, qr_size), Image.ANTIALIAS)

    # Save the QR code as an image file
    try:
        img.save("qrcode.png")
        window['-IMAGE-'].update(filename='qrcode.png')

        sg.popup('QR code successfully created.')
    except Exception as e:
        sg.popup(f'Error creating QR code: {e}')
