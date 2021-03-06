"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

import os
import sys
import logging
import setuptools

PACKAGE_NAME = 'armature'
MINIMUM_PYTHON_VERSION = 3, 6


def check_python_version():
    """Exit when the Python version is too low."""
    if sys.version_info < MINIMUM_PYTHON_VERSION:
        sys.exit("Python {0}.{1}+ is required.".format(*MINIMUM_PYTHON_VERSION))


def read_package_variable(key, filename='__init__.py'):
    """Read the value of a variable from the package without importing."""
    module_path = os.path.join(PACKAGE_NAME, filename)
    with open(module_path) as module:
        for line in module:
            parts = line.strip().split(' ', 2)
            if parts[:-1] == [key, '=']:
                return parts[-1].strip("'")
    logging.warning("'%s' not found in '%s'", key, module_path)
    return None


def build_description():
    """Build a description for the project from documentation files."""
    try:
        readme = open("README.rst").read()
        changelog = open("CHANGELOG.rst").read()
    except IOError:
        return "<placeholder>"
    else:
        return readme + '\n' + changelog


check_python_version()

setuptools.setup(
    name=read_package_variable('__project__'),
    version=read_package_variable('__version__'),

    description="Template for python project",
    url='https://github.com/buuren/project',
    author='John Doe',
    author_email='JohnDoe@gmail.com',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': []},

    long_description=build_description(),
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
    ],

    install_requires=[
        "docopt ~= 0.6.2"
    ]
)
