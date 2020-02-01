from bs4 import BeautifulSoup
from typing import Union, List


class Sanitize:
    def __init__(self, string:str, remove_html: bool, bad_chars: Union[List[str], str]) -> None:
        string = self._remove_html(string) if remove_html else self._scape_html(string)
        self.string = self._remove_markdown_and_bad_chars(string, bad_chars)

    @staticmethod
    def _scape_html(string: str) -> str:
        """ replacing every instance of &, ', ", <, and > with their correct HTML escape codes"""
        escapes = {'\"': '&quot;', '\'': '&#39;', '<': '&lt;', '>': '&gt;'}
        text = string.replace('&', '&amp;')
        for seq, esc in escapes.items():
            text = text.replace(seq, esc)
        return text

    @staticmethod
    def _remove_html(string: str) -> str:
        """ removing entire html tag and returning only inner text itself """
        return BeautifulSoup(string, "html.parser").text

    @staticmethod
    def _remove_markdown_and_bad_chars(string: str, bad_chars: Union[List[str], str]) -> str:
        if isinstance(bad_chars, str):
            bad_chars = list(bad_chars)
        bad_chars = bad_chars + list('\\`*_{}[]()#+-!')
        for char in bad_chars:
            string = string.replace(char, "")
        return string

