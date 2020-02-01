import click
from typing import Callable, Union, List

from post import Post
from sanitize import Sanitize


class CommandLine:
    def __init__(self, url: str, bad_chars: Union[List[str], str]):
        self.command: Callable = self._define_click_command(url, bad_chars)

    @staticmethod
    def _define_click_command(url, bad_chars) -> Callable:
        """ returns a click_command function """
        prompt = click.style(' Type your text for sending to the endpoint \n', bold=True, bg='green', fg='yellow')

        @click.command()
        @click.option('-s', '--string', type=str, prompt=prompt, help='The data(string) for sending to the endpoint')
        @click.option('-r', '--remove', is_flag=True, help='Passing -r removes all html tag, otherwise escapes them')
        def command(string, remove):
            message: str = 'you choose to remove entire html tag' if remove else 'you choose to scape html tag'
            click.secho(message, bg='black', fg='yellow')

            sanitize = Sanitize(string, remove, bad_chars)
            post = Post(url, sanitize.string)
            if post.success:
                click.secho(f'Request sent successfully. response is:', bg='black', fg='green')
            else:
                click.secho(f'Failure on receiving response. status code of response is:', bg='black', fg='red')
            click.echo(f'{post.response}')
        return command