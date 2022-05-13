from tkinter import *

class Tela():
    def enviar(self, event):
        self.result["text"] = self.calculaImc()
        self.result.pack()

    def calculaImc(self):
        peso = float(self.caixaPeso.get())
        altura = float(self.caixaAltura.get())
        imc = (peso)/(altura**2)
        classificacao = ""

        if (imc < 18.5):
            classificacao = "Magreza"
        elif (imc >= 18.5 and imc <= 24.9):
            classificacao = "Ideal"
        elif (imc >= 25 and imc <= 29.9):
            classificacao = "Sobrepeso"
        elif (imc >= 30 and imc <= 34.9):
            classificacao = "Obesidade I"
        elif (imc >= 35 and imc <= 39.9):
            classificacao = "Obesidade II"
        else:
            classificacao = "Obesidade III"
        
        imc = (f"{imc:.2f}")
        imc =str(imc)

        return "Olá " +self.caixaNome.get()+"\nSeu IMC é de: "+imc+"\nPortanto sua classificação é: "+ classificacao
        

    def __init__(self):
        self.janela_principal = Tk()
        self.janela_principal.title("Calculadora de IMC")

        self.fonte = ("Verdana", "8")

        self.container1 = Frame(self.janela_principal, pady = 10)
        self.container1.pack()

        self.container2 = Frame(self.janela_principal, padx = 20, pady = 5)
        self.container2.pack()

        self.container3 = Frame(self.janela_principal, padx = 20, pady = 5)
        self.container3.pack()

        self.container4 = Frame(self.janela_principal, padx = 20, pady = 5)
        self.container4.pack()

        self.container5 = Frame(self.janela_principal, padx = 20, pady = 5)
        self.container5.pack()

        self.labelNome = Label(self.container1, text="Nome", font=self.fonte, width = 10)
        self.labelNome.pack(side = LEFT)

        self.caixaNome = Entry(self.container1, width = 25, font=self.fonte)
        self.caixaNome.pack(side = LEFT)

        self.labelPeso = Label(self.container2, width = 10, text="Peso", font=self.fonte)
        self.labelPeso.pack(side = LEFT)

        self.caixaPeso = Entry(self.container2, width = 25, font=self.fonte)
        self.caixaPeso.pack(side = LEFT)

        self.labelAltura = Label(self.container3, width = 10, text="Altura", font=self.fonte)
        self.labelAltura.pack(side = LEFT)

        self.caixaAltura = Entry(self.container3, width = 25, font=self.fonte)
        self.caixaAltura.pack(side = LEFT)

        self.insert = Button(self.container4, width = 10, text="Calcular IMC", font=self.fonte)
        self.insert.pack(side = LEFT)

        self.insert.bind("<Button-1>", self.enviar)

        self.result = Label(self.container5, width = 35, text="Resultado", font=self.fonte)
        self.result.pack(side = LEFT)

        mainloop()

interface = Tela()
