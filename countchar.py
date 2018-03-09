while True:
    print("Enter 'x' for exit.")
    string = input("Enter a sentence: ")
    if string == 'x':
        break
    else:
        char = input("Enter a character to count: ")
        val = string.count(char)
        print(val,"\n")
