import heapq

data = [1, 5, 11, 9, 7, 2]
array = []
k = 3

for i in range(0, k):
    heapq.heappush(array, data[i])

for i in range(k, len(data)):
    print(data[i])
    if data[i] > array[0]:
        heapq.heappop(array)
        heapq.heappush(array, data[i])