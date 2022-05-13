class MoneyMachine:
    
    change_table = {
        '1': ['Loonies',  1.0],
        '2': ['Toonies', 2.0],
        '3': ['Quarters', 0.25],
        '4': ['Dimes',  0.10],
        '5': ['Nickels', 0.05],
    }
    
    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.profit}")

    def calculate_coins(self):       
        while True:
            selection = input('Select or Insert Coins.')
            if selection in self.change_table:
                try:
                    amount = int(input(f'Enter number of {self.change_table[selection][0]}: '))
                except ValueError:
                    print('You can only enter counting numbers for the number of coins. Please try again.')
                    continue
                self.money_received += (self.change_table[selection][1] * amount)
                print(round(self.money_received, 2), ' inseted into machine.')
            if selection == '6':
                break
        return self.money_received

 
    def display_coins(self):
        print('''
            Accepted Coins
            
              1. Loony
              2. Toony
              3. Quarter
              4. Dime
              5. Nickel
              6. Insert Coins
              ''')
 
 
    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.display_coins()
        self.calculate_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
        
