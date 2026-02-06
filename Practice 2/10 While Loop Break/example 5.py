# Simple echo programm
while True:
    a = input("Enter a word (type 'quit' to exit): ")
    if a.lower() == 'quit':
        print("Goodbye!")
        break
    print(f"You typed: {a}")
