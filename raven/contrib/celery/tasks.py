# -*- coding: utf-8 -*-

from celery.task import task


def get_client():
    """Get the client used."""
    # TODO check other clients
    from raven.contrib.django.models import get_client
    return get_client()


@task(routing_key='sentry')
def send_task(message):
    client = get_client()
    client.send_raw(message)
