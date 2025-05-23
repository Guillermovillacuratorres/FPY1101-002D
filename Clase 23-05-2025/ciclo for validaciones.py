

for i in range(5):
    print(i)
    while True:
        try:
            edad = int(input("Edad: "))    
            break
        except ValueError:
            print("Error.....")
        continue