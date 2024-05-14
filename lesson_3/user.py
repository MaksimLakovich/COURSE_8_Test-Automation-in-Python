class User:

    def __init__(self, first_name, last_name):
        self.user_name = first_name
        self.user_surname = last_name
        
    def print_name(self):
        print("Имя:", self.user_name)

    def print_surname(self):
        print("Фамилия:", self.user_surname)

    def print_name_surname(self):
        print("Итого:", self.user_name, self.user_surname)