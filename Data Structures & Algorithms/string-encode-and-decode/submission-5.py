class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs==[]:
            return '00000'
        x = '???'.join(strs)
        return x


    def decode(self, s: str) -> List[str]:
        if s=='00000':
            return []
        return s.split('???')
        
        

        
