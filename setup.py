from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="unattend-applier",
    version="1.0.0",
    author="JonesDev",
    author_email="jhonatanedu.dev@gmail.com", 
    description="Apply Windows debloat and customization settings from autounattend.xml to running systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GoCodeJones/unattend-applier-library",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Installation/Setup",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.7",
    install_requires=[],  # No external dependencies!
    entry_points={
        "console_scripts": [
            "unattend-apply=unattend_applier.core:main",
        ],
    },
)