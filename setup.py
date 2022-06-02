from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read().replace(".. include:: toc.rst\n\n", "")

# The lines below can be parsed by `docs/conf.py`.
name = "exclusive"
version = "0.2.0"

setup(
    name=name,
    version=version,
    packages=[name,],
    install_requires=[],
    license="MIT",
    url="https://github.com/nthparty/exclusive",
    author="Andrei Lapets",
    author_email="a@lapets.io",
    description="Data structure for representing secret shares of byte " + \
                "vectors based on bitwise XOR, designed for use within " + \
                "secure multi-party computation (MPC) protocol " + \
                "implementations.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
)
 