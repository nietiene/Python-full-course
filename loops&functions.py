# nested while loops
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1 

# for eahc time  i will runs also j will runs twice
# i=1, j=1
# i=1, j=2    

#  else with while loop
x = 1
while x > 4:
    print(x)
    x += 1
else:
    print("Loop finished")    

# when you use break will not run
# x = 1 
# while x > 5:
#     print(x)
#     if x == 2:
#     break # automaticaly here it generate an error
#    x + 1
# else:
# print("This wont run")

# Menu system usin while loop

while True: # it will keep showing menu until you break
    print("\nMenu:")
    print("1. say hello")
    print("2. Exit")
    choice = input("Choose option")

    if choice == "1":
       print("Hello word")
    elif choice == "2":
        print("Good bye!")
        break
    else:
        print("Invalid choice. Try again")