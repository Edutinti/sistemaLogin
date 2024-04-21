import PySimpleGUI as sg
import utils

layot = [
    [sg.Text('Login'), sg.InputText()],
    [sg.Text('Senha'), sg.InputText(password_char='*')],
    [sg.Button('Salvar')],
    [sg.Button('Cadastrar')]
]

janela_principal = sg.Window('Login', layot)

cadastro_aberto = False

while True:
    event, values = janela_principal.read()
    
    if event == sg.WIN_CLOSED:
        break
    if event == 'Cadastrar' and not cadastro_aberto:
        janela_principal.hide()

        layot_cadastro = [
        [sg.Text('LoginCad'), sg.InputText()],
        [sg.Text('SenhaCad'), sg.InputText(password_char='*')],
        [sg.Button('SalvarCad')],
        [sg.Button('Cancelar')]
        ]

        janela_cadastro = sg.Window('Cadastro', layot_cadastro)
        
        cadastro_aberto = True
        
    if cadastro_aberto:    
        event1, values1 = janela_cadastro.read()

        if event1 == sg.WIN_CLOSED or event1 == 'Cancelar':
            janela_cadastro.close()
            janela_principal.un_hide()
            cadastro_aberto = False
            
        elif event1 == 'SalvarCad':
            sg.popup('Cadastro realizado com sucesso!')
            janela_cadastro.close()
            janela_principal.un_hide()
            cadastro_aberto = False

janela_principal.close()

    
    


        



