import random
question_bank = [
    {
        "Question": "What is the capital of France?",
        "Option": ["A. Paris", "B. Madrid", "C. Berlin", "D. Rome"],
        "Answer": "Paris"
    },
    {
        "Question": "Which gas do plants absorb from the atmosphere?",
        "Option": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"],
        "Answer": "Carbon Dioxide"
    },
    {
        "Question": "How many continents are there on Earth?",
        "Option": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "Answer": "7"
    },
    {
        "Question": "What is the hardest natural substance on Earth?",
        "Option": ["A. Iron", "B. Gold", "C. Diamond", "D. Quartz"],
        "Answer": "Diamond"
    },
    {
        "Question": "Who was the first person to walk on the Moon?",
        "Option": ["A. Buzz Aldrin", "B. Yuri Gagarin", "C. Neil Armstrong", "D. John Glenn"],
        "Answer": "Neil Armstrong"
    },
    {
        "Question": "Which is the largest ocean in the world?",
        "Option": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"],
        "Answer": "Pacific Ocean"
    },
    {
        "Question": "Which country is known as the Land of the Rising Sun?",
        "Option": ["A. China", "B. India", "C. South Korea", "D. Japan"],
        "Answer": "Japan"
    },
    {
        "Question": "What is the boiling point of water at sea level?",
        "Option": ["A. 90°C", "B. 95°C", "C. 100°C", "D. 105°C"],
        "Answer": "100°C"
    },
    {
        "Question": "Which instrument measures atmospheric pressure?",
        "Option": ["A. Thermometer", "B. Barometer", "C. Anemometer", "D. Hygrometer"],
        "Answer": "Barometer"
    },
    {
        "Question": "What is the chemical symbol for gold?",
        "Option": ["A. Ag", "B. Au", "C. Gd", "D. Go"],
        "Answer": "Au"
    }
]


def get_random_question(question_bank, num_question):
    if num_question > len(question_bank):
        num_question = len(question_bank)
    return random.sample(question_bank, num_question)
      
  
def getQuestion(questions):
    score = 0
    for idx, Question in enumerate(questions, 1):
        print(f"\nQuestion {idx}: {Question['Question']}")
        for option in Question['Option']:
            print(option)

        answer = input('Select the correct answer (A/B/C/D): ').strip().upper()
        choices_map = {option[0]: option[3:].strip() for option in Question['Option']}

        if answer in choices_map:
            selected_answer = choices_map[answer]
            if selected_answer == Question['Answer']:
                print('YOU HAVE GOT THE CORRECT ANSWER!')
                score += 1
            else:
                print("YOU HAVEN'T GOT THE CORRECT ANSWER!")
        else:
            print('Invalid choice! Try again')

    print(f'\nYou scored {score} out of {len(questions)}')

  
      
while True:
  try :
    n = int(input ('Enter the number question you would like to be asked : '))
    selectedOnes = get_random_question(question_bank, n)
    getQuestion(selectedOnes)
  except :
    print('Enter a valid number')
    continue
  again = input("Do you want to play again? (y/n): ").lower()
  if again != 'y':
      print("Thanks for playing!")
      break
  
 