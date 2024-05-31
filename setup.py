from setuptools import setup, find_packages

setup(
    name='wcn',
    version='0.1',
    description='That is about for create a wcn(wcoins) network.',
    author='WTech',
    author_email='wangtry3417@gmail.com',
    packages=find_packages(),
    license='MLT',
    license_files=('LICENSE'),
    install_requires=[
        'cryptography',
        'requests',
        'random2',
    ],
)
