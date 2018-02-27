import click
import os


class CLIScan(click.MultiCommand):
    def __init__(self, module_path):
        self.module_path = module_path
        super().__init__(self)

    def list_modules(self):
        modules = []
        for filename in os.listdir(self.module_path):
            if filename.endswith('.py'):
                modules.append(filename[:-3])
        modules.sort()
        return modules

    def list_commands(self, ctx):
        return self.list_modules()

    def get_command(self, ctx, name):
        if name in self.list_modules():
            ns = {}
            fn = os.path.join(self.module_path, name + '.py')

            with open(fn) as f:
                code = compile(f.read(), fn, 'exec')
                eval(code, ns, ns)
            return ns['cli']
