# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = {"": "src"}

packages = ["redpajama"]

package_data = {"": ["*"]}

install_requires = [
    "datasets",
    "s3fs",
    "dill",
    "tqdm",
    "nltk",
    "fasttext",
    "polars",
    "pyarrow",
    "numpy",
    "msgspec",
    "boto3",
    "networkit",
    "scrubadub",
    "textstat",
    "xopen",
    "rich",
    "progiter",
    "pybloomfiltermmap3",
    "transformers",
]

dependency_links = []

# entry_points = {"console_scripts": []}

setup_kwargs = {
    "name": "redpajama",
    "version": "0.1.0",
    "description": "",
    "long_description": f"RedPajama-Data: Processing of data for RedPajama",
    "author": "",
    "author_email": "",
    "maintainer": "None",
    "maintainer_email": "None",
    "url": "None",
    "package_dir": package_dir,
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    # "entry_points": entry_points,
    "dependency_links": dependency_links,
    "python_requires": ">=3.7",
}


setup(**setup_kwargs)
