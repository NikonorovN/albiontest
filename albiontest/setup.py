from setuptools import setup, find_packages

version = '1.0.0'

setup(
    name='albiontest',
    version=version,
    packages=find_packages(),
    install_requires=[
        'Django==2.2.2',
        'm3-django-compat==1.9.2',
        'm3-objectpack==2.2.47',
    ],
    scripts=["manage.py"]
)