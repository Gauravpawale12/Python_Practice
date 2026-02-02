# Accept one number from user if the number is less than 10 then print "Hello"
# otherwise print "Demo"
def Display(No):

    if No <= 10:
        return True
    else:
        return False
def main():
    No = int(input("Enter the number :"))
    Ret = Display(No)
    if Ret == True:
        print("Hello")
    else:
        print("Demo")

if __name__ == "__main__":
    main()