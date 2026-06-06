class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = defaultdict(int)

        if len(s) != len(t):
            return False

        for c in range(len(s)):
            s_map[s[c]] += 1
            t_map[t[c]] += 1


        for c in t:
            if s_map[c] != t_map[c]:
                return False
        return True
        