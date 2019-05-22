if __name__ == '__main__':
    s = input()
    
    i =0
    alpha = 0
    digit = 0
    low = 0
    upp = 0
    alnum=0
    while (i<len(s)):
        if s[i].isalnum() == True:
            alnum=1
        if s[i].isalpha() == True:
            alpha=1
        if s[i].isdigit() == True:
            digit=1
        if s[i].islower() == True:
            low=1
        if s[i].isupper() == True:
            upp=1
        i = i+1
    if alnum == 1:
        print("True")
    else:
        print("False")
    if alpha == 1:
        print("True")
    else:
        print("False")
    if digit == 1:
        print("True")
    else:
        print("False")
    if low == 1:
        print("True")
    else:
        print("False")
    if upp == 1:
        print("True")
    else:
        print("False")   