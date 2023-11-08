from hashlib import sha256

def main():
    user_repo = {}

    print("Type exit at anytime to en program...")

    while True:
        mode = input("Enter mode (add|login): ")
        if mode == "add":
            add_user(user_repo)

        elif mode == "login":
            login_user(user_repo)

        elif mode == "exit":
            break

    for user in user_repo:
        print(f'{user} : {user_repo[user]}')

def login_user(user_repo):
    while True:
        username = input("Enter username: ")
        if username == 'exit':
            break
        
        password = input("Enter password: ")
        hash_password = sha256(password.encode('utf-8')).hexdigest()
        
        if user_repo.get(username) == hash_password:
            print("Password is correct")
        elif user_repo.get(username) == None:
            print("User does not exit")
        else:
            print("Incorrect password")

        
    return

def add_user(user_repo):

    while True:
        username = input("Enter username: ")
        if username == "exit":
            break

        password = input("Enter password: ")

        user_repo[username] = sha256(password.encode('utf-8')).hexdigest()
    return

if __name__ == "__main__":
    main()