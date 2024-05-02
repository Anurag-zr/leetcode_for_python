class Solution:
    def romanToInt(self, s: str) -> int:
        my_map = {
            'I': 1,
            "V":5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        if len(s) == 1: return my_map[s[0]]
        ans=0
        for i in range (1,len(s)):
            if my_map[s[i-1]]<my_map[s[i]]:
                ans -= my_map[s[i-1]]
                # print(ans)
                continue

            ans += my_map[s[i-1]]
            # print(ans,2)
        ans += my_map[s[len(s)-1]]
        return ans