import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dimworks", # Replace with your own username
    version="0.0.1",
    author="Guisheng Wang",
    author_email="guisheng.wang66@gmail.com",
    description="Calculate statics for manufacturing quality control",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guishengwang/QCPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)