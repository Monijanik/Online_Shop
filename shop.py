import customer
import admin
class Shop:
	
	def __init__(self):
		self.products = []
		self.orders = []
		self.customers = []
		self.admins = []	
		
	def login_admin(self, name, password):
		admin1 = admin.Admin(name, password)
		admin1.login()

	def login_user(self, email, password):
		customer1 = customer.Customer(email, password)
		customer1.login()


	def register_user(self, name, password, email, birthdate, address):
		with open('users.txt','r') as f:
			lines = f.readlines()

		id = len(lines) + 1
		customer1 = customer.Customer(id, name, password, email, birthdate, address)
		customer1.register()
            
	



