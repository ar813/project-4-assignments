MAX_TERM_VALUE : int = 10000

def main():
    a = 0
    b = 1
    print(a, b, end=" ")
    
    while True:
        next_num = a + b 
        
        if next_num >= MAX_TERM_VALUE:
            break  
        
        print(next_num, end=" ")  
        a, b = b, next_num  
            
if __name__ == '__main__':
    main()