from setuptools import setup, find_packages

setup(
    name="wp_utils",
    version="0.1.0",
    author="Joshua Jenks",
    author_email="joshuadavidjenks@gmail.com",
    description="A utility library for interacting with the WordPress API.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jenksed/wp_utils",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",  # If using BeautifulSoup in utils
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)