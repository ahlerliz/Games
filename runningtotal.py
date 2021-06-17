def main():
    # TODO write your solution here
    count = 1
    print("Enter a sequence of non-decreasing numbers.")
    user_input = input("Enter num: ")
    new_input = input("Enter num: ")
    while int(new_input) >= int(user_input):
        count += 1
        user_input = new_input
        new_input = input("Enter num: ")

    
    print("Thanks for playing!")
    print("Sequence length: " + str(count))
    

if __name__ == "__main__":
    main()
