import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='suruguya',
    version='0.0.1',
    author='marvinody',
    author_email='manny@sadpanda.moe',
    description='suruguya api-like wrapper',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://bitbucket.org/marvinody/suruguya/',
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.5",
    ]
)
