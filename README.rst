pyramid_useragent
=================

Provides an HTTP User-Agent parser and classifier for the
`Pyramid <http://docs.pylonsproject.org>`_ web framework.

|circleci| |pythonversion| |documentation|

Code: https://github.com/pior/pyramid_useragent


.. |circleci| image::
   https://circleci.com/gh/pior/pyramid_useragent.svg?style=svg
   :target: https://circleci.com/gh/pior/pyramid_useragent
   :alt: Tests on CircleCI

.. |pythonversion| image::
   https://img.shields.io/pypi/pyversions/pyramid_useragent.svg
   :target: https://pypi.python.org/pypi/pyramid_useragent
   :alt: Python version on PyPI

.. |documentation| image::
   https://readthedocs.org/projects/pyramid-useragent/badge/?version=latest&style=flat-square
   :target: https://pyramid-useragent.readthedocs.org/
   :alt: Documentation on ReadTheDocs

Setup
-----

Once `pyramid_useragent` is installed, you typically use the ``config.include``
mechanism to include it into your Pyramid project's configuration. In your
Pyramid project's ``__init__.py``:

.. code-block:: python

   config = Configurator(.....)
   config.include('pyramid_useragent')

Alternately, instead of using the Configurator's ``include`` method, you can
activate Pyramid by changing your application's ``.ini`` file, use the
following line:

.. code-block:: ini

   pyramid.includes = pyramid_useragent


Usage
-----

.. code-block:: python

   def demo(request):

       client = request.user_agent_classified

       if client.is_mobile or client.is_tablet:
           return "Download our mobile app!"

       if client.is_bot:
           return "Are you human? I'am human."

       ua = request.user_agent_parsed

       if ua.maincomponent.name == 'Links':
           return "Did you REALLY use Links?"

       if 'AdobeAIR' in ua.components:
           if ua.components['AdobeAIR'].version == '3.9.0.1210':
               return "Much unsecure, so flaws"

       if ua.maincomponent.name == "Mozilla":
           return "This is supposed to describe your platform: %s" % (
               '; '.join(ua.maincomponent.comments))

       return [c.name for c in ua.components.values()]


Tests
-----

For development, this project uses a tool called `DevBuddy <https://github.com/devbuddy/devbuddy>`_.

To install DevBuddy, go to the `install page on Github <https://github.com/devbuddy/devbuddy#install>`_
Once installed, you should be able to run ``bud up`` to setup your development
environment.

If you don't want to use DevBuddy, take a look at the file `dev.yml` to know
how the project is setup, linted, tested, released.


.. code-block:: python

   $ bud test


Documentation
-------------

.. code-block:: python

   pip install -e .[docs]
   cd docs
   make html


Release
=======

Make sure you run the tests just before:

.. code-block:: shell

   $ bud test

Create a new release:

.. code-block:: shell

   $ bud release 0.4.0

Publish the release:

.. code-block:: shell

   $ bud publish
