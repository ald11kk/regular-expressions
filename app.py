import re

f = input("Enter text: ")

while True:
        choice = int(input("""1. findall
2. search
3. split
4. replace\n"""))
        if choice == 1:
            user = input("Search for: ")
            findall = re.findall(user, f)
            print(findall)
        if choice == 2:
            user = input("Search for: ")
            search = re.search(user, f)
            print(search.start())
        if choice == 3:
            user = input("Split by: ")
            split = re.split(user, f)
            print(split)
        if choice == 4:
            user = input("Replace: ")
            userr = input("To: ")
            sub = re.sub(user, userr, f)
            print(sub)