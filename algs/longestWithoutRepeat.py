class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1
        maxi = 0
        seen = ''
        for start in range(len(s)):
            for i in range(start, len(s)):
                char = s[i]
                if char in seen:
                    if len(seen) >= maxi:
                        maxi = len(seen)
                    seen = ''
                    break
                seen += char
        if len(seen) >= maxi:
            return len(seen)
        return maxi

    print(lengthOfLongestSubstring(None, "aabb qer uyc"))
