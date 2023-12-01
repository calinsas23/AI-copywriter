import PySimpleGUI as sg
from Ai_ok import contacteaza_ai
#functie care defineste ferestrele in functie de optiune si apeleaza functia de Ai(apeleaza creierul)

def intreaba_ai(values0, window):
    while True:
        # se citesc valorile si eventurile care au loc in int grafica
        event, values = window.read()
        if event == 'ok':
            #e naspa cu trimisul de parametrii avand in vedere ca difera parametrii de la o optiune la alta
            if values0['optiune'] == 'Caption' or values0['optiune'] == 'Bio':
                replay_original, error_msg = contacteaza_ai(values['cr1'], values['cr2'], values['cr3'], values['cr4'],'','', values0['optiune'], values['nr'])
            elif values0['optiune'] == 'Testimonial':
                replay_original, error_msg = contacteaza_ai(values['cr1'],values['cr2'],values['cr3'], '', '', '', values0['optiune'], values['nr'])
            elif values0['optiune']== 'Tips & Tricks':
                replay_original, error_msg = contacteaza_ai(values['cr1'],'','', '', '', '',values0['optiune'], values['nr'])
            elif values0['optiune']== 'Giveaway':
                replay_original, error_msg = contacteaza_ai(values['cr1'], values['cr2'], values['cr3'],values['cr4'],values['cr5'],values['cr6'], values0['optiune'], values['nr'])
            elif values0['optiune']== 'Collaboration message':
                replay_original, error_msg = contacteaza_ai(values['cr1'], values['cr2'], values['cr3'],values['cr4'], '', '', values0['optiune'], values['nr'])
            if error_msg == '':
                window['iesire'].print("Mesaj original chat gpt: ",replay_original,"\n")
               #window['iesire'].print("\nMesaj refrazat: ",replay_refrazat)
            else:
                window['iesire'].print(error_msg)
        if event == 'clear':
            if values0['optiune'] == 'Caption' or values0['optiune'] == 'Bio':
                window['iesire'].Update('')
                window['cr1'].Update('')
                window['cr2'].Update('')
                window['cr3'].Update('')
                window['cr4'].Update('')
                window['nr'].Update('')
            elif values0['optiune'] == 'Testimonial':
                window['iesire'].Update('')
                window['cr1'].Update('')
                window['cr2'].Update('')
                window['cr3'].Update('')
                window['nr'].Update('')
            elif values0['optiune'] == 'Tips & Tricks':
                window['iesire'].Update('')
                window['cr1'].Update('')
                window['nr'].Update('')
            elif values0['optiune'] == 'Giveaway':
                window['iesire'].Update('')
                window['cr1'].Update('')
                window['cr2'].Update('')
                window['cr3'].Update('')
                window['cr4'].Update('')
                window['cr5'].Update('')
                window['cr6'].Update('')
                window['nr'].Update('')
            elif values0['optiune'] == 'Collaboration message':
                window['iesire'].Update('')
                window['cr1'].Update('')
                window['cr2'].Update('')
                window['cr3'].Update('')
                window['cr4'].Update('')
                window['nr'].Update('')
        if event == sg.WIN_CLOSED or event == 'cancel':
            break
    window.close()
    return 0