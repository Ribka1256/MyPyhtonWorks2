import json  

def add_person() :
    name = input('name : ') 
    age = input ('age : ')
    email = input ('email :')
    
    person = {'name' : name ,'age': age ,'email': email}
    return person
 
def display_people(people) :
    if not people:
        print("No people in the list.")
    for i, person in enumerate(people) :
        print(f"{i + 1}: {person['name']} | {person['age']} | {person['email']}")

def delete_people(people) :
    if not people:
        print("No people to delete.")
        return
    display_people(people)
    
    while True :
        number = input('enter a number to delete')
        try :
            number = int (number)
            if number <= 0 or number > len(people):
                print ('invalid range ')
            else :
                break
        except :
            print ('invalid input')
    people.pop(number - 1 )
    print('person delete')        
        
def search(people) :
    try :
        name = input ('search for aname : ').lower()
        result = []
        
        for person in people :
            name = person['name']
            if search_name in name.lower():
                result.append(person)
        if result:
            display_people(result)
        else:
            print("No matches found.")
    except :
        print('Not found on the search')
        
print ('wellcome to your account management system ! ')
print()

with open('contact.json', 'r') as f :
    people = json.load(f)['contact']


while True :
    print()
    prthing= int('contact list size : ',len (people))
 
    choice= input ('would you like to add, delete, search or quit : ').lower()
  
    if choice == 'add' :
      person = add_person()
      people.append(person)
      print ('you have added another person !')
    elif choice == 'delete' :
      delete_people(people)
    elif choice == 'search' :
      search(people)
    elif choice == 'quit':
        print("Exiting the system. Goodbye!")
        break 
    else :
        print ('invalid input choice')
with open('contact.json', 'w') as f :
    json.dump( {'contact' : people}, f)
      
    
