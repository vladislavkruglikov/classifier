from typing import Dict, List


class Imputer:
    def __init__(self, mapper: Dict[str, List[str]]):
        self._mapper = mapper
        
    
    def _impute(self, text: str) -> str:
        chars = list(text)
        for i, char in enumerate(chars):
            if char in self._mapper:
                chars[i] = "(" + "|".join(self._mapper[char]) + ")"
        
        return "".join(chars)
    
    def impute(self, texts: List[str]) -> str:
        return "|".join(["\\b" + self._impute(text) + "\\b" for text in texts])