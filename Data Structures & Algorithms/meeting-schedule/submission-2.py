"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sortInterval = sorted(intervals, key=lambda i: i.start) # 

        for i in range(1, len(intervals)):
            i1 = sortInterval[i - 1]
            i2 = sortInterval[i]

            if i1.end > i2.start:
                return False
        return True