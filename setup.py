import setuptools

setuptools.setup(
    name="soldexpy",
    version="0.0.2",
    author="leq6c",
    packages=setuptools.find_packages(),
    install_requires=[
        "base58",
        "solders==0.21",
        "solana==0.34.3",
    ],
)

