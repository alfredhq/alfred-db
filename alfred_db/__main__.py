import os
import yaml
from argparse import ArgumentParser
from inspect import isfunction, getargspec

from alembic import command, util
from alembic.config import Config


DIR = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))
MIGRATIONS_DIR = os.path.join(DIR, 'migrations')


def get_alfred_config(path):
    with open(path) as file:
        config = yaml.load(file)
    return {key.upper(): value for key, value in config.items()}


def get_alembic_config(url):
    config_path = os.path.join(MIGRATIONS_DIR, 'alembic.ini')
    config = Config(config_path)
    config.set_main_option('script_location', MIGRATIONS_DIR)
    config.set_main_option('sqlalchemy.url', url)
    return config


def add_arguments(parser, positional, kwargs):
    if 'message' in kwargs:
        parser.add_argument('-m', '--message',
            type=str,
            help="Message string to use with 'revision'",
        )
    if 'sql' in kwargs:
        parser.add_argument('--sql',
            action='store_true',
            help=(
                "Don't emit SQL to database - dump to standard output/file "
                "instead"
            ),
        )
    if 'tag' in kwargs:
        parser.add_argument('--tag',
            type=str,
            help="Arbitrary 'tag' name'"
        )
    if 'autogenerate' in kwargs:
        parser.add_argument('--autogenerate',
            action='store_true',
            help=(
                'Populate revision script with candidate migration '
                'operations, based on comparison of database to model'
            )
        )

    positional_help = {
        'revision': 'revision identifier',
    }
    for arg in positional:
        parser.add_argument(arg, help=positional_help.get(arg))


def main():
    parser = ArgumentParser()

    parser.add_argument('-c', '--config',
        type=str,
        required=True,
        help='Path to the Alfred config',
    )

    subparsers = parser.add_subparsers()

    for name in dir(command):
        if name.startswith('_') or name in ('init', 'list_templates'):
            continue

        func = getattr(command, name)
        if not isfunction(func) or func.__module__ != 'alembic.command':
            continue

        spec = getargspec(func)
        if spec.defaults:
            positional = spec.args[1:-len(spec.defaults)]
            kwargs = spec.args[-len(spec.defaults):]
        else:
            positional = spec.args[1:]
            kwargs = []

        subparser = subparsers.add_parser(func.__name__, help=func.__doc__)
        add_arguments(subparser, positional, kwargs)
        subparser.set_defaults(cmd=(func, positional, kwargs))

    args = parser.parse_args()
    func, positional, kwargs = args.cmd

    alfred_config = get_alfred_config(args.config)
    alembic_config = get_alembic_config(alfred_config['DATABASE_URI'])
    func_args = [getattr(args, k) for k in positional]
    func_kwargs = {k: getattr(args, k) for k in kwargs}
    try:
        func(alembic_config, *func_args, **func_kwargs)
    except util.CommandError as e:
        util.err(str(e))


if __name__ == '__main__':
    main()
