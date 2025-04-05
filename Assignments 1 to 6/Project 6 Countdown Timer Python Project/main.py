import time

def countdown_timer():
    total_seconds = int(input("Enter the countdown time in seconds: "))

    while total_seconds > 0:
        
        minutes, seconds = divmod(total_seconds, 60) # (minutes:seconds)

        time_format = '{:02d}:{:02d}'.format(minutes, seconds) # {:02d} --> at least 2 digits

        print(time_format, end='\r') # end='\r' --> After printing, go back to the beginning of the same line instead of a new line.
        
        time.sleep(1)
        total_seconds -= 1

    print("Time's up!")

countdown_timer()








"""

                        Explaination

minutes, seconds = divmod(total_seconds, 60)

if total_seconds = 120

minutes, seconds = divmod(120, 60) ----> 120 / 60 = 2

60 fits into 120 exactly 2 times
And their is no reminder left 

so,
minute = 2 = value
second = 0 = reminder


minutes, seconds = 02:00

"""