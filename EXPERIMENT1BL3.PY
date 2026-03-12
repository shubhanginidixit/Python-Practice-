# Authentication Decorator
def authenticate(func):
    valid_users = ["admin", "user1", "teacher"]

    def wrapper(username, *args, **kwargs):
        if username in valid_users:
            return func(username, *args, **kwargs)
        else:
            print("Error: Unauthorized user")
    return wrapper


# Function protected by decorator
@authenticate
def access_system(username):
    print(f"Welcome {username}! Access granted.")


# Dynamic input
user = input("Enter username: ")
access_system(user)