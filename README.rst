=========
exclusive
=========

Data structure for representing secret shares of byte vectors based on bitwise XOR, designed for use within secure multi-party computation (MPC) protocol implementations.

|pypi| |readthedocs| |actions| |coveralls|

.. |pypi| image:: https://badge.fury.io/py/exclusive.svg
   :target: https://badge.fury.io/py/exclusive
   :alt: PyPI version and link.

.. |readthedocs| image:: https://readthedocs.org/projects/exclusive/badge/?version=latest
   :target: https://exclusive.readthedocs.io/en/latest/?badge=latest
   :alt: Read the Docs documentation status.

.. |actions| image:: https://github.com/nthparty/exclusive/workflows/lint-test-cover-docs/badge.svg
   :target: https://github.com/nthparty/exclusive/actions/workflows/lint-test-cover-docs.yml
   :alt: GitHub Actions status.

.. |coveralls| image:: https://coveralls.io/repos/github/nthparty/exclusive/badge.svg?branch=main
   :target: https://coveralls.io/github/nthparty/exclusive?branch=main
   :alt: Coveralls test coverage summary.

Purpose
-------

.. |bytes| replace:: ``bytes``
.. _bytes: https://docs.python.org/3/library/stdtypes.html#bytes

This library provides a data structure and methods that make it possible to work with *n*-out-of-*n* XOR-based `secret shares <https://en.wikipedia.org/wiki/Secret_sharing>`__ of bytes-like objects within secure multi-party computation (MPC) protocol implementations. Secret shares are represented using instances of class derived from |bytes|_, and functions are provided both for splitting bytes-like objects into shares and for reconstructing |bytes|_ objects from shares.

Installation and Usage
----------------------
This library is available as a `package on PyPI <https://pypi.org/project/exclusive>`__::

    python -m pip install exclusive

The library can be imported in the usual ways::

    import exclusive
    from exclusive import *

Examples
^^^^^^^^
This library makes it possible to concisely construct multiple XOR-based secret shares from a bytes-like object::

    >>> from exclusive import shares, xor
    >>> (a, b) = shares(bytes([1, 2, 3]))
    >>> (c, d) = shares(bytes([4, 5, 6]))
    >>> ((a ^ c) ^ (b ^ d)) == xor([bytes([1, 2, 3]), bytes([4, 5, 6])])
    True

The number of shares can be specified explicitly (the default is two shares)::

    >>> (r, s, t) = shares(bytes([1, 2, 3]), quantity=3)

.. |xor| replace:: ``xor``
.. _xor: https://exclusive.readthedocs.io/en/latest/_source/exclusive.html#exclusive.exclusive.xor

.. |sum| replace:: ``sum``
.. _sum: https://docs.python.org/3/library/functions.html#sum

For convenience, an |xor|_ operator that is analogous to Python's built-in |sum|_ function is provided::

    >>> xor([bytes([1, 2, 3]), bytes([4, 5, 6])]).hex()
    '050705

.. |share| replace:: ``share``
.. _share: https://exclusive.readthedocs.io/en/latest/_source/exclusive.html#exclusive.exclusive.share

The |share|_ class is derived from the |bytes|_ class. Thus, all methods, operators, and functions that operate on bytes-like objects are supported for |share|_ objects. The |xor|_ operator provided by the library relies on Python's `built-in exclusive or operator <https://docs.python.org/3/reference/expressions.html#binary-bitwise-operations>`__ and can be used for concise reconstruction of values from a collection of secret shares::

    >>> xor([r, s, t]) == bytes([1, 2, 3])
    True

In addition, conversion methods for Base64 strings are included to support encoding and decoding of |share|_ objects::

    >>> share.from_base64('HgEA').hex()
    '1e0100'
    >>> [s.to_base64() for s in shares(bytes([1, 2, 3]))]
    ['mB6G', 'mRyF']

Development
-----------
All installation and development dependencies are fully specified in ``pyproject.toml``. The ``project.optional-dependencies`` object is used to `specify optional requirements <https://peps.python.org/pep-0621>`__ for various development tasks. This makes it possible to specify additional options (such as ``docs``, ``lint``, and so on) when performing installation using `pip <https://pypi.org/project/pip>`__::

    python -m pip install .[docs,lint]

Documentation
^^^^^^^^^^^^^
The documentation can be generated automatically from the source files using `Sphinx <https://www.sphinx-doc.org>`__::

    python -m pip install .[docs]
    cd docs
    sphinx-apidoc -f -E --templatedir=_templates -o _source .. && make html

Testing and Conventions
^^^^^^^^^^^^^^^^^^^^^^^
All unit tests are executed and their coverage is measured when using `pytest <https://docs.pytest.org>`__ (see the ``pyproject.toml`` file for configuration details)::

    python -m pip install .[test]
    python -m pytest

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`__::

    python src/exclusive/exclusive.py -v

Style conventions are enforced using `Pylint <https://www.pylint.org>`__::

    python -m pip install .[lint]
    python -m pylint src/exclusive

Contributions
^^^^^^^^^^^^^
In order to contribute to the source code, open an issue or submit a pull request on the `GitHub page <https://github.com/nthparty/exclusive>`__ for this library.

Versioning
^^^^^^^^^^
The version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`__.

Publishing
^^^^^^^^^^
This library can be published as a `package on PyPI <https://pypi.org/project/exclusive>`__ by a package maintainer. First, install the dependencies required for packaging and publishing::

    python -m pip install .[publish]

Remove any old build/distribution files and package the source into a distribution archive::

    rm -rf build dist src/*.egg-info
    python -m build --sdist --wheel .

Finally, upload the package distribution archive to `PyPI <https://pypi.org>`__ using the `twine <https://pypi.org/project/twine>`__ package::

    python -m twine upload dist/*
