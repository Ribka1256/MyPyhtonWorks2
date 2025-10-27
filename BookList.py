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

# Load from file if exists
try:
    with open('theBookList.txt', 'r') as infile:
        for line in infile:
            parts = line.rstrip('\n').split(',')
            if len(parts) == 3:
                book, author, pages = parts
                new_book = {
                    'book': book,
                    'author': author,
                    'pages': int(pages)
                }
                booklist.append(new_book)
except FileNotFoundError:
    print('📂 <theBookList.txt> not found. Starting with default book list.')
    
def addBook():
    print('\n📘 You are adding a book...')
    book = input('Enter the name of the book: ')
    author = input('Enter the author of the book: ')
    pages = int(input('Enter the number of pages: '))
    
    new_book = {
        'book': book,
        'author': author,
        'pages': pages
    }
    booklist.append(new_book)
    print('✅ Book added successfully!')

def Lookup():
    print('\n🔎 Looking up a book...')
    searchName = input('Enter search keyword: ').lower()
    found = False
    
    for book in booklist:
        if searchName in book['book'].lower() or searchName in book['author'].lower():
            print(f"📚 {book['book']} by {book['author']} ({book['pages']} pages)")
            found = True
    
    if not found:
        print('❌ Not found in the search engine.')

def display():
    print('\n📖 Book list:')
    for i, book in enumerate(booklist, 1):
        print(f"{i}. {book['book']} by {book['author']} ({book['pages']} pages)")

print('\n📚 Welcome to the Book Management List!')
print('📦 Number of books:', len(booklist))

while True:
    try:
        print('\n---- BOOK MANAGER ----')
        print('1. Add a book')
        print('2. Lookup a book')
        print('3. Display all books')
        print('4. Quit')
        choice = int(input('Enter your choice: '))
    except ValueError:
        print('❌ Invalid input. Please enter a number.')
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
            with open('theBookList.txt', 'w') as outfile:
                for book in booklist:
                    outfile.write(f"{book['book']},{book['author']},{book['pages']}\n")
            print('✅ File saved. Exiting the program. Goodbye!')
        except:
            print('❌ Error saving file.')
        break
    else:
        print('❌ Invalid choice. Try again.')

