import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

    name="async-sgc",

    version="0.0.1",

    author="tuna21345",

    author_email="ryo816816816@gmail.com",

    description="discord sgc pack",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="https://github.com/tuna2134/async-sgc",

    packages=setuptools.find_packages(),

    classifiers=[

        "Programming Language :: Python :: 3.7",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

    install_requires=[

        "discord.py >= 1.3.3",

    ],
