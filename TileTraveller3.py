x,y=1,1
Play = True
inv_dir = "Not a valid direction"


#Recives input of 1 or 0 depending on if you can travel to that direction. N E S W.
#So input of can_travel(1,1,1,1) means you can travel every dir
def can_travel(n, e, s, w):
    dirs = []
    if n == 1:
        dirs.append("(N)orth")
    if e == 1:
        dirs.append("(E)ast")
    if s == 1:
        dirs.append("(S)outh")
    if w == 1:
        dirs.append("(W)est")

    s = "You can travel: {}".format(dirs[0])

    for i in range(1, len(dirs), 1):
        s += " or " + dirs[i]
    return s

def get_move():
    u = input("Direction: ")
    u = u.lower()
    return u

while Play:
    if x == 1 and y == 1:
        print(can_travel(1,0,0,0))
        move = get_move()
        if move == 'n':
            x,y = 1,2
        else:
            print(inv_dir)
    elif x ==  1 and y == 2:
        print(can_travel(1,1,1,0))
        move = get_move()
        if move == "n":
            x,y=1,3
        elif move == "e":
            x,y=2,2
        elif move == "s":
            x,y=1,1
        else:
            print(inv_dir)
    elif x ==  1 and y == 3:
        print(can_travel(0,1,1,0))
        move = get_move()
        if move == "e":
            x,y=2,3
        elif move == "s":
            x,y=1,2
        else:
            print(inv_dir)

    elif x ==  2 and y == 1:
        print(can_travel(1,0,0,0))
        move = get_move()
        if move == "n":
            x,y=2,2
        else:
            print(inv_dir)

    elif x ==  2 and y == 2:
        print(can_travel(0,0,1,1))
        move = get_move()
        if move == "w":
            x,y=1,2
        elif move == "s":
            x,y=2,1
        else:
            print(inv_dir)

    elif x ==  2 and y == 3:
        print(can_travel(0,1,0,1))
        move = get_move()
        if move == "w":
            x,y=1,3
        elif move == "e":
            x,y=3,3
        else:
            print(inv_dir)

    #VICTORY ON 3,1
    elif x ==  3 and y == 1:
        print("Victory!")
        Play = False

    elif x ==  3 and y == 2:
        print(can_travel(1,0,1,0))
        move = get_move()
        if move == "n":
            x,y=3,3
        elif move == "s":
            x,y=3,1
        else:
            print(inv_dir)

    elif x ==  3 and y == 3:
        print(can_travel(0,0,1,1))
        move = get_move()
        if move == "w":
            x,y=2,3
        elif move == "s":
            x,y=3,2
        else:
            print(inv_dir)