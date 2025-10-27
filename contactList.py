def add_person():
    name = input('Name: ') 
    age = input('Age: ')
    email = input('Email: ')
    
    person = {'name': name, 'age': age, 'email': email}
    return person

def display_people(people):
    if not people:
        print("No people in the list.")
    for i, person in enumerate(people):
        print(f"{i + 1}: {person['name']} | {person['age']} | {person['email']}")

def delete_people(people):
    if not people:
        print("No people to delete.")
        return
    display_people(people)
    
    while True:
        number = input('Enter a number to delete: ')
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print('Invalid range.')
            else:
                break
        except ValueError:
            print('Invalid input. Please enter a number.')

    people.pop(number - 1)
    print('Person deleted.')        

def search(people):
    try:
        search_name = input('Search for a name: ').lower()
        result = []
        
        for person in people:
            name = person['name']  # FIX: 'perosn' typo corrected
            if search_name in name.lower():
                result.append(person)

        if result:
            display_people(result)
        else:
            print("No matches found.")
    except Exception as e:
        print('Error occurred during search:', e)

# Start of the program
print('Welcome to your account management system!')
print()

people = [
    {'name': 'Rebecca', 'age': '19', 'email': 'rebeccamafitomamo@gmail.com'},
    {'name': 'Saron', 'age': '15', 'email': 'saronmafitomamo@gmail.com'},
    {'name': 'Nardos', 'age': '23', 'email': 'nardosmafitomamo@gmail.com'},
    {'name': 'Birtukan', 'age': '55', 'email': 'birtukanmafitomamo@gmail.com'},
]

while True:
    print('\nContact list size:', len(people))
    choice = input('Would you like to add, delete, search or quit? ').lower()

    if choice == 'add':
        person = add_person()
        people.append(person)
        print('You have added another person!')
    elif choice == 'delete':
        delete_people(people)
    elif choice == 'search':
        search(people)
    elif choice == 'quit':
        print("Exiting the system. Goodbye!")
        break 
    else:
        print('Invalid input choice.')
