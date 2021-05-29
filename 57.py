class Solution:
    def insert(self, intervals, newInterval):
        i = 0
        n = len(intervals)
        output = []
        new_start, new_end = newInterval
        while i < n and new_start > intervals[i][0]:
            output.append(intervals[i])
            i += 1
        
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        else:
            output[-1][1] = max(output[-1][1], new_end)

        while i < n:
            interval = intervals[i]
            s,e = interval
            if output[-1][1] < s:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], e)
            i += 1

        return output

