# coding: utf-8

from __future__ import absolute_import

"""
   Copyright 2020 Jackpine Technologies Corporation

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""




import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cons3rt.api_client import ApiClient
from cons3rt.exceptions import (
    ApiTypeError,
    ApiValueError
)

__author__ = 'Jackpine Technologies Corporation'
__copyright__ = 'Copyright 2020, Jackpine Technologies Corporation'
__license__ = 'Apache 2.0',
__version__ = '1.0.0'
__maintainer__ = 'API Support'
__email__ = 'support@cons3rt.com'


class TemplatesApi(object):
    """NOTE: This class is auto-generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_virtualization_realm_templates(self, virtualization_realm_id, **kwargs):  # noqa: E501
        """List all Templates  # noqa: E501

        Returns a collection of the user's available Templates matching a specified query.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_virtualization_realm_templates(virtualization_realm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int virtualization_realm_id: Virtualization Realm ID to filter by (required)
        :param bool include_registrations: Include templates registered to this virtualization realm
        :param bool include_subscriptions: Include templates this virtualization realm is subscribed to
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[MinimalCons3rtTemplateData]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_virtualization_realm_templates_with_http_info(virtualization_realm_id, **kwargs)  # noqa: E501

    def list_virtualization_realm_templates_with_http_info(self, virtualization_realm_id, **kwargs):  # noqa: E501
        """List all Templates  # noqa: E501

        Returns a collection of the user's available Templates matching a specified query.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_virtualization_realm_templates_with_http_info(virtualization_realm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int virtualization_realm_id: Virtualization Realm ID to filter by (required)
        :param bool include_registrations: Include templates registered to this virtualization realm
        :param bool include_subscriptions: Include templates this virtualization realm is subscribed to
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[MinimalCons3rtTemplateData], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['virtualization_realm_id', 'include_registrations', 'include_subscriptions']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_virtualization_realm_templates" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'virtualization_realm_id' is set
        if self.api_client.client_side_validation and ('virtualization_realm_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['virtualization_realm_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `virtualization_realm_id` when calling `list_virtualization_realm_templates`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'virtualization_realm_id' in local_var_params and local_var_params['virtualization_realm_id'] is not None:  # noqa: E501
            query_params.append(('virtualization_realm_id', local_var_params['virtualization_realm_id']))  # noqa: E501
        if 'include_registrations' in local_var_params and local_var_params['include_registrations'] is not None:  # noqa: E501
            query_params.append(('include_registrations', local_var_params['include_registrations']))  # noqa: E501
        if 'include_subscriptions' in local_var_params and local_var_params['include_subscriptions'] is not None:  # noqa: E501
            query_params.append(('include_subscriptions', local_var_params['include_subscriptions']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'Username']  # noqa: E501

        return self.api_client.call_api(
            '/api/templates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MinimalCons3rtTemplateData]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
