from setuptools import setup, find_packages

with open("documentation/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='TheDoctor',
    version='1.0',
    author='Mariia Katsala',
    author_email='ubuntovka@gmail.com',
    packages=find_packages(),
    description='This is a project of the "TheDoctor" clinic.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Ubuntovka/TheDoctor',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "app"},
    python_requires=">=3.8",
)
