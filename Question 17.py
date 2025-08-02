# 17. Analyze a string & print the count of each category

text=input("Enter a String: ")

letters=spaces=digits=specials=0

for chars in text:
    if chars.isalpha():
        letters += 1
    elif chars.isspace():
        spaces += 1
    elif chars.isdigit():
        digits += 1
    else:
        specials += 1
        
print("Letters: ",letters, sep='')
print("Spaces: ",spaces, sep='')
print("Digits: ",digits, sep='')
print("Specials: ",specials, sep='')