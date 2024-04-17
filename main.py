def bsort(arr):
    n=len(arr)
    k=1
    while(True):
        c=0
        for i in range(n-k):
            if arr[i+1]<arr[i]:
                arr[i+1],arr[i]=arr[i],arr[i+1]
                c=c+1
        if c==0:
            return
        k=k+1