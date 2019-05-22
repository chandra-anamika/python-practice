def count_substring(string, sub_string):
    count=0
    lenSubstr = len(sub_string)
    lenStr = len(string)
    i=0

    #Traversing the string and calculating the number of occurences of substring
    while i<lenStr:
        #Matching from ith to length of substring to substring and increasing the counter in case of match- 
        if string[i:i+lenSubstr]==sub_string:
            count = count +1
        i=i+1
    return count

if __name__ == '__main__':

    #Getting input from console
    print("Enter the String - ",end='')
    string = input().strip()
    print("Enter the Substring - ",end='')
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)