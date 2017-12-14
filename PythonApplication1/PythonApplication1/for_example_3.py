for attempts_left in range(3, 0, -1):
    password = input("Enter your password (you have {} ettempts_left): ".format(attempts_left))
    if password == "111":
        print("Access granted")
        break
else:
    print("Access denied")
