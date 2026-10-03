class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        if (sorted(s)==sorted(t)):
            return True
        else:
             return False
        """

        if (len(s)!=len(t)):
            return False

        count = {}

        for i in s:
            count[i] = count.get(i,0)+1

        for j in t:
            if j not in count:
                return False

            count[j]-=1

            if count[j]<0:
                return False

        return True

        