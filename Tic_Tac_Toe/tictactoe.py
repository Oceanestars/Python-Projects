line_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
O_winner = False
O_count = 0
X_winner = False
X_count = 0
global turn
turn = 0
right = False
impossible_state = False
all_mighty_counter = 0


# Empty Board
print("---------")
print("| " + line_list[0] + " " + line_list[1] + " " + line_list[2] + " |")
print("| " + line_list[3] + " " + line_list[4] + " " + line_list[5] + " |")
print("| " + line_list[6] + " " + line_list[7] + " " + line_list[8] + " |")
print("---------")

# Functions
def toggle_move(turn):
    turn = not turn
    return turn

def check_state_O(line_list):
    counter_O = 0
    for i in line_list:
        if i == "O":
            counter_O += 1
    return counter_O


def check_state_X(line_list):
    counter_X = 0
    for i in line_list:
        if i == "X":
            counter_X += 1
    return counter_X


def check_state_empty(line_list):
    counter_empty = 0
    for i in line_list:
        if i == "_" or i == " ":
            counter_empty += 1
    return counter_empty

Num_of_O = check_state_O(line_list)
Num_of_X = check_state_X(line_list)
Num_of_empty = check_state_empty(line_list)
Num_09 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def check_input():
    coordinate = input("Enter coordinates:  ").split()
    return coordinate

while O_winner == False and X_winner == False:
    coordinate = input("Enter coordinates:  ").split()
    right = False
    while not right:
        if (coordinate[0] not in Num_09 or coordinate[0] not in Num_09) or (coordinate[1]  not in Num_09 or coordinate[1] not in Num_09) or (coordinate[1] == "" or coordinate[0] == ""):
            print("You should enter numbers!")
            coordinate = check_input()
        elif (int(coordinate[0]) < 1 or int(coordinate[0]) > 3) or (int(coordinate[1]) < 1 or int(coordinate[1]) > 3):
            print("Coordinates should be from 1 to 3!")
            coordinate = check_input()
        #  first number is the columns second num is row
        # SWITCH
        if coordinate[0] == "1": # 0, 3,6
            if coordinate[1] == "1":
                if line_list[6] == "_" or line_list[6] == " ":
                    if turn == 0:
                        line_list[6] = "X"
                        right = True
                    elif turn is True:
                        line_list[6] = "O"
                        right = True
                else:
                    print("This cell is occupied! Choose another one!")
                    right = False
                    coordinate = check_input()
            elif coordinate[1] == "2":
                if line_list[3] == "_" or line_list[3] == " ":
                    if turn == 0:
                        line_list[3] = "X"
                        right = True
                    elif turn is True:
                        line_list[3] = "O"
                        right = True
                else:
                    print("This cell is occupied! Choose another one!")
                    right = False
                    coordinate = check_input()
            elif coordinate[1] == "3":
                if line_list[0] == "_" or line_list[0] == " ":
                    if turn == 0:
                        line_list[0] = "X"
                        right = True
                    elif turn is True:
                        line_list[0] = "O"
                        right = True
                else:
                    print("This cell is occupied! Choose another one!")
                    coordinate = check_input()
        elif coordinate[0] == "2": #1,4,7
            if coordinate[1] == "1":
                if line_list[7] == "_" or line_list[7] == " ":
                    if turn == 0:
                        line_list[7] = "X"
                        right = True
                    elif turn is True:

                        line_list[7] = "O"
                        right = True
                else:
                    print("This cell is occupied! Choose another one!")
                    coordinate = check_input()
            elif coordinate[1] == "2":
                if line_list[4] == "_" or line_list[4] == " ":
                    if turn == 0:
                        line_list[4] = "X"
                        right = True
                    elif turn is True:
                        line_list[4] = "O"
                        right = True
                else:
                    print("This cell is occupied! Choose another one!")
                    coordinate = check_input()
            elif coordinate[1] == "3":
                if line_list[1] == "_" or line_list[1] == " ":
                    if turn == 0:
                        line_list[1] = "X"
                        right = True
                    elif turn is True:
                        line_list[1] = "O"
                        right = True
                else:
                    print("This cell is occupied! Choose another one!")
                    coordinate = check_input()
        elif coordinate[0] == "3":#2,5,8
            if coordinate[1] == "1":
                if line_list[8] == "_" or line_list[8] == " ":
                    if turn == 0:
                        line_list[8] = "X"
                        right = True
                    elif turn is True:
                        line_list[8] = "O"
                        right = True
                else:
                    print("This cell is occupied! Choose another one!")
                    coordinate = check_input()
            elif coordinate[1] == "2":
                if line_list[5] == "_" or line_list[5] == " ":
                    if turn == 0:
                        line_list[5] = "X"
                        right = True
                    elif turn is True:
                        line_list[5] = "O"
                        right = True
                else:
                    print("This cell is occupied! Choose another one!")
                    coordinate = check_input()
            elif coordinate[1] == "3":
                if line_list[2] == "_" or line_list[2] == " ":
                    if turn == 0:
                        line_list[2] = "X"
                        right = True
                    elif turn is True:
                        line_list[2] = "O"
                        right = True
                else:
                    print("This cell is occupied! Choose another one!")
                    coordinate = check_input()
        turn = toggle_move(turn)
        all_mighty_counter += 1

    print("---------")
    print("| " + line_list[0] + " " + line_list[1] + " " + line_list[2] + " |")
    print("| " + line_list[3] + " " + line_list[4] + " " + line_list[5] + " |")
    print("| " + line_list[6] + " " + line_list[7] + " " + line_list[8] + " |")
    print("---------")
        # horizontal & vertical
    if line_list[0] == "O" and line_list[1] == "O" and line_list[2] == "O":
        O_winner = True
        O_count += 1

    elif line_list[3] == "O" and line_list[4] == "O" and line_list[5] == "O":
        O_winner = True
        O_count += 1

    elif line_list[6] == "O" and line_list[7] == "O" and line_list[8] == "O":
        O_winner = True
        O_count += 1

    elif line_list[0] == "O" and line_list[3] == "O" and line_list[6] == "O":
        O_winner = True
        O_count += 1

    elif line_list[1] == "O" and line_list[4] == "O" and line_list[7] == "O":
        O_winner = True
        O_count += 1

    elif line_list[2] == "O" and line_list[5] == "O" and line_list[8] == "O":
        O_winner = True
        O_count += 1

    elif line_list[2] == "O" and line_list[4] == "O" and line_list[6] == "O":
        O_winner = True
        O_count += 1

    elif line_list[0] == "O" and line_list[4] == "O" and line_list[8] == "O":
        O_winner = True
        O_count += 1

        # X
    if line_list[0] == "X" and line_list[1] == "X" and line_list[2] == "X":
        X_winner = True
        X_count += 1
    elif line_list[3] == "X" and line_list[4] == "X" and line_list[5] == "X":
        X_winner = True
        X_count += 1
    elif line_list[6] == "X" and line_list[7] == "X" and line_list[8] == "X":
        X_winner = True
        X_count += 1
    elif line_list[0] == "X" and line_list[3] == "X" and line_list[6] == "X":
        X_winner = True
        X_count += 1
    elif line_list[1] == "X" and line_list[4] == "X" and line_list[7] == "X":
        X_winner = True
        X_count += 1
    elif line_list[2] == "X" and line_list[5] == "X" and line_list[8] == "X":
        X_winner = True
        X_count += 1
    elif line_list[2] == "X" and line_list[4] == "X" and line_list[6] == "X":
        X_winner = True
        X_count += 1
    elif line_list[0] == "X" and line_list[4] == "X" and line_list[8] == "X":
        X_winner = True
        X_count += 1

    if O_winner == True and X_winner == False:
        print("O wins")
    elif O_winner == False and X_winner == True:
        print("X wins")

    #Impossible state
    if X_winner == True and O_winner == True:
        impossible_state = True
        print("Impossible")
    elif Num_of_O - Num_of_X >= 2:
        impossible_state = True
        print("Impossible")
    elif Num_of_X - Num_of_O >= 2:
        impossible_state = True
        print("Impossible")
    # Game not finished
    # if all_mighty_counter <= 9 and X_winner == False and O_winner == False and impossible_state == False:
    #     print("Game not finished")

    # Draw
    if all_mighty_counter == 9:
        break
#Draw case
if X_winner == False and O_winner == False:
    print("Draw")
