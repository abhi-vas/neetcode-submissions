class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        min_length = float('inf')

        dict_t = defaultdict(int)
        dict_s = defaultdict(int)

        for stri in t:
            dict_t[stri] += 1
        required=len(dict_t)

        l = 0
        matches = 0
        start = 0
        for r in range(len(s)):

            dict_s[s[r]] += 1

            if dict_t[s[r]] <= dict_s[s[r]] and dict_t[s[r]] > 0:
                matches += 1
            if dict_t[s[r]] <= dict_s[s[r]] - 1 and dict_t[s[r]] > 0:
                matches -= 1

            while matches == required:

                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    start = l

                dict_s[s[l]] -= 1

                if dict_s[s[l]] + 1 <= dict_t[s[l]] and dict_t[s[l]] > 0:
                    matches -= 1
                l += 1

        return '' if min_length == float('inf') else s[start:start + min_length]
            