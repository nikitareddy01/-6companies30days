
class Solution:
    def CountWays(self, str):
        if str[0]=='0' or str[-1]=='0':
            return 0
        elif str.count('0')>=2:
            return 0
        else:	    
            dp = [0] * len(str)
            dp[0] = 1
            for i in range(1,len(dp)):
                #if str[i-1] == '0' and str[i] == '0':
                    #dp[i] = 0
                if str[i-1] == '0' and str[i] != '0':
                    dp[i] = dp[i-1]
                elif str[i-1] != '0' and str[i] == '0':
                    if str[i-1] == '1' or str[i-1] == '2':
                        if i >= 2:
                            dp[i] = dp[i-2]
                        else:
                            dp[i] = 1
                    else:
                        dp[i] = 0
                else:
                    if int(str[i-1 : i+1]) <= 26:
                        if i >= 2:
                            dp[i] = dp[i-1] + dp[i-2]
                        else:
                            dp[i] = dp[i-1] + 1
                    else:
                        dp[i] = dp[i-1]
        #print(dp)
        return dp[-1] % 1000000007


import sys
sys.setrecursionlimit(10**6)
if __name__=='__main__':
        T=int(input())
        for i in range(T):
            str=input()
            ob = Solution()
            ans= ob.CountWays(str)
            print(ans)