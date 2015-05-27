# -*- coding: utf-8 -*-
"""
===============
mllib.documents
===============

http://docs.marklogic.com/guide/rest-dev/documents
http://docs.marklogic.com/REST/client/management
"""

from __future__ import unicode_literals, print_function, absolute_import

from .restclient import RESTClient
from .utils import KwargsSerializer

class DocumentsService(RESTClient):

    def document_put(self, file_, **kwargs):
        """Insert or update document contents and/or metadata, at a caller-supplied document URI.
        http://docs.marklogic.com/REST/PUT/v1/documents

        :param file_: A path to a file or an opened file object in 'rb' mode.
        """
        requirements = {
            'uri': '!',
            'category': '*',
            'database': '?',
            'format': '?',
            'collection': '*',
            'quality': '?',
            'perm': '*',
            'prop': '*',
            'extract': '?',
            'repair': '?',
            'transform': '?',
            'trans': '*',
            'forest-name': '?',
            'temporal-collection': '?',
            'system-time': '?'
        }
        tool = KwargsSerializer(requirements)
        kwargs, headers = tool.requests_params(kwargs, )
        self.rest_put('/v1/documents', )