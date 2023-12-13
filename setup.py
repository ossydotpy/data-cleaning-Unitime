from setuptools import setup, find_packages

setup(
    name="unitime-cleaner",
    version="0.1.0",
    author="Osman Ali",
    author_email="mrali.osman.6@gmail.com",
    description="script for cleaning the raw data output of Unitime into a standard that the explorer accepts.",
    packages=find_packages(),
    install_requires=["pandas"],
    entry_points={
        "console_scripts": [
            "clean=clean.main:main"
        ]
    }
)
