class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 800,
            "milk": 800,
            "coffee": 800,
        }
 
    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        
    def is_enough(self, drink):
        for resource, amount in self.resources.items():
            if amount < drink.ingredients[resource]:
                print(f'There is not enough {resource}. please service this machine')
                return False
        return True

    def call_service(self):
        for k, v in self.resources.items():
            if v < 300:
                print(f'You are running low on {k}. enter service to replenish this machine.')

    def service(self):
        for k in self.resources:
            self.resources[k] = 800
        return self.resources
    
    
    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
        
        
