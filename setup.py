import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='suruguya',
    version='0.0.4',
    author='marvinody',
    author_email='manny@sadpanda.moe',
    description='suruguya api-like wrapper',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://bitbucket.org/marvinody/suruguya/',
    packages=setuptools.find_packages(),
    install_requires=['beautifulsoup4==4.7.1', 'certifi==2019.3.9', 'chardet==3.0.4', 'idna==2.8', 'requests==2.21.0', 'soupsieve==1.9', 'urllib3==1.24.1'],
    classifiers=[
        "Programming Language :: Python :: 3.5",
    ]
)
