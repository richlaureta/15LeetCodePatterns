def forLoop(count, endCount, word) -> int:
    if count == endCount:
        return
    
    print(word[count])
       
    count += 1
    
    forLoop(count, endCount, word)

if __name__ == "__main__":
    count = 0
    endCount = 26
    word = "abcdefghijklmnopqrstuvwxyz"
    forLoop(count, endCount, word)
    print("____________________________")
    for i in range(0, len(word)):
        print(word[i])