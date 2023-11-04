ISpec - Interface Specification
===============================

.. warning::

   ISpec is an **experimental** project, and is not aimed to be used in
   real projects. You can successfully create interfaces with the help
   of `abc <https://docs.python.org/3/library/abc.html>`__ (on which
   *ispec* is based),
   `zope.interface <https://zopeinterface.readthedocs.io>`__, and last
   but not least, the best solution, the
   `Protocol <https://peps.python.org/pep-0544/>`__ from
   `typing <https://docs.python.org/3/library/typing.html>`__.

ISpec is a project aimed to create a simple way of defining interfaces.
What it does is use the `abc <https://docs.python.org/3/library/abc.html>`__
module, make your class inherit ``abc.ABC``, apply the ``abc.abstractmethod``
decorator, and ensure the function signature uses
`type hints <https://peps.python.org/pep-0484/>`__ for parameters and returns.
With this, a class that implements an ISpec interface can't be instantiated
if it doesn't define every function of the interface, and the interface must
declare type hints to improve readability.

Getting started
===============

.. toctree::
   :maxdepth: 2
   :caption: For Users

   users/installation
   users/usage

.. toctree::
   :maxdepth: 2
   :caption: For Developers/Contributors

   developers/api_reference/index
   developers/contributing
   developers/license
   GitHub Repository <https://github.com/CGuichard/ispec>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
