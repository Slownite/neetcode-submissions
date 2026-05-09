class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        r_s = defaultdict(int)
        r_t = defaultdict(int)
        for v_s, v_r in zip(s, t):
            r_s[v_s] += 1
            r_t[v_r] += 1
        return r_s == r_t