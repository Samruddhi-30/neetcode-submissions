class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs==[]:
            return '0'
        x = '???'.join(strs)
        return x


    def decode(self, s: str) -> List[str]:
        if s=='0':
            return []
        return s.split('???')
        
        

        
