print("registration application")
email = input('enter your email')
username = input('enter your username')
password = input('enter your password')
cpassword = input('confirm your password')
gender = input('gender (F/M/O)')

if username and email and password and cpassword and gender:
    if username.isalnum():
        if '@' in email and email.endswith('.com'):
            if password == cpassword:
                if len(password) >= 8:
                    print("registration complete")
                    print("🎉🎉🎉🎉")
                else:
                    print("password too small")      
            else:
                print("password does not match")
        else:
            print("invalid email")
    else:
        print("invalid username")
else:
    print("all fields are required")

