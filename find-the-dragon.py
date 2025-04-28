def game():
    print('            _.===._      ,"^^^^",')
    print('           /_\\^^^/_\\    /  ^ ,^  \\     ,')
    print('           (0\\ ^ /0)\\  / ^  /  ^  \\    /\'')
    print('            \\     /  ^^   ^ \\ ^ \\  ",." /')
    print('             )   (  ^  ^   ^ \\   \\    ,\'')
    print('             (o_o)^    \\ ^   ,)  /`^^`')
    print('              ^V^\\ ^ \\  \\_,-"((((')
    print('              /  /`""/  /')
    print('             (((`   \'(((')
    print('\n\n')
    print('Welcome to Find the Dragon!')
    print("Your mission is to find the dragon.\nYou're at a cross road. Where do you want to go?")
    print(' Type "left" or "right"')
    direction = input('')
    if direction.lower() == 'left':
        print("Swim or Wait?")
        boat = input('')
        if boat.lower() == 'wait':
            print("Which door?")
            print('RED - Green - Blue')
            door = input('')
            if door.lower() == 'green':

                print('               -,,,__')
                print('                \    ``~~--,,__                /   /')
                print('                /              ``~~--,,_     //--//')
                print('     _,,,,-----,\              ,,,,---- >   (c  c)\\')
                print(' ,;''            `\,,,,----\'\'\'\'   ,,-\'\'\'---/   /_ ;___        -,_')
                print('( ''---,;====;,----/             (-,,_____/  /\'/ `;   \'\'\'\'\'----\ `:.')
                print('\'                 \'               `      (oo)/   ;~~~~~~~~~~~~~/--~')
                print(' `;_           ;    \            ;   \   `  \' ,,\'')
                print('    ```-----...|     )___________|    )-----\'\'\'')
                print("                \   /             \   \\")
                print("                /  /,              `\   \\")
                print("              ,'---\ \              ,---`,;,")
                print("                    ```")
                print('\n\n\n')
                print("You Win!")
                print("Your finded the Dragon 🐲!")
            elif door.lower() == 'red':
                print('Burned by fire. Game Over.')
            elif door.lower() == 'blue':
                print("Eaten by beasts. Game Over.")
            else:
                print("The Option is not finded!")
                print(game())



        elif boat.lower() == 'swim':
            print("Attacked by trout. Game Over.")
        else:
            print("The option is not finded!")
            print(game())
    elif direction.lower() == 'right':
        print("Sorry! Fall into a hole. Game Over.")
    else:
        print("The option is not finded!")
        print(game())

print(game())