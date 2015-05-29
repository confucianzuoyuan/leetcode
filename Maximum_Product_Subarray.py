class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) == 0:
            return 0
        min_tmp = A[0]
        max_tmp = A[0]
        result = A[0]
        for i in range(1, len(A)):
            a = A[i] * min_tmp
            b = A[i] * max_tmp
            c = A[i]
            max_tmp = max(max(a,b),c)
            min_tmp = min(min(a,b),c)
            result = max_tmp if max_tmp > result else result
        return result