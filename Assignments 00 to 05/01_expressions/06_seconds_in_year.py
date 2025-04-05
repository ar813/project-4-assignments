DAYS_IN_A_YEAR = 365
HOURS_IN_A_DAY = 24
MINUTES_IN_AN_HOUR = 60
SECONDS_PER_MINUTE = 60

def main():
    SECONDS_IN_A_YEAR = DAYS_IN_A_YEAR * HOURS_IN_A_DAY * MINUTES_IN_AN_HOUR * SECONDS_PER_MINUTE
    print(f"There are {SECONDS_IN_A_YEAR} seconds in a year!")

if __name__ == '__main__':
    main()