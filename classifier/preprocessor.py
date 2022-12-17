from typing import List


class Preprocessor:
    def __init__(self) -> None:
        self._version = "0.0.1"

    def _preprocess(self, text: str) -> str:
        return text

    def preprocess(self, texts: List[str]) -> List[str]:
        return [self._preprocess(text) for text in texts]