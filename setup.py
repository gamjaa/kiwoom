from setuptools import setup, find_packages


# Project Information
VERSION = "0.1.0"
DISTNAME = "kiwoom"
DESCRIPTION = "Simple Python Wrapper for Kiwoom OPEN API+"
LONG_DESCRIPTION = open("README.md", encoding="utf-8").read()
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'
URL = "https://github.com/breadum/kiwoom"
DOWNLOAD_URL = "https://pypi.org/project/kiwoom"
PROJECT_URLS = {
    "Git": "https://github.com/breadum/kiwoom",
    "Tutorials": "https://github.com/breadum/kiwoom/tree/main/tutorials"
}

# Author Information
AUTHOR = "Breadum"
EMAIL = "breadum.kr@gmail.com"

# Miscellaneous
LICENSE = "MIT License"
CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "License :: OSI Approved :: MIT License",
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Topic :: Office/Business :: Financial :: Investment"
]


def setup_package():
    kwargs = {
        "install_requires": [
            'PyQt5 >= 5.12'
        ],
        "setup_requires": [],
        "keywords": ["Kiwoom", "Open API+", "키움", "영웅문"],
        'zip_safe': False
    }

    setup(
        name=DISTNAME,
        version=VERSION,
        author=AUTHOR,
        author_email=EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
        url=URL,
        download_url=DOWNLOAD_URL,
        project_urls=PROJECT_URLS,
        packages=find_packages(),
        python_requires=">=3.6",
        license=LICENSE,
        classifiers=CLASSIFIERS,
        **kwargs
    )


if __name__ == '__main__':
    setup_package()
