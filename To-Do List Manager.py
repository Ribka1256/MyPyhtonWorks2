print('-----------To-Do List Manager-------------')
def add(tasks):
    task_num = int(input('How many tasks would like to add: '))
    for _ in range(task_num):
        task = input('Enter the list you want to add: ')
        tasks.append(task)
    print('Added sucessfully!')
tasks = [
    " working on my project",
    " learning some skils",
    " cooking dinner"
]

def view(tasks):
    print('-----------To-Do List-------------')
    for i, entry in enumerate(tasks, 1):
        print(f"{i}. {entry}")
        
def delete(tasks):
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"🗑️ Deleted: {removed}")
        else:
            print("❌ Invalid task number")
    except ValueError:
        print("❌ Please enter a valid number")


while True:
    print('1, ADD TO THE TO-DO LIST')
    print('2, VIEW THE TO-DO LIST')
    print('3, DELETE  FROM THE TO-DO LIST')
    print('4, QUIT')
    choice = int(input('Enter you choice: '))
    if choice == 1:
        add(tasks)
    elif choice == 2:
        view(tasks)
    elif choice == 3:
        delete(tasks)
    elif choice == 4:
        break
    else:
        print('Not valid')