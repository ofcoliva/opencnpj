from setuptools import setup

setup(
    name="opencnpj",
    version="0.0.1",
    license="MIT License",
    author="ofcoliva",
    long_description="Repository with more instructions available at: https://github.com/ofcoliva/opencnpj",
    long_description_content_type="text/markdown",
    author_email="ofcoliva@gmail.com",
    keywords="opencnpj api cnpj",
    packages=["opencnpj"],
    install_requires=["requests", "pip_system_certs"]
)