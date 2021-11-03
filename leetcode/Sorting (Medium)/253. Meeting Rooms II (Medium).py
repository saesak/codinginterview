'''
this soln didn't work due to time limit 

but works for smaller inputs

O(n^2) time practically
'''

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        max_val = 0
        curr = 0
        
        intervals = sorted(intervals, key = lambda x: x[0])
        
        for i in range(len(intervals)):
            curr = 0
            for j in range(0, i):
                if intervals[j][1] > intervals[i][0] > intervals[j][0]:
                    curr += 1
                elif intervals[j][1] > intervals[i][1] > intervals[j][0]:
                    curr += 1
                elif intervals[j][0] == intervals[i][0]:
                    curr += 1
                    
            max_val = max(max_val, curr + 1)
        
        return max_val

'''
good solution by leetcode, o(nlogn) time cuz sorting, o(n) space for 2 arrays

1. Separate out the start times and the end times in their separate arrays.

2. Sort the start times and the end times separately. Note that this will mess up the original 
correspondence of start times and end times. They will be treated individually now.

3. We consider two pointers: s_ptr and e_ptr which refer to start pointer and end pointer. 
The start pointer simply iterates over all the meetings and the end pointer helps us track 
if a meeting has ended and if we can reuse a room.

4. When considering a specific meeting pointed to by s_ptr, we check if this start timing is 
greater than the meeting pointed to by e_ptr. If this is the case then that would mean some 
meeting has ended by the time the meeting at s_ptr had to start. So we can reuse one of the rooms. 
Otherwise, we have to allocate a new room.

5. If a meeting has indeed ended i.e. if start[s_ptr] >= end[e_ptr], then we increment e_ptr.

6. Repeat this process until s_ptr processes all of the meetings.
'''

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0

        used_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0

        # Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1    
            start_pointer += 1   

        return used_rooms