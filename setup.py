from setuptools import setup, find_packages

setup(
    name='simpleagent',
    version='0.0.1',
    packages=find_packages(),
    description='A simple framework for using agents with LLMs',
    author='Tyler Suard',
    author_email='tyler suard at g mail',
    install_requires=[
        'openai'
    ]
)
