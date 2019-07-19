# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class HelloWorldPlugin(octoprint.plugin.StartupPlugin):
    def on_after_startup(self):
        self._logger.info("************")
        self._logger.info("Hello World!")
        self._logger.info("************")

__plugin_implementation__ = HelloWorldPlugin()