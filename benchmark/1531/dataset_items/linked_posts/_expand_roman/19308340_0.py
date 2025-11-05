def main():
    string=str(input("Enter a roman numeral"))
    total=0
    while string != "": # Empty strings evaluate as False, this can just be 'while string:'
        if string[1] == string[2] or string == len([1]): # Here you are testing the 2nd and 3rd elements.
                                                         # Also, you want to do len(string) == 1
                                                         # string will never == len([1]), so you never
                                                         # execute the code in this block.
            total += string[1]+1   # You want to add the corresponding value of string[0], use a dictionary.
        print (total)

        # Missing the else statement in the pseudocode.
main()
