# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 19:45:27 2020

@author: pasqu
"""
from sys import exit
import pandas as pd
import time
from colored import fg, bg, attr
#assegnazione dataset
dataset = pd.read_csv('dati.csv')
codice = dataset.iloc[:,0].values
importo = dataset.iloc[:,1].values
usato = dataset.iloc[:,2].values
reset = attr('reset')

def main():

	#visualizzazione menu
	controlli()
	menu()

def close():
	exit()

def one():
	print(dataset)
	print()
	print("-------------------------------------------------")
	print("---------Premi invio per tornare al menu---------")
	input()
	menu()

def two():
	print("           codice:")
	for i in range(0, len(codice)):
		print(codice[i])
	print()
	print("-------------------------------------------------")
	print("---------Premi invio per tornare al menu---------")
	input()
	menu()
    
def three():
	x = 0
	color_red_bg = bg(1)
	color_green_bg = bg(2)
	for i in range(0, len(importo)):
		x += float(importo[i])
	print("Totale speso: "+color_red_bg, x, "€" + reset)
	print("Budget disponibile: "+color_green_bg, 500 - x, "€" + reset)
	print()
	print("-------------------------------------------------")
	print("---------Premi invio per tornare al menu---------")
	input()
	menu()
  
def four():

	print("            codice importo")
	for i in range(0, len(codice)):
		if usato[i] == " ":
			print(codice[i] + " " + importo[i])
	print("-------------------------------------------------")
	print("---------Premi invio per tornare al menu---------")
	input()
	menu()

def five():
	print("-------------------------------------------------")
	cod_da_agg = input("Inserisci il codice: ")
	imp_da_agg = input("Inserisci l'importo: ")
	usat_da_agg = input("Hai usato il codice?: ")
	if usat_da_agg == "NO" or usat_da_agg == "no" or usat_da_agg == ("No") or usat_da_agg == ("nO"):
		usat_da_agg = " "
	else:
		usat_da_agg = "X"
	
	print("-------------------------------------------------")
	print("---------Premi invio per tornare al menu---------")
	input()
	menu()

def choice(x):
	if x == 0:
		print("ciao")
		return close()
	if x == 1:
		return one()    
	if x == 2:
		return two()    
	if x == 3:
		return three()
	if x == 4:
		return four()
	if x == 5:
		return five()


def menu():
	time.sleep(0.2)
	color_red = fg(124)
	color_yellow = fg(214)
	color_orange = fg(166)
	color_yellow_lg = fg(220)
	color_yellow_lg_plus = fg(226)

	print(color_red + "			|                *             )                |")
	print("			|              (  `         ( /(                |")
	print("			|              )\\))(   (    )\\())    (          |")
	print("			|             ((_)()\\  )\\  ((_)\\     )\\         |")
	print("			|             (_()((_)((_)  _((_) _ ((_)        |")
	print(color_orange + "			|             |  \\/  || __|| \\| || | | |        |")
	print("			|             | |\\/| || _| | .` || |_| |        |")
	print(color_yellow + "			|             |_|  |_||___||_|\\_| \\___/         |"+ reset)
	time.sleep(0.2)
	print(color_yellow + "			|  1) VISUALIZZAZIONE TUTTA LA TABELLA          |")
	time.sleep(0.3)
	print(color_yellow + "			|  2) VISUALIZZAZIONE TUTTI I CODICI            |")
	time.sleep(0.3)
	print(color_yellow + "			|  3) VISUALIZZAZIONE SOLDI SPESI               |")
	time.sleep(0.3)
	print(color_yellow_lg + "			|  4) VISUALIZZAZIONE CODICI NON UTILIZZATI     |")
	time.sleep(0.3)
	print( color_yellow_lg + "			|  5) INSERISCI UN NUOVO CODICE                 |")
	time.sleep(0.3)
	print(color_yellow_lg +"			|  0) USCITA                                    |")
	time.sleep(0.2)
	print(color_yellow_lg_plus + "			-------------------------------------------------")
	print(color_yellow_lg_plus + "			-------------------------------------------------"+ reset)
	print()
	print()
	print("Inserisci numero operazione da eseguire")
	x = int(input(">>>  "))
	choice(x)

def controlli():
	color = bg("chartreuse_3b")

	print("Controllo in corso")
	print("[", end = '', flush = "True")
	for i in range(0, len(importo)):
		time.sleep(0.1)
		print(color +" "+reset, end = '', flush = "True")
		importo[i] = importo[i].replace(",", ".")
	for i in range(0, len(usato)):
		time.sleep(0.1)
		print(color +" "+reset, end = '', flush = "True")
		usato[i] = str(usato[i]).replace("nan", " ")
	print("]")
	print("Controllo completato al 100%")
	print()
	print("avvio menu...")
	time.sleep(0.5)


main()
