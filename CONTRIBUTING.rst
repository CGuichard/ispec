Contributing
============

Thank you for wanting to contribute to this project!

The following elements will allow you to contribute with a little guide to learn how to make an approved contribution. Don’t hesitate to share some new ideas to improve it!

Table of Contents
-----------------

-  `Contributing <#contributing>`__

   -  `Table of Contents <#table-of-contents>`__
   -  `Code of Conduct <#code-of-conduct>`__
   -  `How to contribute? <#how-to-contribute>`__

      -  `Setup <#setup>`__

         -  `Clone the repository <#clone-the-repository>`__
         -  `Create the environment <#create-the-environment>`__

      -  `Organization <#organization>`__

         -  `Report issues <#report-issues>`__
         -  `Work on issues <#work-on-issues>`__
         -  `Pull Requests <#pull-requests>`__

      -  `Writing code <#writing-code>`__

         -  `Clean Code <#clean-code>`__
         -  `Development method <#development-method>`__
         -  `Linters & Formatters <#linters--formatters>`__
         -  `Tests <#tests>`__
         -  `Security <#security>`__
         -  `Documentation <#documentation>`__

      -  `Git <#git>`__

         -  `Ignore <#ignore>`__
         -  `Hooks <#hooks>`__
         -  `Pull <#pull>`__
         -  `Branches <#branches>`__
         -  `Commit <#commit>`__

            -  `Types <#types>`__
            -  `Scopes <#scopes>`__
            -  `Subject <#subject>`__

Code of Conduct
---------------

When you are contributing, keep in mind:

-  Remain respectful of different points of view and experiences.
-  Accept constructive criticism.
-  Show sympathy for other contributors.

How to contribute?
------------------

Setup
~~~~~

Clone the repository
^^^^^^^^^^^^^^^^^^^^

.. code:: bash

   git clone git@github.com:cguichard/ispec

Create the environment
^^^^^^^^^^^^^^^^^^^^^^

First, create an isolated Python virtual environment:

.. code:: bash

   virtualenv -p $(which python3) .venv
   source .venv/bin/activate
   pip install --upgrade pip
   # OR
   python3 -mvenv --upgrade-deps .venv
   source .venv/bin/activate

List available commands:

.. code:: bash

   make help

In order to develop in the best conditions, you must install in editable
mode.

.. code:: bash

   make install-dev

This project uses multiple tools for its development, and your virtual environment
created earlier is just here to give you a working development environment.
The tools are handled in sub-virtual environments created by `Tox <https://tox.wiki>`__,
a virtual env manager and automation tool. The ``install-dev`` only gives you the tools that you will be
directly using, delegating other installations inside of *Tox* virtual envs.

In order to complete the environment setup, you must install some Git Hooks.
You can refer to the dedicated section of this document:
`Hooks <#hooks>`__

Organization
~~~~~~~~~~~~

Report issues
^^^^^^^^^^^^^

There are two kinds of issue:

-  `Bug report <https://github.com/CGuichard/ispec/issues/new?template=bug_report.md>`__
-  `Feature request <https://github.com/CGuichard/ispec/issues/new?template=feature_request.md>`__

Click on these links to visit the issue creation page, with a simple
template to guide you.

Work on issues
^^^^^^^^^^^^^^

You can work on every open issue. Keep in mind to reference them in your
commits and pull requests, by following the `GitHub
convention <https://docs.github.com/en/github/writing-on-github/autolinked-references-and-urls#issues-and-pull-requests>`__.

You must work on a separate branch for each issue. Check out the `branch
naming convention <#branches>`__.

Pull Requests
^^^^^^^^^^^^^

Please follow these guidelines:

-  Use a clear and descriptive title.
-  Include every relevant issue number in the body, not in the title.
-  Give a complete description of every change made in the body.

If a branch is merged and no longer needed, make sure it was closed.

Writing code
~~~~~~~~~~~~

Clean Code
^^^^^^^^^^

Writing clean code is very important for a project. References such as
“Clean Code”, by Robert C. Martin, are good to keep in mind. Readable
code is not a luxury, it is a necessity.

Let us be reminded of the Zen of Python, by Tim Peters:

.. code:: text

   Beautiful is better than ugly.
   Explicit is better than implicit.
   Simple is better than complex.
   Complex is better than complicated.
   Flat is better than nested.
   Sparse is better than dense.
   Readability counts.
   Special cases aren't special enough to break the rules.
   Although practicality beats purity.
   Errors should never pass silently.
   Unless explicitly silenced.
   In the face of ambiguity, refuse the temptation to guess.
   There should be one-- and preferably only one --obvious way to do it.
   Although that way may not be obvious at first unless you're Dutch.
   Now is better than never.
   Although never is often better than *right* now.
   If the implementation is hard to explain, it's a bad idea.
   If the implementation is easy to explain, it may be a good idea.
   Namespaces are one honking great idea -- let's do more of those!

You are not alone for this difficult task. In the next sections you will
find about our recommended development method, our linting and
formatting tools, and how to use tests.

Development method
^^^^^^^^^^^^^^^^^^

The favored method of development will be TDD (Test Driven
Development).

The TDD process can be explained like this:

1. Add a test.
2. Run all tests. The new test should fail for expected reasons (failing
   by compilation error doesn’t count as true failing, you must be able
   to compile your code).
3. Write the simplest code that passes the new test.
4. All tests should now pass.
5. Refactor as needed, using tests after each refactors to ensure that
   functionality is preserved

Repeat…

Linters & Formatters
^^^^^^^^^^^^^^^^^^^^

To ensure good code writing, we use a lot of lint/validation tools:

-  `validate-pyproject <https://validate-pyproject.readthedocs.io>`__:
   command line tool and Python library for validating ``pyproject.toml``,
   includes models defined for ``PEP 517``, ``PEP 518`` and ``PEP 621``.
-  `flake8 <https://flake8.pycqa.org>`__: style guide enforcement, with
   the use of ~50 plugins.
-  `pylint <https://pylint.pycqa.org>`__: pylint checks for errors, enforces
   a coding standard, looks for code smells, and can make suggestions about
   how the code could be refactored.
-  `vulture <https://github.com/jendrikseipp/vulture>`__: finds unused code.
-  `mypy <https://mypy.readthedocs.io>`__: static type checker.
-  `bandit <https://bandit.readthedocs.io>`__: tool designed to find
   common security issues in Python code.
-  `xenon <https://xenon.readthedocs.io>`__: code complexity monitoring tool based on `radon <https://radon.readthedocs.io>`__.

In order to help you, some formatters are run just before the linters:

-  `black <https://black.readthedocs.io>`__: code formatter
-  `isort <https://pycqa.github.io/isort/>`__: python utility / library
   to sort imports alphabetically, and automatically separated into
   sections and by type.
-  `autoflake <https://github.com/PyCQA/autoflake>`__: removes unused
   imports and unused variables.
-  `eradicate <https://github.com/myint/eradicate>`__: removes
   commented-out code.

These tools (format & lint) are run with:

.. code:: bash

   make format lint

.. note::

   All of these are also run for each commit, failing the commit
   if at least one error is found.

Tests
^^^^^

We shall always aim for the highest code coverage in our tests, and our
development environment should use tools that will help us ensure it.

The test frameworks used are unittest and pytest, run with tox. Thanks to
pytest-cov, code coverage is evaluated and fails under 90% of test coverage.

Run the tests with *make*:

.. code:: bash

   make test

.. note::

   Tests also run before each push, failing it if at least one test fails.

Security
^^^^^^^^

We use `safety <https://pypi.org/project/safety>`__ to check our Python dependencies
for potential security vulnerabilities and suggests the proper remediations for
vulnerabilities detected.

.. code:: bash

   make security

.. note::

   Security check is run before each push, failing the push if it fails.

Documentation
^^^^^^^^^^^^^

This project is documented with `Sphinx <https://www.sphinx-doc.org>`__.
The documentation source can be found in the
`docs/source <https://github.com/CGuichard/ispec/tree/master/docs/source/>`__ folder.

You can build the docs with:

.. code:: bash

   make docs

If you want to clean the docs before building, and serve the docs with
an http server after the build:

.. code:: bash

   make docs serve

.. note::

   Security check is run before each push, failing the push if it fails.

Git
~~~

Ignore
^^^^^^

When you want to hide something from Git’s all-seeing eyes, don’t
stubbornly use the ``.gitignore`` file. There are three native ways in
Git to ignore files/folders:

1. ``.gitignore``: Patterns that should be version-controlled and
   distributed to other repositories via clone (i.e., files that all
   developers will want to ignore), to put it bluntly, non-tracked files
   generated by the project lifecycle can be put here.
2. ``.git/info/exclude``: Patterns that are specific to a particular
   repository but which do not need to be shared with other related
   repositories (e.g., auxiliary files that live inside the repository
   but are specific to one user’s workflow).
3. Patterns which a user wants Git to ignore in all situations (e.g.,
   backup or temporary files generated by the user’s editor of choice)
   generally go into a file specified by ``core.excludesFile`` in the
   user’s ``~/.gitconfig``.

More details in the full *official* documentation of Git
`here <https://git-scm.com/docs/gitignore>`__.

To summarize, don’t write in the ``.gitignore`` files generated by your
workflow if it is not common to all developers on the project. To serve
that purpose, mandatory tools must be specified in this section.

*There is no mandatory IDE/tool at the moment.*

Hooks
^^^^^

To activate our Git Hooks, please run the following commands:

.. code:: bash

   pre-commit install --install-hooks

Our hooks needs the following dependencies:

-  Python (>=3.9), Go (>=1.19), pre-commit (~=3.1)

Pull
^^^^

It is good practice to pull with rebase over a normal pull.

.. code:: bash

   git switch <your-branch>

   # classic
   git pull

   # much better
   git pull --rebase

But do keep in mind that to be able to rebase, you’ll need to have a
clean state of your repository, with no changes to commit. If that’s not
the case, you can use ``stash`` in addition:

.. code:: bash

   git switch <your-branch>
   git stash
   git pull --rebase
   git stash pop

If you don’t want to specify ``--rebase`` each time you pull, configure
it:

.. code:: bash

   git config --local pull.rebase true

And if you don’t want to manually ``stash`` at each rebase, you can also
configure it:

.. code:: bash

   git config --local rebase.autostash true

Now each ``git pull`` will use ``--rebase`` and automatically ``stash``!

Branches
^^^^^^^^

Here’s our branch naming convention:

-  Immutable branches:

   -  ``master``: our main branch, must have no error.
   -  ``develop``: branch used to work, where you merge your work
      branches.

-  Work branches:

   -  ``<scope>/<short-name>``: you work here.

List of scopes:

-  **fix**: fix a bug
-  **feat**: add a feature
-  **docs**: documentation changes
-  **refactor**: code refactoring

Those are examples, if you come up with other scopes, you can use them.
You can also use a scope from our commit convention as a branch scope.

We will prefer the use of “-” over “_“.

Example:

.. code:: bash

   git checkout -b fix/sanitize-paths

Don’t forget to delete your local branches when you don’t need them
anymore.

.. code:: bash

   git branch -d <branch-name>

To keep your local refs to remote branches clean, use:

.. code:: bash

   git remote prune origin

Here’s one process that you can follow once your local branch was
pushed, successfully merged into ``develop``, and if you don’t need it
anymore:

.. code:: bash

   git switch develop
   git pull
   git branch -d <my-branch>
   git remote prune origin

You can also use a scope from our commit convention as a branch scope.

Commit
^^^^^^

Based on `Conventional
Commits <https://www.conventionalcommits.org/en/v1.0.0/>`__.

Summary :

.. code:: text

   <type>(<scope>): <subject>

The scope is optional, you can find a simpler form:

.. code:: text

   <type>: <subject>

In order to be concise, type and scope should not be longer than 10
characters. Limit the first line to 70 characters or less.

Types
'''''

-  **build:** Changes that affects the build system or external
   dependencies, such as adding a dependency, or modifying the build
   system.
-  **ci:** Changes in CI.
-  **chore:** Changes which does not modify the code sources nor the
   tests.
-  **docs:** Addition or modification of documentation/comment.
-  **style:** Changes that does not affect the sense/meaning of the code
   (space, formatting, semicolon, newline, etc …).
-  **typo:** Correction of a typographical problem in the code (example:
   correction of a spelling error in a string).
-  **refactor:** Code change that doesn’t fix a bug or add a feature.
-  **perf:** Code change that improves performance.
-  **feat:** Adding or modifying a feature.
-  **fix:** Bug fix.
-  **test:** Addition of missing tests or correction of existing tests.
-  **revert:** Rollback changes from a previous commit.

Scopes
''''''

This part is optional, it can be used to define more precisely what is
impacted. Examples:

.. code:: text

   build(wheel): add x to the wheel
   refactor(modulename): change x in y class

Subject
'''''''

This is the content of your commit message. Please follow these rules:

-  It starts with a lowercase letter.
-  It does not end with a point.
-  It must be conjugated in the imperative.
-  The message should explain the what and the why, but not how.

.. code:: bash

   git commit -m "type(scope): message"

If you need a longer message, you can add a “body” to the commit.

.. code:: bash

   git commit

Git then opens an editor to write the commit.

.. code:: text

   type(scope): message less than 70 characters

   I am the body of the commit and I am not limited in size.
   However, keep in mind that if the commit needs a large description it may be better to have an issue with it.
