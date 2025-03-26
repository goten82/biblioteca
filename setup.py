from setuptools import setup, find_packages

setup(
    name="biblioteca",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click>=7.0",
        "requests>=2.22.0",
        "python-dateutil>=2.8.1",
        "pyyaml>=5.1",
    ],
    entry_points={
        "console_scripts": [
            "biblioteca=biblioteca.cli:main",
        ],
    },
    author="Giuseppe Ninniri",
    author_email="goten.ninniri@gmsail.com",
    description="A library management system",
    long_description=open("readMe.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/goten82/biblioteca",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
