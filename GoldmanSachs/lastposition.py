# Python program to find the position where
# last item is delivered.

# n ==> Size of circle
# m ==> Number of items
# k ==> Initial position
def lastPosition(n, m, k):
    
    # n - k + 1 is number of positions
    # before we reach beginning of circle
    # If m is less than this value, then
    # we can simply return (m-1)th position
    if (m <= n - k + 1):
       return m + k - 1
 
    # Let us compute remaining items before
    # we reach beginning.
    m = m - (n - k + 1)
 
    # We compute m % n to skip all complete
    # rounds. If we reach end, we return n
    # else we return m % n
    if(m % n == 0):
        return n
    else:
        return m % n
 
if __name__=='__main__':
    n = 5
    m = 8
    k = 2
    print(lastPosition(n, m, k))