def rabbit_recur(n,k):
    if n < 2:
        return n
    return k*rabbit_recur(n-2, k) + rabbit_recur(n-1,k)
        
print(rabbit_recur(30,4))
