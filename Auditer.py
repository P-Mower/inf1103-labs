
fail = 0 
total = 0


while (True): 
    stock= (input("Please enter a stock quantity : "))
    
    if stock.isdigit():
        total += int(stock)
        if total > 500 :
            print (" Alert! Inventory has overstocked. ")
            break

    elif stock =="quit":
        print("Total Units Processed:" , total )
        print("Number of Failed/Rejected Entries:", fail)
        break
        
    else: 
        fail += 1
        print("error")
            
        
        
        
        
        