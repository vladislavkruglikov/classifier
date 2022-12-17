import re
import pandas as pd

from tqdm import tqdm
from typing import Tuple, List, Dict


class Voter:
    def __init__(self, category_to_items: Dict[str, List[str]], default_category: str, default_rank: int):
        self._default_rank = default_rank
        self._default_category = default_category
        self._category_to_items = category_to_items
        
    def _vote(self, text: str) -> Tuple[str, int]:
        for rank, pairs in enumerate(zip(*[
            [(category, item) for item in items] for category, items in self._category_to_items.items()
        ]), start=1):
            for category, item in pairs:
                match = re.search(fr"\b{item}\b", text, re.IGNORECASE)
                if match:
                    return category, rank

        return self._default_category, self._default_rank
        
    def vote(self, df: pd.DataFrame):
        results = [self._vote(text) for text in tqdm(df.text)]
        ranks = [result[1] for result in results]
        categories = [result[0] for result in results]
        df["category_predicted"] = categories
        df["category_predicted_rank"] = ranks
        return df