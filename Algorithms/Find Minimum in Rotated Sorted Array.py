class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        L = 0; R = len(num)-1
        while L < R and num[L] > num[R]:
            M = (L+R)/2
            if num[M] < num[R]:
                R = M
            else:
                L = M+1
        return num[L]