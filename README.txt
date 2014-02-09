pyramid_useragent
=================

.. image:: https://drone.io/bitbucket.org/pior/pyramid_useragent/status.png
    :target: https://drone.io/bitbucket.org/pior/pyramid_useragent
    :alt: Tests on drone.io

Provides an HTTP User-Agent parser for the
`Pyramid <http://docs.pylonsproject.org>`_ web framework.

.. See `pyramid_useragent documentation
   <http://pyramid-useragent.readthedocs.org/>`_ for more information.


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

    def parsed(request):
        ua = request.user_agent_parsed  # I'am reified!

        name_of_first_component = ua.maincomponent.name
        version_of_first_component = ua.maincomponent.version
        comments_of_first_component = ua.maincomponent.comments

        name_of_third_component = ua.components.values()[2].name

        if request.user_agent_parsed.maincomponent.name == 'Links':
            return "Did you really use Links?"
        else:
            return ua.components.values()
