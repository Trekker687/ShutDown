def shutdown(t):
    
    if t == "Yes":
        print("Shutting down")
    elif t == "No":
        print("Aborting shutdown")
    else:
        print("Sorry, invalid input")


x = input("Shutdown? Enter Yes/No: ")
shutdown(x)