import sys

people = []

def read_person():
    id = int(input('Enter Person Id: '))
    name = input('Enter Person name: ')
    age = int(input('Enter person age: '))
    location = input('Enter person location: ')
    person = {id: id, name: name, age: age, location : location}
    return person

def create():
    person = read_person()
    people.append(person)
    print(f'Employee with Id= {person[id]} added successfully')

def readById(id = 10):
    if len(people) == 0:
        print('No person details available')
        return
    for person in people:
        if person[id] == id:
            print(person)
            return
    print(f'Person with Id = {id} not found')

def update(location = 'mandya', id = 101):
    if len(people) == 0:
        print('No person details available')
        return
    for person in people:
        if person[id] == id:
            person[location] = location
            print(f'Employee with Id = {id} updated')
            return
    print(f'Person with Id = {id} not found')

def delete():
    if len(people) == 0:
        print('No person details available')
        return
    for person in people:
        i = 0
        if person[id] == id:
            del people[i]
            print(f'Employee with Id = {id} updated')
            return
        i += 1
    print(f'Person with Id = {id} not found')

def readAll():
    if len(people) == 0:
        print('No person details available')
        return
    for person in people:
        print(person)

def menu(choice):
    match choice:
        case 1 : create()
        case 2 : readById(id=10)
        case 3 : update()
        case 4 : delete()
        case 5 : readAll()
        case 6 : sys.exit('End of Program')
        case _ : print('Invaid choice eneterd')

def start_app():
    while True:
        print('1:Create 2:Read-by-Id 3:Update 4:Delete 5:Read-All 6:Exit')
        choice = int(input('Enter your choice: '))
        menu(choice)

start_app()
