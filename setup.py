# Copyright (c) 2013 python-gerrit Developers.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages


setup(
    name="python-gerrit",
    version='0.0.1',
    author="Flavio Percoco",
    author_email="flaper87@flaper87.org",
    description=("Gerrit SSH Lib"),
    license="Apache License v2",
    url="https://github.com/FlaPer87/python-gerrit",
    packages=find_packages('.'),
    package_data={'': ['LICENSE', 'README.md']},
    include_package_data=True,
    long_description=open('README.md').read(),
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    scripts=[],
    platforms=['Any'],
    install_requires=['distribute', 'paramiko'],
    entry_points={},
)
