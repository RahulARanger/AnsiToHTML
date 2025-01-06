from typing import Dict
from ansitohtml.theme import DEFAULT
import pytest


@pytest.mark.parametrize("theme", (DEFAULT, ))
def test_all_presence_of_keys(theme: Dict[int, str]):
    # 8 color codes
    for _ in range(30, 37):
        assert _ in theme

    # 16 color codes
    for _ in range(90, 97):
        assert _ in theme
