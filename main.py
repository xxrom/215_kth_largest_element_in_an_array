# import times

from typing import List


# time= O(N)/ memory= O(N)
class Solution:

  def findKthLargest(self, nums: List[int], k: int) -> int:
    items = {}

    # Fill items dict with items and count them
    for num in nums:
      if num not in items:
        items[num] = 1
      else:
        items[num] += 1

    for num in sorted(items.keys(), reverse=True):
      # Remove counted items from top to bottom
      k -= items[num]
      # Find ans number
      if k <= 0:
        return num

    return None


my = Solution()
n = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
# start_time = time.time()
ans = my.findKthLargest(n, k)
# print('time', time.time() - start_time)
print("> ans = ", ans)

# Runtime: 56 ms, faster than 97.87% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 14.7 MB, less than 10.00% of Python3 online submissions for Kth Largest Element in an Array.