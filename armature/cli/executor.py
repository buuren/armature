import subprocess
import os


class CLIExecutor:
    def __init__(self):
        self.devnull = open(os.devnull, 'w')

    def execute(self, args, cwd, env):

        subprocess.call(
            args=args,
            cwd=cwd,
            env=env,
            stdout=self.devnull,
            stderr=self.devnull
        )


if __name__ == "__main__":
    a = CLIExecutor()
