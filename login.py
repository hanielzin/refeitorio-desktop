#IMPORTANDO A BIBLIOTECA
import customtkinter
from modulo import banco

def verificar_login():
    email_usuario = email.get()
    senha_usuario = senha.get()

    consulta = f"SELECT * FROM nutricionista WHERE email = '{email_usuario}' and senha = '{senha_usuario}'"
    resultado = banco(consulta)

    if resultado:
        print('ACERTOU')
    else:
        print('TÁ ERRADO')

#CRIANDO A JANELA
janela = customtkinter.CTk()
janela.title('Login - Nosso Refeitório')
janela.geometry('600x380')

#ELEMENTOS DA JANELA
titulo = customtkinter.CTkLabel(janela, text='Faça Login', font=('Arial', 30, 'bold'))
titulo.pack(pady=30)

campo_email = customtkinter.CTkLabel(janela, text='Informe seu endereço de E-mail')
campo_email.pack()

email = customtkinter.CTkEntry(janela)
email.pack()

campo_senha = customtkinter.CTkLabel(janela, text='Informe a sua senha')
campo_senha.pack()

senha = customtkinter.CTkEntry(janela)
senha.pack()

botao_login = customtkinter.CTkButton(janela, text='Entrar', command=verificar_login)
botao_login.pack(pady=20)

#PERMITE A VISUALIZAÇÃO DA JANELA DEIXANDO ELA ATIVA NUM LOOP
janela.mainloop()