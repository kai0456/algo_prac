from collections import deque

#BFS:

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        room_visit = [0] * len(rooms)
        
        # The 0th room is gaurenteed being visited.
        room_visit[0] = 1

        # create queue to store keys collected from vistied roomes
        q = deque()

        if len(rooms) == 0:
            return True

        keys = rooms[0]
        for key in keys:
            q.append(key)

        while q:
            # print(q)
            key = q.popleft()

            # if the rooms is visited earlier, skip visit it again to prevent a loop.
            if room_visit[key] == 1:
                continue
            else:
                # flag the visit roome
                room_visit[key] = 1

                # grap new new keys
                new_keys = rooms[key]

                for key in new_keys:
                    if key not in q:
                        q.append(key)


        if sum(room_visit) == len(rooms):
            return True
        else:
            return False

