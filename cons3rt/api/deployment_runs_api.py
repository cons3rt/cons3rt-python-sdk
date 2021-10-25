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


class DeploymentRunsApi(object):
    """NOTE: This class is auto-generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_category_to_deployment_run(self, id, runid, **kwargs):  # noqa: E501
        """Assign Category to Run  # noqa: E501

        Assigns the Category as a filter tag to the provided Deployment Run.<br> <br> Altering the Category will affect future Run filtering.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_category_to_deployment_run(id, runid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of category (required)
        :param str runid: ID of run to assign (required)
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
        return self.add_category_to_deployment_run_with_http_info(id, runid, **kwargs)  # noqa: E501

    def add_category_to_deployment_run_with_http_info(self, id, runid, **kwargs):  # noqa: E501
        """Assign Category to Run  # noqa: E501

        Assigns the Category as a filter tag to the provided Deployment Run.<br> <br> Altering the Category will affect future Run filtering.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_category_to_deployment_run_with_http_info(id, runid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of category (required)
        :param str runid: ID of run to assign (required)
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

        all_params = ['id', 'runid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_category_to_deployment_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `add_category_to_deployment_run`")  # noqa: E501
        # verify the required parameter 'runid' is set
        if self.api_client.client_side_validation and ('runid' not in local_var_params or  # noqa: E501
                                                        local_var_params['runid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `runid` when calling `add_category_to_deployment_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'runid' in local_var_params and local_var_params['runid'] is not None:  # noqa: E501
            query_params.append(('runid', local_var_params['runid']))  # noqa: E501

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
            '/api/categories/{id}/run', 'PUT',
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

    def delete_deployment_run(self, id, **kwargs):  # noqa: E501
        """Delete Deployment Run  # noqa: E501

        Deletes a single inactive Deployment Run with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_deployment_run(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param bool purge: Delete all dependencies of the deployment run
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
        return self.delete_deployment_run_with_http_info(id, **kwargs)  # noqa: E501

    def delete_deployment_run_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete Deployment Run  # noqa: E501

        Deletes a single inactive Deployment Run with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_deployment_run_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param bool purge: Delete all dependencies of the deployment run
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

        all_params = ['id', 'purge']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_deployment_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `delete_deployment_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'purge' in local_var_params and local_var_params['purge'] is not None:  # noqa: E501
            query_params.append(('purge', local_var_params['purge']))  # noqa: E501

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
            '/api/drs/{id}', 'DELETE',
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

    def download_deployment_run_test_report(self, id, **kwargs):  # noqa: E501
        """Download Report  # noqa: E501

        Downloads a single Test Report for the specified Deployment Run.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_deployment_run_test_report(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param str file: Report file name
        :param str number: Report number
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.download_deployment_run_test_report_with_http_info(id, **kwargs)  # noqa: E501

    def download_deployment_run_test_report_with_http_info(self, id, **kwargs):  # noqa: E501
        """Download Report  # noqa: E501

        Downloads a single Test Report for the specified Deployment Run.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_deployment_run_test_report_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param str file: Report file name
        :param str number: Report number
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'file', 'number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_deployment_run_test_report" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `download_deployment_run_test_report`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'file' in local_var_params and local_var_params['file'] is not None:  # noqa: E501
            query_params.append(('file', local_var_params['file']))  # noqa: E501
        if 'number' in local_var_params and local_var_params['number'] is not None:  # noqa: E501
            query_params.append(('number', local_var_params['number']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['APIKeyHeader', 'Username']  # noqa: E501

        return self.api_client.call_api(
            '/api/drs/{id}/downloadreport', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def download_host(self, id, role, **kwargs):  # noqa: E501
        """Download Host  # noqa: E501

        Downloads a single Host Bundle for the specified Deployment Run.<br> <br> Based on the background flag, the download will either be done in the foreground (false), background (true), or be determined by asset size (no value).<br> <br> If the background flag is set to true (or no value for the background flag is provided), and the host is larger than the site threshold, it will be prepared for download in the background and an email with a link to retrieve the asset will be sent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_host(id, role, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param str role: Name of host to bundle for download (required)
        :param bool background: Force the download to happen in the background
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.download_host_with_http_info(id, role, **kwargs)  # noqa: E501

    def download_host_with_http_info(self, id, role, **kwargs):  # noqa: E501
        """Download Host  # noqa: E501

        Downloads a single Host Bundle for the specified Deployment Run.<br> <br> Based on the background flag, the download will either be done in the foreground (false), background (true), or be determined by asset size (no value).<br> <br> If the background flag is set to true (or no value for the background flag is provided), and the host is larger than the site threshold, it will be prepared for download in the background and an email with a link to retrieve the asset will be sent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_host_with_http_info(id, role, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param str role: Name of host to bundle for download (required)
        :param bool background: Force the download to happen in the background
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'role', 'background']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_host" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `download_host`")  # noqa: E501
        # verify the required parameter 'role' is set
        if self.api_client.client_side_validation and ('role' not in local_var_params or  # noqa: E501
                                                        local_var_params['role'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `role` when calling `download_host`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'role' in local_var_params and local_var_params['role'] is not None:  # noqa: E501
            query_params.append(('role', local_var_params['role']))  # noqa: E501
        if 'background' in local_var_params and local_var_params['background'] is not None:  # noqa: E501
            query_params.append(('background', local_var_params['background']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['APIKeyHeader', 'Username']  # noqa: E501

        return self.api_client.call_api(
            '/api/drs/{id}/downloadhost', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_deployment_run(self, id, **kwargs):  # noqa: E501
        """Retrieve Deployment Run  # noqa: E501

        Returns a single Deployment Run by the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_deployment_run(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: FullDeploymentRun
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_deployment_run_with_http_info(id, **kwargs)  # noqa: E501

    def get_deployment_run_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve Deployment Run  # noqa: E501

        Returns a single Deployment Run by the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_deployment_run_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(FullDeploymentRun, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_deployment_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `get_deployment_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

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
            '/api/drs/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FullDeploymentRun',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_deployment_run_reports(self, id, **kwargs):  # noqa: E501
        """List Reports  # noqa: E501

        Returns a collection of the Test Reports for a single Deployment Run.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_deployment_run_reports(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_deployment_run_reports_with_http_info(id, **kwargs)  # noqa: E501

    def get_deployment_run_reports_with_http_info(self, id, **kwargs):  # noqa: E501
        """List Reports  # noqa: E501

        Returns a collection of the Test Reports for a single Deployment Run.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_deployment_run_reports_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[str], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_deployment_run_reports" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `get_deployment_run_reports`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

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
            '/api/drs/{id}/reports', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_deployment_runs(self, id, **kwargs):  # noqa: E501
        """List Deployment Runs  # noqa: E501

        Returns a collection of the Deployment Runs for a single Deployment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_deployment_runs(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment (required)
        :param int maxresults: Maximum number of results to return
        :param int page: Requested page number
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[MinimalDeploymentRun]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_deployment_runs_with_http_info(id, **kwargs)  # noqa: E501

    def get_deployment_runs_with_http_info(self, id, **kwargs):  # noqa: E501
        """List Deployment Runs  # noqa: E501

        Returns a collection of the Deployment Runs for a single Deployment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_deployment_runs_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment (required)
        :param int maxresults: Maximum number of results to return
        :param int page: Requested page number
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[MinimalDeploymentRun], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'maxresults', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_deployment_runs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `get_deployment_runs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'maxresults' in local_var_params and local_var_params['maxresults'] is not None:  # noqa: E501
            query_params.append(('maxresults', local_var_params['maxresults']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501

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
            '/api/deployments/{id}/runs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MinimalDeploymentRun]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_deployment_runs1(self, search_type, **kwargs):  # noqa: E501
        """List Deployment Runs  # noqa: E501

        Returns a collection of the user's relevant Deployment Runs matching a specified query.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_deployment_runs1(search_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str search_type: Deployment run status (required)
        :param bool in_project: Include project runs
        :param int maxresults: Maximum number of results to return
        :param int page: Requested page number
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[MinimalDeploymentRun]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_deployment_runs1_with_http_info(search_type, **kwargs)  # noqa: E501

    def get_deployment_runs1_with_http_info(self, search_type, **kwargs):  # noqa: E501
        """List Deployment Runs  # noqa: E501

        Returns a collection of the user's relevant Deployment Runs matching a specified query.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_deployment_runs1_with_http_info(search_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str search_type: Deployment run status (required)
        :param bool in_project: Include project runs
        :param int maxresults: Maximum number of results to return
        :param int page: Requested page number
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[MinimalDeploymentRun], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['search_type', 'in_project', 'maxresults', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_deployment_runs1" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'search_type' is set
        if self.api_client.client_side_validation and ('search_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['search_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `search_type` when calling `get_deployment_runs1`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_type' in local_var_params and local_var_params['search_type'] is not None:  # noqa: E501
            query_params.append(('search_type', local_var_params['search_type']))  # noqa: E501
        if 'in_project' in local_var_params and local_var_params['in_project'] is not None:  # noqa: E501
            query_params.append(('in_project', local_var_params['in_project']))  # noqa: E501
        if 'maxresults' in local_var_params and local_var_params['maxresults'] is not None:  # noqa: E501
            query_params.append(('maxresults', local_var_params['maxresults']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501

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
            '/api/drs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MinimalDeploymentRun]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_host(self, id, hostid, **kwargs):  # noqa: E501
        """Retrieve Host  # noqa: E501

        Returns the specified Host in the Deployment Run by the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_host(id, hostid, async_req=True)
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
        :return: FullDeploymentRunHost
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_host_with_http_info(id, hostid, **kwargs)  # noqa: E501

    def get_host_with_http_info(self, id, hostid, **kwargs):  # noqa: E501
        """Retrieve Host  # noqa: E501

        Returns the specified Host in the Deployment Run by the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_host_with_http_info(id, hostid, async_req=True)
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
        :return: tuple(FullDeploymentRunHost, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_host" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `get_host`")  # noqa: E501
        # verify the required parameter 'hostid' is set
        if self.api_client.client_side_validation and ('hostid' not in local_var_params or  # noqa: E501
                                                        local_var_params['hostid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `hostid` when calling `get_host`")  # noqa: E501

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
            '/api/drs/{id}/host/{hostid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FullDeploymentRunHost',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_host_access(self, id, hostid, **kwargs):  # noqa: E501
        """List Host Access Logs  # noqa: E501

        Returns a collection of the Host Access Logs for a single Deployment Run.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_host_access(id, hostid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param str hostid: ID of host (required)
        :param int maxresults: Maximum number of results to return
        :param int page: Requested page number
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[RemoteAccessSession]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_host_access_with_http_info(id, hostid, **kwargs)  # noqa: E501

    def get_host_access_with_http_info(self, id, hostid, **kwargs):  # noqa: E501
        """List Host Access Logs  # noqa: E501

        Returns a collection of the Host Access Logs for a single Deployment Run.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_host_access_with_http_info(id, hostid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param str hostid: ID of host (required)
        :param int maxresults: Maximum number of results to return
        :param int page: Requested page number
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[RemoteAccessSession], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'hostid', 'maxresults', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_host_access" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `get_host_access`")  # noqa: E501
        # verify the required parameter 'hostid' is set
        if self.api_client.client_side_validation and ('hostid' not in local_var_params or  # noqa: E501
                                                        local_var_params['hostid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `hostid` when calling `get_host_access`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501
        if 'hostid' in local_var_params:
            path_params['hostid'] = local_var_params['hostid']  # noqa: E501

        query_params = []
        if 'maxresults' in local_var_params and local_var_params['maxresults'] is not None:  # noqa: E501
            query_params.append(('maxresults', local_var_params['maxresults']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501

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
            '/api/drs/{id}/host/{hostid}/access', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RemoteAccessSession]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_host_configuration_metrics(self, id, start, end, **kwargs):  # noqa: E501
        """Retrieve Metrics  # noqa: E501

        Returns metric data for Deployment Runs launched by members of the specified Project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_host_configuration_metrics(id, start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of project (required)
        :param int start: Interval start time, specified in seconds since epoch (required)
        :param int end: Interval end time, specified in seconds since epoch (required)
        :param int interval: Number of intervals
        :param str interval_unit: Interval unit
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_host_configuration_metrics_with_http_info(id, start, end, **kwargs)  # noqa: E501

    def get_host_configuration_metrics_with_http_info(self, id, start, end, **kwargs):  # noqa: E501
        """Retrieve Metrics  # noqa: E501

        Returns metric data for Deployment Runs launched by members of the specified Project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_host_configuration_metrics_with_http_info(id, start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of project (required)
        :param int start: Interval start time, specified in seconds since epoch (required)
        :param int end: Interval end time, specified in seconds since epoch (required)
        :param int interval: Number of intervals
        :param str interval_unit: Interval unit
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'start', 'end', 'interval', 'interval_unit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_host_configuration_metrics" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `get_host_configuration_metrics`")  # noqa: E501
        # verify the required parameter 'start' is set
        if self.api_client.client_side_validation and ('start' not in local_var_params or  # noqa: E501
                                                        local_var_params['start'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `start` when calling `get_host_configuration_metrics`")  # noqa: E501
        # verify the required parameter 'end' is set
        if self.api_client.client_side_validation and ('end' not in local_var_params or  # noqa: E501
                                                        local_var_params['end'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `end` when calling `get_host_configuration_metrics`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'start' in local_var_params and local_var_params['start'] is not None:  # noqa: E501
            query_params.append(('start', local_var_params['start']))  # noqa: E501
        if 'end' in local_var_params and local_var_params['end'] is not None:  # noqa: E501
            query_params.append(('end', local_var_params['end']))  # noqa: E501
        if 'interval' in local_var_params and local_var_params['interval'] is not None:  # noqa: E501
            query_params.append(('interval', local_var_params['interval']))  # noqa: E501
        if 'interval_unit' in local_var_params and local_var_params['interval_unit'] is not None:  # noqa: E501
            query_params.append(('intervalUnit', local_var_params['interval_unit']))  # noqa: E501

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
            '/api/projects/{id}/metrics/hostconfiguration', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_host_instance_types(self, id, hostid, **kwargs):  # noqa: E501
        """List available instance types for host  # noqa: E501

        Returns a collection of available instance types for resizing a Deployment Run Host.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_host_instance_types(id, hostid, async_req=True)
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
        :return: TargetInstanceTypes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_host_instance_types_with_http_info(id, hostid, **kwargs)  # noqa: E501

    def get_host_instance_types_with_http_info(self, id, hostid, **kwargs):  # noqa: E501
        """List available instance types for host  # noqa: E501

        Returns a collection of available instance types for resizing a Deployment Run Host.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_host_instance_types_with_http_info(id, hostid, async_req=True)
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
        :return: tuple(TargetInstanceTypes, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_host_instance_types" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `get_host_instance_types`")  # noqa: E501
        # verify the required parameter 'hostid' is set
        if self.api_client.client_side_validation and ('hostid' not in local_var_params or  # noqa: E501
                                                        local_var_params['hostid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `hostid` when calling `get_host_instance_types`")  # noqa: E501

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
            '/api/drs/{id}/host/{hostid}/resize', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TargetInstanceTypes',  # noqa: E501
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

    def perform_host_action(self, id, deploymentrunhostid, action, **kwargs):  # noqa: E501
        """Execute Host Action  # noqa: E501

        Executes an action against the specified Host in the Deployment Run for the ID provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.perform_host_action(id, deploymentrunhostid, action, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param str deploymentrunhostid: ID of host (required)
        :param str action: Action to perform (required)
        :param int cpu: Desired number of CPUs, if resizing host in a non instance type based virtualization realm
        :param int ram: Desired amount of RAM in Mebibytes, if resizing host in a non instance type based virtualization realm
        :param str instance_type_name: The instance type name to resize to, if resizing host in an instance type based virtualization realm
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
        return self.perform_host_action_with_http_info(id, deploymentrunhostid, action, **kwargs)  # noqa: E501

    def perform_host_action_with_http_info(self, id, deploymentrunhostid, action, **kwargs):  # noqa: E501
        """Execute Host Action  # noqa: E501

        Executes an action against the specified Host in the Deployment Run for the ID provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.perform_host_action_with_http_info(id, deploymentrunhostid, action, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param str deploymentrunhostid: ID of host (required)
        :param str action: Action to perform (required)
        :param int cpu: Desired number of CPUs, if resizing host in a non instance type based virtualization realm
        :param int ram: Desired amount of RAM in Mebibytes, if resizing host in a non instance type based virtualization realm
        :param str instance_type_name: The instance type name to resize to, if resizing host in an instance type based virtualization realm
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

        all_params = ['id', 'deploymentrunhostid', 'action', 'cpu', 'ram', 'instance_type_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method perform_host_action" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `perform_host_action`")  # noqa: E501
        # verify the required parameter 'deploymentrunhostid' is set
        if self.api_client.client_side_validation and ('deploymentrunhostid' not in local_var_params or  # noqa: E501
                                                        local_var_params['deploymentrunhostid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `deploymentrunhostid` when calling `perform_host_action`")  # noqa: E501
        # verify the required parameter 'action' is set
        if self.api_client.client_side_validation and ('action' not in local_var_params or  # noqa: E501
                                                        local_var_params['action'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `action` when calling `perform_host_action`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'deploymentrunhostid' in local_var_params and local_var_params['deploymentrunhostid'] is not None:  # noqa: E501
            query_params.append(('deploymentrunhostid', local_var_params['deploymentrunhostid']))  # noqa: E501
        if 'action' in local_var_params and local_var_params['action'] is not None:  # noqa: E501
            query_params.append(('action', local_var_params['action']))  # noqa: E501
        if 'cpu' in local_var_params and local_var_params['cpu'] is not None:  # noqa: E501
            query_params.append(('cpu', local_var_params['cpu']))  # noqa: E501
        if 'ram' in local_var_params and local_var_params['ram'] is not None:  # noqa: E501
            query_params.append(('ram', local_var_params['ram']))  # noqa: E501
        if 'instance_type_name' in local_var_params and local_var_params['instance_type_name'] is not None:  # noqa: E501
            query_params.append(('instanceTypeName', local_var_params['instance_type_name']))  # noqa: E501

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
            '/api/drs/{id}/hostaction', 'PUT',
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

    def publish_deployment_run(self, id, **kwargs):  # noqa: E501
        """Publish Deployment Run  # noqa: E501

        Publishes the specified Deployment as a Composition.<br> <br> Consumers will be able to connect to the run, but will not be able to manage the composition.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.publish_deployment_run(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
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
        return self.publish_deployment_run_with_http_info(id, **kwargs)  # noqa: E501

    def publish_deployment_run_with_http_info(self, id, **kwargs):  # noqa: E501
        """Publish Deployment Run  # noqa: E501

        Publishes the specified Deployment as a Composition.<br> <br> Consumers will be able to connect to the run, but will not be able to manage the composition.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.publish_deployment_run_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
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

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method publish_deployment_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `publish_deployment_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

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
            '/api/drs/{id}/publish', 'POST',
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

    def redeploy_container_asset(self, id, hostid, installationid, **kwargs):  # noqa: E501
        """Re-deploy Container Asset  # noqa: E501

        Re-deploys the specified Container Asset installation on the single Host in the specified Deployment Run.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.redeploy_container_asset(id, hostid, installationid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param str hostid: ID of host (required)
        :param str installationid: ID of container asset installation (required)
        :param InputContainerComponent input_container_component: The updated Container Component definition
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
        return self.redeploy_container_asset_with_http_info(id, hostid, installationid, **kwargs)  # noqa: E501

    def redeploy_container_asset_with_http_info(self, id, hostid, installationid, **kwargs):  # noqa: E501
        """Re-deploy Container Asset  # noqa: E501

        Re-deploys the specified Container Asset installation on the single Host in the specified Deployment Run.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.redeploy_container_asset_with_http_info(id, hostid, installationid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param str hostid: ID of host (required)
        :param str installationid: ID of container asset installation (required)
        :param InputContainerComponent input_container_component: The updated Container Component definition
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

        all_params = ['id', 'hostid', 'installationid', 'input_container_component']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method redeploy_container_asset" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `redeploy_container_asset`")  # noqa: E501
        # verify the required parameter 'hostid' is set
        if self.api_client.client_side_validation and ('hostid' not in local_var_params or  # noqa: E501
                                                        local_var_params['hostid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `hostid` when calling `redeploy_container_asset`")  # noqa: E501
        # verify the required parameter 'installationid' is set
        if self.api_client.client_side_validation and ('installationid' not in local_var_params or  # noqa: E501
                                                        local_var_params['installationid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `installationid` when calling `redeploy_container_asset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501
        if 'hostid' in local_var_params:
            path_params['hostid'] = local_var_params['hostid']  # noqa: E501

        query_params = []
        if 'installationid' in local_var_params and local_var_params['installationid'] is not None:  # noqa: E501
            query_params.append(('installationid', local_var_params['installationid']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'input_container_component' in local_var_params:
            body_params = local_var_params['input_container_component']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'Username']  # noqa: E501

        return self.api_client.call_api(
            '/api/drs/{id}/host/{hostid}/container', 'PUT',
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

    def redeploy_deployment_run_hosts(self, id, **kwargs):  # noqa: E501
        """Redeploy Deployment Run Hosts  # noqa: E501

        Requests the redeploy of one or more deployment run hosts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.redeploy_deployment_run_hosts(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param list[RestIdObject] rest_id_object: The collection of deployment run host ids to redeploy
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
        return self.redeploy_deployment_run_hosts_with_http_info(id, **kwargs)  # noqa: E501

    def redeploy_deployment_run_hosts_with_http_info(self, id, **kwargs):  # noqa: E501
        """Redeploy Deployment Run Hosts  # noqa: E501

        Requests the redeploy of one or more deployment run hosts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.redeploy_deployment_run_hosts_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param list[RestIdObject] rest_id_object: The collection of deployment run host ids to redeploy
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

        all_params = ['id', 'rest_id_object']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method redeploy_deployment_run_hosts" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `redeploy_deployment_run_hosts`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'rest_id_object' in local_var_params:
            body_params = local_var_params['rest_id_object']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'Username']  # noqa: E501

        return self.api_client.call_api(
            '/api/drs/{id}/redeployhosts', 'PUT',
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

    def relaunch_deployment_run(self, id, **kwargs):  # noqa: E501
        """Relaunch Deployment Run  # noqa: E501

        Launches a new Deployment Run with the same configuration as the specified Deployment Run.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.relaunch_deployment_run(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.relaunch_deployment_run_with_http_info(id, **kwargs)  # noqa: E501

    def relaunch_deployment_run_with_http_info(self, id, **kwargs):  # noqa: E501
        """Relaunch Deployment Run  # noqa: E501

        Launches a new Deployment Run with the same configuration as the specified Deployment Run.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.relaunch_deployment_run_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method relaunch_deployment_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `relaunch_deployment_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

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
            '/api/drs/{id}/rerun', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def release_deployment_run(self, id, **kwargs):  # noqa: E501
        """Release Deployment Run  # noqa: E501

        Releases the Deployment Run for the ID provided.<br> <br> If the user is an Administrator, the force flag is honored.<br> <br> If the user is a non-Admin, the force flag is only honored in the event that a release request experiences an exception known to be resolved by a force.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.release_deployment_run(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param bool force: Force the release of this run
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
        return self.release_deployment_run_with_http_info(id, **kwargs)  # noqa: E501

    def release_deployment_run_with_http_info(self, id, **kwargs):  # noqa: E501
        """Release Deployment Run  # noqa: E501

        Releases the Deployment Run for the ID provided.<br> <br> If the user is an Administrator, the force flag is honored.<br> <br> If the user is a non-Admin, the force flag is only honored in the event that a release request experiences an exception known to be resolved by a force.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.release_deployment_run_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param bool force: Force the release of this run
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

        all_params = ['id', 'force']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method release_deployment_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `release_deployment_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'force' in local_var_params and local_var_params['force'] is not None:  # noqa: E501
            query_params.append(('force', local_var_params['force']))  # noqa: E501

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
            '/api/drs/{id}/release', 'PUT',
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

    def remove_category_from_deployment_run(self, id, runid, **kwargs):  # noqa: E501
        """Unassign Category from deployment run  # noqa: E501

        Removes the Category as a filter tag from the provided Run.<br> <br> Altering the Category will affect future run filtering.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_category_from_deployment_run(id, runid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of category (required)
        :param str runid: ID of run to unassign (required)
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
        return self.remove_category_from_deployment_run_with_http_info(id, runid, **kwargs)  # noqa: E501

    def remove_category_from_deployment_run_with_http_info(self, id, runid, **kwargs):  # noqa: E501
        """Unassign Category from deployment run  # noqa: E501

        Removes the Category as a filter tag from the provided Run.<br> <br> Altering the Category will affect future run filtering.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_category_from_deployment_run_with_http_info(id, runid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of category (required)
        :param str runid: ID of run to unassign (required)
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

        all_params = ['id', 'runid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_category_from_deployment_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `remove_category_from_deployment_run`")  # noqa: E501
        # verify the required parameter 'runid' is set
        if self.api_client.client_side_validation and ('runid' not in local_var_params or  # noqa: E501
                                                        local_var_params['runid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `runid` when calling `remove_category_from_deployment_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'runid' in local_var_params and local_var_params['runid'] is not None:  # noqa: E501
            query_params.append(('runid', local_var_params['runid']))  # noqa: E501

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
            '/api/categories/{id}/run', 'DELETE',
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

    def retest_deployment_run(self, id, **kwargs):  # noqa: E501
        """Re-test Deployment Run  # noqa: E501

        Re-executes all Tests in the specified Deployment Run.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retest_deployment_run(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
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
        return self.retest_deployment_run_with_http_info(id, **kwargs)  # noqa: E501

    def retest_deployment_run_with_http_info(self, id, **kwargs):  # noqa: E501
        """Re-test Deployment Run  # noqa: E501

        Re-executes all Tests in the specified Deployment Run.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retest_deployment_run_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
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

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retest_deployment_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `retest_deployment_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

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
            '/api/drs/{id}/retest', 'PUT',
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

    def set_deployment_run_lock(self, id, lock, **kwargs):  # noqa: E501
        """Update Lock  # noqa: E501

        Update the Lock on a single Deployment Run with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_deployment_run_lock(id, lock, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param bool lock: The desired lock state (required)
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
        return self.set_deployment_run_lock_with_http_info(id, lock, **kwargs)  # noqa: E501

    def set_deployment_run_lock_with_http_info(self, id, lock, **kwargs):  # noqa: E501
        """Update Lock  # noqa: E501

        Update the Lock on a single Deployment Run with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_deployment_run_lock_with_http_info(id, lock, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param bool lock: The desired lock state (required)
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

        all_params = ['id', 'lock']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_deployment_run_lock" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `set_deployment_run_lock`")  # noqa: E501
        # verify the required parameter 'lock' is set
        if self.api_client.client_side_validation and ('lock' not in local_var_params or  # noqa: E501
                                                        local_var_params['lock'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `lock` when calling `set_deployment_run_lock`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'lock' in local_var_params and local_var_params['lock'] is not None:  # noqa: E501
            query_params.append(('lock', local_var_params['lock']))  # noqa: E501

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
            '/api/drs/{id}/setlock', 'PUT',
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

    def set_power_schedule_for_deployment_run(self, id, **kwargs):  # noqa: E501
        """Update Power Schedule  # noqa: E501

        Updates the Power Schedule for a single Deployment Run with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_power_schedule_for_deployment_run(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param PowerSchedule power_schedule: The desired power schedule
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
        return self.set_power_schedule_for_deployment_run_with_http_info(id, **kwargs)  # noqa: E501

    def set_power_schedule_for_deployment_run_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update Power Schedule  # noqa: E501

        Updates the Power Schedule for a single Deployment Run with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_power_schedule_for_deployment_run_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
        :param PowerSchedule power_schedule: The desired power schedule
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

        all_params = ['id', 'power_schedule']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_power_schedule_for_deployment_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `set_power_schedule_for_deployment_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'power_schedule' in local_var_params:
            body_params = local_var_params['power_schedule']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'Username']  # noqa: E501

        return self.api_client.call_api(
            '/api/drs/{id}/powerschedule', 'PUT',
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

    def unpublish_deployment_run(self, id, **kwargs):  # noqa: E501
        """Unpublish Deployment Run  # noqa: E501

        Unpublishes the specified Deployment as a Composition.<br> <br> Consumers will no longer be able to connect to the run, and the run will no longer appear to consumers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unpublish_deployment_run(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
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
        return self.unpublish_deployment_run_with_http_info(id, **kwargs)  # noqa: E501

    def unpublish_deployment_run_with_http_info(self, id, **kwargs):  # noqa: E501
        """Unpublish Deployment Run  # noqa: E501

        Unpublishes the specified Deployment as a Composition.<br> <br> Consumers will no longer be able to connect to the run, and the run will no longer appear to consumers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unpublish_deployment_run_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of deployment run (required)
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

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method unpublish_deployment_run" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `unpublish_deployment_run`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

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
            '/api/drs/{id}/publish', 'DELETE',
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
