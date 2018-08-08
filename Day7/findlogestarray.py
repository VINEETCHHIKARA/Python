from sets import Set
def findLongestConseqSubseq(arr, n):
 
    s = Set()
    ans=0
 
    
    for ele in arr:
        s.add(ele)
 
    
    for i in range(n):
 
         
        if (arr[i]-1) not in s:
 
            
            j=arr[i]
            while(j in s):
                j+=1
 
            
            ans=max(ans, j-arr[i])
    return ans
 

if __name__=='__main__':
    n = 7
    arr = [2, 5, 7, 0, 1, 3, 4, 8, 9, 10]
    print "Length of the Longest contiguous subsequence is ",
    print  findLongestConseqSubseq(arr, n)
