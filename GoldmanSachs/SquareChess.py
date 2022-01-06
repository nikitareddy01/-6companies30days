class Solution:
    def squaresInChessBoard(self, N):
        ans= (N*(N+1)*(2*N+1))//6
        return ans 


if __name__=='__main__':
        N=int(input())
        ob=Solution()
        print(ob.squaresInChessBoard(N))