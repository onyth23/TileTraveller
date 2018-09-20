x,y=1,1
Play = True

print("You can travel: (N)orth.")

while Play:
    if x == 1 and y == 1:
        move = input("Direction: ")
        move = move.lower()
        if move == "n":
            print("You can travel: (N)orth or (E)ast or (S)outh.")
            x,y=1,2
        else:
            print("Not a valid direction!")

    elif x ==  1 and y == 2:
        move = input("Direction: ")
        move = move.lower()
        if move == "n":
            print("You can travel: (E)ast or (S)outh.")
            x,y=1,3
        elif move == "e":
            print("You can travel: (S)outh or (W)est.")
            x,y=2,2
        elif move == "s":
            print("You can travel: (N)orth.")
            x,y=1,1
        else:
            print("Not a valid direction!")

    elif x ==  1 and y == 3:
        move = input("Direction: ")
        move = move.lower()
        if move == "e":
            print("You can travel: (E)ast or (W)est.")
            x,y=2,3
        elif move == "s":
            print("You can travel: (N)orth or (E)ast or (S)outh.")
            x,y=1,2    
        else:
            print("Not a valid direction!")

    elif x ==  2 and y == 1:
        move = input("Direction: ")
        move = move.lower()
        if move == "n":
            print("You can travel: (S)outh or (W)est.")
            x,y=2,2
        else:
            print("Not a valid direction!") 
    elif x ==  2 and y == 2:
        move = input("Direction: ")
        move = move.lower()
        if move == "w":
            print("You can travel: (N)orth or (E)ast or (S)outh.")
            x,y=1,2 
        elif move == "s":
            print("You can travel: (N)orth.")
            x,y=2,1 
        else:
            print("Not a valid direction!")
            
    elif x ==  2 and y == 3:
        move = input("Direction: ")
        move = move.lower()
        if move == "w":
            print("You can travel: (E)ast or (S)outh.")
            x,y=1,3
        elif move == "e":
            print("You can travel: (S)outh or (W)est.")
            x,y=3,3
        else:
            print("Not a valid direction!")
            
    elif x ==  3 and y == 1:
        print("Victory!")
        Play = False
    elif x ==  3 and y == 2:
        move = input("Direction: ")
        move = move.lower()
        if move == "n":
            print("You can travel: (S)outh or (W)est.")
            x,y=3,3 
        elif move == "s":
            x,y=3,1
        else:
            print("Not a valid direction!")
            
    elif x ==  3 and y == 3:
        move = input("Direction: ")
        move = move.lower()
        if move == "w":
            print("You can travel: (E)ast or (W)est.")
            x,y=2,3
        elif move == "s":
            print("You can travel: (N)orth or (S)outh.")
            x,y=3,2
        else:
            print("Not a valid direction!")
            