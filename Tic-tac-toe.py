#ini
#this initializes the variables
def ini():
    global marker, possible_level, possible_order, possible_option, best, range, win, user_move, comp_move
    
    marker=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    possible_level=["1","2","3"]
    possible_order=["first", "second"]
    possible_option=["1","2","3"]
    range=["1","2","3","4","5","6","7","8","9"]
    win=[("1","2","3"),("4","5","6"),("7","8","9"),("1","4","7"),("1","5","9"),("2","5","8"),("3","6","9"),("3","5","7")]
    user_move=[]
    comp_move=[]
    position=" "

#boardprint
#this simply prints board on the screen
def boardprint():
        print"+-------+-------+-------+"
        print"|   1   |   2   |   3   |"
        print"|   "+marker[1]+"   |   "+marker[2]+"   |   "+marker[3]+"   |"
        print"|       |       |       |"
        print"+-------+-------+-------+"
        print"|   4   |   5   |   6   |"
        print"|   "+marker[4]+"   |   "+marker[5]+"   |   "+marker[6]+"   |"
        print"|       |       |       |"
        print"+-------+-------+-------+"
        print"|   7   |   8   |   9   |"
        print"|   "+marker[7]+"   |   "+marker[8]+"   |   "+marker[9]+"   |"
        print"|       |       |       |"
        print"+-------+-------+-------+"

#play
#this is where the game is played
def play():

    if order=="first":
        placement()
        boardprint()

        if checkwin()==None:
            raw_input("Press enter to let computer decide.")
            next_move=compmoves()
            marker[int(next_move)]="X"
            comp_move.append(next_move)
            boardprint()
            
    elif order=="second":
        raw_input("Press enter to let computer decide.")
        next_move=compmoves()
        marker[int(next_move)]="X"
        comp_move.append(next_move)
        boardprint()

        if checkwin()==None:
            placement()
            boardprint()

#placement
#this takes desired position from the user
#and updates the positions of the board
def placement():

    position=raw_input("Your turn.. choose your position: ")
    while position not in range or marker[int(position)]!=" ":
        position=raw_input("Wrong input, choose again: ") 
    marker[int(position)]="O"
    user_move.append(position)   

    
#checkwin
#this checks if there is a winner
def checkwin():
    status=" "
    
    for i in win:
        if i[0] in user_move and i[1] in user_move and i[2] in user_move:
            status="win"
            return status

    for i in win:
        if i[0] in comp_move and i[1] in comp_move and i[2] in comp_move:
            status="lose"
            return status

    if status==" ":
        if len(comp_move)+len(user_move)==9:
            return "draw"

#compmoves
#this decides the best position for computer
def compmoves():
    if level=="1":
        best=["5","1","3","7","9","2","4","6","8"]
    elif level=="2":
        best=["1","3","7","9","5","2","4","6","8"]
    elif level=="3":
        best=["2","4","6","8","1","3","7","9","5"]

#first, computer decides if there is a next move that will win the game
    for i in win:
        if i[0] in comp_move and i[1] in comp_move:
            if i[2] not in user_move:
                return i[2]
        elif i[0] in comp_move and i[2] in comp_move:
            if i[1] not in user_move:
                if level!="3":
                    return i[1]
        elif i[1] in comp_move and i[2] in comp_move:
            if i[0] not in user_move:
                if level!=3:
                    return i[0]

    #now it determines if player has a next move that will win the game

    if level!="3":
        for i in win:
            if i[0] in user_move and i[1] in user_move:
                if i[2] not in comp_move:
                    return i[2]
            elif i[0] in user_move and i[2] in user_move:
                if i[1] not in comp_move:
                    return i[1]
            elif i[1] in user_move and i[2] in user_move:
                if i[0] not in comp_move:
                    return i[0]

    #now it decides according to the best available moves
    #in insane mode, from the center(5), to the points(1,3,7,9),
    #to the sides(2,4,6,8)

    used_move=comp_move+user_move
    for i in best:
        if i not in used_move:
            return str(i)
            
 
#chooseoption
#this lets user choose the option
def chooseoption():
    print"      **********************"
    print"      *    1 - Insane      *"
    print"      *    2 - Pro         *"
    print"      *    3 - Noob        *"
    print"      **********************\n"

    level=raw_input("Level : ")
    while level not in possible_level:
        print"Your options are 1, 2, or 3"
        level=raw_input("Level : ")

    return level

#this is the main body of the program
option="1"
ini()
print"############# TIC TAC TOE #############\n"
print"Welcome to the game of tic-tac-toe"
print"Each section of the board will be marked by a number\n"
boardprint()
print"\nYou may select the difficulty level"

while option!="3":
    if option=="1":
        print"\n"
        level=chooseoption()

    order=raw_input("Would you like to go first, or second?")
    while order not in possible_order:
        print"Your options are first, or second"
        order=raw_input("Would you like to go first, or second?")        

    print"\n\n"

    boardprint()
    while checkwin()==None:
        play()
        
    if checkwin()=="win":
        print"########### Victorious! ###########\n"
    elif checkwin()=="lose":
        print"########### You were defeated! ###########\n"
    elif checkwin()=="draw":
        print"########### TIE ###########\n"

    print"Here are some options for you"
    print"\n"
    print"      *******************************"
    print"      *    1 - Change difficulty    *"
    print"      *    2 - Play again           *"
    print"      *    3 - Quit                 *"
    print"      *******************************\n"

    option=raw_input("Choose option : ")
    while option not in possible_option:
        print"Your options are 1, 2, or 3"
        option=raw_input("Choose option : ")
    ini()

print"Goodbye"

    
