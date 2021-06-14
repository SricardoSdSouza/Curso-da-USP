'Calculando a Iluminação'
print("ESTE PROGRAMA VISA CALCULAR A ILUMINAÇÃO NECESSÁRIA PARA SEU COMODO")
import math
comprimento = float(input("Digite o valor do comprimento = "))
altura = float(input("Digite o valor para a altura = "))
largura = float(input("Digite o valor da largura = "))
k=round(float((comprimento*largura)/((comprimento+largura)*altura)),2)
area=comprimento*largura
y=k
if k >4.5:
    print("A letra da tabela 10 é = A ") 
elif y > 3.5 and y <= 4.5:
    y =y-0.1
    k==y
    print("A letra da tabela 10 para K =",k,"é : B")
elif y >2.75 and y <= 3.5:
    y=y-0.1
    k==y
    print("A letra da tabela 10 para K =",k,"é : C")
elif y >2.25 and y <= 2.75:
    y=y-0.1
    k==y
    print(" A letra da tabela 10 para K =",k,"é : D")
elif y >1.75 and y <= 2.25:
    y=y-0.1
    k==y
    print(" A letra da tabela 10 para K =",k,"é : E")
elif y >1.35 and y <= 1.75:
    y=y-0.1
    k==y
    print(" A letra da tabela 10 para k =",k,"é : F")
elif y >1.12 and y <= 1.35:
    y=y-0.1
    k==y
    print(" A letra da tabela 10 para K =",k,"é : G")
elif y > 0.90 and y <= 1.12:
    y=y-0.1
    k==y
    print(" A letra da tabela 10 para K =",k,"é : H")
elif y >= 0.70 and y <= 0.90:
    print(" A letra da tabela 10 para K =",k,"é : I")
elif y <= 0.70:
    y=y-0.1
    k==y
    print(" A letra da tabela 10 para K=",k,"é = J")   
else:
    print("Não existe na tabela 10")

idade=int(input("Digite a idade que frequentará o ambiente = "))
velocidadeDePrecisao=(input("\nDigite a Velocidade de precisão, se = sem importância, Importante, Critica = "))
VdP=velocidadeDePrecisao
percentual=int(input("Digite o percentual de refletância do ambiente sem o simbolo % = "))
luminancia=int(input("Na tabela 4 ou 6, verifique a quantidade de lux necessária = "))
Utilização=float(input("Digite o coeficiente de utilização = "))
depreciacao=float(input("Digite o fator de depreciação=  "))
fatorManutenção=float(input("Digite o fator de manutenção = "))
lampada=float(input("Digite a potência em Watts da lâmpada que será utilizada = "))
lux=float(input("Digite a quantidade de lux da lãmpada = "))
if idade <40:
    SomaIdade=-1
elif idade >= 40 and idade <= 55:
    SomaIdade=0
else:
    SomaIdade=1
if len(VdP) == 15:
    SomaIdade =SomaIdade + -1
elif len(VdP) == 10:
    SomaIdade =SomaIdade + 0
else:
    SomaIdade =SomaIdade + 1
if percentual > 70:
    SomaIdade =SomaIdade + -1
if percentual >=30 and percentual <=70:
    SomaIdade =SomaIdade + 0
else:
    SomaIdade =SomaIdade + 1
phi=round(float((luminancia*area)/(Utilização*depreciacao)),2)
theta=int(lampada*lux)
quantidadeLampadas=int(phi/theta)
fluxoL=round(float((luminancia*area)/(Utilização*depreciacao*fatorManutenção)),2)

print("A quantidade de lãmpadas necessárias pelo calculo de fato médio é = ",quantidadeLampadas,".")
print("A quantidade de lãmpadas necessárias pelo calculo de fluxo luminoso é = ",quantidadeLampadas,".")

