from tkinter import Tk, Button, mainloop

janela = Tk()
janela.title('Meu Primeiro Botão')
janela.geometry("300x200")

botao = Button(janela, text = 'Ops')
botao.pack(pady = 70)

janela.mainloop()