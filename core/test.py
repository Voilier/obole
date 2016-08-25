# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.test.runner import DiscoverRunner


class CustomRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        pass

    def teardown_databases(self, old_config, **kwargs):
        pass
