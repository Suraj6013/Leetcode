class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        #Your code here
        A.reverse()
        for i in range(N):
            if A[i]<=X:
                y =  A[i]
                A.reverse()
                for j in range(N):
                    if A[j] == y:
                        return j
                break
        return -1
x = Solution()
print(x.findFloor([1,2,8,10,10,12,19], 7, 5))