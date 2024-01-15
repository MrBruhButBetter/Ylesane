users_string = input("Enter your Text here: ")
arv = 0

for i in users_string.lower():
    if(i == 'a' or i == '' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'õ' or i == 'ö' or i == 'ü'):
        arv += 1
print(arv)