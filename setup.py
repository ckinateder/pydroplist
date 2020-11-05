import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="supreme-community-ckinateder", # Replace with your own username
    version="0.0.1",
    author="Calvin Kinateder",
    author_email="calvinkinateder@gmail.com",
    description="A python module to grab data from supremecommunity.com and list drop products",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ckinateder/supreme-community",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)