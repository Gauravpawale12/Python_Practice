'''
Docstring for practice9

Write a program which accept one number from user and print
that number of even numbers on screen
'''
def PrintEvenNumbers(No):
    count = 0
    num = 2

    while count < No:
        print(num, end=" ")
        num = num + 2
        count = count + 1

def main():
    value = int(input("Enter number : "))
    PrintEvenNumbers(value)

if __name__ == "__main__":
    main()
