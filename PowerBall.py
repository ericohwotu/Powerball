# Employee power ball project
# coded by Eric Ohwotu
import random

def run():
    #define initial vairables
    employees = [] #list to hold all employees that would be playing
    pool = [] #list to hold all numbers guessed
    finished = False #boolean to quit powerball

    # main menu for interactions
    while not finished:
        print('Welcome to the powerball project')
        print('There are currently', len(employees), 'employee(s) playing')
        print('1) To add a new employee type in 1')
        print('2) To view all employees type in 2')
        print('3) To run the powerball type in 3')
        print('4) To Exit type in 4')
        print('please input your choice: ', end='')
        choice  = input() # handle choice input

        #ensure a number is put in
        if not choice.isdigit():
            continue
        else:
            choice = int(choice)
        
        if choice ==1:
            employee, numbers = add_employee() # display the prompts to get employee information
            employees.append(employee) # add new employee to employees list
            pool.append(numbers) # add the preferred numbers to the global pool
            
        elif choice == 2:
            display_employees(employees)

        elif choice == 3:
            display_employees(employees)
            run_powerball(pool)

        elif choice == 4:
            finished = True

    
        
def add_employee():
    # function to add new employees and there powerball numbers
    states=['1st','2nd','3rd','4th','5th']
    numbers=[];
    exception = ''
    cur = 1
    pcur = 1

    # Get the employee's name
    print()
    print('Enter your first name: ', end='')
    first_name = input()
    print('Enter your last name: ', end='')
    last_name = input()
    
    while cur<=5:
        print('Enter ', states[cur-1],' # (1 thru 69', exception, '): ',sep='', end='')
        x = input()

        #ensure a number is put in
        if not x.isdigit():
            continue
        else:
            x = int(x)
        
        # ensure the number is in the range and no duplicates
        if (x>69 or x<1) or x in numbers:
            continue
        
        # if no error add it to the array of numbers
        numbers.append(x)

        # add the exclusion text prompt for user
        exception = ' excluding'
        
        for n in numbers:
            exception += ' ' + str(n) + ','

        exception = exception[0:-1] # strip the last ',' from the string
        li = exception.rsplit(',',1) # split from the last ',' to replace with 'and'
        
        if len(li)>1:
            exception = li[0] + ' and ' + li[1]
        cur += 1

        
    while pcur==1:
        print('Enter Power ball (1 thru 26): ', end='')
        x = input()

        #ensure a number is put in
        if not x.isdigit():
            continue
        else:
            x = int(x)
            
        # ensure number is in range
        if (x>26 or x<1):
            continue
        
        powerball = x
        numbers.append(powerball)
        pcur += 1

    # creat the employee dictionary object
    employee = {'firstname':first_name,
                'lastname':last_name,
                '1stnumber':numbers[0],
                '2ndnumber':numbers[1],
                '3rdnumber':numbers[2],
                '4thnumber':numbers[3],
                '5thnumber':numbers[4],
                'powerball':powerball}
    
    return (employee, numbers)


def display_employees(employees):
    # print all the employees that are participating in the power ball
    print()
    for e in employees:
        print(e['firstname'],e['lastname'],e['1stnumber'],e['2ndnumber'],e['3rdnumber'],
              e['4thnumber'],e['5thnumber'],'Powerball:', e['powerball'])

def run_powerball(pool):
    #function to run the powerball and display winning numbers
    max_range = [69,69,69,69,69,26] #max range to correspond with the numbers last is powerball
    
    favourites = [[row[i] for row in pool]for i in range(len(pool[0]))] # variable to hold the favourites for each selection
    
    unique_favourite = set() #create set to hold the unique favourite numbers

    winning_numbers = [0,0,0,0,0,0] # variable to hold the winning powerball numbers

    # for each powerball guess number get the max value
    for i in range(0,len(favourites)):
        for n in favourites[i]:
            unique_favourite.add(n)
            
        prev_x = 0

        # assign winning numbers
        for n in unique_favourite:
            x = favourites[i].count(n) # count the unique numbers

            # decide the winning numbers:
            # if this is the max experienced
            if x > prev_x:
                if not n in winning_numbers and i < 5:
                    winning_numbers[i] = n
                else:
                    winning_numbers[i] = n
                    
                prev_x = x

            # if there are multiple max numbers
            elif x == prev_x:
                if random.randint(1,2) == 2 and (not n in winning_numbers) and i < 5:
                    winning_numbers[i] = n
                elif random.randint(1,2) == 2:
                    winning_numbers[i] = n

                prev_x = x
                
        # in the case that no unique numbers satisfied the criteria then come up with random winner
        if winning_numbers[i] == 0 or (winning_numbers[i] in winning_numbers[:i]) and i < 5:
            
            winner_found = False
            while not winner_found:
                rnd = random.randint(1,69)
                if rnd in winning_numbers:
                    continue
                else:
                    winning_numbers[i] = rnd
                    winner_found = True

    #add all values to the powerball dictionary
    powerball = {'1stnumber':winning_numbers[0],
                 '2ndnumber':winning_numbers[1],
                 '3rdnumber':winning_numbers[2],
                 '4thnumber':winning_numbers[3],
                 '5thnumber':winning_numbers[4],
                 'powerball':winning_numbers[5]}
    
    #print winning numbers
    print()
    print('The Winning Power Ball numbers are: ')
    print()        
    print(powerball['1stnumber'],powerball['2ndnumber'],powerball['3rdnumber'],
              powerball['4thnumber'],powerball['5thnumber'], 'Power Ball:', powerball['powerball'])
    print()

if __name__ == "__main__":
    run()
