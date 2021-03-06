from random import choice
import os.path


class RPSGame:
    computer_input = ''
    user_input = ''
    game_score = 0

    def __init__(self, user_name):
        self.username = user_name
        print("Hello, " + user_name)

    def greeting(self):
        if not os.path.isfile('rating.txt'):  # Checks if the database file exists and if not the creates one in same directory!
            create_file = open('rating.txt', 'w+')
            create_file.close()

        open_file_read = open('rating.txt', 'r')
        user_list = open_file_read.readlines()
        open_file_read.close()
        user_dict = {}
        for i in range(len(user_list)):  # logic of reading score from a user profile.
            user_list[i] = user_list[i].replace('\n', '')
        for user in user_list:
            user = user.split(' ')
            name = user[0]
            score = user[1]
            user_dict[name] = score
        if self.username in user_dict:  # Checks for user's previous record and starts off the game from there!
            print("Your previous profile score is " + user_dict[self.username])
            print("Play along and we'll keep adding your winning points to your profile!!")
            self.game_score = int(user_dict[self.username])
        else:  # Creates a new profile for new user
            open_file_append = open("rating.txt", 'a')
            open_file_append.write(self.username + " " + "0\n")
            open_file_append.close()
            print("Welcome to your first game, " + self.username + " (Score: 0)")
            print("Start playing and we'll keep adding it to the profile")
            self.game_score = 0
        return

    def score_reading(self):  # reads score on request when user chooses '!score'
        open_file_read = open('rating.txt', 'r')
        user_list = open_file_read.readlines()
        open_file_read.close()
        user_dict = {}
        for i in range(len(user_list)):
            user_list[i] = user_list[i].replace('\n', '')
        for user in user_list:
            user = user.split(' ')
            name = user[0]
            score = user[1]
            user_dict[name] = score
            if self.username in user_dict:
                print("Your score: " + user_dict[self.username])
                self.game_score = int(user_dict[self.username])
                break
        return

    def score_writing(self):  # updates score for the user after every round in the database
        open_file_read = open('rating.txt', 'r')
        user_list = open_file_read.readlines()
        open_file_read.close()
        user_list_new = []
        open_file_write = open('rating.txt', 'w+')
        for i in range(len(user_list)):
            user_list[i] = user_list[i].replace('\n', '')
        for user in user_list:
            user = user.split(' ')
            name = user[0]
            score = user[1]
            if name == self.username:
                score = self.game_score
            user_score_updated = str(name) + ' ' + str(score) + '\n'
            user_list_new.append(str(user_score_updated))
        open_file_write.writelines(user_list_new)
        open_file_write.close()
        return

    def game(self):  # logic of game where the computer chooses its choice and is compared to the user's choice
        while True:
            self.user_input = input("Enter choice:")
            self.choices = ['rock', 'paper', 'scissors']
            self.computer_input = choice(self.choices)
            win = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

            if self.user_input in self.choices:
                if win[self.user_input] == self.computer_input:
                    print("Well done. Computer chose " + self.computer_input + " and failed")
                    self.game_score += 100
                    player.score_writing()

                elif self.user_input == self.computer_input:
                    print("There is a draw (" + self.computer_input + ")")
                    self.game_score += 50
                    player.score_writing()
                else:
                    print("Sorry, but computer chose " + self.computer_input)

            elif self.user_input == '!score':
                player.score_reading()

            elif self.user_input == '!exit':
                print("Bye!")
                break
            else:
                print("Invalid input")


player = RPSGame(input("Enter your name:"))
player.greeting()
player.game()
