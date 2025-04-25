'''
Author: Sepehr Rafiei
Date: 25 April, 2025
'''



'''
For two sum, we use two pointers from opposite ends moving closer towards the center.
If the sum at the two pointers is equal to k, we add to our answer list.
If sum is less, we move left pointer up, guaranteeing us a larger number.
If sum is more, we move right pointer down, bringing our sum lower.

This is possible because our arr is ordered.

I also added a start argument, which helps three sum use two_sum, starting at the correct index.
'''
def two_sum(arr, start, k):
    answer = []
    left, right = start, len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]
        if total == k:
            answer.append((left, right))
            left += 1
            right -= 1
        elif total < k:
            left += 1
        else:
            right -= 1
    return answer




'''
For three sum, we for loop through each index, then find all pairs using our 2 sum that is equal to k - arr[i].
we add to our answers.
'''
def three_sum(arr, k):
    answer = []
    for i in range(len(arr)):
        pairs = two_sum(arr, i + 1, k - arr[i])
        for left, right in pairs:
            answer.append((i, left, right))
    return answer





'''
With three sum we notice a recursive pattern, where n sum can be computed using n - 1 sum.
We use this property to create a recursive solution.
Our base case becomes two sum, then for any n greater we loop through and find the solution for n minus 1.
'''
def n_sum(arr, n, k, start=0):
    answer = []

    if n == 2:
        left, right = start, len(arr) - 1
        while left < right:
            total = arr[left] + arr[right]
            if total == k:
                answer.append([left, right])
                left += 1
                right -= 1
            elif total < k:
                left += 1
            else:
                right -= 1
    else:
        for i in range(start, len(arr)):
            sub_results = n_sum(arr, n - 1, k - arr[i], i + 1)
            for sub in sub_results:
                answer.append([i] + sub)

    return answer
