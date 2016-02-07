from setuptools import setup

setup(
    name='excelcsv',
    version='0.0.0',
    author='Yuya Unno',
    author_email='unnonouno@gmail.com',
    packages=['excelcsv'],
    tests_require=['nose', 'coverage'],
    test_suite='nose.collector',
)
