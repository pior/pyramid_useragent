import re
import collections

from user_agents.parsers import UserAgent as UserAgentClassifier

"""
Parse the User-Agent header of a Pyramid request. The parsed User-Agent is
available on request.user_agent_parsed.

The parsing operation is safe: mal-formed User-Agent components are ignored.
"""

def includeme(config):
    """
    Set up a request method ``user_agent_parsed`` returning an instance of
    :py:class:`UserAgent` initialized with the client User-Agent.
    """

    config.add_request_method(get_user_agent_parsed,
                              'user_agent_parsed',
                              reify=True) #pragma NOCOVER
    config.add_request_method(get_user_agent_classified,
                              'user_agent_classified',
                              reify=True) #pragma NOCOVER

def get_user_agent_parsed(request):
    return UserAgent(request.user_agent)

def get_user_agent_classified(request):
    return UserAgentClassifier(request.user_agent or '')


class UserAgentComponent(object):
    """
    Simple object representing a single User-Agent component
    """

    def __init__(self, name=None, version=None, comments=None):
        self.name = name
        """Name part of a User-Agent component"""

        self.version = version
        """Version part of a User-Agent component"""

        self.comments = comments
        """Comment part of a User-Agent component as a list"""

    def __str__(self):
        if self.version is None:
            return '%s' % (self.name)
        else:
            return '%s/%s' % (self.name, self.version)

    def __repr__(self):
        return '<UserAgentComponent %s/%s>' % (self.name, self.version)


class UserAgent(object):
    """
    Extract User-Agent components from a string.

    .. NOTE:: The parsing operation is safe: mal-formed User-Agent components
       are ignored.
    """

    UAREGEX = re.compile(r'([^/ ]+)(/(\S+))?( \(([^\)]*)\))?')

    def __init__(self, string=None):
        self.components = collections.OrderedDict()
        """
        List of :py:class:`UserAgentComponent` (order is kept by using an
        OrderedDict)
        """

        self.string = None
        """Original User-Agent string"""

        if string:
            self.parse(string)

    @property
    def maincomponent(self):
        """Most significant :py:class:`UserAgentComponent`"""
        if len(self.components) >= 1:
            return next(iter(self.components.values()))

    def parse(self, string):
        """Parse a User-Agent string"""

        self.string = string
        for parts in re.findall(self.UAREGEX, string):

            name = parts[0].strip()
            version = parts[2].strip() if parts[2] else None
            comments = [c.strip() for c in parts[4].split(';')]

            component = UserAgentComponent(
                name=name,
                version=version,
                comments=comments
                )
            self.components[component.name] = component

    def __repr__(self):
        if self.maincomponent:
            return '<UserAgent %s>' % self.maincomponent
        else:
            return '<UserAgent>'

    def __str__(self):
        if self.maincomponent:
            return str(self.maincomponent)
        else:
            return 'EmptyUserAgent'
