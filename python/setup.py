# shaml/python/setup.py
from setuptools import setup, find_packages

setup(
    name='shaml',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[],
    author='Ghazi Khan',
    author_email='hello@mgks.dev',
    description='A shameless library for auto-correcting variable types.',
    long_description=open('../README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mgks/shaml',
    license='MIT',
)