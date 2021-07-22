class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        dm = {}
        
        for i in range(len(tickets)):
            if tickets[i][0] not in dm:
                dm[tickets[i][0]] = [tickets[i][1]]
            else:
                dm[tickets[i][0]].append(tickets[i][1])
                
        for k, v_list in dm.items():
            v_list.sort()
        
        
        path = []
        itinerary_len = len(tickets) + 1


        def backtrack(start, dm):

            if len(path) == itinerary_len:
                return True
            elif start not in dm or len(dm[start]) == 0:
                return False

            for i in range(0, len(dm[start])):
                dest = dm[start][i]
                del dm[start][i]
                path.append(dest)

                if backtrack(dest, dm):
                    return True

                path.pop()
                dm[start].insert(i, dest)

            return False

        path = ['JFK']    
        if backtrack('JFK', dm):
            return path

