#Create a function that will Retrieve and log user details
#Elderny, james, jonathan => food, gym

main = int(input("Type 0 to insert info and 1 for get info: \n"))
def getdate():
    import datetime
    return datetime.datetime.now()
time = getdate()

user = int(input("Type 0 for Elderny, 1 for James and 2 for Jonathan\n"))

def take():
    if user == 0:
            elderny_ask = int(input("Type 0 to select Food, and 1 to select Exercise\n"))
            if elderny_ask == 0:
                print("You've selected Food file\n")
                elderny_food = input("Please type the name of food that you ate today: \n")
                with open("elderny_food.txt", "a") as f:
                    a = f.write(str(time) + ": " + elderny_food + "\n")
                    print("\nYour data has been successfully saved to the file named as 'elderny_food' ")
            elif elderny_ask == 1:
                print("You've selected Exercise file\n")
                elderny_gym = input("Please Type the name of Exercise you did today: \n")
                with open("elderny_gym.txt", "a") as f:
                    a = f.write(str(time) + ": " + elderny_gym + "\n")
                    print("\nYour data has been successfully saved to the file named as 'elderny_gym'")
    elif user == 1:
        james_ask = int(input("Type 0 to select Food, and 1 to select Exercise\n"))
        if james_ask == 0:
            print("You've selected Food file\n")
            james_food = input("Please type the name of food that you ate today: \n")
            with open("james_food.txt", "a") as f:
                a = f.write(str(time) + ": " + james_food + "\n")
                print("\nYour data has been successfully saved to the file named as 'james_food' ")
        elif james_ask == 1:
            print("You've selected Exercise file\n")
            james_gym = input("Please Type the name of Exercise you did today: \n")
            with open("james_gym.txt", "a") as f:
                a = f.write(str(time) + ": " + james_gym + "\n")
                print("\nYour data has been successfully saved to the file named as 'james_gym'")
    elif user == 2:
        jonathan_ask = int(input("Type 0 to select Food, and 1 to select Exercise\n"))
        if jonathan_ask == 0:
            print("You've selected Food file\n")
            jonathan_food = input("Please type the name of food that you ate today: \n")
            with open("jonathan_food.txt", "a") as f:
                a = f.write(str(time) + ": " + jonathan_food + "\n")
                print("\nYour data has been successfully saved to the file named as 'jonathan_food' ")
        elif jonathan_ask == 1:
            print("You've selected Exercise file\n")
            jonathan_gym = input("Please Type the name of Exercise you did today: \n")
            with open("jonathan_gym.txt", "a") as f:
                a = f.write(str(time) + ": " + jonathan_gym + "\n")
                print("\nYour data has been successfully saved to the file named as 'jonathan_gym'")
def give():
    if user == 0:
        elderny_ask = int(input("Type 0 to select Food, and 1 to select Exercise\n"))
        if elderny_ask == 0:
          with open("elderny_food.txt") as f:
            a = f.read()
            print(a)
        elif elderny_ask == 1:
            with open("elderny_gym.txt") as f:
                a = f.read()
                print(a)
    elif user == 1:
        james_ask = int(input("Type 0 to select Food, and 1 to select Exercise\n"))
        if james_ask == 0:
          with open("james_food.txt") as f:
            a = f.read()
            print(a)
        elif james_ask == 1:
            with open("james_gym.txt") as f:
                a = f.read()
                print(a)
    elif user == 2:
        jonathan_ask = int(input("Type 0 to select Food, and 1 to select Exercise\n"))
        if jonathan_ask == 0:
          with open("jonathan_food.txt") as f:
            a = f.read()
            print(a)
        elif jonathan_ask == 2:
            with open("jonathan_gym.txt") as f:
                a = f.read()
                print(a)
if main == 0:
    take()
elif main == 1:
    give()