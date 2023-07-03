def maximumMeetings(self,n,start,end):
    # code here
    ans = []
    for i in range(n):
        ans.append([end[i],start[i]])

    ans.sort(key = lambda x:x[0])
    
    limit = ans[0][0]
    count = 1
    
    for i in range(1,n):
        if ans[i][1] >  limit:
            count += 1
            limit = ans[i][0]
    return count