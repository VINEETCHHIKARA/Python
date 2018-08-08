def maxProduct(arr,n):
    if n<2 :
        print("pair does not exsist")
    else:
        a=arr[0]
        b=arr[1]
        for i in range(0,n):
            for j in range(i+1,n):
                if arr[i]*arr[j]>a*b and i!=j:
                    a=arr[i]
                    b=arr[j]
        print("frist num ={0} Second num ={1} product ={2}".format(a,b,a*b))

arr= [1,2]
n= len(arr)
maxProduct(arr,n)
