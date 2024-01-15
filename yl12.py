thislist = ["Apple", "Cherry", "Strawberry"] #-- Your fruit list
print (thislist) #-- Prints what are in your list



print(thislist[0]) #-- Reads first thing from left to right (The python language count starts with 0)
thislist.append("Banana") #-- Adds a new element to your list
print(thislist) #-- Prits your thislist again, after "Banana" was added



print(thislist[-1]) #-- The negative noumer will start counting from rigt to left, while positve are starting from left to right
thislist[0] = "Blueberry" #-- Changes the first element in list on element that in string
print(thislist) #-- Prints new version of list



thislist.remove("Cherry") #-- Removes an element in list
print(thislist) #-- Prints list without the element that was removed



thislist.reverse() #-- Revers the list, so it will read from rigt to left, insted of left to right

#-- Example NORMAL: (Red, Blue, Black)..... REVERSED: (Black, Blue, Red)

print(thislist) #-- Prints list, but reversed
thislist.sort() #-- Sorts listed elements by alphabet
print(thislist) #-- Prints list by alphabet letters