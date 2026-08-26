class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        size=len(s)

        neg=False
        val=0

        for i in range(size):
            char=s[i]

            if i==0:
                if char=='-':
                    neg=True
                    continue
                elif char=='+':
                    neg=False
                    continue

            if char.isdigit():
                val=val*10+(int(char))
            else:
                break

        INT32_MIN = -2147483648
        INT32_MAX = 2147483647

        def clamp_to_int32(val):
            return max(INT32_MIN, min(val, INT32_MAX))

        if neg:
            val*=-1
        return clamp_to_int32(val)
