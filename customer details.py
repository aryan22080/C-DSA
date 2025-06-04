class Customer:
    def __init__(self,n,ph):
       self.name = n 
       self.phone = ph 
    def get_name(self):
       return self.name 
    def set_phone(self,ph):
       return self.phone
    def get_phone(self):
       return self.phone
       
c = Customer('Aryan',8971413300)
print(c.get_name())
print(c.get_phone())