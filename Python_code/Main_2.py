import PySimpleGUI as sg
import os
import openai
from Ai_ok import contacteaza_ai
from Functie_comunicare import intreaba_ai
#fereastra pentru optiune
layout_princ = [[sg.Combo(['Social', 'Blog', 'ADS', 'Email', 'Site', 'Marketing'],
              default_value='None', key='optiune_p')],
             [sg.Button('ok', key='ok_princ')]
             ]
window_princ = sg.Window('Window Title', layout_princ, size=(100, 100))
while True:
    #in values_princ este memorata alegerea : Instagram, Blog, Ads, Email
    event_princ, values_princ = window_princ.read()
    if event_princ == 'ok_princ':
        if values_princ['optiune_p'] == 'Social':
            layout_social=[[sg.Combo(['Caption', 'Bio', 'Testimonial', 'Tips & Tricks', 'Giveaway', 'Collaboration message'],
                      default_value='None', key='optiune')],
                     [sg.Button('ok',key='ok_social')]
                     ]
            window_social = sg.Window('Window Title', layout_social, size=(100, 100))
            while True:
                #in values_social este memorata alegerea : Caption, Bio, Testimonial etc
                event_social, values_social = window_social.read()
                # se citesc valorile si eventurile care au loc in int grafica
                if event_social == 'ok_social':
                    if values_social['optiune'] == 'Caption':
                        layout_caption = [
                            [sg.Text('Ideea_de baza', size=(10, 1)), sg.InputText(key='cr1')],
                            [sg.Text('Detaliul 1', size=(10, 1)), sg.InputText(key='cr2')],
                            [sg.Text('Detaliul 2', size=(10, 1)), sg.InputText(key='cr3')],
                            [sg.Text('Detaliul 3', size=(10, 1)), sg.InputText(key='cr4')],
                            [sg.Text('Token_nr', size=(10, 1)), sg.InputText(key='nr', size=(5, 1))],
                            [sg.Text('Shh, AI vorbeste', size=(15, 1))],
                            [sg.Multiline('', size=(10, 20), enable_events=True, key='iesire', expand_x=True, expand_y=True,
                                          justification='left')],
                            [sg.Button('ok'), sg.Button('cancel'), sg.Button('clear')]
                            ]
                        rightclick = ['&Edit', ['C&ut', '&Copy', '&Paste', '&Undo']]
                        window_caption = sg.Window('Window Title', layout_caption, size=(715, 700), right_click_menu=rightclick)
                        intreaba_ai(values_social, window_caption)
                    elif values_social['optiune'] == 'Bio':
                        layout_Bio = [
                            [sg.Text('Ideea_de baza', size=(10, 1)), sg.InputText(key='cr1')],
                            [sg.Text('Detaliul 1', size=(10, 1)), sg.InputText(key='cr2')],
                            [sg.Text('Detaliul 2', size=(10, 1)), sg.InputText(key='cr3')],
                            [sg.Text('Detaliul 3', size=(10, 1)), sg.InputText(key='cr4')],
                            [sg.Text('Token_nr', size=(10, 1)), sg.InputText(key='nr', size=(5, 1))],
                            [sg.Text('Shh, AI vorbeste', size=(15, 1))],
                            [sg.Multiline('', size=(10, 20), enable_events=True, key='iesire', expand_x=True, expand_y=True,
                                          justification='left')],
                            [sg.Button('ok'), sg.Button('cancel'), sg.Button('clear')]
                            ]
                        rightclick = ['&Edit', ['C&ut', '&Copy', '&Paste', '&Undo']]
                        window_Bio = sg.Window('Window Title', layout_Bio, size=(715, 700), right_click_menu=rightclick)
                        intreaba_ai(values_social, window_Bio)
                        #nu stiu cat de bine am inteles eu testimonialul dar l-am implementat ca un review mai formal
                    elif values_social['optiune'] == 'Testimonial':
                        layout_Testimonial = [
                            [sg.Text('Produsul/serviciul: ', size=(15, 1)), sg.InputText(key='cr1')],
                            [sg.Text('Calitatea 1:', size=(10, 1)), sg.InputText(key='cr2')],
                            [sg.Text('Calitatea 2: ', size=(10, 1)), sg.InputText(key='cr3')],
                            [sg.Text('Token_nr', size=(10, 1)), sg.InputText(key='nr', size=(5, 1))],
                            [sg.Text('Shh, AI vorbeste', size=(15, 1))],
                            [sg.Multiline('', size=(10, 20), enable_events=True, key='iesire', expand_x=True, expand_y=True,
                                          justification='left')],
                            [sg.Button('ok'), sg.Button('cancel'), sg.Button('clear')]
                            ]
                        rightclick = ['&Edit', ['C&ut', '&Copy', '&Paste', '&Undo']]
                        window_Testimonial = sg.Window('Window Title', layout_Testimonial, size=(715, 700), right_click_menu=rightclick)
                        intreaba_ai(values_social, window_Testimonial)
                    elif values_social['optiune'] == 'Tips & Tricks':
                        layout_Tips = [
                            [sg.Text('Ideea_de baza:', size=(10, 1)), sg.InputText(key='cr1')],
                            #[sg.Text('Detaliul 1', size=(10, 1)), sg.InputText(key='cr2')],
                            #[sg.Text('Detaliul 2', size=(10, 1)), sg.InputText(key='cr3')],
                            #[sg.Text('Detaliul 3', size=(10, 1)), sg.InputText(key='cr4')],
                            [sg.Text('Token_nr', size=(10, 1)), sg.InputText(key='nr', size=(5, 1))],
                            [sg.Text('Shh, AI vorbeste', size=(15, 1))],
                            [sg.Multiline('', size=(10, 20), enable_events=True, key='iesire', expand_x=True, expand_y=True,
                                          justification='left')],
                            [sg.Button('ok'), sg.Button('cancel'), sg.Button('clear')]
                            ]
                        rightclick = ['&Edit', ['C&ut', '&Copy', '&Paste', '&Undo']]
                        window_Tips = sg.Window('Window Title', layout_Tips, size=(715, 700), right_click_menu=rightclick)
                        intreaba_ai(values_social, window_Tips)
                    elif values_social['optiune'] == 'Giveaway':
                        layout_Giveaway = [
                            [sg.Text('Produs/serviciu: ', size=(17, 1)), sg.InputText(key='cr1')],
                            [sg.Text('Organizator: ', size=(10, 1)), sg.InputText(key='cr2')],
                            [sg.Text('Detalii: ', size=(10, 1)), sg.InputText(key='cr3')],
                            [sg.Text('Cand: ', size=(10, 1)), sg.InputText(key='cr4')],
                            [sg.Text('Conditii_participare: ', size=(25, 1)), sg.InputText(key='cr5')],
                            [sg.Text('Detalii extragere: ', size=(25, 1)), sg.InputText(key='cr6')],
                            [sg.Text('Token_nr', size=(10, 1)), sg.InputText(key='nr', size=(5, 1))],
                            [sg.Text('Shh, AI vorbeste', size=(15, 1))],
                            [sg.Multiline('', size=(10, 20), enable_events=True, key='iesire', expand_x=True, expand_y=True,
                                          justification='left')],
                            [sg.Button('ok'), sg.Button('cancel'), sg.Button('clear')]
                            ]
                        rightclick = ['&Edit', ['C&ut', '&Copy', '&Paste', '&Undo']]
                        window_Giveaway = sg.Window('Window Title', layout_Giveaway, size=(715, 700), right_click_menu=rightclick)
                        intreaba_ai(values_social, window_Giveaway)
                    elif values_social['optiune'] == 'Collaboration message':
                        layout_collaboration = [
                            [sg.Text('Destinatar:', size=(10, 1)), sg.InputText(key='cr1')],
                            [sg.Text('Numele_meu:', size=(10, 1)), sg.InputText(key='cr2')],
                            [sg.Text('Scopul:', size=(10, 1)), sg.InputText(key='cr3')],
                            [sg.Text('Compania::', size=(10, 1)), sg.InputText(key='cr4')],
                            [sg.Text('Token_nr', size=(10, 1)), sg.InputText(key='nr', size=(5, 1))],
                            [sg.Text('Shh, vorbeste Ai-ul', size=(15, 1))],
                            [sg.Multiline('', size=(10, 20), enable_events=True, key='iesire', expand_x=True, expand_y=True,
                                          justification='left')],
                            [sg.Button('ok'), sg.Button('cancel'), sg.Button('clear')]
                            ]
                        rightclick = ['&Edit', ['C&ut', '&Copy', '&Paste', '&Undo']]
                        window_collaboration = sg.Window('Window Title', layout_collaboration, size=(715, 700), right_click_menu=rightclick)
                        intreaba_ai(values_social, window_collaboration)
                if event_social == sg.WIN_CLOSED or event_social == 'cancel':
                    break
    if event_princ == sg.WIN_CLOSED or event_princ == 'cancel':
        break
window_social.close()
window_princ.close()


