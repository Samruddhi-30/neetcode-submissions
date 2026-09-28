class Solution:

    def encode(self, strs: List[str]) -> str:
        x = '???'.join(strs)
        return x


    def decode(self, s: str) -> List[str]:
        return s.split('???')
        
        

        
