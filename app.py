import tkinter as tk


def calcular_imc():
    altura = float(entrada_altura.get()) / 100  
    peso = float(entrada_peso.get())
    imc = peso / (altura * altura)
    resultado.config(text=f"IMC: {imc:.2f}")


def reiniciar():
    entrada_nome.delete(0, "end")
    entrada_endereco.delete(0, "end")
    entrada_altura.delete(0, "end")
    entrada_peso.delete(0, "end")
    resultado.config(text="IMC: ")


def sair():
    janela.quit()


janela = tk.Tk()
janela.title("Calculadora de IMC")


label_nome = tk.Label(janela, text="Nome do Paciente:")
label_nome.grid(row=0, column=0, padx=10, pady=5)
label_endereco = tk.Label(janela, text="Endereço completo:")
label_endereco.grid(row=1, column=0, padx=10, pady=5)
label_altura = tk.Label(janela, text="Altura (cm):")
label_altura.grid(row=2, column=0, padx=10, pady=5)
label_peso = tk.Label(janela, text="Peso (Kg):")
label_peso.grid(row=3, column=0, padx=10, pady=5)


entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1, padx=10, pady=5)
entrada_endereco = tk.Entry(janela)
entrada_endereco.grid(row=1, column=1, padx=10, pady=5)
entrada_altura = tk.Entry(janela)
entrada_altura.grid(row=2, column=1, padx=10, pady=5)
entrada_peso = tk.Entry(janela)
entrada_peso.grid(row=3, column=1, padx=10, pady=5)


botao_calcular = tk.Button(janela, text="Calcular", command=calcular_imc)
botao_calcular.grid(row=4, column=0, padx=10, pady=5)
botao_reiniciar = tk.Button(janela, text="Reiniciar", command=reiniciar)
botao_reiniciar.grid(row=4, column=1, padx=10, pady=5)
botao_sair = tk.Button(janela, text="Sair", command=sair)
botao_sair.grid(row=5, column=0, columnspan=2, padx=10, pady=5)


resultado = tk.Label(janela, text="Resultado: ")
resultado.grid(row=2, column=2, columnspan=2, padx=10, pady=5)


resultado_frame = tk.Frame(janela, borderwidth=2, relief="solid")
resultado_frame.grid(row=2, column=2, columnspan=2, padx=10, pady=5)
resultado = tk.Label(resultado_frame, text="Resultado: ")
resultado.pack()




janela.mainloop()
