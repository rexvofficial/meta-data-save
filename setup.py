import os
import re

from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')

def get_version():
    init = open(os.path.join(ROOT, 'mscommonutils', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="meta-data-save-rexvofficial", # Replace with your own username
    version=get_version(),
    author="Rex Varghese",
    author_email="rexvofficial@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rexvofficial/meta-data-save",
    packages=find_packages(exclude=['tests*']),
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    zip_safe=False,
    python_requires='>=3.6',
)
