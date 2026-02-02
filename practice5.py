# Accept one number from user and print that number of "*" on screen


def main():
    No = int(input("Enter the number :"))

    while No != 0:
        print("*\t",end="")
        No -= 1
if __name__ == "__main__":
    main()
