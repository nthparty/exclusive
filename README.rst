=========
exclusive
=========

Data structure for representing secret shares of byte vectors based on bitwise XOR, designed for use within secure multi-party computation (MPC) protocol implementations.

|pypi|

.. |pypi| image:: https://badge.fury.io/py/exclusive.svg
   :target: https://badge.fury.io/py/exclusive
   :alt: PyPI version and link.

Purpose
-------

.. |bytes| replace:: ``bytes``
.. _bytes: https://docs.python.org/3/library/stdtypes.html#bytes

This library provides a data structure and methods that make it possible work with *n*-out-of-*n* `additive secret shares <https://en.wikipedia.org/wiki/Secret_sharing>`_ of bytes-like objects within secure multi-party computation (MPC) protocol implementations. Secret shares are represented using instances of class derived from |bytes|_, and functions are provided both for splitting bytes-like objects into shares and for reconstructing |bytes|_ objects from shares.

Package Installation and Usage
------------------------------
The package is available on `PyPI <https://pypi.org/project/exclusive/>`_::

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

The |share|_ class is derived from the |bytes|_ class. Thus, all methods, operators, and functions that operate on bytes-like objects are supported for |share|_ objects. The |xor|_ operator provided by the library relies on Python's `built-in exclusive or operator <https://docs.python.org/3/reference/expressions.html#binary-bitwise-operations>`_ and can be used for concise reconstruction of values from a collection of secret shares::

    >>> xor([r, s, t]) == bytes([1, 2, 3])
    True

In addition, conversion methods for Base64 strings are included to support encoding and decoding of |share|_ objects::

    >>> share.from_base64('HgEA').hex()
    '1e0100'
    >>> [s.to_base64() for s in shares(bytes([1, 2, 3]))]
    ['mB6G', 'mRyF']

Testing and Conventions
-----------------------
All unit tests are executed and their coverage is measured when using `pytest <https://docs.pytest.org/>`_ (see ``setup.cfg`` for configuration details)::

    python -m pip install pytest pytest-cov
    python -m pytest

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`_::

    python exclusive/exclusive.py -v

Style conventions are enforced using `Pylint <https://www.pylint.org/>`_::

    python -m pip install pylint
    python -m pylint exclusive

Contributions
-------------
In order to contribute to the source code, open an issue or submit a pull request on the `GitHub page <https://github.com/nthparty/exclusive>`_ for this library.

Versioning
----------
The version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`_.

Publishing
----------
This library can be published as a `package on PyPI <https://pypi.org/project/exclusive/>`_ by a package maintainer. Install the `wheel <https://pypi.org/project/wheel/>`_ package, remove any old build/distribution files, and package the source into a distribution archive::

    python -m pip install wheel
    rm -rf dist *.egg-info
    python setup.py sdist bdist_wheel

Next, install the `twine <https://pypi.org/project/twine/>`_ package and upload the package distribution archive to PyPI::

    python -m pip install twine
    python -m twine upload dist/*