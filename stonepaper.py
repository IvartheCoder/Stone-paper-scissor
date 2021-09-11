def main():

    import random
    # r>s and s>p and p>r  
    def play():
        user = input("Whats your choice? 'r' for Rock, 'p' for paper, 's' for scissor\n")
        computer = random.choice(['r', 'p', 's'])
        
        if user == computer:
            return "it\'s a tie"
        
        if is_win(user, computer):
            return "You win and the Computer lost"
            
        if is_win(computer, user):
            return "You lost and the Computer won"

    def is_win(player, computer):

        if (player == "r" and computer == "s") or (player == "s" and computer == "p") or (player == "p" and computer == "r"):
            return True
    print(play())

    restart = input("do you wish to play again? (Y) for Yes and (N) for No.").lower()

    if restart == "y":
        main()  
    elif restart == "n":
        exit()    
main()        