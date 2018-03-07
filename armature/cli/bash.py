import click
from modules.executor import Executor


MODULE = "bash"
cli_executor = Executor(module=MODULE)


@click.group()
def cli():
    pass


@cli.command()
def spawn_shell():
    """Build dev_tools docker image"""
    click.echo('spawn_shell')

    cli_executor.run(
        cli="spawn_shell",
        use_docker_run_wrapper=True
    )
