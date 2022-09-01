import random

def play():
    user = input("What is your choice? \n'r' for rock, \n'p' for paper, \n's' for scissors: ")

    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It is a Tie'

    #r>s, s>p, p>r
    if is_win(user, computer):
        return 'You Won!'
    
    return 'You Lost!!'

def is_win(player, opponent):
    print(f"\nYou chose: {player}\nThe computer chose: {opponent} ")
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

def main():
    print(play())

if __name__ == '__main__':
    main()