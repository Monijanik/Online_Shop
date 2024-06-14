class Category:
     def __init__(self, name, id):
         self.name = name
         self.id = id
         self.allCategories = []
         
     def add(self):
         with open('categories.txt', 'a') as f:
              f.write(self.name + ',' + self.id + '\n')
         print(f"Category {self.name} was added successfully!")
         
     def category_list(self):
         with open('categories.txt', 'r') as f:
             for line in f:
                 self.allCategories.append(line.strip())
         return self.allCategories
	