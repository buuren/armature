import click

'''

export VAGRANT_HOME = $(shell pwd)/vagrant/home
export VAGRANT_TOOLS = $(shell pwd)/vagrant/tools
export VAGRANT_ENV = $(shell pwd)/vagrant/env

PACKER_LOG = 0
VAGRANT_LOG = 0
IMAGE_NAME = centos7
IMAGE_ARCH = x86_64
IMAGE_FORMAT = raw
ARTIFACTS_DIR = $(shell pwd)/artifacts

SHELL = /bin/bash
PACKER_CONFIG = $(shell pwd)/packer/templates/$(IMAGE_NAME).json
ROOT_PASSWORD =  $(shell jq '.variables.ssh_password' $(PACKER_CONFIG) | sed -e 's/"//g')
KICKSTART_CONFIG = $(shell pwd)/packer/http/$(IMAGE_NAME)-kickstart.cfg
ARTIFACT_NAME = $(ARTIFACTS_DIR)/$(IMAGE_NAME)-$(IMAGE_ARCH).$(IMAGE_FORMAT)


help:
	@echo -e "$$PROJECT_HELP_MSG"

packer: packer-prepare packer-validate packer-build packer-clean
upload: packer packer-upload
vagrant:  vagrant-clean vagrant-convert vagrant-box vagrant-init vagrant-post

packer-prepare:
	rm -rf artifacts
	@sed -i -e 's/^rootpw.*/rootpw $(ROOT_PASSWORD)/g' $(KICKSTART_CONFIG)

packer-validate:
	PACKER_LOG=${PACKER_LOG} ${PACKER_BIN} validate $(PACKER_CONFIG)

packer-build:
	PACKER_LOG=${PACKER_LOG} ${PACKER_BIN} build $(PACKER_CONFIG)

packer-clean:
	sed -i -e 's/^rootpw.*/rootpw/g' ${KICKSTART_CONFIG}
	rm -rf packer_cache

packer-upload:
	echo ToDo

vagrant-convert:
	cd ${ARTIFACTS_DIR} && \
	qemu-img convert -f raw -O qcow2 $(IMAGE_NAME)-$(IMAGE_ARCH).raw $(IMAGE_NAME)-$(IMAGE_ARCH).qcow2 && \
	mv $(IMAGE_NAME)-$(IMAGE_ARCH).qcow2 $(VAGRANT_TOOLS)/box.img

vagrant-box:
	cd $(VAGRANT_TOOLS) && \
	tar cvzf $(IMAGE_NAME).box ./metadata.json ./Vagrantfile ./box.img && \
	vagrant plugin install vagrant-libvirt && \
	vagrant box add --name $(IMAGE_NAME) $(IMAGE_NAME).box --provider=libvirt --force

vagrant-init:
	rm -rf $(VAGRANT_ENV)/*
	cp packer/keys/* $(VAGRANT_ENV)
	cd $(VAGRANT_ENV) && vagrant init $(IMAGE_NAME)

vagrant-clean:
	rm -f $(VAGRANT_TOOLS)/box.img
	rm -rf $(VAGRANT_ENV)/*
	rm -rf $(VAGRANT_HOME)/*

vagrant-post:
	@echo -e "$$VAGRANT_SETUP"

.PHONY: packer upload vagrant help

#MAKECMDGOALS
'''


class VagrantWrapper:
    def __init__(self, terraform):
        self.envs: dict = {
            "VAGRANT_HOME": "$(shell pwd) / vagrant / home",
            "VAGRANT_TOOLS": "$(shell pwd) / vagrant / tools",
            "VAGRANT_ENV": "$(shell pwd) / vagrant / env"
        }

        self.options: dict = {
            "VAGRANT_LOG": "0"
        }
        pass


@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))


@cli.command()
def sync():
    click.echo('Synching')