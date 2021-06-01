from collections import Counter

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        element_counter = Counter(arr)
        element_list = list(element_counter.items())
        element_list.sort()
        answer = 0
        for element, cnt in element_list:
            if cnt >= element:
                answer = element
            else:
                answer += cnt
        return answer