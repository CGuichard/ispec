ISpec - Interface Specification
===============================

|GitHub| |Language| |Documentation| |Style| |Lint| |Security| |Stability| |Contributions|

`Pull Request <https://github.com/CGuichard/ispec/pulls>`__
**·** `Bug Report <https://github.com/CGuichard/ispec/issues/new?template=bug_report.md>`__
**·** `Feature Request <https://github.com/CGuichard/ispec/issues/new?template=feature_request.md>`__

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

Table of Contents
-----------------

-  `ISpec - Interface
   Specification <#ispec---interface-specification>`__

   -  `Table of Contents <#table-of-contents>`__
   -  `Getting started <#getting-started>`__

      -  `Installation <#installation>`__

   -  `Contributing <#contributing>`__
   -  `License <#license>`__

Getting started
---------------

Installation
~~~~~~~~~~~~

.. code:: bash

   pip install git+https://github.com/CGuichard/ispec.git
   # pip install git+https://github.com/CGuichard/ispec.git@<tag>

Contributing
------------

If you want to contribute to this project or understand how it works,
please check `CONTRIBUTING.rst <CONTRIBUTING.rst>`__.

Any contribution is greatly appreciated.

License
-------

Distributed under the MIT License. See `LICENSE <LICENSE>`__ for more
information.

.. |GitHub| image:: https://img.shields.io/badge/license-MIT-yellow?style=flat-square
   :target: https://github.com/CGuichard/ispec/blob/master/LICENSE
.. |Language| image:: https://img.shields.io/badge/language-Python-3776ab?style=flat-square&logo=Python
   :target: https://www.python.org/
.. |Documentation| image:: https://img.shields.io/badge/documentation-sphinx-0a507a?style=flat-square
   :target: https://www.sphinx-doc.org/en/master/usage/index.html
.. |Style| image:: https://img.shields.io/badge/style-black-9a9a9a?style=flat-square
.. |Lint| image:: https://img.shields.io/badge/lint-flake8,%20pylint,%20mypy-brightgreen?style=flat-square
.. |Security| image:: https://img.shields.io/badge/security-bandit,%20safety-purple?style=flat-square
.. |Stability| image:: https://img.shields.io/badge/stability-experimental-orange?style=flat-square
.. |Contributions| image:: https://img.shields.io/badge/contributions-welcome-orange?style=flat-square
   :target: https://github.com/CGuichard/ispec/blob/master/CONTRIBUTING.rst
