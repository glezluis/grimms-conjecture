from grimm import *

def main():
    menuval = ''

    while menuval != 'q':
        menu()
        menuval = input('enter a choice: ').lower()

        if menuval == 'f':
            a,b = input_range()
            allsets = consecutive_composites((a,b))

            if allsets:
                print('%d consecutive composite sets found between [%d, %d]' % (len(allsets),  a, b))
            else:
                print('no consecutive composite sets found')

        elif menuval == 'p':
            if not allsets: 
                print_comps(consecutive_composites(input_range()))
            else:
                print_comps(allsets)

        elif menuval != 'q':
            print('\n*** enter valid input ***')

if __name__ == '__main__':
    main()