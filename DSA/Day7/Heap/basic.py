import heapq
numbers = [8,3,5,1,10]

heapq.heapify(numbers)

print(numbers)
print(heapq.heappop(numbers))
heapq.heappush(numbers, 2)
print(numbers)