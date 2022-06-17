def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def is_valid_string(str):
    try:
        float(str)
        return False
    except ValueError:
        return True


def Insert():
    a = input("Enter the First Entry : ")
    b = input("Enter the Second Entry : ")
    c = input("Enter the Third Entry : ")

    f = open("readwrite.txt","a")
    if(a.isnumeric() and isfloat(b) and is_valid_string(c)):
        f.write(a + ", " + b+", " + c + "\n")
        print("\nInserted Successfully..\n") 
        f.close()
    else:
        print("\nEntered Values is not Proper..\n")

def read():
    f = open("readwrite.txt","r")
    last = f.readlines()[-1]
    last = last.strip('\n')
    l = last.split(", ")
    print(l)

if __name__ == "__main__":

    while(True):
        print("1: Insert")
        print("2: Read")
        print("3: Exit")
        choice = int(input("Enter your Chocie : "))

        if(choice==1):
            Insert()
        elif(choice==2):
            read()
        elif(choice==3):
            exit()
        else:
            print("Enter Valid Choice..!!")

    

