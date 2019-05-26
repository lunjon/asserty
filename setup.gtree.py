import setuptools
import gtree


long_description = """
Gtree is a general tree implementation that provides a simple (and quite limited) API.

One of the more useful features is the functionality that allows one to build trees from dictionaries.

See examples at the github page for more information!
"""

setuptools.setup(
    name="gtree",
    version=gtree.version,
    description="A general tree implementation providing convinient methods for defining trees in JSON or YAML files.",
    long_description=long_description,
    url="https://github.com/lunjon/gtree",
    author="Jonathan Lundholm",
    author_email="jon.lundholm@gmail.com",
    license="MIT",
    packages=["gtree"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)