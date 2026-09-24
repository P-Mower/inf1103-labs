

total_units = 0
current_total = 0
failed_attempts = 0


def get_valid_input():
        stock = input("Please enter a stock quantity (or type 'quit' to exit): ")
        if stock.isdigit():
            return int(stock)
        elif stock == "quit":
            return stock
        else:
            print("error")
            return None
        
def process_delivery(current_total, new_value):
    current_total = current_total + new_value
    return current_total
    
def calculate_tax(amount):
    tax = amount*0.1 
    return tax

def generate_report(total_units, failed_attempts):
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)
    
while (True): 
    stock = get_valid_input()

    if stock == None:
        failed_attempts += 1
        continue
    
    if stock == "quit":
            generate_report(total_units, failed_attempts)
            break
        
    else: 
        total_units += 1
        current_total = process_delivery(current_total, stock)
        print("Tax Amount:", calculate_tax(stock))
        print ("Total Inventory:", current_total)
        if current_total > 500:
            print ("Alert! Inventory has overstocked.")
            break
        
            
        
        
        
        
        