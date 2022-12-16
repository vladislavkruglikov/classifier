from typing import List
from classifier.imputer import Imputer
from classifier.evaluator import Evaluator
from classifier.constants import RU_CHAR_TO_AUGMENTED_CHARS


def build_imputer() -> Imputer:
    imputer = Imputer(mapper=RU_CHAR_TO_AUGMENTED_CHARS)
    return imputer


def build_evaluator(category: str, items: List[str]) -> Evaluator:
    imputer = build_imputer()
    evaluator = Evaluator(category=category, items=items, imputer=imputer)
    return evaluator
