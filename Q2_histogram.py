#Solve for maximum area under histogram problem using stacks.
#complexity O(n)
def HistogramArea(ar):
    ans = 0
    ar = [-1] + ar
    ar.append(-1)
    n = len(ar)
    stack = [0] # here it is used as stack,index stack[-1] => top of stack  

    for i in range(n):
        while ar[i] < ar[stack[-1]]:
            h = ar[stack.pop()]
            # print 'h=',h,'i=',i,stack
            area = h*(i-stack[-1]-1)
            ans = max(ans, area)
        stack.append(i)
    return ans

print HistogramArea([5, 8, 1, 6, 5, 1, 9]); # 10  