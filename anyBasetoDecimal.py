def reverse(A):
    s=""
    for ele in A:
        s=ele+s
    return s
def power(base,x):
    if x==0:
        return 1
    return base*power(base,x-1)

def anyBasetoDecimal(A,B):
    """
    reverse the string
    A[i]*(base**(i)
    :return:
    """
    A=reverse(A)
    ans=0
    for i in range(len(A)):
        x=int(A[i])
        ans+=(x*(power(B,i)))
    return ans

if __name__ == '__main__':
    A=input()
    B=int(input())
    print(anyBasetoDecimal(A,B))