class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a=a[::-1]
        b=b[::-1]
        c=''
        i=j=0
        carry=0
        while i<len(a) or j<len(b):
            if i<len(a) and j<len(b):
                total=int(a[i])+int(b[j])+carry
                i+=1
                j+=1
            elif i<len(a):
                total=int(a[i])+carry
                i+=1
            else:
                total=int(b[j])+carry
                j+=1
            
            if total>1:
                carry=1
                total-=2
            else:
                carry=0
            c+=str(total)
        if carry==1:
            c+=str(carry)
        c=c[::-1]
        return c