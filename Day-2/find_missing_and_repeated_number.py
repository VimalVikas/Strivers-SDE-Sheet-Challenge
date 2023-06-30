def repeatedNumber(self, A):
    ans=[]

    sum1=sum(A)

    n=len(A)

    s=n*(n+1)//2

    A=list(set(A))

    sum2=sum(A)

    rep_num=sum1-sum2

    ans.append(rep_num)

    ans.append(s-sum2)

    return ans