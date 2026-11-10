# Write a Python program to find three numbers from an array such that the sum of three numbers equal to zero.
# Input : [-1,0,1,2,-1,-4] 
# Output : [[-1, -1, 2], [-1, 0, 1]] 
# Note : Find the unique triplets in the array.

l = [1, -1, 0, -1, -1, 2]

result = [] 

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        for k in range(j + 1, len(l)):
            if l[i] + l[j] + l[k] == 0:
                triplet = tuple(sorted([l[i], l[j], l[k]]))

                if triplet not in result:
                    result.append(triplet)

print(result)