#Goal: Create a variable env = "production". 
# Write an if statement that only prints "Executing Delete" if 
# env is NOT equal to "production". Otherwise, 
# print "Access Denied: Cannot delete in Prod!"
env = "production"
env = input("Enter Your Id: ")
if env != "production":
    print("Executing Delete")
else:
    print("Access Denied: Cannot delete in Prod!")