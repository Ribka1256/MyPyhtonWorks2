import random
import json
import time  

def loadQuestion():
    with open('question.json' , 'r') as f :
        question = json.load(f)['question']
    return question

def get_randoma_question(question , num_question) :
    if num_question > len(question) :
        num_question = len(question)
    
    random_question = random.sample(question , num_question)
    return random_question

def ask_question(question) :
    print (question['Question'])
    for i,option in enumerate(question['Option']) :
        print(str(i+1) + '.',option)
        
    try:
        num = int(input('Select the correct number: '))
        if 1 <= num <= len(question['Option']):
            if question['Option'][num - 1] == question['Answer']:
                print("✅ Correct!")
                return True
            else:
                print(f"❌ Wrong! Correct answer: {question['Answer']}")
                return False
        else:
            print("❗ Invalid choice. Please select a number within the range.")
            return False
    except ValueError:
        print("❗ Invalid input. Please enter a number.")
        return False
    

question = loadQuestion()
total_question = int(input('enter the number of question : '))
random_question =get_randoma_question(question ,total_question )
correct = 0
startTime = time.time()

for question in random_question:
    isCorrect = ask_question(question)
    if isCorrect:
        correct += 1 
        
    print('-----------------------------')
    
completeTime = time.time() - startTime
print('summary')
print('total question : ', total_question )
print('correct answer : ', correct)
print('score' , str(round((correct / total_question) * 100 , 2))  + '%')
print('time : ' ,completeTime , 'seconds')
    