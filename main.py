import PySimpleGUI as sg
from utils import Cadastro
from utils import Login

layot = [
    [sg.Text('Login'), sg.Input(key='login')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Button('Salvar')],
    [sg.Button('Cadastrar')]
]

janela_principal = sg.Window('Login', layot)

cadastro_aberto = False

while True:
    event, values = janela_principal.read()
    
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Salvar':
        login = values['login']
        senha = values['senha']
        loginStr = str(login)
        senhaStr = str(senha)

        login = Login()
        login.validar_login(loginStr, senhaStr)

    if event == 'Cadastrar' and not cadastro_aberto:
        janela_principal.hide()

        layot_cadastro = [
        [sg.Text('Novo Login'), sg.Input(key='novoLogin')],
        [sg.Text('Nova Senha'), sg.Input(key='novaSenha', password_char='*')],
        [sg.Button('Salvar Cadastro')],
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
            
        elif event1 == 'Salvar Cadastro':
            sg.popup('Cadastro realizado com sucesso!')
            cadLogin = values1['novoLogin']
            cadSenha = values1['novaSenha']

            cadLoginStr = str(cadLogin)
            cadSenhaStr = str(cadSenha)

            cadastro = Cadastro()
            cadastro.cadastroPessoa(cadLoginStr, cadSenhaStr)

            janela_cadastro.close()
            janela_principal.un_hide()
            cadastro_aberto = False

janela_principal.close()

    
    


        



