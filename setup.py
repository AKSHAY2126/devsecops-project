from setuptools import setup, find_packages

setup(
    name="devsecops-app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Flask==2.3.3",
    ],
)