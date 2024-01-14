class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        s_dict = Counter(s)
        t_dict = Counter(t)

        count = 0
        for c in s_dict:
            if c in t_dict:
                if s_dict[c] == t_dict[c]:
                    count += s_dict[c]
                else:
                    count += min(s_dict[c],t_dict[c])      

        
        return len(s) - count
