def get_row_col():
    import random
    col = ["A", "B", "C"]
    row = [1, 2, 3]
    played = 0
    fact1 = False
    fact2 = False
    gameover = False
    repeat = True
    def printboard():
            print("A  " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
            print("  -----------")
            print("B  " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
            print("  -----------")
            print("C  " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
            print("  -----------")
            print("   1   2   3")
    board = [ [" ", " ", " "],                                                           [" ", " ", " "],                                                           [" ", " ", " "] ]
    printboard()
    while played < 9 and not gameover:
        count1 = 0
        count2 = 0
        turn = []
        setup = []
        print("\n")
        put = input("Enter the position: ")
        if len(put) != 2:
            print("You must enter 2 characters.")
            continue
        elif not put[0].isalpha():
            print("First character must be an alphabetical letter.")
            continue
        elif not put[1].isdecimal():
            print("Second character must be a number.")
            continue
        therow = int(put[1])
        put = put[0].upper() + put[1]
        if (put[0] in col):
            turn.append(put[0])
            fact1 = True
        else:
            fact1 = False
        
        if (therow in row):
            fact2 = True
        else:
            fact2 = False
            
        if ((fact2 == False) or (fact1 == False)):
            print("You did not enter an input between A to C, and 1 to 3, e.g., A2")
            continue
        else:
            turn.append(therow)      
        for c in col:
            if (put[0] == c):
                setup.append(count1)
            else:
                count1 += 1
        for r in row:
            if (therow == r):
                setup.append(count2)
            else:
                count2 += 1
        intcol = int(setup[0])
        introw = int(setup[1])
        count3 = 0
        count4 = 0
        if board[intcol][introw] == "X" or board[intcol][introw] == "O":
            print("This field has already been markeeed")
            continue
        else:
            board[intcol][introw] = "X"
        
        def crosses(playing):
            nonlocal played
            nonlocal gameover
            if playing == "X":
                message = ("You win!")
            else:
                message = ("You lose.")
            if board[0][0] == playing and board[1][0] == playing and board[2][0] == playing:
                print(message)
                gameover = True
            elif board[0][1] == playing and board[1][1] == playing and board[2][1] == playing:
                print(message)
                gameover = True
            elif board[0][2] == playing and board[1][2] == playing and board[2][2] == playing:
                print (message)
                gameover = True
            elif board[0][0] == playing and board[1][1] == playing and board[2][2] == playing:
                print (message)
                gameover = True
            elif board[1][0] == playing and board[1][1] == playing and board[1][2] == playing:
                print (message)
                gameover = True
            elif board[0][0] == playing and board[0][1] == playing and board[0][2] == playing:
                print (message)
                gameover = True
            elif board[0][2] == playing and board[1][1] == playing and board[2][0] == playing:
                print (message)
                gameover = True
            elif board[2][0] == playing and board[2][1] == playing and board[2][2] == playing:
                print (message)
                gameover = True
            else:
                played += 1
        print("\n")
        printboard()
        print("\n")
        crosses("X")
        foecol = random.randint(0,2)
        foerow = random.randint(0,2)
        foeturn = True
        
        if played == 9 or gameover == True:
            foeturn = False
            
        
        while foeturn == True:
            if board[foecol][foerow] == "X" or board[foecol][foerow] == "O":
                foecol = random.randint(0,2)
                foerow = random.randint(0,2)
            else:
                board[foecol][foerow] = "O"
                print("CPU's turn:")
                printboard()
                foeturn = False
        crosses("O")
    
    
    
 
get_row_col()