print('Welcome to our Restaurant \'The Taste\'')
while True:
    food_type = int(input('1:Veg 2:NonVeg \t Your choice please: '))
    match food_type:
        case 1 :
            print('1:Mylari-Dosa 2:Mushroom-Biryani 3:Chana-Battura')
            choice = int(input('Your choice please: '))
            match choice:
                case 1 : print('Here is your Yummy Yummy Dosa Maam')
                case 2 : print('Here is your Spicy Biryani Sir')
                case 3 : print('Here India\'s biggest Poori Sir')
                case _ : print('Sorry Maam, did you order Grass???')
        case 2 :
            print('1:ChickenCurry 2:FishFry 3:MuttonPulav')
            choice = int(input('Your choice please: '))
            match choice:
                case 1 : print('Here is your Yummy Yummy Chicken Maam')
                case 2 : print('Here is your Spicy Fish Fry Sir')
                case 3 : print('Here India\'s hot selling Hanumantu Biryani!')
                case _ : print('Sorry Maam, did you order Cockroaches???')
        case _ : print('Guru, idu restaurant, Garden alla!')
    choice = input('Would like to have more: (Yes/No)')
    if choice.lower() not in ('yes', 'y'):
    # if choice.lower() == 'yes' or choice.lower() == 'y':
        break # breaks the while loop
print('Thank you Visit again!!')
