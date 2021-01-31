import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hy-nbp", # 
    version="0.0.2",
    author="J.Angel",
    author_email="jorgeangel.mn@gmail.com",
    description="N body problem solution",
    long_description="This package offers a simple API to solve the N body problem of Celestial Mechanics",
    long_description_content_type="text/markdown",
    url="https://github.com/J-angelm/hy-nbp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)