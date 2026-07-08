class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag={}
        note={}

        for c in magazine:
            if c in mag:
                mag[c]+=1
            else:
                mag[c]=1
        for c in ransomNote:
            if c in note:
                note[c]+=1
            else:
                note[c]=1

        for char in note:
            if char not in mag or mag[char]<note[char]:
                return False
        return True