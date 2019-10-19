from setuptools import setup

setup (
    name = "jichu",
    version = "0.0.1",
    description = "Infura for Fetch.AI.",
    license = "Apache License 2.0",
    packages = ["jichu"],
    install_requires = ["fetchai-ledger-api==0.9.0a2", "flask", "pytest"],
    author = "Theo Turner",
    author_email = "theo@turner.se",
    keywords = ["blockchain", "infura", "fetch.ai", "fetchai", "crypto", "cryptocurrency", "hosted", "node"],
    url = "https://github.com/theoturner/jichu",
    classifiers = [
        "Development Status :: 1 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]
)