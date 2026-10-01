



total_units = 0
current_total = 0
failed_attempts = 0
file = "inventory.txt"

def load_inventory(file):
    
    with open(file, 'a+') as f:  
        f.seek(0)             
        if f.read() == '': 
            return [0]
        else:
            f.seek(0)
            inventory = [int(line) for line in f.readlines() if line.strip().isdigit()]
            return inventory
        
def save_inventory(file, inventory):
    current_total = sum(inventory)
    with open(file, 'w') as f:
        f.writelines([str(item) + "\n" for item in inventory])
        f.write("\nTotal Inventory: " + str(current_total) + "\n")
        
def get_valid_input():
        stock = input("Please enter a stock quantity (or type 'quit' to exit): ").strip()
        if stock.isdigit():
            return int(stock[0])
        elif stock == "quit":
            return stock
        else:
            print("error")
            return None
        
def process_delivery(current_total, new_value):
    current_total.append(new_value)
    return current_total
    
def calculate_tax(amount):
    tax = amount*0.1 
    return tax

def generate_report(total_units, failed_attempts):
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)
    

current_list = load_inventory(file)
while (True): 
    
    stock = get_valid_input()

    if stock == None:
        failed_attempts += 1
        continue
    
    if stock == "quit":
            generate_report(total_units, failed_attempts)
            save_inventory(file, current_list)
            break
        
    else: 
        total_units += 1
        current_list = process_delivery(current_list, stock)
        current_total = sum(current_list)
        print("Tax Amount:", calculate_tax(stock))
        print ("Total Inventory:", current_total)
        if current_total > 500:
            print ("Alert! Inventory has overstocked.")
            save_inventory(file, current_list)
            break
        
            
        
        
        
        
        