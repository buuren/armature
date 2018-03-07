import os
from utils.config_parser import ConfigParser
from subprocess import Popen, PIPE


class Executor:
    def __init__(self, module: str, cli: str):
        self.current_env = os.environ.copy()
        self.json_data = ConfigParser(
            path="/home/vlad/infra/armature/armature/conf/modules.json"
        ).return_json()

        self.module = module
        self.cli = cli
        self.module_data = self.json_data['modules'][module]

    def __enter__(self):
        self.dependency_handler(step="before")
        return self

    def __exit__(self, type, value, traceback):
        self.dependency_handler(step="after")
        return self

    def dependency_handler(self, step: str):
        if step in self.module_data['cli'][self.cli] and self.module_data['cli'][self.cli]:
            for dependency in self.module_data['cli'][self.cli][step]:
                print("running dependency %s" % dependency)

                with Executor(module=self.module, cli=dependency) as dependency_executor:
                    dependency_executor.run(
                        cli=dependency,
                        use_docker_run_wrapper=True
                    )
        return self

    def render_variables(self, str_in: str) -> str:
        return str_in.format(**self.json_data['variables'])

    def get_docker_run_wrapper(self) -> str:
        return '{0}'.format(
            self.render_variables(self.json_data['docker_run_wrapper'])
        )

    def get_cmd_args(self, cli: str) -> str:
        cmd_args = 'cd {cwd} && {args}'.format(
            cwd='/home/vlad/infra/' + self.module_data['cli'][cli]['cwd'],
            args=self.render_variables(self.module_data['cli'][cli]['args'])
        )

        return cmd_args

    def get_cmd(self, cli: str, use_docker_run_wrapper: bool = False) -> str:
        cmd_args = self.get_cmd_args(cli)

        cmd = '{docker_wrapper} {args}'.format(
            docker_wrapper=self.get_docker_run_wrapper() if use_docker_run_wrapper else '',
            args=cmd_args if not use_docker_run_wrapper else '"{0}"'.format(cmd_args)
        )
        print("cmd -> [%s]" % cmd)
        return cmd

    def run(self, cli: str, use_docker_run_wrapper: bool = False) -> None:
        with Popen(args=self.get_cmd(cli, use_docker_run_wrapper), stdout=PIPE, bufsize=1,
                   universal_newlines=True, shell=True) as process:
            for line in process.stdout.readlines():
                print(line, end='')

        rc = process.poll()
        print(rc)



if __name__ == '__main__':
    pass
