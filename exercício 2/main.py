from tkinter import * 
from funcoes import *

janela = Tk()

janela.title = Label(text="Calculadora")

numero1 = []
numero2 = []
operacao = ""



'''def somar():
    soma = n1 + n2
    return soma

def subtrair(n1,n2):
    subtrair = n1 - n2
    return subtrair

def multiplicar(n1,n2):
    multiplicar = n1 * n2
    return multiplicar

def dividir(n1,n2):
    dividir = n1 / n2
    return dividir'''


def registrar_numero(numero):
    global numero1
    numero1 = numero

def registrar_operacao(op):
    global operacao 
    operacao = op

entrada = Entry(width=40)

sete = Button(janela,text="7",height=5,width=10, command = lambda : registrar_numero(7)).grid(row=0, column=0)
nove = Button(janela,text="9",height=5,width=10, command = lambda : registrar_numero(9)).grid(row=0, column=2)
somatorio = Button(janela,text="+",height=5,width=10, command=registrar_operacao("+")).grid(row=0, column=3)
oito = Button(janela,text="8",height=5,width=10, command = lambda : registrar_numero(8)).grid(row=0, column=1)

multiplicacao = Button(janela,text="*",height=5,width=10, command=registrar_operacao("*")).grid(row=1, column=3)
seis  = Button(janela,text="6",height=5,width=10, command = lambda : registrar_numero(6)).grid(row=2, column=2)
cinco = Button(janela,text="5",height=5,width=10, command = lambda : registrar_numero(5)).grid(row=2, column=1)
quatro = Button(janela,text="4",height=5,width=10, command = lambda : registrar_numero(4)).grid(row=2, column=0)

subtracao = Button(janela,text="-",height=5,width=10, command=registrar_operacao("-")).grid(row=2, column=3)
tres  = Button(janela,text="3",height=5,width=10, command = lambda : registrar_numero(3)).grid(row=1, column=2)
dois = Button(janela,text="2",height=5,width=10, command = lambda : registrar_numero(2)).grid(row=1, column=1)
um = Button(janela,text="1",height=5,width=10, command = lambda : registrar_numero(1)).grid(row=1, column=0)

divisao = Button(janela,text="/",height=5,width=10, command=registrar_operacao("/")).grid(row=3, column=2)
igual = Button(janela,text="=",height=5,width=10).grid(row=3, column=1)
zero = Button(janela,text="0",height=5,width=10).grid(row=3, column=0)

def resultado():
    if operacao != "":
        conjunto1 = registrar_numero()
        numero1.append(conjunto1)

    else:
        conjunto2 = registrar_numero()
        numero1.append(conjunto2)

resultado()

janela.mainloop()

