class Node(object):
    def __init__(self,val):
        self.val=val
        self.neighbors=[]

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        nodem={}
        valm={}

        for equation,value in zip(equations,values):
            x,y=equation[0],equation[1]
            valm[(x,y)]=value
            valm[(y,x)]=1/value
            if x not in nodem:
                nodem[x]=Node(x)
            if y not in nodem:
                nodem[y]=Node(y)
            nodem[x].neighbors.append(nodem[y])
            nodem[y].neighbors.append(nodem[x])

        def bfs(src, dest):
            if src not in nodem or dest not in nodem:
                return -1
            q=collections.deque()
            q.append((nodem[src],1))
            visited=set()
            visited.add(src)
            while q:
                cur,weight=q.popleft()
                if cur==nodem[dest]:
                    return weight
                for neighbor in cur.neighbors:
                    if neighbor.val not in visited:
                        visited.add(neighbor.val)
                        q.append((neighbor,valm[(cur.val,neighbor.val)]*weight))
            return -1
        
        ans=[]
        for query in queries:
            ans.append(bfs(query[0],query[1]))

        return ans