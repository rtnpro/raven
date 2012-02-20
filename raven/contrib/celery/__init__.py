"""
raven.contrib.celery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2010 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from celery.task import task
from raven.base import Client
from raven.contrib.celery.tasks import send_task


class CeleryMixin(object):
    def send_encoded(self, message):
        "Errors through celery"
        send_task.delay(message)

    def send_raw(self, message):
        return super(CeleryMixin, self).send_encoded(message)


class CeleryClient(CeleryMixin, Client):
    pass

