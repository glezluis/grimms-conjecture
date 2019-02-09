from grimm import *
def main():
    allsets = {}
    menuval = ''

    while menuval is not 'q':
        menu()
        menuval = input('enter a choice: ')
        if menuval is 'f':
            a,b = input_range()
            allsets = consecutive_composites((a,b))
            print('%d consecutive composite sets found between [%d, %d]' % (len(allsets),  a, b))
        elif menuval is 'p':
            if not allsets: 
                print_comps(consecutive_composites(input_range()))
            else:
                print_comps(allsets)
        elif menuval is not 'q':
            print('enter valid input')

if __name__ == '__main__':
    main()