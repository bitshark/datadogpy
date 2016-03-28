from datadog.api.base import ListableAPIResource


class Reports(ListableAPIResource):
    """
    A wrapper around Host HTTP API.
    """
    _class_name = 'reports'
    _class_url = '/reports/v2/overview'
    _absolute_url = True
