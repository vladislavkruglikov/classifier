import pytest

from classifier.preprocessor import Preprocessor


preprocessor = Preprocessor(do_stem=True, remove_stop_words=True, black_list=r"\b.*id.*\b")


@pytest.mark.parametrize(
    "text, expected", [
        ("привет", "привет"),
        ("привет, как дела?", "привет дел"),
        ("ты красивый", "красив"),
        ("ну был крутой!", "крут"),
        ("что за tokenid интересный", "интересн")
    ]
)
def test_preprocessor(text: str, expected: str) -> None:
    assert preprocessor._preprocess(text) == expected