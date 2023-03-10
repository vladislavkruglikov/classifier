import re
import nltk
import string

from typing import List, Set
from classifier.constants import RU_CHARS_LOWER
from nltk.stem.snowball import RussianStemmer, EnglishStemmer


nltk.download('stopwords')


class Preprocessor:
    def __init__(self, 
                do_stem: bool = False,
                remove_stop_words: bool = False,
                black_list: str = None,
                max_token_length: int = 25,
                remove_single_letter_token: bool = False) -> None:
        self._do_stem = do_stem
        self._version = "0.0.5"
        self._char_mapping = {
            "e": "е",
            "ё": "е",
            "o": "о",
            "c": "с",
            "a": "а",
            "k": "к",
            "f1": "ф1"
        }
        self._black_list = black_list
        self._ru_stemmer = RussianStemmer()
        self._en_stemmer = EnglishStemmer()
        self._max_token_length = max_token_length
        self._remove_stop_words = remove_stop_words
        self._special_symbols = string.punctuation + "-–’"
        self._remove_single_letter_token= remove_single_letter_token
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

    def _text_contains_only_vocab(self, text: str, vocab: Set) -> bool:
        for char in text:
            if char not in vocab:
                return False
        return True

    def _remove_emojis(self, text: str) -> str:
        pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            u"\U00002500-\U00002BEF"  # chinese char
            u"\U00002702-\U000027B0"
            u"\U00002702-\U000027B0"
            u"\U000024C2-\U0001F251"
            u"\U0001f926-\U0001f937"
            u"\U00010000-\U0010ffff"
            u"\u2640-\u2642" 
            u"\u2600-\u2B55"
            u"\u200d"
            u"\u23cf"
            u"\u23e9"
            u"\u231a"
            u"\ufe0f"  # dingbats
            u"\u3030"
            "]+", re.UNICODE)
        return re.sub(pattern, '', text)

    def _preprocess(self, text: str) -> str:
        text = text.lower()

        text = self._apply_char_mapping(text)

        tokens = text.split()
        tokens = [token.strip(self._special_symbols) for token in tokens]
        tokens = [token for token in tokens if not token.isdigit()]

        if self._remove_stop_words:
            tokens = [token for token in tokens if token not in self._stopwords]

        if self._do_stem:
            tokens = [self._stem(token) for token in tokens]

        tokens = [token for token in tokens if len(token) <= self._max_token_length]

        if self._black_list:
            tokens = [token for token in tokens if not re.search(self._black_list, token)]

        if self._remove_single_letter_token:
            tokens = [token for token in tokens if len(token) > 1]

        # remove tokens such as 2,/323
        tokens = [token for token in tokens if not self._text_contains_only_vocab(token, vocab=self._special_symbols + string.digits)]

        # Th,.is, выа is,. A te34d,fst! -> This выа is A te34dfst
        # need to keep digits for such cases as f1
        tokens = [token.translate(str.maketrans('', '', self._special_symbols)) for token in tokens]

        tokens = [self._remove_emojis(token) for token in tokens]

        text = " ".join(tokens)

        return text

    def preprocess(self, texts: List[str]) -> List[str]:
        return [self._preprocess(text) for text in texts]