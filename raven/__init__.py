"""
sentry
~~~~~~

:copyright: (c) 2010 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

__all__ = ('VERSION', 'Client')

try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('django-sentry').version
except Exception, e:
    VERSION = 'unknown'

from base import Client