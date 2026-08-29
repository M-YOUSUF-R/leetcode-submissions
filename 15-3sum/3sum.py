class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        p ,n,z= [],[],[] 

        for i in nums:
            if i > 0:
                p.append(i)
            elif i < 0:
                n.append(i)
            else:
                z.append(i)
        N,P = set(n),set(p)
        # if atleast 3 zero
        if len(z) >= 3:
            res.add(tuple([0,0,0]))

        # one zero with same but different nums
        if z:
            for i in p:
                if -1*i in N:
                    res.add(tuple([-1*i,0,i]))
        

        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1* (p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))
        return list(res)