from setuptools import setup

setup(
    name="opencnpj",
    version="0.0.1",
    license="MIT License",
    author="ofcoliva",
    description="Wrapper para a API OpenCNPJ",
    long_description="Repository with more instructions available at: https://github.com/ofcoliva/opencnpj",
    long_description_content_type="text/markdown",
    url="https://github.com/ofcoliva/opencnpj",
    author_email="ofcoliva@gmail.com",
    keywords="opencnpj api cnpj",
    packages=["opencnpj"],
    install_requires=["requests", "pip_system_certs", "pydantic"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)