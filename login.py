
def login(username, password):
    if username == "admin" and password == "1234":
        return "Login Successful - Welcome to Dashboard"
    return "Invalid Username or Password"

if __name__ == "__main__":
    print(login("admin", "1234"))
    print(login("admin", "wrong"))
