def twoSum(numbers: list[int], target: int) -> list[int]:
    startIndex = 0
    endIndex = len(numbers) - 1

    while startIndex < endIndex:
        if (numbers[startIndex] + numbers[endIndex]) == target:
            return [startIndex + 1, endIndex + 1]
        elif numbers[startIndex] + numbers[endIndex] > target:
            endIndex -= 1
        else: 
            startIndex += 1

if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9

    print(twoSum(numbers, target))