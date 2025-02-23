from setuptools import setup, find_packages

setup(
    name="hgvs-ext",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Add your project dependencies here
    ],
    python_requires=">=3.10",
    author="Your Name",
    author_email="your.email@example.com",
    description="HGVS Extension Package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/hgvs-ext",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
