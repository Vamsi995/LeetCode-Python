class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        B = nums2
        A = nums1
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        count = 0
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1
                    count = max(count, memo[i][j])
        return count
        
        