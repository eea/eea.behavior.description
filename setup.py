""" eea.behavior.description Installer
"""
import os
from os.path import join
from setuptools import setup, find_packages

NAME = 'eea.behavior.description'
PATH = NAME.split('.') + ['version.txt']
VERSION = open(join(*PATH)).read().strip()

setup(
    name=NAME,
    version=VERSION,
    description="An add-on for Plone",
    long_description_content_type="text/x-rst",
    long_description=(
        open("README.rst").read() + "\n" +
        open(os.path.join("docs", "HISTORY.txt")).read()
    ),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='EEA Add-ons Plone Zope',
    author='European Environment Agency: IDM2 A-Team',
    author_email='eea-edw-a-team-alerts@googlegroups.com',
    url='https://github.com/eea/eea.behavior.description',
    license='GPL version 2',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['eea', 'eea.behavior'],
    include_package_data=True,
    zip_safe=False,
        python_requires="==2.7",
        install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
    ],
    extras_require={
        'test': [
            'plone.app.testing',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """
)
