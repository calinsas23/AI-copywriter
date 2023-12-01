import PySimpleGUI as sg
import os
import openai
from Ai_ok import social_media_caption

layout = [
    [sg.Combo(['Caption', 'BIO', 'Testimonial', 'Tips & Tricks', 'Giveaway', 'Collaboration message'],
                default_value='None', key='optiune')],
    [sg.Text('Context1', size=(10, 1)), sg.InputText(key='cr1')],
    [sg.Text('Context2', size=(10, 1)), sg.InputText(key='cr2')],
    [sg.Text('Context3', size=(10, 1)), sg.InputText(key='cr3')],
    [sg.Text('Context1', size=(10, 1)), sg.InputText(key='cr4')],
    [sg.Text('Context2', size=(10, 1)), sg.InputText(key='cr5')],
    [sg.Text('Context3', size=(10, 1)), sg.InputText(key='cr6')],
    [sg.Text('Shh, AI vorbeste', size=(15, 1))],
    [sg.Multiline('', size=(10, 20), enable_events=True, key='iesire', expand_x=True, expand_y=True,
                  justification='left')],
    [sg.Button('ok'), sg.Button('cancel'), sg.Button('clear')]
]
raspuns = []
rightclick = ['&Edit', ['C&ut', '&Copy', '&Paste', '&Undo']]
window = sg.Window('Window Title', layout, size=(715, 700), right_click_menu=rightclick)
while True:
    # se citesc valorile si eventurile care au loc in int grafica
    event, values = window.read()
    if event == 'ok':
        raspuns, varianta_t, error_msg = social_media_caption(values['cr1'], values['cr2'], values['cr3'], values['cr4'], values['cr5'], values['cr6'], values['optiune'])
        if error_msg =='':
            window['iesire'].print(raspuns)
            window['iesire'].print(varianta_t)
        else:
            window['iesire'].print(error_msg)
    if event == 'clear':
        window['iesire'].Update('')
        window['cr1'].Update('')
        window['cr2'].Update('')
        window['cr3'].Update('')
    if event == sg.WIN_CLOSED or event == 'cancel':
        break
window.close()
