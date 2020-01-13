from setuptools import setup, find_packages

import crawlab.config

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='crawlab-sdk',
    version=crawlab.config.VERSION,
    packages=find_packages(),
    url='https://github.com/crawlab-team/crawlab-sdk',
    license='BSD-3-Clause',
    author='tikazyq',
    author_email='tikazyq@163.com',
    description='Python SDK for Crawlab',
    long_description=long_description,
    scripts=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'Click==7.0',
        'requests==2.22.0',
        'prettytable==0.7.2',
        'scrapy==1.8.0',
        'pymongo==3.10.1',
    ],
    entry_points={
        'console_scripts': [
            'crawlab=crawlab:main'
        ]
    }
)
