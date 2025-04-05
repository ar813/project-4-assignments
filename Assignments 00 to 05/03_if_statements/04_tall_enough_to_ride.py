MINIMUM_HEIGHT: int = 50

def main():
    while True:
        tall = int(input("How tall are you? "))
        
        if tall >= MINIMUM_HEIGHT:
            print("You're tall enough to ride!")
            break 
        else:
            print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()
