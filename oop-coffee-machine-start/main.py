from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

class Main:
    def __init__(self):
        self.menu = Menu()
        self.coffee_maker = CoffeeMaker()
        self.money_machine = MoneyMachine()
 
    def machine_running(self):
        running = True
        while running:
            options = self.menu.get_items()
            choice = input(f'What would you like? {options} ')
            if choice == 'off':
                print('Shutting down')
                running = False
            elif choice == 'report':
                self.coffee_maker.report()
                self.money_machine.report()
            elif choice == 'service':
                self.coffee_maker.service()
            else:
                drink = self.menu.find_drink(choice)
                if drink:
                    if self.coffee_maker.is_enough(drink):
                        if self.money_machine.make_payment(drink.cost):
                            self.coffee_maker.make_coffee(drink)
                    self.coffee_maker.call_service()

                    
if __name__ == '__main__':
    Main().machine_running()