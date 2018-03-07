"""Do nothing, but document it.

No, really, it doesn't do anything.
"""
import os
from modules.cli_scan import CLIScan

if __name__ == '__main__':
    module_path = os.path.join(os.path.dirname(__file__), 'cli')
    cliscan = CLIScan(cli_path=module_path)
    cliscan()
