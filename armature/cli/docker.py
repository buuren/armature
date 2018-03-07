import click
from modules.executor import Executor


MODULE = "docker"


@click.group()
def cli():
    pass


@cli.command()
def build_dev_tools():
    """Build dev_tools docker image"""
    click.echo('build_dev_tools')

    cli_executor.run(
        cli="build_dev_tools"
    )

@cli.command()
def exec(config):
    """Validate configuration file"""
    click.echo('validate')



@cli.command()
def run(config):
    """Build virtual machine image"""
    click.echo('build')


@cli.command()
def clean(config):
    """Cleanup"""
    click.echo('clean')
