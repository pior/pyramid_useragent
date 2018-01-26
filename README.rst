pyramid_useragent
=================


Project Info
------------

Provides an HTTP User-Agent parser and classifier for the
`Pyramid <http://docs.pylonsproject.org>`_ web framework.

* Documentation: http://pyramid-useragent.readthedocs.org/
* PyPI: https://pypi.python.org/pypi/pyramid_useragent
* Bitbucket: https://bitbucket.org/pior/pyramid_useragent
* |droneio|

.. |droneio| image::
   https://drone.io/bitbucket.org/pior/pyramid_useragent/status.png
   :target: https://drone.io/bitbucket.org/pior/pyramid_useragent
   :alt: Tests on drone.io


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

.. code-block:: python

   pip install -e .[testing]
   nosetests


Documentation
-------------

.. code-block:: python

   pip install -e .[docs]
   cd docs
   make html

