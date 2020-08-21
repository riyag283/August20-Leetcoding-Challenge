class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        all_values=[]
        def backtrack(N,K,mylist):
            if len(mylist)==N:
                if mylist[0]=='0' and len(mylist)>1:
                    return
                s = int(''.join(map(str, mylist)))
                if len(str(s))==N:
                    all_values.append(int(s))
                    return
                else:
                    return
            
            for i in range(10):                
                if len(mylist)==0:
                    mylist.append(i)
                    backtrack(N,K,mylist)
                    mylist.pop()
                else:
                    lastNo=mylist[-1]
                    if abs(lastNo-i)==K:
                        mylist.append(i)
                        backtrack(N,K,mylist)
                        mylist.pop()
        
        backtrack(N,K,[])
        
        return all_values
