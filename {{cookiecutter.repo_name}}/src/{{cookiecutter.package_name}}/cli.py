"""Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -m{{cookiecutter.package_name}}` python will execute
    ``__main__.py`` as a script. That means there will not be any
    ``{{cookiecutter.package_name}}.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there"s no ``{{cookiecutter.package_name}}.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
{%- if cookiecutter.command_line_interface == "click" %}

import click
{%- elif cookiecutter.command_line_interface == "argparse" %}

import argparse
{%- else %}

import sys
{%- endif %}

from .{{ cookiecutter.module_name }} import {{ cookiecutter.function_name }}
{%- if cookiecutter.command_line_interface == "click" %}


@click.command()
@click.argument("names", nargs=-1)
def run(names):
    """Print the result of the computation.

    Args:
        names (list): List of arguments.

    Returns:
        int: A return code.

    """
    click.echo({{ cookiecutter.function_name }}(names))
{%- elif cookiecutter.command_line_interface == "argparse" %}

parser = argparse.ArgumentParser(description="Command description.")
parser.add_argument(
    "names",
    metavar="NAME",
    nargs=argparse.ZERO_OR_MORE,
    help="A name of something.",
)


def run(args=None):
    """Print the result of the computation.

    Args:
        args (list): List of arguments.

    Returns:
        int: A return code.

    Example:
        >>> run(["1", "2", "3"])
        1
        0

    """
    args = parser.parse_args(args=args)
    print({{ cookiecutter.function_name }}(args.names))
    return 0
{%- else %}


def run(argv=sys.argv):
    """Print the result of the computation.

    Args:
        argv (list): List of arguments.

    Returns:
        int: A return code.

    Example:
        >>> run(["1", "2", "3"])
        1
        0

    """
    print({{ cookiecutter.function_name }}(argv))
    return 0
{%- endif %}
