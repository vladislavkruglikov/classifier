import string

from typing import List


class Preprocessor:
    def __init__(self) -> None:
        self._version = "0.0.2"
        self._char_mapping = {
            "e": "е",
            "ё": "е",
            "o": "о",
            "c": "с",
            "a": "а",
        }
        self._special_symbols = string.punctuation + "-"

    def _apply_char_mapping(self, text: str) -> str:
        for char, replacement in self._char_mapping.items():
            text = text.replace(char, replacement)
        return text

    def _preprocess(self, text: str) -> str:
        text = text.lower()

        text = self._apply_char_mapping(text)

        tokens = text.split()
        tokens = [token.strip(self._special_symbols) for token in tokens]
        tokens = [token for token in tokens if not token.isdigit()]

        text = " ".join(tokens)

        return text

    def preprocess(self, texts: List[str]) -> List[str]:
        return [self._preprocess(text) for text in texts]