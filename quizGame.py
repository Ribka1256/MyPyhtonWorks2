questions : [ 
    {"Question" : "Who painted the Mona Lisa?",
    "Option": ["Leonardo da Vinci" , "Pablo Picasso" ,  "Vincent van Gogh" , "Michelangelo"],
    "Answer " : "Leonardo da Vinci"},

    {"Question" : "What is the capital city of Australia?",
    "Option" : ["Sydney", "Melbourne", "Canberra", "Brisbane"],
    "Answer" : "Canberra"

    },

    {"Question" : "Which planet is known as the Red Planet?",
    "Option" : ["Earth", "Venus", "Mars", "Jupiter"],
    "Answer" : "Mars"

    },

    {"Question" : "What is the largest mammal in the world?",
    "Option" : ["African Elephant", "Blue Whale", "Giraffe", "Orca"],
    "Answer" : "Blue Whale"},

    {"Question" : "Which element has the chemical symbol 'O'?",
    "Option" : ["Oxygen", "Gold", "Osmium", "Iron"],
    "Answer" : "Oxygen"},

    {"Question" : "Who discovered penicillin?",
    "Option" : ["Marie Curie", "Alexander Fleming", "Louis Pasteur", "Joseph Lister"],
    "Answer" : "Alexander Fleming"},

    {"Question" : "What is the longest river in the world?",
    "Option" : ["Amazon", "Yangtze", "Nile", "Mississippi"],
    "Answer" : "Nile"},

    {"Question" : "Which language has the most native speakers?",
    "Option" : ["English", "Spanish", "Mandarin Chinese", "Hindi"],
    "Answer" : "Mandarin Chinese"},

    {"Question" : "In which year did World War II end?",
    "Option" : ["1945", "1939", "1918", "1950"],
    "Answer" : "1945"},

    {"Question" : "What is the smallest prime number?",
    "Option" : ["1", "2", "3", "5"],
    "Answer" : "2"}
    ]
score = 0

def get_question(questions):
    global score
    
    for idx, question in enumerate(questions, 1):
        print(f"\nQuestion {idx}: {question['Question']}")
        letters = ['a', 'b', 'c', 'd']
        for i,option in enumerate(question['Option']):
            print(f"{letters[i]}. {option}")
        answer = input('Enter your answer(a/b/c/d): ').lower()
        if answer in letters:
            chosen_option = question['Option'][letters.index(answer)]
            if chosen_option == question['Answer']:
                print('You have got the correct answer')
                score += 1
        else:
            print('You have not gor the correct answer')
            print(f"The correct answer is {question['Answer']}")
    print(f'Your score is {score}')
    
def main():
    de= get_question(questions)

main()


import random
def guess(topOfRange):
    try:
        topOfRange = int(input('Enter the top of your range: '))
        if topOfRange < 1:
            print('Please enter a number greater than 0.')
            
    except ValueError:
        print('Invalid number. Please enter a valid integer.')
        #continue

    guessed = random.randint(1, topOfRange)

    guessedNum = False
    while True:     
        choice = int(input('Enter your choice: ')) 
        if choice < guessed:
            print('Too low!')
        elif choice > guessed:
            print('Too high')
        elif choice == guessed:
            print('You have guessed it right conguratulation')
            guessedNum = True
            print(f'You have guessed it in {score} attempt')
            break