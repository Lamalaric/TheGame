import msvcrt
import time
import os
def saveLoad(writeRead, ORE, LIQUID, NivHDV, NivCAS, NivCAMP, NivMineOr, NivMineElixir):
	if writeRead == 1:
		toWrite = ("Gold : " + str(ORE) + " $Elixir :" + str(LIQUID) +  "$Niveau HDV :" + str(NivHDV) + "$Niveau caserne :" + str(NivCAS) + "$Niveau camp :" + str(NivCAMP)+ "$Niveau mine Or :" + str(NivMineOr)+ "$Niveau mine Elixir :" + str(NivMineElixir))
		fichier = open("gameSave.txt", "w")
		fichier.write(toWrite)
		fichier.close()
		quit()

	elif writeRead == 2: 
		fichier = open("gameSave.txt", "r")
		hdv,cas,camp = fichier.read().split("$")
		hdv, nivHDV = hdv.split("_")
		cas, nivCAS = cas.split("_")
		camp, nivCAMP = camp.split("_")
		print(hdv, nivHDV, ",", cas, nivCAS, ",", camp, nivCAMP)
		fichier.close()

def main():


	gold = int(500)
	elixir = int(500)
	nivMineOr = int(1)
	nivMineElixir = int(1)
	nivHDV = int(1)
	nivCAS = int(1)
	nivCAMP = (1)


	while 1:

	#MENU DES ACTIONS
		print("""----------    Menu, choisissez vos actions:			   Appuyez sur Q pour quitter.\n\n1: Voir le niveau de vos batiments\n2: Voir le montant de vos ressources
3: Améliorer un batiment\n4: Obtenir des ressources\n5: Sauvegarder et quitter\n\nChoix:""", end='')
		action = msvcrt.getch()
		print("\n---------------------")


	#ACTION 1 -- AFFICHAGE NIVEAU BATIMENTS
		if str(action) == "b'1'":
			print("\nHDV niveau: ", nivHDV, "\nCaserne niveau: ", nivCAS, "\nCamp niveau: ", nivCAMP, "\nMine d'or niveau: ", nivMineOr, "\nMine d'elixir niveau: ", nivMineElixir, "\n")


	#ACTION 2 -- AFFICHAGE GOLD / ELIXIR
		elif str(action) == "b'2'":
			print("\nVous avez ", gold, " or.", sep = '')
			print("Vous avez", elixir, "elixir.\n")



	#ACTION 3 -- AMELIORER UN BATIMENT
		elif str(action) == "b'3'":
			batUp = int(input("\nQuel batiment souhaitez-vous améliorer ?\n1: HDV\n2: Caserne\n3: Camp\n4: Mine or\n5: Mine elixir\nChoix:"))
			
			if batUp == 1:		#Amélioration HDV
				print("\nVous avez besoin de 100 gold pour améliorer ce bâtiment. Etes vous sûr ?\nAppuyez sur 'o' si oui, sinon appuyez sur 'n'\nChoix: ")
				keyPressed = msvcrt.getch()
				if str(keyPressed) == "b'o'":
					if gold >= 100:
						nivHDV += 1				
						print("\nBravo! Votre HDV est passé au niveau ", nivHDV, "!\n")
						gold -= 100
					else:
						print("Vous n'avez pas assez d'or!\n")
				elif str(keyPressed) == "b'n'":
					print("\nTrès bien, à bientôt dans la boutique!\n")
				
				else:
					print("Mauvaise touche, appuyez sur 'q' pour quitter!")



			elif batUp == 2:	#Amélioration Caserne
				print("Vous avez besoin de 200 gold pour améliorer ce bâtiment. Etes vous sûr ?\nAppuyez sur 'o' si oui, sinon appuyez sur 'n'\nChoix: ")
				keyPressed = msvcrt.getch()
				if str(keyPressed) == "b'o'":
					if gold >= 200:
						nivCAS += 1				
						print("\nBravo! Votre caserne est passé au niveau ", nivCAS, "!\n")
						gold -= 200
					else:
						print("Vous n'avez pas assez d'or!\n")
				elif str(keyPressed) == "b'n'":
					print("\nTrès bien, à bientôt dans la boutique!\n")
				
				else:
					print("Mauvaise touche, appuyez sur 'q' pour quitter!")



			elif batUp == 3:	#Amélioration camp
				print("Vous avez besoin de 50 gold pour améliorer ce bâtiment. Etes vous sûr ?\nAppuyez sur 'o' si oui, sinon appuyez sur 'n'\nChoix: ")
				keyPressed = msvcrt.getch()
				if str(keyPressed) == "b'o'":
					if gold >= 50:
						nivCAMP += 1				
						print("\nBravo! Votre camp est passé au niveau ", nivCAMP, "!\n")
						gold -= 50
					else:
						print("Vous n'avez pas assez d'or!\n")
				elif str(keyPressed) == "b'n'":
					print("\nTrès bien, à bientôt dans la boutique!\n")
				
				else:
					print("Mauvaise touche, appuyez sur 'q' pour quitter!")	



			elif batUp == 4:	#Amélioration mine d'or
				print("Vous avez besoin de 50 gold pour améliorer ce bâtiment. Etes vous sûr ?\nAppuyez sur 'o' si oui, sinon appuyez sur 'n'\nChoix: ")
				keyPressed = msvcrt.getch()
				if str(keyPressed) == "b'o'":
					if gold >= 50:
						nivMineOr += 1				
						print("\nBravo! Votre mine d'or est passé au niveau ", nivMineOr, "!\n")
						gold -= 50
					else:
						print("Vous n'avez pas assez d'or!\n")
				elif str(keyPressed) == "b'n'":
					print("\nTrès bien, à bientôt dans la boutique!\n")
				
				else:
					print("Mauvaise touche, appuyez sur 'q' pour quitter!")	



			elif batUp == 5:	#Amélioration mine d'elixir
				print("Vous avez besoin de 50 gold pour améliorer ce bâtiment. Etes vous sûr ?\nAppuyez sur 'o' si oui, sinon appuyez sur 'n'\nChoix: ")
				keyPressed = msvcrt.getch()
				if str(keyPressed) == "b'o'":
					if gold >= 50:
						nivMineElixir += 1				
						print("\nBravo! Votre mine d'elixir est passé au niveau ", nivMineElixir, "!\n")
						gold -= 50
					else:
						print("Vous n'avez pas assez d'or!\n")
				elif str(keyPressed) == "b'n'":
					print("\nTrès bien, à bientôt dans la boutique!\n")
				
				else:
					print("Mauvaise touche, appuyez sur 'q' pour quitter!")	



	#ACTION 4 -- MINE D'OR / D'ELIXIR
		elif str(action) == "b'4'":
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
					print("Mauvaise touche")



	#ACTION 5 -- SAUVEGARDER ET QUITTER
		elif str(action) == "b'5'": 
			saveLoad(1, gold, elixir, nivHDV, nivCAS, nivCAMP, nivMineOr, nivMineElixir)
			print("\n")

	#ACTION Q -- QUITTER
		elif str(action).lower() == "b'q'":
			quit()

	#ACTION AUTRES -- ERREUR
		else:
			main()

			

main()
os.system("pause")