#I will be creating an ec2 name generator
import random
import string

#creating a function that generates random strings
def random_gen():
    generator = string.ascii_letters + string.digits
    return " ".join(random.choice(generator) for _ in range(20))


#input of user's department
department = input("Welcome to LUIT!! , Will you please input the depart you will be working in : \nFinancialops \nAccounting  \nMarketing: ")

#department name 
for _ in department:
    if department == "Accounting" or department.lower() == "accounting":
        break
    elif department == "Financialops" or department.lower() == "financialops":
        break
    elif department == "Marketing" or department.lower() == "marketing":
        break
    else:
        print("Your input was incorrect \n Check the spelling or use all lowercase \n The name of the Finance department is financialops \n contact IT engineer if issue persists")

    
num_of_ec2 = int(input("Type the number of instance needed : "))

if num_of_ec2 > 0:
    print("The number of instances needed is being allocated: \n NOTE: Maximum number of instances is 20")
    for _ in range(1, num_of_ec2 +1):
        ec2_name = department
        ec2_uniqueId = ec2_name + "_" + random_gen()
        print("Here is you ec2s unique ID: ", ec2_uniqueId)
