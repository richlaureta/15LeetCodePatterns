def subsets(nums: list[int]) -> list[list[int]]:
    #Problem #78 Subsets - Medium -  Concept by Greg Hogg(Youtuber)
    
    n = len(nums)
    finalAnswer, tracker = [], []

    def backTrack(index: int):
        if index == n:
            finalAnswer.append(tracker[:]) #Return copy of the tracker
            return
        
        #Don't pick nums[index]
        backTrack(index + 1)

        #Pick nums[index]
        tracker.append(nums[index])
        backTrack(index + 1)
        tracker.pop()

    backTrack(0)
    return finalAnswer

def permute(nums: list[int]) -> list[list[int]]:
    #Problem #46 Permutations - Medium - Solution Concept by YouTube Channel Greg Hogg - Understanding the Solution
     
    length = len(nums)
     
    answer = []
    partialSolution = []
    
    def depthFirstSearchPermutation():
        if len(partialSolution) == length:
            answer.append(partialSolution.copy())
            return
        for number in nums:
            if number not in partialSolution:
                partialSolution.append(number)
                depthFirstSearchPermutation()
                partialSolution.pop()
                
    depthFirstSearchPermutation()
    
    return answer

if __name__ == "__main__":
    nums = [1, 2, 3]

    print(permute(nums))