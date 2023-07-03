def JobScheduling(self,Jobs,n):
    
    # code here
    jobs = Jobs
    jobs.sort(key=lambda x: x.profit, reverse=True)
    maxi = jobs[0].deadline
    for i in range(1,len(jobs)):
        maxi = max(maxi, jobs[i].deadline)
    
    slot = [-1] * (maxi+1)
    count = 0
    pro = 0
    
    for i in range(n):
        for j in range(jobs[i].deadline, 0,-1):
            if slot[j] == -1:
                slot[j] = i
                count += 1
                pro += jobs[i].profit
                break
    return count, pro