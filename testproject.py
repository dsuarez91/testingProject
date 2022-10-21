import pickle
import random

# Menu constants
GENERAL_INVENTORY = '1'
GENERAL_ACCOUNTS = '2'
ORDERS_MENU = '3'
REPORTS_MENU = '4'

CLOSE_OUT = 'exit'


# CSV and Data
INVENTORY_DATA_FILE = 'inventory.dat'
ACCOUNTS_DATA_FILE = 'account.dat'
ORDERS_DATA_FILE = 'orders.dat'
ORDERS_CSV = 'Orders.csv'
INVENTORY_CSV = 'Inventory.csv'
ACCOUNTS_CSV = 'Accounts.csv'

# Delimeter
DELIMETER = ','

def main():
    
    # Load inventory
    item_inventory = load_inventory()
    # Load accounts
    account_data = load_accounts()
    # Load orders
    orders = load_orders()
    
    # Condition for menu option to run program
    option = True
    while option:
        general_menu()
        options = input('\nMenu choice: ')
        if(options == GENERAL_INVENTORY):
            inventory_menu(item_inventory)
        elif(options == GENERAL_ACCOUNTS):
            account_menu(account_data)
        elif(options == ORDERS_MENU):
            order_menu(orders, item_inventory, account_data)
        elif(options == REPORTS_MENU):
            reports_menu(orders, item_inventory, account_data)
        elif(options == CLOSE_OUT):
            option = False
            save_inv(item_inventory)
            save_acc(account_data)
            save_orders(orders)
                  
def general_menu():
    print('\nGeneral Menu')
    print('1: Inventory')
    print('2: Accounts')
    print('3: Orders')
    print('4: Reports')
    print('Exit to save and close out the program')
    
def inventory_menu(item_inventory):

    add_inventory = '1'
    search_inventory = '2'
    modidy_inventory = '3'
    delete_inventory = '4'
    previous_menu = 'exit'
    
    
    print('\nInventory Menu')
    print('1: Add To Inventory')
    print('2: Search Inventory')
    print('3: Modify Inventory')
    print('4: Delete From Inventory')
    print('Exit to return to the previous menu')

    option = True
    while option:        
        options = input('\nMenu choice: ')
        if(options == add_inventory):
            add_inv(item_inventory)
        elif(options == search_inventory):
            search_inv(item_inventory)
        elif(options == modidy_inventory):
            modify_inv(item_inventory)
        elif(options == delete_inventory):
            del_inv(item_inventory)
        elif(options == previous_menu):
            option = False
            main()

def account_menu(account_data): 
    add_account = '1'
    search_account = '2'
    modify_account = '3'
    delete_account = '4'
    previous_menu = 'exit'
    
    print('Account Menu')  
    print('1: Add Account')
    print('2: Search Account')
    print('3: Modify Account')
    print('4: Delete Account')
    print('Exit to return to the previous menu')
    
    option = True
    while option:
        options = input('\nMenu choice: ')
    # Account flow
        if(options == add_account):
            add_acc(account_data)
        elif(options == search_account):
            search_acc(account_data)
        elif(options == modify_account):
            modify_acc(account_data)
        elif(options == delete_account):
            del_acc(account_data)
        elif(options == previous_menu):
            general_menu()

def order_menu(orders, item_inventory, account_data):
    
    create_order = '1'
    search_order = '2'
    modify_order = '3'
    delete_order = '4'
    previous_menu = 'exit'
    
    print('Order Menu')
    print('1: Create Order')
    print('2: Search Order')
    print('3: Modify Order')
    print('4: Cancel Order')
    print('Exit to return to the previous menu')
    
    option = True
    while option:
        options = input('\nMenu choice: ')
        # Order flow
        if(options == create_order):
            create_order(orders, account_data, item_inventory)
        elif(options == search_order):
            search_order(orders)
        elif(options == modify_order):
            modify_order(orders)
        elif(options == delete_order):
            cancel_order(orders)
        elif(options == previous_menu):
            option = False
            main()

def reports_menu(orders, item_inventory, account_data):
    
    import_inventory_csv = '1'
    export_inventory_csv = '2'
    import_account_csv = '3'
    export_account_csv = '4'
    import_orders_csv = '5'
    export_orders_csv = '6'
    previous_menu = 'exit'
    
    print('Reports Menu') 
    print('1: Import Inventory')
    print('2: Export Inventory')
    print('3: Import Accounts')
    print('4: Export Accounts')
    print('5: Import Orders')
    print('6: Export Orders')
    print('Exit to return to the previous menu')
    
    option = True
    while option:
        options = input('\nMenu choice: ')
            # Reports flow
        if(options == import_inventory_csv):
            import_inv_csv(item_inventory)
        elif(options == export_inventory_csv):
            export_inv_csv(item_inventory)
        elif(options == import_account_csv):
            import_acc_csv(account_data)
        elif(options == export_account_csv):
            export_acc_csv(account_data)
        elif(options == import_orders_csv):
            import_orders(orders)
        elif(options == export_orders_csv):
            export_orders(orders)
        elif(options == previous_menu):
            option = False
            main()
    
def load_orders():
    # load orders file from dat
    try:
        # Open file
        with open(ORDERS_DATA_FILE, 'rb') as load_order:
            
            # Unpickle
            order_dict = pickle.load(load_order)
    
    # Exception when the file can't open
    except:
        # Display error
        print('Error loading orders, a new file will be generated.')
        # Empty dict
        order_dict = {}
    
    return order_dict

def load_inventory():
    # Load inventory file from dat
    try:
        # Open file
        with open(INVENTORY_DATA_FILE, 'rb') as load_inv:
            
            # Unpickle
            inv_dict = pickle.load(load_inv)
    
    # Exception when the file can't open
    except:
        # Display load error
        print('Error loading inventory, a new file will be generated.')
        # Empty dictionary
        inv_dict = {}
    
    return inv_dict
    
def load_accounts():
    # Load accounts file from dat
    try:
        # Open
        with open(ACCOUNTS_DATA_FILE, 'rb') as load_accs:
            
            # Unpickle
            acc_dict = pickle.load(load_accs)
    
    # Exception for couldn't open
    except:
        # Display load error
        print('Error loading accounts, new file will be generated.')
        # Empty dictionary
        acc_dict = {}
    
    return acc_dict

def save_inv(item_inventory):
    # Serializing inventory data to dat with pickle
    try:
        with open(INVENTORY_DATA_FILE, 'wb') as save_inv:
            pickle.dump(item_inventory, save_inv)
    
    except:
        print('There was an error saving the inventory data.')
    
def save_acc(account_data):
    # Serializing account data to dat with pickle
    try:
        with open(ACCOUNTS_DATA_FILE, 'wb') as save_accs:
            pickle.dump(account_data, save_accs)
    
    except:
        print('There was an error saving the account data.')

def save_orders(orders):
    try:
        with open(ORDERS_DATA_FILE, 'wb') as save_order:
            pickle.dump(orders, save_order)
    
    except :
        print('There was an error saving the account data.')

def add_inv(item_inventory):
    # Input to add more items
    add_item = 'yes'
    
    # Add items to inventory
    while add_item == 'Yes' or add_item == 'yes' or add_item == 'Y' or add_item == 'y':
        print('Enter item information:')
        item_no = input('Item number: ')
        item_desc = input('Item description:')
        item_qty =  input('Item qty: ')
        item_price = input('Price: ')
        
        # Create inventory entry
        inventory = [item_no, item_desc, item_qty, item_price]
        
        # Use item number as the key
        item_inventory[item_no] = inventory
        
        # Asking to add another item
        add_item = input('Add another item? ')
        
        if add_item == 'N' or add_item == 'n' or add_item == 'No' or add_item == 'no':
            inventory_menu(item_inventory)
    
def search_inv(item_inventory):
    search_item = 'yes'
    # Search inventory by item number
    
    while search_item == 'Yes' or search_item == 'yes' or search_item == 'Y' or search_item == 'y':
        item_no = input('Enter item number to search inventory: ')
    
        if item_no in item_inventory:
            items = item_inventory[item_no]
            print(f'Item no: {items[0]}')
            print(f'Item description: {items[1]}')
            print(f'Item qty: {items[2]}')
            print(f'Price: ${items[3]}')
    
        if item_no not in item_inventory:
            item_desc = input('Enter items description: ')
        
            if item_desc in item_inventory:
                desc = item_inventory[item_desc]
                print(f'Item no: {desc[0]}')
                print(f'Item description: {desc[1]}')
                print(f'Item qty: {desc[2]}')
                print(f'Price: ${desc[3]}')
            
            else:
                print('Item number and/or descrition was not found.')
        
        search_item = input('Search for another item? ')    
                
        if search_item == 'No' or search_item == 'no' or search_item == 'N' or search_item == 'n':
            inventory_menu(item_inventory)
       
def modify_inv(item_inventory):
    modify_another = 'yes'
    
    # Modify the inventory
    while modify_another == 'Yes' or modify_another == 'yes' or modify_another == 'Y' or modify_another == 'y':
        
        item_mod = input('What is the item number to modify: ')

        for item in list(item_inventory):
            if item[0] == item_mod:
                new_qty = input('New QTY: ')
            
                item_inventory[2] = new_qty
            print('Item has been modified.')
        
        modify_another = input('Do you want to modify another item? ')
    
        if modify_another == 'No' or modify_another == 'no' or modify_another == 'N' or modify_another == 'n':
            inventory_menu(item_inventory)
        
def del_inv(item_inventory):
    delete_another = 'yes'
    
    while delete_another == 'Yes' or delete_another == 'yes' or delete_another == 'Y' or delete_another == 'y':
    # Delete item from inventory
        del_item = input('Enter Item number you want to delete: ')
    
        if del_item in item_inventory:
            del item_inventory[del_item]
            print('Item deleted')
    
        else:
            print('Item not found')
    
        delete_another = input('Do you want to delete another item? ')
    
        if delete_another == 'No' or delete_another == 'no' or delete_another == 'N' or delete_another == 'n':
            inventory_menu(item_inventory)
    
def add_acc(account_data):
    # Input to add another account
    add_acc = 'Yes' or 'yes' or 'Y' or 'y'
    
    # Add account to file
    while add_acc == True:
        print('Enter customers information:')
        first_name = input('Frist Name: ')
        Last_name = input('Last Name:')
        address =  input('Address: ')
        email = input('Email: ')
        credit_card = input('Enter credit card number: ')
        
        # Create account entry
        account = [first_name, Last_name, address, email, credit_card]
        
        # Use item number as the key
        account_data[email] = account
        
        # Asking to add another item
        add_acc = input('Add another item? ')
    
def search_acc(account_data):
    # Ask for customer email
    email = input('Enter customers email to look up account: ')
    
    if email in account_data:
        acc = account_data[email]
        print(f'First Name: {acc[0]}')
        print(f'Last Name: {acc[1]}')
        print(f'Address: {acc[2]}')
        print(f'Email: {acc[3]}')
        
    else:
        print('Account was not found')
    
def modify_acc(account_data):
    info == 'email' or 'credit card' or 'first name' or 'last name' or 'address'
    
    acc_search = input('Enter the email of the account you want to modify: ')
    
    if acc_search in account_data:
        info = input('What field needs to be modified? ')
        if info == 'first name':
            new_first = input('Enter new first name: ')
            acc_search[0] = new_first
        elif info == 'last name':
            new_last = input('Enter new last name: ')
            acc_search[1] = new_last
        elif info == 'address':
            new_address = input('Enter new address')
            acc_search[2] = new_address
        elif info == 'email':
            new_email = input('Enter new email: ')
            acc_search[3] = new_email
        elif info == 'credit card':
            new_cc = input('Enter new credit card info: ')
            acc_search[4] = new_cc
        print('Account has been modified.')
        
    else:
        print('Account does not exist.')
    
def del_acc(account_data):
    del_acc = input('Enter email of the account you want to delete: ')
    
    if del_acc in account_data:
        del account_data[del_acc]
        print('Account is deleted.')
    
    else:
        print('Account was not found.')
               
def create_order(orders, account_data, item_inventory):
    # Input to add another account
    create_order = 'Yes' or 'yes' or 'Y' or 'y'
    
    total_price = 0
    
    # Add account to file
    while create_order == True:
        
        acc_look_up = input('Enter account number to create order: ')
        
        if acc_look_up in account_data:
  
            print('Enter order information:')
        
            item_no = input('Item number: ')
            item_desc = input('Item description:')
            item_qty = input('Qty: ')
            
            if item_no in item_inventory:
                
                total_price += item_no[3] * item_qty
            
        order_number = random.randrange(1000000 , 9999999)
        
        # Create order entry
        order = [order_number, acc_look_up, item_no, item_desc, item_qty, total_price]
        
        # Use item number as the key
        orders[order_number] = order
        
        # Asking to add another item
        create_order = input('Create another order? ')
        
def search_order(orders):
    order_no = input('Enter the order number you want to look up: ')
    
    if order_no in orders:
        order = orders[order_no]
        print(f'Order Number: {order[0]}')
        print(f'Account Number: {order[1]}')
        print(f'Item Number: {order[2]}')
        print(f'Item Qty: {order[3]}')
        print(f'Item Description: {order[4]}')
        print(f'Total: ${order[5]}')
    
    else:
        print('Order was not found.')
    
def modify_order(orders, account_data, item_inventory):
    order_mod = input('Enter the order number you want to modify: ')
       
def cancel_order(orders):
    del_order = input('Enter order number to delete: ')
    
    if del_order in orders:
        del orders[del_order]
        print('Order has been cancelled and deleted.')
    
    else:
        print('Order was not found.')
    
def import_inv_csv(item_inventory):
    # Export inventory CSV file and add to dict
    try:
        with open(INVENTORY_CSV) as import_csv:
            slot = import_csv.readlines()
            
        # Loop to read each slot in the csv file to add to dict
        for items in slot:
            item_inv = items.rstrip('\n').split((DELIMETER))
            
            item_inventory[item_inv[0]] = item_inv
    
    except:
        print('There was an error importing the inventory CSV.')
    
def export_inv_csv(item_inventory):
    # Export inventory CSV file
    try:
        with open(INVENTORY_CSV, 'w') as inv_csv:
            for item in item_inventory.values():
                
                # Join items with delimeter
                slot = DELIMETER.join(item)
                
                inv_csv.write(slot + '\n')
        print(f'CSV file has been generated.')
    except:
        print('An error has a occured generating the inventory CSV file.')
    
def import_acc_csv(account_data):
    # Import accounts CSV file and add to dict
    try:
        with open(ACCOUNTS_CSV) as import_accs:
            slot = import_accs.readlines()
            
        # Loop to read each account in the csv file to add to dict
        for accs in slot:
            acc_info = accs.rstrip('\n').split((DELIMETER))
            
            account_data[acc_info[0]] = acc_info
    except:
        print('There was an error importing the accounts CSV.')
    
def export_acc_csv(account_data):
    # Export account CSV file
    try:
        with open(ACCOUNTS_CSV, 'w') as accs_csv:
            for acc in account_data.values():
                
                # Join items with delimeter
                info = DELIMETER.join(acc)
                
                accs_csv.write(info + '\n')
        print('CSV file has been generated.')
    except:
        print('An error has a occured generating the accounts CSV file.')
        
def import_orders(orders):
    
    try:
        with open(ORDERS_CSV) as order_csv:
            csv = order_csv.readlines()
            
        for order in csv:
            order_info = order.rstrip('\n').split((DELIMETER))
        
            orders[order_info[0]] = order
    except:
        print('There was an error importing the orders csv.')

def export_orders(orders):
    
    try:
        with open(ORDERS_CSV, 'w') as orders_csv:
            for order in orders.values():
                
                info = DELIMETER.join(order)
                
                orders_csv.write(info + '\n')
        print('CSV file has been generated.')
    except:
        print('An error has a occured generating the accounts CSV file.')
       
if __name__ == '__main__':
    main()