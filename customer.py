class Customer:

    def __init__(self, id, name, password, email, birthdate, address):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.birthdate = birthdate
        self.address = address
        self.shopping_cart = []

    def login(self):
        with open('users.txt', 'r') as f:
            for line in f:
                if self.email in line and self.password in line:
                    return (f"Dear {self.name} You have signed in successfully!")
            else:
                return (f"{self.name} was not found ")
    def register(self):
        with open('users.txt', 'a') as f:
            f.write(self.id + ', ' + self.name + ', ' + self.password + ', ' + self.email + ', ' + self.birthdate + ', ' + self.address + '\n')

        return (f"Dear {self.name} you have signed up successfully!")

    def display_personal_info(self):
        print(f"Your email address is {self.email} and your birthdate is {self.birthdate} and your address is {self.address}")        

    def display_shopping_cart(self):
        print(f"Here is your shopping cart: {self.shopping_cart}")   