"""Notify another app via webhook
"""

import structlog
import requests

from notifiers.utils import NotifierUtils

class LineNotifier(NotifierUtils):
    """Class for handling webhook notifications
    """

    def __init__(self, token):
        self.logger = structlog.get_logger()
        self.url = 'https://notify-api.line.me/api/notify'
        self.token = token


    def notify(self, message):
        """Sends the message.

        Args:
            message (str): The message to send.
        """

        headers = {
            'content-type':'application/x-www-form-urlencoded',
            'Authorization':'Bearer ' + self.token
        }

        request = requests.post(self.url, headers=headers, data = { 'message': '\n' + message })
        if not request.status_code == requests.codes.ok:
            self.logger.error("Request failed: %s - %s", request.status_code, request.content)


