'''
This is the BoxEd package. It provides temporary file editing support.
'''

from setuptools import find_packages, setup

setup(
    name='boxed',
    author='Pythocrates',
    author_email='23015037+Pythocrates@users.noreply.github.com',
    url='https://github.com/Pythocrates/BoxEd',
    description=__doc__,

    use_scm_version=True,
    setup_requires=['setuptools_scm>=3.3.3'],
    packages=find_packages(),
    install_requires=[
    ],

    entry_points={
    },

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT',
        'Operating System :: OS Independent',
    ],
)
