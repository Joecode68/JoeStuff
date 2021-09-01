# Tic Tac Toe
#
# This is my version of Tic Tac Toe - Joe Fernandez
#
# The following are workareas
# and constants identified by all caps in their names.

tsq01 = {'sq01':' ','sq02':' ','sq03':' ','sq04':' ','sq05':' ','sq06':' ',
         'sq07':' ','sq08':' ','sq09':' '}
# Available choices - updated, removed, as the square positions are chosen
tsq02 = {'sq01':'1','sq02':'2','sq03':'3','sq04':'4','sq05':'5','sq06':'6',
         'sq07':'7','sq08':'8','sq09':'9'}
# KEYS to the squares
KEYS = ['sq01','sq02','sq03','sq04','sq05','sq06','sq07','sq08','sq09']
# Win Combinations

WIN_COMB = {'h1':['sq01','sq02','sq03'],'h2':['sq04','sq05','sq06'],'h3':['sq07','sq08','sq09'],
            'v1':['sq01','sq04','sq07'],'v2':['sq02','sq05','sq08'],'v3':['sq03','sq06','sq09'],
            'd1':['sq01','sq05','sq09'],'d2':['sq03','sq05','sq07']}
WIN_KEYS = ['h1','h2','h3','v1','v2','v3','d1','d2']
result = ' '
available_choices = []
current_player = ' '
xoro = ['x','X','o','O']
TAG = '-'
keep_playing = True
answer = ' '
check = False
yes_no = ['y','Y','n','N']
# from IPython.display import clear_output
import os
from os import system, name

# define our clear function
def clear_screen():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')



def set_players():
    global available_choices, current_player
    current_player = get_player()
    print(current_player)
    available_choices = update_choices(available_choices)
    return


def get_player():
    global current_player,xoro
    current_player = ' '
    while (current_player in xoro) != True:
        current_player = input("First player please select your preference : X or O   ")
        # print(current_player)
    else:
        return current_player.upper()


def board_print():
    print(f' Tic Tac Toe\t\tAvailable Choices\n')
    for x in range(0,8,3):
        print(f'   |   |   \t\t   |   |   ')
        print(f"{tsq01[KEYS[x]]}  | {tsq01[KEYS[x+1]]} | {tsq01[KEYS[x+2]]} \t\t {tsq02[KEYS[x]]} | {tsq02[KEYS[x+1]]} | {tsq02[KEYS[x+2]]}  ")
        print(f'   |   |   \t\t   |   |   ')
        if x != 6:
            print(f'___|___|___\t\t___|___|___')
        else:
            # print(f'\n\n Available Choices Length: {len(available_choices)}')
            continue
    return



def update_choices(lst):
    lst = []
    for x in range(len(tsq02)):
        if tsq02[KEYS[x]]!= '-':
            lst.append(tsq02[KEYS[x]])
            continue
        else:
            continue
    return lst


def get_choice(x):
    print(f'\n\nPlayer {current_player}\n')
    while (x in available_choices) != True:
        x = input("Select a location number from the Available Choices :  ")
        #print(x)
       # x = x
    else:
        return int(x)


def update_board():             # update the board
    global result, current_player
    tsq01[KEYS[result-1]] = current_player
    tsq02[KEYS[result-1]] = TAG
    return



def update_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
    return


def check_winner(x,y,z):
    for w in range(len(WIN_KEYS)):
        if tsq01[x[y[w]][0]] == z and tsq01[x[y[w]][1]] == z and tsq01[x[y[w]][2]] == z:
            return True
            break
        else:
            continue
    else:
        return False


def play_game():
    global check, tsq01, tsq02, available_choices, result
    while (len(available_choices)) != 0:
        #print('\n'*100)
        #clear_output()
        clear_screen()
        board_print()
        result = get_choice(result)
        # print(result)
        update_board()
        if len(available_choices) <=5:
            check = check_winner(WIN_COMB,WIN_KEYS,current_player)
            if  check == True:
                break
            else:
                pass
        else:
            pass
        update_player()
        available_choices = update_choices(available_choices)

    clear_screen()
    # print('\n'*100)
    #clear_output()
    board_print()
    if  check == True:
        print(f'\n\nPlayer {current_player} is the Winner!!\n\n')
    else:
        print(f'\n\nNo Winners - A Tie Game!!\n\n')
        pass

    # Tic Tac Toe input squares
    tsq01 = {'sq01':' ','sq02':' ','sq03':' ','sq04':' ','sq05':' ','sq06':' ',
             'sq07':' ','sq08':' ','sq09':' '}
    # Available choices - updated, removed, as the square positions are chosen
    tsq02 = {'sq01':'1','sq02':'2','sq03':'3','sq04':'4','sq05':'5','sq06':'6',
             'sq07':'7','sq08':'8','sq09':'9'}
    check = False
    return



def tic_tac_toe():
    global keep_playing, answer
    while keep_playing == True:
        set_players()
        play_game()
        answer = ' '
        while (answer in yes_no) != True:
            answer = input("Play again? : y for Yes; n for No   ")
        else:
            answer = answer.upper()
            if answer == 'N':
                keep_playing = False
            else:
                continue
    else:
        keep_playing = True
        print(f'\n\nThank You for playing Tic Tac Toe')
        return



tic_tac_toe()
