name = input("Enter your name here: ")

city = input("Enter the name of your city you live: ")
if city  == "Saaremaa":
    print("That's cool, at latest you aren't from Hiiuma")

age = int(input("Your age here: "))
if age  <18:
    print("Your age of ", age, " are not allowed to dirve a car yet")
elif age == 18:
    print("Your age of " , age , "is allowed to drive a car")