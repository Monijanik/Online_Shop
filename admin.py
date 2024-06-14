class Admin:
	def __init__(self, name, password):
		self.name = name
		self.password = password

	def display(self):
		print(f"Dear {self.name} you are one of our admins")

	def login(self):
		with open('admins.txt', 'r') as f:
			for line in f:
				if self.name in line and self.password in line:
					return (f"Dear {self.name} You have signed in successfully!")
			else:
				return (f"{self.name} login is not allowed")