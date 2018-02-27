"""Do nothing, but document it.

No, really, it doesn't do anything.
"""
import os
from cli.scan import CLIScan
from utils.logger import LoggingHandler


if __name__ == '__main__':
    # log = LoggingHandler(name=__name__).log
    # log.info("")
    module_path = os.path.join(os.path.dirname(__file__), 'modules')

    cliscan = CLIScan(module_path=module_path)
    cliscan()
