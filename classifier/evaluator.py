import re
import pandas as pd

from typing import List
from classifier.imputer import Imputer


class Evaluator:
    def __init__(self, category: str, items: List[str], imputer: Imputer):
        self._category = category
        self._pattern = re.compile(imputer.impute(items), re.IGNORECASE)
        
    def _search(self, text: str):
        return self._pattern.search(text) is not None
    
    def compute_metrics(self, df: pd.DataFrame):
        for category in df.category.unique():
            tmp = df[
                (df.category == category)
                & (df.text.apply(lambda text: self._search(text) == True))
            ]
            
            output = "y_true={y_true:<14} y_pred={y_pred:<14} count_pred={count_pred:.2f}"
            print(output.format(y_true=category, y_pred=self._category, count_pred=len(tmp) / (df.category == category).sum()))
            
    def compute_false_negative(self, df: pd.DataFrame):
        """
        Shows samples where we were not 
        able to match to given category
        """
        return df[
            (df.category == self._category)
            & (df.text.apply(lambda text: self._search(text) == False))
        ]