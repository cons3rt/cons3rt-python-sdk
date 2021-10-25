# coding: utf-8

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


from __future__ import absolute_import

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


class IdentitiesApi(object):
    """NOTE: This class is auto-generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_identity(self, id, hostid, cloud_resource_object, **kwargs):  # noqa: E501
        """Create a host identity  # noqa: E501

        Creates an identity for the deployment run host with access to the resources requested by the user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_identity(id, hostid, cloud_resource_object, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param str hostid: ID of host (required)
        :param list[CloudResourceObject] cloud_resource_object: The cloud resources to be accessed by the host identity (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[BaseIdentity]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_identity_with_http_info(id, hostid, cloud_resource_object, **kwargs)  # noqa: E501

    def create_identity_with_http_info(self, id, hostid, cloud_resource_object, **kwargs):  # noqa: E501
        """Create a host identity  # noqa: E501

        Creates an identity for the deployment run host with access to the resources requested by the user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_identity_with_http_info(id, hostid, cloud_resource_object, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param str hostid: ID of host (required)
        :param list[CloudResourceObject] cloud_resource_object: The cloud resources to be accessed by the host identity (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[BaseIdentity], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'hostid', 'cloud_resource_object']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_identity" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `create_identity`")  # noqa: E501
        # verify the required parameter 'hostid' is set
        if self.api_client.client_side_validation and ('hostid' not in local_var_params or  # noqa: E501
                                                        local_var_params['hostid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `hostid` when calling `create_identity`")  # noqa: E501
        # verify the required parameter 'cloud_resource_object' is set
        if self.api_client.client_side_validation and ('cloud_resource_object' not in local_var_params or  # noqa: E501
                                                        local_var_params['cloud_resource_object'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cloud_resource_object` when calling `create_identity`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501
        if 'hostid' in local_var_params:
            path_params['hostid'] = local_var_params['hostid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'cloud_resource_object' in local_var_params:
            body_params = local_var_params['cloud_resource_object']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'Username']  # noqa: E501

        return self.api_client.call_api(
            '/api/drs/{id}/host/{hostid}/identity', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[BaseIdentity]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_identity(self, id, hostid, **kwargs):  # noqa: E501
        """Delete host identity  # noqa: E501

        Deletes the identity of a deployment run host.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_identity(id, hostid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param str hostid: ID of host (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_identity_with_http_info(id, hostid, **kwargs)  # noqa: E501

    def delete_identity_with_http_info(self, id, hostid, **kwargs):  # noqa: E501
        """Delete host identity  # noqa: E501

        Deletes the identity of a deployment run host.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_identity_with_http_info(id, hostid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param str hostid: ID of host (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(bool, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'hostid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_identity" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `delete_identity`")  # noqa: E501
        # verify the required parameter 'hostid' is set
        if self.api_client.client_side_validation and ('hostid' not in local_var_params or  # noqa: E501
                                                        local_var_params['hostid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `hostid` when calling `delete_identity`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501
        if 'hostid' in local_var_params:
            path_params['hostid'] = local_var_params['hostid']  # noqa: E501

        query_params = []

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
            '/api/drs/{id}/host/{hostid}/identity', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_identity_by_id(self, id, hostid, username, **kwargs):  # noqa: E501
        """Deletes identity for specified user  # noqa: E501

        Deletes an identity for a user specified by name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_identity_by_id(id, hostid, username, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param str hostid: ID of host (required)
        :param str username: Username of the identity to be deleted (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[BaseIdentity]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_identity_by_id_with_http_info(id, hostid, username, **kwargs)  # noqa: E501

    def delete_identity_by_id_with_http_info(self, id, hostid, username, **kwargs):  # noqa: E501
        """Deletes identity for specified user  # noqa: E501

        Deletes an identity for a user specified by name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_identity_by_id_with_http_info(id, hostid, username, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param str hostid: ID of host (required)
        :param str username: Username of the identity to be deleted (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[BaseIdentity], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'hostid', 'username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_identity_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `delete_identity_by_id`")  # noqa: E501
        # verify the required parameter 'hostid' is set
        if self.api_client.client_side_validation and ('hostid' not in local_var_params or  # noqa: E501
                                                        local_var_params['hostid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `hostid` when calling `delete_identity_by_id`")  # noqa: E501
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in local_var_params or  # noqa: E501
                                                        local_var_params['username'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `username` when calling `delete_identity_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501
        if 'hostid' in local_var_params:
            path_params['hostid'] = local_var_params['hostid']  # noqa: E501
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']  # noqa: E501

        query_params = []

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
            '/api/drs/{id}/host/{hostid}/identity/{username}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[BaseIdentity]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_identities(self, id, hostid, **kwargs):  # noqa: E501
        """Get Host Identities  # noqa: E501

        Returns a collection of identities for the deployment run host  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_identities(id, hostid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param str hostid: ID of host (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[BaseIdentity]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_identities_with_http_info(id, hostid, **kwargs)  # noqa: E501

    def get_identities_with_http_info(self, id, hostid, **kwargs):  # noqa: E501
        """Get Host Identities  # noqa: E501

        Returns a collection of identities for the deployment run host  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_identities_with_http_info(id, hostid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param str hostid: ID of host (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[BaseIdentity], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'hostid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_identities" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `get_identities`")  # noqa: E501
        # verify the required parameter 'hostid' is set
        if self.api_client.client_side_validation and ('hostid' not in local_var_params or  # noqa: E501
                                                        local_var_params['hostid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `hostid` when calling `get_identities`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501
        if 'hostid' in local_var_params:
            path_params['hostid'] = local_var_params['hostid']  # noqa: E501

        query_params = []

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
            '/api/drs/{id}/host/{hostid}/identities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[BaseIdentity]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_identity(self, id, hostid, **kwargs):  # noqa: E501
        """Get Host Identity For User  # noqa: E501

        Returns the deployment run host identity for the user, if one exists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_identity(id, hostid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param str hostid: ID of host (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[CloudResourceAccessListing]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_identity_with_http_info(id, hostid, **kwargs)  # noqa: E501

    def get_identity_with_http_info(self, id, hostid, **kwargs):  # noqa: E501
        """Get Host Identity For User  # noqa: E501

        Returns the deployment run host identity for the user, if one exists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_identity_with_http_info(id, hostid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param str hostid: ID of host (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[CloudResourceAccessListing], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'hostid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_identity" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `get_identity`")  # noqa: E501
        # verify the required parameter 'hostid' is set
        if self.api_client.client_side_validation and ('hostid' not in local_var_params or  # noqa: E501
                                                        local_var_params['hostid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `hostid` when calling `get_identity`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501
        if 'hostid' in local_var_params:
            path_params['hostid'] = local_var_params['hostid']  # noqa: E501

        query_params = []

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
            '/api/drs/{id}/host/{hostid}/identity', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CloudResourceAccessListing]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
