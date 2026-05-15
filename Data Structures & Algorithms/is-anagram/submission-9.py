class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)
        for vs, vt in zip(s, t):
            dict_s[vs] += 1
            dict_t[vt] += 1
        return dict_s == dict_t