import click
from utils.config_parser import ConfigParser


load_json_data = ConfigParser(path="/home/vlad/infra/armature/armature/conf/modules.json").return_json()


class PackerConfig:
    def __init__(self):
        self.json_data = load_json_data
        self.binary = "packer"


pass_config = click.make_pass_decorator(PackerConfig, ensure=True)


@click.group()
@pass_config
def cli(config):
    click.echo('Running binary %s' % config.binary)


@cli.command()
@pass_config
def prepare(config):
    """Prepares environment"""
    click.echo('prepare')
    # @sed -i -e 's/^rootpw.*/rootpw $(ROOT_PASSWORD)/g' $(KICKSTART_CONFIG)


@cli.command()
@pass_config
def validate(config):
    """Validate configuration file"""
    click.echo('validate')
    # PACKER_LOG=${PACKER_LOG} ${PACKER_BIN} validate $(PACKER_CONFIG)'


@cli.command()
@pass_config
def build(config):
    """Build virtual machine image"""
    click.echo('build')
    click.echo('Running binary %s' % config.json_data)
    # PACKER_LOG=${PACKER_LOG} ${PACKER_BIN} build $(PACKER_CONFIG)


@cli.command()
@pass_config
def clean(config):
    """Cleanup"""
    click.echo('clean')
    # sed -i -e 's/^rootpw.*/rootpw/g' ${KICKSTART_CONFIG}
