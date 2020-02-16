import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Jhash-pkg-ModdingNinja",
    version="1.0.0",
    author="Jaide Evans",
    author_email="jaevans300@gmail.com",
    description="A dumb little encryption module made originally as a joke between me and my friend",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ModdingNinja/Jhash-Encryption",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)