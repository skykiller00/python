Food_list = {
    'pizza': ['cheese', 'onion', 'green_papper', 'mushroom'],
    'hamburger': ['beef', 'pork', 'chicken', 'lettuce', 'tomato', 'cheese', 'onion', 'cucumber'],
    'pasta': ['fish', 'beef', 'onion', 'basil', 'meatball', 'black_papper'],
    'fried_chicken': ['leg', 'wings', 'breast', 'chili', 'papper'],
    'ice_cream': ['vanilla', 'Chocolate', 'strawbarry', 'banana'],
    'french_fries': ['small_portion', 'medium', 'large_portion'],
    'cake': ['cream', 'chocolate', 'mango', 'toon'],
    'drinks': ['cola', 'sprite', 'coffee', 'milkshake']
    }
# print menu
for key in Food_list.keys():
    print(key.title())
choice = input('Please choose you favorite food:\n')

Food_select = {
    'pizza': [],
    'hamburger': [],
    'pasta': [],
    'fried_chicken': [],
    'ice_cream': [],
    'french_fries': [],
    'cake': [],
    'drinks': []
    }
Drop_out = True
# Enter a list according to the user
while Drop_out:
    if choice.isalpha():
        if choice == 'q':
            for key in list(Food_select.keys()):
                if not Food_select.get(key):
                    del Food_select[key]
            print(Food_select)
            Drop_out = False
            break
        elif choice == 'b':
            print('You have returned to the top')
        else:
            # choice = choice.title()
            print(Food_list[choice])
            choice2 = input(
                'Please choose the ingredients you like:\nDrop out:q\nReturn to superior:b\n')
            if choice2.isalpha():
                if choice2 == "q":
                    for key in list(Food_select.keys()):
                        if not Food_select.get(key):
                            del Food_select[key]
                    print(Food_select)
                    Drop_out = False
                    break
                elif choice2 == "b":
                    for key in Food_list.keys():
                        print(key)
                    choice = input('Please choose you favorite food:\n')
                else:
                    while choice2 in Food_list[choice]:
                        Food_select[choice].append(choice2)
                        print(Food_select[choice])
                                                
                        if choice2 not in Food_list[choice]:
                            print('Please select according to the ingredient list!')
                        break
            else:
                print('Please follow the menu order!')

    else:
        print('Please follow the menu order!')
