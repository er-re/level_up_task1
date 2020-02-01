import click
from typing import Callable, Union, List

from command_line import CommandLine


class Main:
    def __init__(self, url: str, bad_chars:  Union[List[str], str]) -> None:
        command: Callable = CommandLine(url, bad_chars).command
        try:
            command()
        except Exception as e:
            print(e)
            click.secho('Some error happened. please try again', bg='black', fg='red')


if __name__ == '__main__':
    bad_chars = ['!~@#$%^&*']
    url = 'https://jsonplaceholder.typicode.com/posts'
    Main(url, bad_chars)





