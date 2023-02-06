import os
from math import *
import platform
import update_file # CHAMANDO O ATUALIZADOR


class ferramentas:
	
	# verifica valor para nevegar
	def opcao(m,M):
		while True:
			n = input("\033[92m")
			try:
				if(int(n) >= m and int(n) <= M):
					break
				else:
					print("\033[31mERRO RESPOSTA INVÁLIDA\033[m")
			except:
				print("\033[31mERRO CARACTERE INVÁLIDO\033[m")
				
		print("\033[m")
		return int(n)
	
	# Verifica se e um numero
	def valor():
		while True:
			v=input('\033[92m')
			v=v.replace(",",".")
			try:
				l=float(v)
			except:
				print("\033[91mERRO VALOR INVALIDO !!!\033[m")
			else:
				print("\033[m")
				break
		return l
	
	# Detecta a plataforma
	def plataforma():
		return platform.system()
		
	# Limpa a tela
	def limp():
		s=ferramentas.plataforma()
		
		if s == "Linux" :
			os.system("clear")
			
		if s == "Windows" :
			os.system("cls")
			
		if s == "Darwin" :
			os.system("clear")
	
	# formata para valor normal		
	def numb_valor(g):
		g=f"{float(g):.2f}"
		g=str(g).replace(".",",").strip()
		g.replace(" ","").replace("  ","")
		if(g ==""):
			return 0
		else:
			if(len(g)-1 - g.find(",") <2):
				g+="0"
		
			m=0		
			if(len(g)-3 > 3):
				m=len(g)-3
				l=list(g)
				while (m > 2):
					m-=3
					l.insert(m," ")
				r=""
				for kl in range(0,len(l)):
					r+=str(l[kl])
				g=r
			return g	

	# edita o titulo
	def titulo(text=''):
		print('\033[96m_'*50)
		print()
		print(text.center(50))
		print('\033[96m_\033[m'*50)
		print()
		
		
class calculo_eletrico():
	def __init__(self):
		 ferramentas.titulo("CALCULO DE ILUMINAÇÃO E TOMADAS")
		 
		 print("Digite a largura do comodo")
		 h=ferramentas.valor()
		 print("Digite o comprimento do comodo")
		 c=ferramentas.valor()
		 
		 p=h+h+c+c
		 area=h*c
		 ferramentas.limp()
		 ferramentas.titulo("RESULTADO")
		 print(f"Dimenções {ferramentas.numb_valor(h)} m x {ferramentas.numb_valor(c)} m")
		 print(f"Perimetro : {ferramentas.numb_valor(p)} m")
		 print(f"Area : {ferramentas.numb_valor(area)} m\n")
		 
		 if area<=6:
		 	print(f"1 ponto de iluminacao 100 VA\n")
		 else:
		 	print(f"{((area- 6)//4)+1} pontos de iluminação /carga de {(60*((area- 6)//4))+100} VA\n")
		 if p <= 6:
		 	print(f"1 ponto de tomada / carga de 100 VA \n")
		 else:
			 print(f"{p//5} pontos de tomadas / carga de {(p//5)*100} VA\n")
			 print(f"{p//3.5} pontos de tomadas caso seja uma cozinha,area de serviço etc ...\n")
			 if p//3.5<=3:
			 	print(f"carga de {(p//3.5)*600} VA com 600 VA para as 3 primeiras\n")
			 else:
			 	print(f"carga de 1800 VA com 600 VA para as 3 primeiras + {(p//3.5)-3} de 100 VA dando {((p//3.5)*100)-300} com o total de {((p//3.5)*100)+1500} VA")
		
			
class aterramento():
	def __init__(self):
		ferramentas.titulo("CALCULO DE ATERRAMENTO")
		self.run()
		
	def r3(self):
		return (self.y*100)/self.w
		
	def cor(self):
		g=self.r3()
		if(g<30):
			print('\033[91mO aterramento é Pessimo')
		if(g>30 and g<50):
			print('\033[93mO aterramento é Ruim')
		if(g>50 and g<80):
			print('\033[94mO aterramento é Intermediario')
		if(g>80):
			print('\033[92mO aterramento é Otimo')
		
	def run(self):
		print('Digite a Tensão da rede : ')
		self.w=ferramentas.valor()
		print('\033[mDigite a Tensão do aterramento : ')
		self.y=ferramentas.valor()
		
		self.cor()
		print(f"com o nivel de {self.r3():.2f} %\033[m\n")

		
class menu():
	def __init__(self):
		# VERIFICANDO ATUALIZACOES
		if update_file.check_atualizacao("https://github.com/Lucas836-hub/script_obras"):
			self.titulo("ATUALIZANDO")
			# ATUALIZANDO O SCRIPT LOCAL
			update_file.atualizar("https://github.com/Lucas836-hub/script_obras")

		ferramentas.limp()
		ferramentas.titulo("MENU PRINCIPAL")
		print("Digite 1 - para Calculo eletrico\n       2 - para Calculo de aterramento")
		op=ferramentas.opcao(1,2)
		self.seg_op(op)
		
		l=True
		while l:
			print("\n\nDigite 1 - para Excutar Novamente\n       2 - para Menu Principal\n       3 - para sair")
			n=ferramentas.opcao(1,3)
			if n == 2:
				menu()
			if n ==3:
				l=False
				exit()
			else:
				self.seg_op(op)
			
	def seg_op(self,op):
		ferramentas.limp()
		if op == 1:
			calculo_eletrico()
		if op == 2:
			aterramento()
				
if __name__ == "__main__":
	menu()