import msvcrt
import time
import os
def saveLoad(writeRead):
	if writeRead == 1:
		fichier = open("sauvegardeJeu.txt", "w")
		fichier.write(nivHDV, nivCAS, nivCAMP)
		fichier.close()

	elif writeRead == 2:
		fichier = open("sauvegardeJeu.txt", "r")
		hdv,cas,camp = fichier.read().split("$")
		hdv, nivHDV = hdv.split("_")
		cas, nivCAS = cas.split("_")
		camp, nivCAMP = camp.split("_")
		print(hdv, nivHDV, ",", cas, nivCAS, ",", camp, nivCAMP)
		fichier.close()

gold = int(0)
elixir = int(0)
nivMineOr = int(1)
nivMineElixir = int(1)
nivHDV = int(1)
nivCAS = int(1)
nivCAMP = (1)



while 1:


#MENU DES ACTIONS
	action = int(input("""----------    Menu, choisissez vos actions:			   Appuyez sur Q pour quitter.\n\n1: Voir le niveau de vos batiments\n2: Voir le montant de vos ressources
3: Améliorer un batiment\n4: Obtenir des ressources\n5: Sauvegarder et quitter\n\nChoix:"""))
	print("\n---------------------")



#ACTION 1 -- AFFICHAGE NIVEAU BATIMENTS
	if action == 1:
		print("\nHDV niveau: ", nivHDV, "\nCaserne niveau: ", nivCAS, "\nCamp niveau: ", nivCAMP, "\n")


#ACTION 2 -- AFFICHAGE GOLD / ELIXIR
	elif action == 2:
		print("\nOr: ", gold, sep = '')
		print("Elixir: ", elixir, "\n")



#ACTION 3 -- AMELIORER UN BATIMENT
	elif action == 3:
		batUp = int(input("\nQuel batiment souhaitez-vous améliorer ?\n1: HDV\n2: Caserne\n3: Camp\n4: Mine or\n5: Mine elixir\nChoix:"))
		if batUp == 1:		#Amélioration HDV
			yesNo = input("\nVous avez besoin de 100 gold pour améliorer ce bâtiment. Etes vous sûr ?\nAppuyez sur 'o' si oui, sinon appuyez sur 'n'\nChoix: ")
			if str(keyPressed) == "b'o'":
				if gold >= 100:
					nivHDV += 1				
					print("\nBravo! Votre HDV est passé au niveau ", nivHDV, "!\n")
					gold -= 100
				else:
					print("Vous n'avez pas assez d'or!\n")
			elif str(keyPressed) == "b'n'":
				print("\nTrès bien, à bientôt dans la boutique!\n")
			
			elif:
				print("Mauvaise touche, appuyez sur 'q' pour quitter!")


			"""if gold >= 100:
				nivHDV += 1				
				print("Bravo! Votre HDV est passé au niveau ", nivHDV, "!\n")
				gold -= 100
			else:
				print("Vous n'avez pas assez d'or!\n")"""

		elif batUp == 2:	#Amélioration Caserne
			yesNo = input("Vous avez besoin de 200 gold pour améliorer ce bâtiment. Etes vous sûr ?\nAppuyez sur 'o' si oui, sinon appuyez sur 'n'\nChoix: ")
			if str(keyPressed) == "b'o'":
				if gold >= 200:
					nivCAS += 1				
					print("\nBravo! Votre caserne est passé au niveau ", nivCAS, "!\n")
					gold -= 200
				else:
					print("Vous n'avez pas assez d'or!\n")
			elif str(keyPressed) == "b'n'":
				print("\nTrès bien, à bientôt dans la boutique!\n")
			
			elif:
				print("Mauvaise touche, appuyez sur 'q' pour quitter!")


		elif batUp == 3:	#Amélioration camp
			yesNo = input("Vous avez besoin de 50 gold pour améliorer ce bâtiment. Etes vous sûr ?\nAppuyez sur 'o' si oui, sinon appuyez sur 'n'\nChoix: ")
			if str(keyPressed) == "b'o'":
				if gold >= 50:
					nivCAMP += 1				
					print("\nBravo! Votre camp est passé au niveau ", nivCAMP, "!\n")
					gold -= 50
				else:
					print("Vous n'avez pas assez d'or!\n")
			elif str(keyPressed) == "b'n'":
				print("\nTrès bien, à bientôt dans la boutique!\n")
			
			elif:
				print("Mauvaise touche, appuyez sur 'q' pour quitter!")		



#ACTION 4 -- MINE D'OR / D'ELIXIR
	elif action == 4:
		print("\nAppuyez sur 'o' pour gagner de l'or, 'e' pour gagner de l'elixir ou 'q' pour quitter")
		while 1:
			time.sleep(0.05)
			keyPressed = msvcrt.getch()
			if str(keyPressed) == "b'o'":
				print(nivMineOr, " d'or gagné, total: ", gold, sep = '')
				gold += nivMineOr
			elif str(keyPressed) == "b'e'":
				print(nivMineElixir, " d'elixir gagné, total: ", elixir, sep = '')
				elixir += nivMineElixir
			elif str(keyPressed) == "b'q'":
				print("\n")
				break
			else:
				print("Mauvaise touche..")



#ACTION 5 -- SAUVEGARDER ET QUITTER
	elif action == 5:
		saveLoad(1)
		print("\n")


os.system("pause")