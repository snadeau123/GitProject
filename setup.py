from setuptools import setup, find_packages

setup(
    name='gitproject',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'gitpython',
        'termcolor'
    ],
    entry_points={
        'console_scripts': [
            'gitproject=gitproject.main:main'
        ]
    },
    description='A Python tool for managing and synchronizing multiple Git repositories within a project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/snadeau123/GitProject',
    author='Sebastien Nadeau',
    author_email='snadeau@breakingwalls.ca',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Version Control :: Git',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='git version-control project-management',
)