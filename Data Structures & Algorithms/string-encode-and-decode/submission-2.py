class Solution:

    def encode(self, strs: List[str]) -> str:
        newstr=""
        for word in strs:
            newstr += str(len(word)) + "#" + word

        return newstr

    def decode(self, s: str) -> List[str]:
        newlst = []
        i=0
        while i<len(s):
            j=i
            while(s[j]!='#'):
                j+=1

            dist = int(s[i:j])
            word = s[j+1: j+dist+1]
            newlst.append(word)
            i=j+1+dist

        return newlst
            
            
            
                
                
                
            
