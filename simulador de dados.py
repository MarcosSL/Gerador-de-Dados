import random
class dado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.menssagem = "Quer gerar um novo valor para o dado? "

    def pergunta(self):
        res = input(self.menssagem)
        try:
            if res == "sim" or res == "s":
                self.gerar()
                self.pergunta()
            elif res == "not" or res == "n":
                print("Obrigado por jogar!!")
            else:
                print("Erro")
        except:
            print("ERROR")

    def gerar(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

dd = dado()
dd.pergunta()