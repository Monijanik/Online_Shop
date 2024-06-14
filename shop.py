import customer, catagory
import admin
import uuid
class Shop:
	
	def __init__(self):
		self.products = []
		self.orders = []
		self.customers = []
		self.categories = []	
		
	def login_admin(self, name, password):
		admin1 = admin.Admin(name, password)
		return admin1.login()

	def login_user(self, email, password):
		customer1 = customer.Customer(email, password)
		return customer1.login()


	def register_user(self, name, password, email, birthdate, address):
		with open('users.txt','r') as f:
			lines = f.readlines()

		id = uuid.uuid4()
		customer1 = customer.Customer(id, name, password, email, birthdate, address)
		return customer1.register()
            
	def add_category(self, name):
		id = uuid.uuid4()
		category1 = catagory.Category




