class ChangeAge:
    
    name = 'jack' #try to change this too
    
    def __init__(self, age):
        self.age = age

    @staticmethod
    def print_name():
        print(ChangeAge.name)
        
    def print_age(self):
        print(self.age)