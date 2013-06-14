import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="gerrit",
    version='0.0.1',
    author="Flavio Percoco",
    author_email="flaper87@flaper87.org",
    description=("Gerrit SSH Lib"),
    license="BSD",
    url="https://github.com/FlaPer87/python-gerrit",
    packages=find_packages('.'),
    include_package_data=True,
    long_description=read('README.md'),
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    scripts=[],
    platforms=['Any'],
    install_requires=['distribute', 'paramiko'],
    entry_points={},
)
