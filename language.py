import random
common_words = [
    {"spanish": "hola", "english": "hello"},
    {"spanish": "adiós", "english": "goodbye"},
    {"spanish": "gracias", "english": "thank you"},
    {"spanish": "por favor", "english": "please"},
    {"spanish": "sí", "english": "yes"},
    {"spanish": "no", "english": "no"},
    {"spanish": "¿cómo estás?", "english": "how are you?"},
    {"spanish": "bien", "english": "well"},
    {"spanish": "mal", "english": "bad"},
    {"spanish": "amigo", "english": "friend"},
    {"spanish": "familia", "english": "family"},
    {"spanish": "comida", "english": "food"},
    {"spanish": "agua", "english": "water"},
    {"spanish": "casa", "english": "house"},
    {"spanish": "escuela", "english": "school"},
    {"spanish": "trabajo", "english": "work"},
    {"spanish": "tiempo", "english": "time"},
    {"spanish": "día", "english": "day"},
    {"spanish": "noche", "english": "night"},
    {"spanish": "amor", "english": "love"},
    {"spanish": "dinero", "english": "money"},
    {"spanish": "feliz", "english": "happy"},
    {"spanish": "triste", "english": "sad"},
    {"spanish": "grande", "english": "big"},
    {"spanish": "pequeño", "english": "small"}
]

start = input('Please Enter to start the progam...')

def quiz(words, num_quiz):
    if num_quiz > len(words):
        num_quiz = len(words)
    return random.sample(words, num_quiz)

def show_quiz(quiz_words):
    
        score = 0
        for word in quiz_words:
            print(f'What is the English translation of {word["spanish"]}?')
            answer = input('Enter your answer: ').strip().lower()
            if answer == word["english"].lower():
                print('You have got the correct answer')
           
                score += 1
            else:
                print(f'❌ Wrong! The correct answer is: "{word["english"]}"\n')
                
        print(f'Your final score: {score}/{len(quiz_words)}')

while True:
   try:
        n = int(input('Enter the number of questions you would like to be asked (or 0 to exit): '))
        if n == 0:
            print('Exiting the quiz. Goodbye!')
            break
        quiz_list = quiz(common_words, n)
        show_quiz(quiz_list)
   except :
        print("Please enter a valid number.")
