import random

movies = ["Anand", 'Drishyam', 'Golmaal', 'VikramVedha', 'Blackk Friday', 'Dangal', 'Shiva']

def create_question(movies):
    n = len(movies)
    letters = list(movies)
    temp = []
    for i in range(n):
        if letters[i] == " ":
            temp.append(' ')
        else:
            temp.append('*')
    qn = " ".join(str(x) for x in temp)
    return qn

def is_present(letter, movies):
    c = movies.count(letter)
    if c == 0:
        return False
    else:
        return True

def unlock(qn, movies, letter):
    ref = list(movies)
    qn_list = list(qn)
    temp = []
    n = len(movies)
    for i in range(n):
        if ref[i] == ' ' or ref[i] == letter:
            temp.append(ref[i])
        else:
            if qn_list[i] == '*':
                temp.append('*')
            else:
                temp.append(ref[i])
    qn_new = " ".join(str(x) for x in temp)
    return qn_new

def play():
    p1name = input('Enter Your Name player-1: \n')
    p2name = input('Enter Your Name player-2: \n')
    pp1 = 0
    pp2 = 0
    turn = 0
    willing = True

    while willing:
        print(f"Player {turn % 2 + 1} - {p1name if turn % 2 == 0 else p2name}\n")
        picked_movie = random.choice(movies)
        qn = create_question(picked_movie)
        print(qn)
        modified_qn = qn
        not_said = True

        while not_said:
            letter = input('Your Letter: ')
            if is_present(letter, picked_movie):
                # unlock the blank spaces
                modified_qn = unlock(modified_qn, picked_movie, letter)
                print(modified_qn)
                d = input('Press 1 to guess the movie or 2 to unlock another letter: ')
                if d == '1':
                    ans = input('Your answer: ')
                    if ans == picked_movie:
                        if turn % 2 == 0:
                            pp1 += 1
                        else:
                            pp2 += 1
                        print('Your answer is correct!')
                        not_said = False
                        print(f'{p1name if turn % 2 == 0 else p2name}, your score is {pp1 if turn % 2 == 0 else pp2}')
                    else:
                        print("Wrong Answer\n")
                        not_said = False # break out of the loop
            else:
                print(letter, 'not found')

        c = input('Press 1 to continue or 0 to quit: ')
        if c == '0':
            print(f'{p1name}, your score is {pp1}')
            print(f'{p2name}, your score is {pp2}')
            print('Thanks for playing')
            willing = False

        turn += 1

play()