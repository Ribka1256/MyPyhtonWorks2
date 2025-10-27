animal = [
    {'animalType' : 'dog' , 'name' : 'joe', 'age' : '3'},
    {'animalType' : 'cat' , 'name' : 'emma', 'age' : '3'},
    {'animalType' : 'rabbit' , 'name' : 'finn', 'age' : '8'},
    {'animalType' : 'parott' , 'name' : 'kely', 'age' : '6'},
    
]
try:
    with open('THEANIMALLIST.txt', 'r') as infile:
        for line in infile:
            try:
                animalType , name, age = line.strip().split(',')
                animal.append({
                    'animalType ' : animalType,
                    'name' : name,
                    'age' : age,
                })
                
            except:
                print('⚠️ Skipping a malformed line in the file.')
        
except FileNotFoundError:
    print('📂 <THEANIMALLIST.txt> not found — starting with default animal list.')
   

def addAnimal():
    print('adding another animal')
    animalType = input('Enter the name the animal you would like to enter : ')
    name = input('Enter the pet the of the you entered : ')
    age = input('Enter the age of the animal you entered : ')
    
    animal.append({
        'animalType': animalType,
        'name': name,
        'age': age
    })
    print('animal added succesfully')
    
def displayAnimal():
    print('Displaying the animals ')
    for i, entry in enumerate(animal, 1):
        print(f"{i}. {entry['animal']} named {entry['name']} {entry['age']} ")

def searchAnimal():
    print('searching the animal')
    searchType= input('Enter the animal type you would like to search : ').lower()
    found = False
    for entry in animal :
        if entry['animalType'].lower() == searchType:
            print(f"✅ Found: {entry['animalType']} named {entry['name']} ({entry['age']} years old)")
            found = True 
    if not found :
        print('not found')
            
print ('-----------ANIMAL TYPE DATABASE------------------')
while True :
    choice = input('WOULD YOU LIKE TO ADD , SEARCH , DISPLAY ANIMAL TYPE , NAME AND AGE OR QUIT OUT OF THE PROGRAM : ').lower()
    if choice == 'add':
        addAnimal()
    elif choice == 'display':
        displayAnimal()
    elif choice == 'search':
        searchAnimal()
    elif choice == 'quit':
        print('💾 Saving to file...')
        try:
          with open('THEANIMALLIST.txt', 'w') as outfile:
            for entry in animal:
                outfile.write(','.join([entry['animalType'], entry['name'], str(entry['age'])]) + '\n')
            print('✅ File saved. Exiting the program. Goodbye!')
            break
        except Exception as e:
            print('❌ Error saving to file.')
            break
    else :
        print('invaild choice try again')
        continue
    
            

        
        
    
