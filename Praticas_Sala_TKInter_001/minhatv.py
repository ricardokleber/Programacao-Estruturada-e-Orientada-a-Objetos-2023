from tkinter import *

controle = Tk()
controle.title('Controle Remoto')
controle.geometry("250x250")

def aumentarVolume():
    print("Volume Aumentou")

def diminuirVolume():
    print("Volume Diminuiu")

def ligaTV():
    televisao = Toplevel(controle)
    televisao.title("TV")
    canal2 = PhotoImage(file="rc.gif")
    exibir_imagem = Label(televisao, image=canal2)
    exibir_imagem.image = canal2
    exibir_imagem.pack()

botao_ligar = Button(controle, text="Ligar", command=ligaTV)
botao_ligar.pack(pady=10)

botao_desligar = Button(controle, text="Desligar", command=controle.quit)
botao_desligar.pack(pady=10)

volume = Label(controle, text="Volume")
volume.pack(pady=10)

vol_aumentar = Button(controle, text="+", command=aumentarVolume)
vol_aumentar.pack(pady=10)

vol_baixar = Button(controle, text="-", command=diminuirVolume)
vol_baixar.pack(pady=10)

controle.mainloop()