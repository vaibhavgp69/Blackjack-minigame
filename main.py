import random
import os
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def print_results(ply_cards,comp_cards):
	print(f"\nYour cards were: {ply_cards} , Your score : {sum(ply_cards)}")
	print(f"\nComputers cards were: {comp_cards} , Computers score : {sum(comp_cards)}")

def game():
	os.system('cls')
	k=0
	print(logo)
	comp_cards=random.choices(cards,k=2)
	ply_cards=random.choices(cards,k=2)
	print(f"\n\n\nYour cards: {ply_cards} , current score : {sum(ply_cards)}")
	print(f"\nComputers First card: {comp_cards[0]}")
	
	#comps game
	while (sum(comp_cards)<=17):
		comp_cards.append(random.choice(cards))
		if 11 in comp_cards and sum(comp_cards)>21:
				comp_cards.remove(11)
				comp_cards.append(1)
	if(sum(ply_cards)==21):
		print("\n\nYou win with a BlackJack 😌/ayo\😌")
		print_results(ply_cards,comp_cards)	
		k=1
	while (sum(ply_cards)<21):
		if input("\nType 'y' to Get another card ,type 'n' to pass: ")=='y':
			new_card=random.choice(cards)
			ply_cards.append(new_card)
			if 11 in ply_cards and sum(ply_cards)>21:
				ply_cards.remove(11)
				ply_cards.append(1)
			print(f"\nYou pulled a : {new_card} , Your total is : {sum(ply_cards)}")
		
		else:
			break	
	
		
	if sum(ply_cards)>21 and 11 not in ply_cards:
		print("\n\nYou Lose from overpulling 😔")
		print_results(ply_cards,comp_cards)
		
	elif (sum(ply_cards)==sum(comp_cards)):
		print("\n\nDraw")
		print_results(ply_cards,comp_cards)
		
	elif(sum(ply_cards)==21) and k!=1:
		print("\n\nYou win with a BlackJack 😌/ayo\😌")
		print_results(ply_cards,comp_cards)		
	
	elif (sum(comp_cards))>21 :
		print("\n\nYou win , computer overpulled 😌")
		print_results(ply_cards,comp_cards)

	elif(sum(comp_cards)==21):
		print("\n\\nYou lose , Computer got  a BlackJack 💀💀")
		print_results(ply_cards,comp_cards)	
		
	elif(sum(ply_cards)<21):
		if (sum(ply_cards)>sum(comp_cards)):
			print("\n\nYou win against the computer 😌")
			print_results(ply_cards,comp_cards)
		else:
			print("\n\nYou lose against the computer 😔 ")
			print_results(ply_cards,comp_cards)
	start()
def start():
	if input("\n\n\nDo you want to Play a game of Black-Jack? , enter 'y' for yes and 'n for no'") =='y':
	 	game()
	else:
		os.system('cls')
		print(logo)
		print("\n\nThank you for playing Blackjack :)")
start()







