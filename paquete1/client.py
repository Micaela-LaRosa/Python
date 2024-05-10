class Client():
    def __init__(self, name, lastname, address, phone):
        self.__name = name
        self.__lastname = lastname
        self.__address = address
        self.__phone = phone

    def __str__(self):
        return f'The clients info is: {self.__name}, {self.__lastname}, {self.__address} and {self.__phone}'
    
    def buy(self, item, market):
        self.item = item
        self.market = market
        return f'The client {self.__name} bought a/an {self.item} on {self.market}'
    
    def ask_for(self, item, num_calls, phone):
        self.item = item
        self.num_calls = num_calls
        self.phone = phone
        return f'The client {self.__name} ask for a/an {self.item} calling {self.num_calls} times, and left his phone number {self.phone}'

