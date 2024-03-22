import random
from modelBasedAgent import Agente
class Ambiente():
    
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C

        self.estado = {
            self.A:random.choice(("Vazio","Cheio")),
            self.B:random.choice(("Vazio","Cheio")),
            self.C:random.choice(("Vazio","Cheio"))
        }

        self.agent = Agente(random.choice((self.A,self.B,self.C)))
        
        self.agent.memoria = {
            "A":None,
            "B":None,
            "C":None,
        }
        pass

    def estadoInicialDoAmbiente(self):
        """ESTE MÉTODO MOSTRA O ESTADO INICIAL DO AMBIENTE"""
        print("Estado inicial do Ambiente: {}.".format(self.estado))
        pass

    def localizacaoEPercepcaoInicialDoAgente(self):
        """ESTE MÉTODO MOSTRA A LOCALIZAÇÃO INICIAL DO AGENTE E O ESTADO DESSA MESMA LOCALIZAÇÃO"""
        self.local = self.agent.localizacao
        print("Localizacao inicial do agente "+str(self.local)+" estado ("+self.estado[self.local]+")")
        pass

    def accaoDoAgente(self):
        """ESTE MÉTODO PERMITE MOVER UM AGENTE NO SENTIDO HORÁRIO DE MODO QUE ELE REALIZE ACCOES"""
        if self.agent.localizacao == (0,0):
            if self.estado[self.agent.localizacao]=="Vazio":
                self.agent.accao = "Encher"
                self.agent.pontuacao += 10
                self.estado[self.agent.localizacao]="Cheio"
                self.agent.localizacao
                self.agent.accao = "Mover para (0,1)"
                self.agent.pontuacao -= 1
                self.agent.memoria["A"] = "Cheio"
            else:
                self.agent.accao = "Mover para (0,1)"
                self.agent.pontuacao -= 1
                self.agent.memoria["A"] = "Cheio"
            print("Memório do agente",self.agent.memoria)
            
            self.agent.localizacao = self.B
            if self.estado[self.agent.localizacao]=="Vazio":
                self.agent.accao = "Encher"
                self.agent.pontuacao += 10
                self.estado[self.agent.localizacao]="Cheio"
                self.agent.accao = "Mover para (0,2)"
                self.agent.pontuacao -= 1
                self.agent.memoria["B"] = "Cheio"
            else:
                self.agent.accao = "Mover para (0,2)"
                self.agent.pontuacao -= 1
                self.agent.memoria["B"] = "Cheio"
            print("Memório do agente",self.agent.memoria)

            self.agent.localizacao = self.C
            if self.estado[self.agent.localizacao]=="Vazio":
                self.agent.accao = "Encher"
                self.agent.pontuacao += 10
                self.estado[self.agent.localizacao]="Cheio"
                self.agent.memoria["C"] = "Cheio"
            else:
                self.agent.memoria["C"] = "Cheio"
                
            print("Estado do Ambiente após a realizacão das acções: \n{}.".format(self.estado))
            print("Pontuacao =",self.agent.pontuacao)
            print("Memório do agente",self.agent.memoria)
            pass

        elif self.agent.localizacao == (0,1):
            if self.estado[self.agent.localizacao]=="Vazio":
                self.agent.accao = "Encher"
                self.agent.pontuacao += 10
                self.estado[self.agent.localizacao]="Cheio"
                self.agent.accao = "Mover para (0,2)"
                self.agent.pontuacao -= 1
                self.agent.memoria["B"] = "Cheio"
            else:
                self.agent.accao = "Mover para (0,2)"
                self.agent.pontuacao -= 1
                self.agent.memoria["B"] = "Cheio"
            print("Memório do agente",self.agent.memoria)
            
            self.agent.localizacao = self.C
            if self.estado[self.agent.localizacao]=="Vazio":
                self.agent.accao = "Encher"
                self.agent.pontuacao += 10
                self.estado[self.agent.localizacao]="Cheio"
                self.agent.accao = "Mover para (0,2)"
                self.agent.pontuacao -= 1
                self.agent.memoria["C"] = "Cheio"
            else:
                self.agent.accao = "Mover para (0,2)"
                self.agent.pontuacao -= 1
                self.agent.memoria["C"] = "Cheio"
            print("Memório do agente",self.agent.memoria)

            self.agent.localizacao = self.A
            if self.estado[self.agent.localizacao]=="Vazio":
                self.agent.accao = "Encher"
                self.agent.pontuacao += 10
                self.estado[self.agent.localizacao]="Cheio"
                self.agent.memoria["A"] = "Cheio"
            else:
                self.agent.memoria["A"] = "Cheio"

            print("Estado do Ambiente após a realizacão das acções:\n {}.".format(self.estado))
            print("Pontuacao =",self.agent.pontuacao)
            print("Memório do agente",self.agent.memoria)
            pass
        
        else:
            if self.estado[self.agent.localizacao]=="Vazio":
                self.agent.accao = "Encher"
                self.agent.pontuacao += 10
                self.estado[self.agent.localizacao]="Cheio"
                self.agent.accao = "Mover para (0,0)"
                self.agent.pontuacao -= 1
                self.agent.memoria["C"] = "Cheio"
            else:
                self.agent.accao = "Mover para (0,0)"
                self.agent.pontuacao -= 1
                self.agent.memoria["C"] = "Cheio"
            print("Memório do agente",self.agent.memoria)
            
            self.agent.localizacao = self.A
            if self.estado[self.agent.localizacao]=="Vazio":
                self.agent.accao = "Encher"
                self.agent.pontuacao += 10
                self.estado[self.agent.localizacao]="Cheio"
                self.agent.accao = "Mover para (0,1)"
                self.agent.pontuacao -= 1
                self.agent.memoria['A'] = "Cheio"
            else:
                self.agent.accao = "Mover para (0,1)"
                self.agent.pontuacao -= 1
                self.agent.memoria['A'] = "Cheio"
            print("Memório do agente",self.agent.memoria)

            self.agent.localizacao = self.B
            if self.estado[self.agent.localizacao]=="Vazio":
                self.agent.accao = "Encher"
                self.agent.pontuacao += 10
                self.estado[self.agent.localizacao]="Cheio"
                self.agent.memoria['B'] = "Cheio"
            else:
                self.agent.memoria['B'] = "Cheio"
                
            print(" Estado do Ambiente após a realizacao das acções:\n {}.".format(self.estado))
            print("Pontuacao =",self.agent.pontuacao)
            print("Memório do agente",self.agent.memoria)
            pass
        pass
           
    pass