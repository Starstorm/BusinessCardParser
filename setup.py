from distutils.core import setup

setup(
    name='BusinessCardParser',
    version='1.0.0',
    install_requires=['names_dataset', 'spacy'],
    long_description=open('README.md').read(),
)
