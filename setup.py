from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(


    name="pythorn",
    version="1.0.0",
    description="A Python module for all data structures and algorithms.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/robin025/pythorn",
    author="Robin Singh",
    author_email="robin25tech@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Education ",
        "Intended Audience :: Developers ",

        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Natural Language :: English",
        "Operating System :: OS Independent"

    ],
    packages=find_packages(),
    include_package_data=True,
)
