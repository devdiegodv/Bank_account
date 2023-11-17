class Person:
    """
    Represents a generic person with a name and last name.

    Attributes:
    - name (str): The first name of the person.
    - last_name (str): The last name of the person.
    """
    def __init__(self, name, last_name):
        """
        Initializes a new Person object.

        Parameters:
        - name (str): The first name of the person.
        - last_name (str): The last name of the person.
        """
        self.name = name
        self.last_name = last_name

class Client(Person):
    """
    Represents a client, inheriting from the Person class, with additional attributes
    for managing a bank account.

    Attributes:
    - name (str): The first name of the client.
    - last_name (str): The last name of the client.
    - number_account (int): The client's account number.
    - balance (float): The current balance in the client's account. Default is 0.
    """
    def __init__(self, name, last_name, number_account, balance = 0):
        """
        Initializes a new Client object, extending the Person class.

        Parameters:
        - name (str): The first name of the client.
        - last_name (str): The last name of the client.
        - number_account (int): The client's account number.
        - balance (float): The initial balance in the client's account. Default is 0.
        """
        super().__init__(name, last_name)
        self.number_account = number_account
        self.balance = balance

    def __str__(self):
        """
        Returns a string representation of the Client object.

        Returns:
        str: A formatted string containing the client's name, last name, account number,
             and account balance.
        """
        return f'Client: {self.name} {self.last_name}\nAccount balance {self.number_account}: ${self.balance}'
    
    def deposit(self, deposit_mount):
        """
        Deposits a specified amount into the client's account.

        Parameters:
        - deposit_amount (float): The amount to be deposited.

        Prints:
        - 'Deposit accepted' if the deposit is successful.
        """
        self.balance += deposit_mount
        print('Deposit accepted')
    
    def withdraw(self, withdraw_amount):
        """
        Withdraws a specified amount from the client's account if sufficient funds are available.

        Parameters:
        - withdraw_amount (float): The amount to be withdrawn.

        Prints:
        - 'Withdrawal made' if the withdrawal is successful.
        - 'Insufficient funds' if the account balance is less than the withdrawal amount.
        """
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print('Withdrawal made')
        else:
            print('Insufficient funds')

    def create_client():
        """
        Method to create a new Client object by taking user input for name,
        last name, and account number.

        Returns:
        Client: A new Client object with user-provided information.
        """
        name = input('Type your name: ')
        last_name = input('Type your last name: ')
        account_number = input('Type your number account')