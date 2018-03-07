import click
from modules.executor import Executor
from utils.config_parser import ConfigParser

json_data = ConfigParser(
    path="/home/vlad/infra/armature/armature/conf/modules.json"
).return_json()

MODULE = "packer"


@click.group()
def cli():
    pass


@cli.command()
def prepare_template():
    """Validate configuration file"""
    click.echo('prepare_template')

    with Executor(module=MODULE, cli="prepare_template") as cli_executor:
        cli_executor.run(
            cli="prepare_template",
            use_docker_run_wrapper=True
        )


@cli.command()
def validate_template():
    """Validate configuration file"""
    click.echo('validate_template')

    with Executor(module=MODULE, cli="validate_template") as cli_executor:
        cli_executor.run(
            cli="validate_template",
            use_docker_run_wrapper=True
        )


@cli.command()
def build_template():
    """Build virtual machine image"""
    click.echo('build')
    # PACKER_LOG=${PACKER_LOG} ${PACKER_BIN} build $(PACKER_CONFIG)


@cli.command()
def clean():
    """Cleanup"""
    click.echo('clean')