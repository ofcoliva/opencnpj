from setuptools import setup

with open ("README.md", "r") as f:  readme = f.read()

setup(
    version="0.0.1",
    license="MIT License",
    author="ofcoliva",
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email="ofcoliva@gmail.com",
    keywords="opencnpj api cnpj",
    packages=["opencnpj"],
    install_requires=["requests", "pip-system-certs"]
)