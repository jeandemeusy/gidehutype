import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="gidehutype",
    version="0.0.1",
    scripts=["bin/gidehutype"],
    author="Jean Demeusy",
    author_email="dev.jdu@gmail.com",
    description="A usefull type system for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=["gidehutype"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)