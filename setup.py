from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='TeXicode',
    version='1.0.3',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    entry_points={
        'console_scripts': [
            'txc=texicode.main:main',
        ],
    },
    install_requires=[
        # List your dependencies here
    ],
    long_description=description,
    long_description_content_type="text/markdown",
)
