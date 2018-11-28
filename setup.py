import setuptools


with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name = "capncord.py",
    packages = setuptools.find_packages(),
    version = "0.2.1",
    description = "A wrapper for the Capncord API.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = "LyricLy",
    author_email = "gulliverhanson@gmail.com",
    url = "https://github.com/LyricLy/capncord.py",
    keywords = ["wrapper", "capncord", "capncord.py"],
    install_requires = requirements,
    license = "CC0",
    classifiers = [
            "Development Status :: 3 - Alpha",
            "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
            "Intended Audience :: Developers",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3 :: Only",
            "Topic :: Internet",
            "Topic :: Software Development :: Libraries",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Utilities"
    ]
)