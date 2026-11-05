import sys

def create():
    print('Employee added successfully')

def readById(id=10):
    print(f'Employee with Id={id} name is Nithin')

def update():
    print('Employee updated')

def delete():
    print()

def readAll():
    print()

def menu(choice):
    match choice:
        case 1 : create()
        case 2 : readById(id=10)
        case 3 : update()
        case 4 : delete()
        case 5 : readAll()
        case 6 : sys.exit('End of Program')
        case _ : print('Inva;id choice eneterd')


def start_app():
    while True:
        print('1:Create 2:Read-by-Id 3:Update 4:Delete 5:Read-All 6:Exit')
        choice = int(input('Enter your choice'))
        menu(choice)

start_app()

