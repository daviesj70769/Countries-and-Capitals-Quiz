import csv
from random import shuffle

country_list = []
leaderboard = []

def read_file(file_name):
        with open(file_name + '.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)

            next(reader)
            for line in reader:
                if file_name == 'country_capitals_csv':
                    country_list.append([line[0], line[1]])
                    shuffle(country_list)
                else:
                    leaderboard.append([line[0], line[1]])

def write_file(name, score):
        with open('scores.csv', 'a', newline='\n') as scores:
            writer = csv.writer(scores)
            writer.writerow([name, score])

def load_scores():
        leaderboard.clear()
        try:
            read_file('scores')
            leaderboard.sort(key=lambda leader: leader[1], reverse=True)
        except FileNotFoundError:
            write_file('name', 'score')

while True:
        read_file('country_capitals_csv')
        load_scores()

        my_score = 0
        print("How well do you know your capitals?\nType 'quit' at any time to exit\n" + "*" * 35)

        for i in range(10):
            guess = input("What is the capital of {country_list[i][0]}?\n>> ")
            if guess == 'quit':
                break
            if guess.title() == country_list[i][1]:
                my_score += 1
                print('Correct!')
            else:
                print("The correct answer is {country[i][1]}")
            print('Your score is: ', my_score)

        print("Game Over\nScore:", my_score)
        my_name = input("Enter your name to save the score: ")
        if len(my_name) > 0:
            write_file(my_name, my_score)
        else:
            write_file('Player', my_score)

        print("Top Scores:")

        load_scores()

        if len(leaderboard) < 3:
            for i in range(len(leaderboard)):
                print('{i + 1}. {leader board[i][0]} - {leader board[i][1]}')
        else:
            for i in range(3):
                print('{i + 1}. {leader board[i][0]} - {leader board[i][1]}')

        play_again = input("Type yes to play again: ")
        if play_again.lower() != 'yes':
            break

        print("Thank you for playing")

