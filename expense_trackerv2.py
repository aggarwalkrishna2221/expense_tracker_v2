def computePay():
    aboveAverage = []
    belowAverage = []
    average = 0 
    lowest = None
    highest = None
    expenses=[]
    total = 0
    days = 0
    abavg = 0
    bavg = 0

    while True:
        inp = input("Enter your expenses:- ")
        if inp == "done":
            break
        try:
            float_inp = float(inp)
            if float_inp<0:
                print("Expense cannot be negative. ")
            expenses.append(float_inp)
        except:
            print("Enter a valid number. Pls try again")

        days = days + 1
        total = total + float_inp
        
        for i in expenses:
            if highest is None:
                highest = i
            elif highest < i:
                highest = i
            
            if lowest is None:
                lowest = i
            elif lowest > i:
                lowest = i
            
            
            
        average = total/days

        for expense in expenses:
            if expense > average:
                abavg += 1
            elif average > expense:
                bavg =+ 1
        
       
        
        
        
        

    print("---Detailed Summary----")
    print("Expenses: ", expenses)
    print("Days recorded: ", days)
    print("Total: ", total)
    print("Average: ", average)
    print("Highest: ", highest)
    print("Lowest", lowest)
    print("Days above average: ", abavg)
    print("Days below average: ", bavg)
        

computePay()