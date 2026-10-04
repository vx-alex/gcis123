def validate(userid, passwd):
    if userid != "admin" or passwd != "password":
        raise ValueError("Invalid userid or password!")
    print("Welcome,", userid)

   

def login():
    attempts = 4

    while attempts > 0:
        userid = input("Enter userid: ")
        passwd = input("Enter password: ")

        try:
            validate(userid, passwd)
            print("Login successful!")
            break

        except ValueError:
            attempts -= 1
            print("Invalid.", attempts, "attempts remaining")


login()