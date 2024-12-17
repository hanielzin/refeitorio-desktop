import customtkinter 

janela = customtkinter.CTk()

frame_principal = customtkinter.CTkFrame(janela)
frame_principal.pack(fill="both", expand=True)

titulo_principal = customtkinter.CTkLabel(frame_principal, text="Bem-vindo ao Nosso Refeitório",
font=("Arial", 24, "bold"))
titulo_principal.pack(pady=30)

mensagem_boas_vindas = customtkinter.CTkLabel(frame_principal, text="Login realizado com sucesso!",
font=("Arial", 16))
mensagem_boas_vindas.pack(pady=10)

botao_sair = customtkinter.CTkButton(frame_principal, text="Sair", command=janela.quit)
botao_sair.pack(pady=20)

janela.mainloop()