import re
import collections

"""
Parse the User-Agent header of a Pyramid request. The parsed User-Agent is
available on request.user_agent_parsed.

The parsing operation is safe: mal-formed User-Agent components are ignored.
"""

def includeme(config):
    config.add_request_method(get_user_agent,
                              'user_agent_parsed',
                              reify=True) #pragma NOCOVER

def get_user_agent(request):
    return UserAgent(request.user_agent)


class UserAgentComponent(object):

    def __init__(self, name=None, version=None, comments=None):
        self.name = name
        self.version = version
        self.comments = comments

    def __str__(self):
        if self.version is None:
            return '%s' % (self.name)
        else:
            return '%s/%s' % (self.name, self.version)

    def __repr__(self):
        return '<UserAgentComponent %s/%s>' % (self.name, self.version)


class UserAgent(object):
    """
    Extract only well-formed User-Agent components from a string.
    Does not fail on mal-formed User-Agent strings.
    """

    UAREGEX = re.compile(r'([^/ ]+)(/(\S+))?( \(([^\)]*)\))?')

    def __init__(self, string=None):
        self.components = collections.OrderedDict()
        self.string = None
        if string:
            self.parse(string)

    @property
    def maincomponent(self):
        if len(self.components) >= 1:
            return self.components.values()[0]

    def parse(self, string):
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
