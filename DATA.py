def Hash(num):
    if num % 2 == 0:
        print(f"{num} That's an even number!")
    else:
        print(f"{num} That's an odd number!")

print("Odd or Even? Let's See!")

try:
    josh = int(input("Pick a number, any number: "))
    Hash(josh)
except ValueError:
    print("Aguy mali haha")
