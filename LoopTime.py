def myfunction(n):
    for i in range(0,n+1):
        print("First Loop")
    
    j=1
    while(j<=n+1):
        print("Second Loop",j)
        j=j*2

    for i in range(1,100):
        print("Third Loop")

myfunction(5)
print("Total Iterations for Loop 1: n")
print("Total Iterations for Loop 2: logn")
print("Total Iterations for Loop 3: 99")