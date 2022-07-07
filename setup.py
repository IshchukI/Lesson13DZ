#!/usr/bin/env python
import io

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with io.open("requirements.txt") as f:
    required = f.read().splitlines()

with io.open("Readme.md", encoding="utf-8") as f:
    long_description = f.read()

def main():
    setup(
        name='mypackage-name',
        version='1.0',
        description='My Package Description',
        long_description=long_description,
        long_description_content_type="text/markdown",
        url='https://github.com/tishyk/mypackage-install/tree/master',
        author='Sergii Tishchenko',
        author_email='contact@demo.com',
        packages=['doc_analyzer',
                  'doc_analyzerpdf_analyzer'],
        install_requires=required,
        include_package_data=True,
        keywords="mypackage for product test",

    )


if __name__ == '__main__':
    main()
