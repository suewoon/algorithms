# https://leetcode.com/problems/meeting-rooms-ii/
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        meeting_rooms = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(meeting_rooms, intervals[0][1]) # 끝나는 시각을 min heap에 저장

        for interval in intervals[1:]:
            meeting_start, meeting_end = interval
            print(meeting_rooms[0], meeting_start)
            if meeting_rooms[0] <= meeting_start:  # 새로운 미팅의 시작시간보다 빨리 끝나는 미팅이 있다면 그 미팅룸 활용 가능
                heapq.heappop(meeting_rooms)
                heapq.heappush(meeting_rooms, meeting_end)
            else:  # 아니면 새로운 미팅룸 할당
                heapq.heappush(meeting_rooms, meeting_end)
        return(len(meeting_rooms))
