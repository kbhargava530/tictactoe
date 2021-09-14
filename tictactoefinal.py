box1=[]
box2=[]
box3=[]
box4=[]
box5=[]
box6=[]
box7=[]
box8=[]
box9=[]



print("    box1 | box2 | box3")
print(" --------------------------")
print("    box4 | box5 | box6")
print(" --------------------------")
print("    box7 | box8 | box9")



print ("hello, welcome to tictactoe. In this game, you are tyring to get three of your symbols in a row to beat your opponent. Good luck!")
name1=input("You are player one and you will be placing X's on the board. What's your name?")
print()
name2=input("You are player two and you will be placing O's on the board. What's your name?")
print()

#move 1 player X
#MOVE 1

def moveX():
	move=input(name1 + ", where would you like to place your first X?") 
	if move == "box1":
		box1.append("X")
	elif move == "box2":
		box2.append("X")
	elif move == "box3":
		box3.append("X")
	elif move == "box4":
		box4.append("X")
	elif move == "box5":
		box5.append("X")
	elif move == "box6":
		box6.append("X")
	elif move == "box7":
		box7.append("X")
	elif move == "box8":
		box8.append("X")
	elif move == "box9": 
		box9.append("X")
		
	else:
		print("not an option")
		
	print ("    ", *box1 , "	|	",	*box2 ,	"	|	" , *box3, "	"	)
	print ("------------------------------------")
	print ("    ", *box4 , "	|	",	*box5 ,	"	|	" , *box6, "	"	)
	print ("------------------------------------")
	print ("    ", *box7 , "	|	",	*box8 ,	"	|	" , *box9, "	"	)
	
		
	
#move 1	player O
#MOVE 2
	
	move=input(name2 + ", where would you like to place your first O?") 
	if move == "box1":
		box1.append("O")
	elif move == "box2":
		box2.append("O")
	elif move == "box3":
		box3.append("O")
	elif move == "box4":
		box4.append("O")
	elif move == "box5":
		box5.append("O")
	elif move == "box6":
		box6.append("O")
	elif move == "box7":
		box7.append("O")
	elif move == "box8":
		box8.append("O")
	elif move == "box9": 
		box9.append("O")
		
	else:
		print("not an option")
				
		
	print ("    ", *box1 , "	|	",	*box2 ,	"	|	" , *box3, "	"	)
	print ("------------------------------------")
	print ("    ", *box4 , "	|	",	*box5 ,	"	|	" , *box6, "	"	)
	print ("------------------------------------")
	print ("    ", *box7 , "	|	",	*box8 ,	"	|	" , *box9, "	"	)
	
	
	
	
#move 2 player X	
#MOVE 3	
	move=input(name1 + ", where would you like to place your second X?") 
	if move == "box1":
		box1.append("X")
	elif move == "box2":
		box2.append("X")
	elif move == "box3":
		box3.append("X")
	elif move == "box4":
		box4.append("X")
	elif move == "box5":
		box5.append("X")
	elif move == "box6":
		box6.append("X")
	elif move == "box7":
		box7.append("X")
	elif move == "box8":
		box8.append("X")
	elif move == "box9": 
		box9.append("X")
		
	else:
		print("not an option")
		
	print ("    ", *box1 , "	|	",	*box2 ,	"	|	" , *box3, "	"	)
	print ("------------------------------------")
	print ("    ", *box4 , "	|	",	*box5 ,	"	|	" , *box6, "	"	)
	print ("------------------------------------")
	print ("    ", *box7 , "	|	",	*box8 ,	"	|	" , *box9, "	"	)
	
		
	
#move 2 player O	
#MOVE 4	
	move=input(name2 + ", where would you like to place your second O?") 
	if move == "box1":
		box1.append("O")
	elif move == "box2":
		box2.append("O")
	elif move == "box3":
		box3.append("O")
	elif move == "box4":
		box4.append("O")
	elif move == "box5":
		box5.append("O")
	elif move == "box6":
		box6.append("O")
	elif move == "box7":
		box7.append("O")
	elif move == "box8":
		box8.append("O")
	elif move == "box9": 
		box9.append("O")
		
	else:
		print("not an option")
				
		
	print ("    ", *box1 , "	|	",	*box2 ,	"	|	" , *box3, "	"	)
	print ("------------------------------------")
	print ("    ", *box4 , "	|	",	*box5 ,	"	|	" , *box6, "	"	)
	print ("------------------------------------")
	print ("    ", *box7 , "	|	",	*box8 ,	"	|	" , *box9, "	"	)
	


#move 3 player X	
#MOVE 5
	
	move=input(name1 + ", where would you like to place your third X?") 
	if move == "box1":
		box1.append("X")
	elif move == "box2":
		box2.append("X")
	elif move == "box3":
		box3.append("X")
	elif move == "box4":
		box4.append("X")
	elif move == "box5":
		box5.append("X")
	elif move == "box6":
		box6.append("X")
	elif move == "box7":
		box7.append("X")
	elif move == "box8":
		box8.append("X")
	elif move == "box9": 
		box9.append("X")
		
	else:
		print("not an option")
		
	print ("    ", *box1 , "	|	",	*box2 ,	"	|	" , *box3, "	"	)
	print ("------------------------------------")
	print ("    ", *box4 , "	|	",	*box5 ,	"	|	" , *box6, "	"	)
	print ("------------------------------------")
	print ("    ", *box7 , "	|	",	*box8 ,	"	|	" , *box9, "	"	)
	
	
	if "X" in box1 and "X" in box2 and "X" in box3:
		print ("you won!")
		quit()
	elif "X" in box4 and "X" in box5 and "X" in box6:
		print ("you won!")
		quit()
	elif "X" in box7 and "X" in box8 and "9" in box3:
		print ("you won!")
		quit()
	elif "X" in box1 and "X" in box4 and "X" in box7:
		print ("you won!")
		quit()
	elif "X" in box2 and "X" in box5 and "X" in box8:
		print ("you won!")
		quit()
	elif "X" in box3 and "X" in box6 and "X" in box9:
		print ("you won!")
		quit()
	elif "X" in box1 and "X" in box5 and "X" in box9:
		print ("you won!")
		quit()
	elif "X" in box3 and "X" in box5 and "X" in box7:
		print ("you won!")
		quit()
	
		
	
#move 3 player O
#MOVE 6		
	move=input(name2 + ", where would you like to place your third O?") 
	if move == "box1":
		box1.append("O")
	elif move == "box2":
		box2.append("O")
	elif move == "box3":
		box3.append("O")
	elif move == "box4":
		box4.append("O")
	elif move == "box5":
		box5.append("O")
	elif move == "box6":
		box6.append("O")
	elif move == "box7":
		box7.append("O")
	elif move == "box8":
		box8.append("O")
	elif move == "box9": 
		box9.append("O")
		
	else:
		print("not an option")
				
		
	print ("    ", *box1 , "	|	",	*box2 ,	"	|	" , *box3, "	"	)
	print ("------------------------------------")
	print ("    ", *box4 , "	|	",	*box5 ,	"	|	" , *box6, "	"	)
	print ("------------------------------------")
	print ("    ", *box7 , "	|	",	*box8 ,	"	|	" , *box9, "	"	)
	
	if "O" in box1 and "O" in box2 and "O" in box3:
		print ("you won!") 
		quit()
	elif "O" in box4 and "O" in box5 and "O" in box6:
		print ("you won!")
		quit()
	elif "O" in box7 and "O" in box8 and "O" in box3:
		print ("you won!")
		quit()
	elif "O" in box1 and "O" in box4 and "O" in box7:
		print ("you won!")
		quit()
	elif "O" in box2 and "O" in box5 and "O" in box8:
		print ("you won!")
		quit()
	elif "O" in box3 and "O" in box6 and "O" in box9:
		print ("you won!")
		quit()
	elif "O" in box1 and "O" in box5 and "O" in box9:
		print ("you won!")
		quit()
	elif "O" in box3 and "O" in box5 and "O" in box7:
		print ("you won!")
		quit()
		
	


#move 4 player X	
#MOVE 7
	
	move=input(name1 + ", where would you like to place your fourth X?") 
	if move == "box1":
		box1.append("X")
	elif move == "box2":
		box2.append("X")
	elif move == "box3":
		box3.append("X")
	elif move == "box4":
		box4.append("X")
	elif move == "box5":
		box5.append("X")
	elif move == "box6":
		box6.append("X")
	elif move == "box7":
		box7.append("X")
	elif move == "box8":
		box8.append("X")
	elif move == "box9": 
		box9.append("X")
		
	else:
		print("not an option")
		
	print ("    ", *box1 , "	|	",	*box2 ,	"	|	" , *box3, "	"	)
	print ("------------------------------------")
	print ("    ", *box4 , "	|	",	*box5 ,	"	|	" , *box6, "	"	)
	print ("------------------------------------")
	print ("    ", *box7 , "	|	",	*box8 ,	"	|	" , *box9, "	"	)
	

	if "X" in box1 and "X" in box2 and "X" in box3:
		print ("you won!")
		quit()
	elif "X" in box4 and "X" in box5 and "X" in box6:
		print ("you won!")
		quit()
	elif "X" in box7 and "X" in box8 and "9" in box3:
		print ("you won!")
		quit()
	elif "X" in box1 and "X" in box4 and "X" in box7:
		print ("you won!")
		quit()
	elif "X" in box2 and "X" in box5 and "X" in box8:
		print ("you won!")
		quit()
	elif "X" in box3 and "X" in box6 and "X" in box9:
		print ("you won!")
		quit()
	elif "X" in box1 and "X" in box5 and "X" in box9:
		print ("you won!")
		quit()
	elif "X" in box3 and "X" in box5 and "X" in box7:
		print ("you won!")
		quit()
	
		
	
#move 4 player O
#MOVE 8	
	move=input(name2 + ", where would you like to place your fourth O?") 
	if move == "box1":
		box1.append("O")
	elif move == "box2":
		box2.append("O")
	elif move == "box3":
		box3.append("O")
	elif move == "box4":
		box4.append("O")
	elif move == "box5":
		box5.append("O")
	elif move == "box6":
		box6.append("O")
	elif move == "box7":
		box7.append("O")
	elif move == "box8":
		box8.append("O")
	elif move == "box9": 
		box9.append("O")
		
	else:
		print("not an option")
				
		
	print ("    ", *box1 , "	|	",	*box2 ,	"	|	" , *box3, "	"	)
	print ("------------------------------------")
	print ("    ", *box4 , "	|	",	*box5 ,	"	|	" , *box6, "	"	)
	print ("------------------------------------")
	print ("    ", *box7 , "	|	",	*box8 ,	"	|	" , *box9, "	"	)
	
	if "O" in box1 and "O" in box2 and "O" in box3:
		print ("you won!") 
		quit()
	elif "O" in box4 and "O" in box5 and "O" in box6:
		print ("you won!")
		quit()
	elif "O" in box7 and "O" in box8 and "O" in box3:
		print ("you won!")
		quit()
	elif "O" in box1 and "O" in box4 and "O" in box7:
		print ("you won!")
		quit()
	elif "O" in box2 and "O" in box5 and "O" in box8:
		print ("you won!")
		quit()
	elif "O" in box3 and "O" in box6 and "O" in box9:
		print ("you won!")
		quit()
	elif "O" in box1 and "O" in box5 and "O" in box9:
		print ("you won!")
		quit()
	elif "O" in box3 and "O" in box5 and "O" in box7:
		print ("you won!")
		quit()
		
	
	
#move 5 player X
#MOVE 9 FINAL MOVE
	move=input(name1 + ", where would you like to place your FINAL X?") 
	if move == "box1":
		box1.append("X")
	elif move == "box2":
		box2.append("X")
	elif move == "box3":
		box3.append("X")
	elif move == "box4":
		box4.append("X")
	elif move == "box5":
		box5.append("X")
	elif move == "box6":
		box6.append("X")
	elif move == "box7":
		box7.append("X")
	elif move == "box8":
		box8.append("X")
	elif move == "box9": 
		box9.append("X")
		
	else:
		print("not an option")
		
	print ("    ", *box1 , "	|	",	*box2 ,	"	|	" , *box3, "	"	)
	print ("------------------------------------")
	print ("    ", *box4 , "	|	",	*box5 ,	"	|	" , *box6, "	"	)
	print ("------------------------------------")
	print ("    ", *box7 , "	|	",	*box8 ,	"	|	" , *box9, "	"	)
	
	
	if "X" in box1 and "X" in box2 and "X" in box3:
		print ("you won!")
		quit()
	elif "X" in box4 and "X" in box5 and "X" in box6:
		print ("you won!")
		quit()
	elif "X" in box7 and "X" in box8 and "9" in box3:
		print ("you won!")
		quit()
	elif "X" in box1 and "X" in box4 and "X" in box7:
		print ("you won!")
		quit()
	elif "X" in box2 and "X" in box5 and "X" in box8:
		print ("you won!")
		quit()
	elif "X" in box3 and "X" in box6 and "X" in box9:
		print ("you won!")
		quit()
	elif "X" in box1 and "X" in box5 and "X" in box9:
		print ("you won!")
		quit()
	elif "X" in box3 and "X" in box5 and "X" in box7:
		print ("you won!")
		quit()
	else:	
		print ("nobody won")

print("hello")	
moveX()



