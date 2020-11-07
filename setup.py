import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydroplist",
    version="1.0.1",
    author="Calvin Kinateder",
    author_email="calvinkinateder@gmail.com",
    description="A python module to grab data from droplists online and list products on the next drop, given the brand being searched for.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ckinateder/supreme-community",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)