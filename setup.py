from setuptools import setup

setup(
    name='freelunch',
    version='0.0.1',
    description='Meta-heuristic optimisation tools',
    py_modules=['freelunch'],
    package_dir={'':'src'},
)

from setuptools import setup


# The text of the README file
with open('README.md') as f:
    rm = f.read()

# This call to setup() does all the work
setup(
    name="freelunch",
    version="0.0.1",
    description="Heuristic and meta-heuristic optimisation suite in Python",
    long_description=rm,
    long_description_content_type="text/markdown",
    url="https://github.com/MDCHAMP/FreeLunch",
    author="Max Champneys",
    author_email="max.champneys@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["freelunch"],
    package_dir={'':'src'},
    include_package_data=False,
    install_requires=["numpy"],
)