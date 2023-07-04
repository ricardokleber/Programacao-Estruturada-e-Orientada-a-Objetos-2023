from tkinter import Tk, Label, mainloop

janela = Tk()
janela.title('Meu Primeiro Texto')
janela.geometry("300x200")

label= Label(janela, text="Olá, Mundo!!!", font= ('Courier 20'))
label.pack(pady = 70)

janela.mainloop()