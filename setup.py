import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

    name="async-sgc",

    version="0.0.1",

    author="1ntegrale9",

    author_email="1ntegrale9uation@gmail.com",

    description="discord sgc pack",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="https://github.com/DiscordBotPortalJP/dispander",

    packages=setuptools.find_packages(),

    classifiers=[

        "Programming Language :: Python :: 3.7",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

    install_requires=[

        "discord.py >= 1.3.3",

    ],

)