booklist = [
    {
        'book': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'pages': 400
    },
    {
        'book': '1984',
        'author': 'George Orwell',
        'pages': 328
    },
    {
        'book': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'pages': 279
    },
    {
        'book': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'pages': 180
    },
    {
        'book': 'Moby-Dick',
        'author': 'Herman Melville',
        'pages': 635
    }
]
try:
    infile = open('theBookList.txt', 'r')
    line = infile.readline()
    while line:
        try:
            book, author, pages = line.rstrip('\n').split(',')
            booklist.append({
                'book': book,
                'author': author,
                'pages': int(pages)
            })
            line = infile.readline()
        except:
            print('⚠️ Skipping a malformed line in the file.')
    infile.close()
except FileNotFoundError:
    print('📂 <theBookList.txt> not found — starting with default book list.')
    booklist = []
    
    
def addBook():
    print('you are adding a book')
    book = input('Enter the name of the you would like to insert : ')
    author = input('enter the author of the the book you would like to insert : ')
    pages = int(input('Enter the number of the page : '))
     
    new_book = {
        'book': book,
        'author': author,
        'pages': pages
    }
    booklist.append(new_book)
    print('✅ Book added successfully!')
    

def Lookup():
    print('you are lookingup a book ')
    searchName = input('Enter search key : ').lower()
    found = False
    
    for book in booklist:
        if searchName in book['book'].lower() or searchName in book['author'].lower():
            print(f"📚 {book['book']} by {book['author']} ({book['pages']} pages)")
            found = True
    
    if not found:
        print('❌ Not found in the search engine.')
            
def display():
    print('display book')
    for i,book in enumerate(booklist, 1):
        print(f"{i}. {book['book']} by {book['author']} ({book['pages']} pages)")

print('wellcome to book management list !')
print ('number of books : ', len(booklist))
while True :
    try :
        print('----BOOKMANAGER-----')
        print('1, Add a book')
        print('2, Lookup a book')
        print('3, Display a book')
        print('4, Quit')
        choice = int(input('Enter your choice : '))
    except :
        print('invalid choice try again')
        continue
    if choice == 1:
        addBook()
    elif choice == 2:
        Lookup()
    elif choice == 3:
        display()
    elif choice == 4:
        print('💾 Saving to file...')
        try:
            outfile = open('theBookList.txt', 'w')
            for book in booklist:
                outfile.write(','.join([book['book'], book['author'], str(book['pages'])]) + '\n')
            outfile.close()
            print('✅ File saved. Exiting the program. Goodbye!')
            break
        except:
            print('❌ Error saving to file.')
            break
    else:
        print('❌ Invalid choice. Try again.')

    
    

        
       
        
        
        
          
        
      
    
    

