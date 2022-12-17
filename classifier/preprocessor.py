import nltk
import string

from typing import List
from classifier.constants import RU_CHARS_LOWER
from nltk.stem.snowball import RussianStemmer, EnglishStemmer


nltk.download('stopwords')


class Preprocessor:
    def __init__(self, remove_stop_words: bool = False) -> None:
        self._stem = stem
        self._version = "0.0.3"
        self._char_mapping = {
            "e": "е",
            "ё": "е",
            "o": "о",
            "c": "с",
            "a": "а",
        }
        self._ru_stemmer = RussianStemmer()
        self._en_stemmer = EnglishStemmer()
        self._remove_stop_words = remove_stop_words
        self._special_symbols = string.punctuation + "-"
        self._stopwords = set(nltk.corpus.stopwords.words(["russian", "english"]))

    def _is_ru(self, text: str) -> bool:
        for char in text:
            if char not in RU_CHARS_LOWER:
                return False
        return True

    def _stem(self, text: str) -> str:
        if self._is_ru(text):
            return self._ru_stemmer.stem(text)
        return self._en_stemmer.stem(text)

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

        if self._remove_stop_words:
            tokens = [token for token in tokens if token not in self._stopwords]

        text = " ".join(tokens)

        return text

    def preprocess(self, texts: List[str]) -> List[str]:
        return [self._preprocess(text) for text in texts]