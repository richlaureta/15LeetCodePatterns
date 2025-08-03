def reverseWords(s: str) -> str:
    #Problem # 151 Reverse Words in a String
    reversedString = ""
    myStack = []

    for index in range(len(s) - 1, -1, -1):
        if s[index] != " ":
            myStack.append(s[index])
        else:
            if len(myStack) > 0:
                while len(myStack) > 0:
                    reversedString += myStack.pop()
                reversedString += " "
        
        if len(myStack) > 0 and index == 0:
            while len(myStack) > 0:
                    reversedString += myStack.pop()
    
    trimmedString = reversedString.rstrip()
    return trimmedString
        

if __name__ == "__main__":
    s = "a good example"

    print(reverseWords(s))