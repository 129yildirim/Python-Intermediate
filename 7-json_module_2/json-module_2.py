import json

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class UserRepository:
    current_user = {}
    logged_in = False
    def register(self, user:User):
        file_data = {}
        
        with open('users.json', 'r') as f:
            try:
                file_data = json.load(f)
            except json.JSONDecodeError:
                pass
            if user.username in file_data:
                print('Failed to register! This username is taken.')
                return
        with open('users.json', 'w') as f:
            file_data[user.username] = user.__dict__
            json.dump(file_data, f, indent=4)
        
        print("Registered succesfully.")
    def log_in(self, username, password):
         file_data = {}
         with open('users.json', 'r') as f:
            try:
                file_data = json.load(f)
            except json.JSONDecodeError:
                pass
            if self.logged_in:
                print('Failed. Log out first.')
            elif username in file_data and file_data[username]['password'] == password:
                self.current_user = file_data[username]
                print('Logged in successfully')
                self.logged_in = True
            else:
                print('Failed to log in. Wrong username or password')
    def log_out(self):
        if self.logged_in:
            self.logged_in = False
            self.current_user = {}
            print('Logged out successfully')
        else:
            print('Failed to log out. Log in first.')
    
    def identity(self):
        if self.logged_in == True:
            file_data = {}
            print('username:', self.current_user['username'], '\nemail:', self.current_user['email'])
        else:
            print('Failed to show identity. You need to log in first.')

repository = UserRepository()

while(True):
    print('Menu'.center(50, '*'))
    option = input('1 - Register\n2 - Log in\n3 - Log out\n4 - Identity\n5 - Exit\nEnter your option here:')
    if option == '1':
        username = input('username: ')
        email = input('email: ')
        password = input('password: ')
        user = User(username, email, password)
        repository.register(user)
        
    elif option == '2':
        username = input('username: ')
        password = input('password: ')
        repository.log_in(username, password)
    elif option == '3':
        repository.log_out()
    elif option == '4':
        repository.identity()
    elif option == '5':
        break




