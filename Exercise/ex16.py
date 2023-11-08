from hashlib import sha256

def main():
    user_repo = {}

    while True:
        username = input("Enter username: ")
        if username == "exit":
            break

        password = input("Enter password: ")

        user_repo[username] = sha256(password.encode('utf-8')).hexdigest()

    for user in user_repo:
        print(f'{user} : {user_repo[user]}')

if __name__ == "__main__":
    main()