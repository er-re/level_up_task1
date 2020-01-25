A python Command line app which posts a string to the provided endpoint using post request
=======


This scripts uses 'Click' python package which is for creating beautiful command line interfaces.

more about click:

Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. It’s the “Command Line Interface Creation Kit”. It’s highly configurable but comes with sensible defaults out of the box.

[click official website](https://click.palletsprojects.com/en/7.x/)


## For using this app:

* open a command-line or terminal and then go to the script directory

* type `python cli_app.py` and then enter

## more about functionality:

*This app by default removes all markdown elements.*

*It also removes some unfavorable characters from the string like '@#$!%^&~'.*

*But it give you an option for escaping the html tag or removing entire tag and remaining only inner text of them.*

*This functionality was handled by '--remove' or '-r' flag which you should passing it when you want to removing entire html tag, otherwise by default it escapes them*

*Type  `python cli_app.py --help` for viewing the builtin cli help*
