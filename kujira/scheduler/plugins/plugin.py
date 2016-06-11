# -*- coding: utf-8 -*-
"""Abstaction for scheduler's plugins (tasks)"""

from datetime import datetime

class Plugin(object):
    """Plugin class is an abstraction for task"""
    name = None

    def __init__(self, **params):
        self.create_date = datetime.now()
        self.params = params
        self.database = None


    def set_db_instance(self, database):
        """Set instance of mongo database connection

        :param database: mongo db connection"""
        self.database = database

    def is_valid(self):
        """Check if task is valid

        Check if task has all params and if they are valid"""
        raise NotImplementedError("Plugin.is_valid must be implemented!")

    def can_run(self):
        """Check if task can be run

        It should return False if task is duplicate of another one"""
        raise NotImplementedError("Plugin.can_run must be implemented!")

    def subtasks(self):
        """Get subtasks

        This function returns subtasks which must be executed
        to complete this task"""
        raise NotImplementedError("Plugin.subtasks must be implemented!")

    def data(self):
        """Get dictionary containing all information about task"""
        return {
            'title': self.name,
            'subtasks': self.subtasks(),
            'parallel': self.params['parallel']}
