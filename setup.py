import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="loop-calc",
    version="0.1.0",
    author="Fin Christensen",
    author_email="christensen.fin@gmail.com",
    description="This program evaluates loop programs as described in the lecture 'Grundlagen der theoretischen Informatik 2'.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fin-ger/loop-calc",
    packages=setuptools.find_packages(),
    install_requires=[
        'pyparsing>=2',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [ 'loop-calc = loop:main' ]
    }
)
