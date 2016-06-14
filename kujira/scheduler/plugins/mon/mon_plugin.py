# -*- coding: utf-8 -*-
"""Base class for monitor plugins"""

from kujira.scheduler.plugins.plugin import Plugin


class MonPlugin(Plugin):
    """MonPlugin implements common methods mon plugins"""

    def is_valid(self):
        if 'host' not in self.params:
            return (False, "'host' param is required!")

        return (True, None)
