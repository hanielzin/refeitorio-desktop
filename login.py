#IMPORTANDO A BIBLIOTECA
import customtkinter
from modulo import banco
import subprocess

def verificar_login():
    email_usuario = email.get()
    senha_usuario = senha.get()

    consulta = f"SELECT * FROM nutricionista WHERE email = '{email_usuario}' and senha = '{senha_usuario}'"
    resultado = banco(consulta)

    if resultado:
        janela.destroy()
        subprocess.run(["python", "cadastro_alimentos.py"])
    else:
        mensagem_erro.configure(text="E-mail ou senha incorretos!", text_color="red")

#CRIANDO A JANELA
janela = customtkinter.CTk()
janela.title('Login - Nosso Refeitório')
janela.geometry('600x380')
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

frame_login = customtkinter.CTkFrame(janela)
frame_login.pack(fill = "both", expand = True)

#ELEMENTOS DA JANELA
titulo = customtkinter.CTkLabel(frame_login, text='Faça Login', font=('Arial', 30, 'bold'))
titulo.pack(pady=30)

email = customtkinter.CTkEntry(frame_login, placeholder_text = 'E-mail')
email.pack(pady=5)

senha = customtkinter.CTkEntry(frame_login, placeholder_text = 'Senha')
senha.pack(pady=5)

mensagem_erro = customtkinter.CTkLabel(frame_login, text="")
mensagem_erro.pack()

botao_login = customtkinter.CTkButton(frame_login, text='Entrar', command=verificar_login)
botao_login.pack(pady=20)

#PERMITE A VISUALIZAÇÃO DA JANELA DEIXANDO ELA ATIVA NUM LOOP
janela.mainloop()