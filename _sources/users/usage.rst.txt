Usage
=====

ISpec gives you 3 classes decorators.

The @ispec decorator
--------------------

This decorator is the main one, it is used to declare interfaces.
An interface is considered here as a Python abstract class were
type hints must be defined. The module ``abc`` is used.

Example
~~~~~~~

.. code:: python

    from ispec import ispec


    @ispec
    class MyInterface:
        def method_dummy(self, a: str) -> str:
            ...

        @staticmethod
        def static_method_dummy(b: str) -> str:
            ...

        @classmethod
        def class_method_dummy(cls, c: str) -> str:
            ...


    class A(MyInterface):
        def method_dummy(self, a: str) -> str:
            print(f"method {a=}")

        @staticmethod
        def static_method_dummy(b: str) -> str:
            print(f"static method {b=}")

        @classmethod
        def class_method_dummy(cls, c: str) -> str:
            print(f"class method {c=}")


    mi: MyInterface = A()


Errors
~~~~~~

If an implementation is wrong, an error will be fired.

.. code:: python

    class B(MyInterface):
        pass


    mi: MyInterface = B()

.. code:: text

    TypeError: Can't instantiate abstract class B with abstract methods class_method_dummy, method_dummy, static_method_dummy


The interface raises an error if missing type hints.

.. code:: python

    @ispec
    class MyInterfaceBis:
        def method_dummy(self, a: str):
            ...

        @staticmethod
        def static_method_dummy(b) -> str:
            ...

        @classmethod
        def class_method_dummy(cls, c):
            ...

.. code:: text

    ispec.exceptions.ClassValidationError:

    __main__.MyInterfaceBis: could not validate class
    - MyInterfaceBis.method_dummy: missing annotation for method return
    - MyInterfaceBis.static_method_dummy: missing annotation for parameter b
    - MyInterfaceBis.class_method_dummy: missing annotation for method return and parameter c


The @abstractclass decorator
----------------------------

If you only want the abstract class behavior but not the type hints checks:

.. code:: python

    from ispec import abstractclass


    @abstractclass
    class MyAbstractClass:
        ...


The @typehint decorator
----------------------------

If you want the type hints checks, but do not care about making the class abstract:

.. code:: python

    from ispec import typehint


    @typehint
    class MyTypeHintedClass:
        ...
