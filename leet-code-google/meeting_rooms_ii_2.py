# https://leetcode.com/problems/meeting-rooms-ii/
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # 어느 미팅이 언제 시작, 끝 정보는 필요 없음
        # 시작할 때 그것보다 일찍 끝나는 미팅이 있기만 하면됨
        # 시작시간 < 끝 시간이므로 자기 자신과 비교할 일은 애초에 없음
        start_timings = sorted([start for start, in intervals])
        end_timings = sorted([end for ,end in intervals])
        rooms = 0
        s_ptr, e_ptr = 0, 0
        while s_ptr < len(start_timings):
            if start_timings[s_ptr] < end_timings[e_ptr]:
                rooms +=1
            else:
                e_ptr +=1
            s_ptr+=1
       return rooms
