import click
from bs4 import BeautifulSoup
from markdown import markdown
import requests
from typing import Callable
from typing import Union, List


class CLIApp:
    """a command line app which send a string to the provided endpoint with a post request and shows it's responses."""

    def __init__(self, url: str) -> None:
        self.url: str = url
        self.response: str
        self.status_code: int
        self.cli: Callable = self.define_click_cli_function()
        try:
            self.cli()
        except Exception as e:
            print(e)
            click.secho('Some error happened. please try again', bg='black', fg='red')
            return

    def define_click_cli_function(self) -> Callable:
        """
        :return: a click_module function
        Click_module for implementing each command needs to declare a function using some decorators.
        this function (which would be interpreted as a cli Command) has implemented sending request to the endpoint
        It receives a parameter for choosing between removing entire html tag or escaping them.
        """
        prompt = click.style(' Type your text for sending to the endpoint \n', bold=True, bg='green', fg='yellow')

        @click.command()
        @click.option('-s', '--string', type=str, prompt=prompt, help='The data(string) for sending to the endpoint')
        @click.option('-r', '--remove', is_flag=True, help='Passing -r removes all html tag, otherwise escapes them')
        def command(string, remove):
            click.echo(string)
            if remove:
                click.secho('you choose to remove entire html tag', bg='black', fg='yellow')
                string = self.sanitize_html_by_removing_entire_tag(string)
            else:
                click.secho('you choose to scape html tag', bg='black', fg='yellow')
                string = self.sanitize_html_by_scape(string)

            string = self.sanitize_markdown(string)
            string = self.remove_unfavorable_character(string, ['!@#$%^&*~`'])

            self.send_request(string)
            if self.status_code == 201:
                click.secho(f'Request sent successfully. response is:', bg='black', fg='green')
                click.echo(f'{self.response}')
            else:
                click.secho(f'Failure on receiving response. status code of response is: \n {self.status_code}', bg='black', fg='red')
        return command

    def sanitize_markdown(self, string: str) -> str:
        """
        :param string: input string
        :return: sanitizes all markdown element like ## (Header 2) and returns pure text itself
        """
        html = markdown(string)
        return self.sanitize_html_by_removing_entire_tag(html)

    @staticmethod
    def sanitize_html_by_scape(string: str) -> str:
        """
        :param string: input string
        :return: This replaces every instance of &, ', ", <, and > with their correct HTML escape codes
        """
        escapes = {'\"': '&quot;',
                   '\'': '&#39;',
                   '<': '&lt;',
                   '>': '&gt;'}
        # This is done first to prevent escaping other escapes.
        text = string.replace('&', '&amp;')
        for seq, esc in escapes.items():
            text = text.replace(seq, esc)
        return text

    @staticmethod
    def sanitize_html_by_removing_entire_tag(string: str) -> str:
        """
        :param string: input string
        :return: sanitizes all html tag like <span> and returns pure text itself
        """
        text = BeautifulSoup(string,  "html.parser").text
        return text

    @staticmethod
    def remove_unfavorable_character(string: str, unfavorable_chars: Union[List[str], str]) -> str:
        """
        :param string: input string
        :param unfavorable_chars: list or joined of unfavorable_chars like !@#$%^^@
        :return: inputted string which has no unfavorable_chars in it
        """
        if isinstance(unfavorable_chars, str):
            unfavorable_chars = list(unfavorable_chars)
        for char in unfavorable_chars:
            string = string.replace(char, "")
        return string

    def send_request(self, string: str) -> None:
        """
        :param string: input string
        :return: None, it only assign corresponding value to the instances attribute.
        status_code and responses text of posted request
        """
        response = requests.post(self.url, string)
        self.status_code = response.status_code
        self.response = response.text


if __name__ == '__main__':
    # mock_url = 'https://my-json-server.typicode.com/er-re/jsonplaceholder/posts'
    mock_url = 'https://jsonplaceholder.typicode.com/posts'
    CLIApp(mock_url)


