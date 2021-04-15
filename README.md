Data dummy generator
=====


Random name, username, email, phone, address, ipv4 generator


Installation
------------

install with pip::

    pip install data-dummy==0.1


Usage
-----

Names can be used as a command line utility or imported as a Python package.

Here are examples of all current features:

.. code-block:: pycon
   
    >>> import dummy
    >>> dummy.name()
    'Yuliana Sudradjat'
    >>> dummy.username()
    'Yuliana'
    >>> dummy.email()
    'Bernard@gmail.com'
    >>> dummy.address()
    'Jl. Dr A Rivai Bukittinggi Telp: 0752-21720'
    >>> dummy.phone()
    '+62812-0989-0128'
    >>> dummy.ipv4()
    '123.124.5.12'


License
-------

This project is released under an `MIT License`_.

Data in the following files are public domain (derived from 1990 Census data):

- dist.all.last
- dist.female.first
- dist.male.first

.. _mit license: http://th.mit-license.org/2013
.. _available on PyPI: http://pypi.python.org/pypi/names/
