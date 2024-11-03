age = int(input('Type ypur age : '))

match age:
    case 1:
        print('child')
    case 10:
        print('child')
    case 100:
        print('unreal val')
    case -1:
        print("don't be a liar")
    case _:
        print('no special cases :)')