import os
from setuptools import setup


def read(name):
    return open(os.path.join(os.path.dirname(__file__), name)).read()


setup(
    name='excelcsv',
    version='0.0.0',
    description='excelcsv: CSV utility for Excel',
    long_description=read('README.md'),
    author='Yuya Unno',
    author_email='unnonouno@gmail.com',
    url='https://github.com/unnonouno/excelcsv',
    license='MIT',
    packages=['excelcsv'],
    tests_require=['nose', 'coverage'],
    test_suite='nose.collector',
)
