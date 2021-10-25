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


class ScenariosApi(object):
    """NOTE: This class is auto-generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_trusted_project(self, id, trustedid, **kwargs):  # noqa: E501
        """Assign Trusted Project to Asset  # noqa: E501

        Allows members of the provided Project to access the specified Asset.<br> <br> The Asset must have a visibility set to TRUSTED_PROJECT for this to have any effect.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_trusted_project(id, trustedid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of asset (required)
        :param str trustedid: ID of project to trust (required)
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
        return self.add_trusted_project_with_http_info(id, trustedid, **kwargs)  # noqa: E501

    def add_trusted_project_with_http_info(self, id, trustedid, **kwargs):  # noqa: E501
        """Assign Trusted Project to Asset  # noqa: E501

        Allows members of the provided Project to access the specified Asset.<br> <br> The Asset must have a visibility set to TRUSTED_PROJECT for this to have any effect.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_trusted_project_with_http_info(id, trustedid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of asset (required)
        :param str trustedid: ID of project to trust (required)
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

        all_params = ['id', 'trustedid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_trusted_project" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `add_trusted_project`")  # noqa: E501
        # verify the required parameter 'trustedid' is set
        if self.api_client.client_side_validation and ('trustedid' not in local_var_params or  # noqa: E501
                                                        local_var_params['trustedid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `trustedid` when calling `add_trusted_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'trustedid' in local_var_params and local_var_params['trustedid'] is not None:  # noqa: E501
            query_params.append(('trustedid', local_var_params['trustedid']))  # noqa: E501

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
            '/api/assets/{id}/addtrustedproject', 'PUT',
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

    def clone_scenario(self, id, name, **kwargs):  # noqa: E501
        """Clone Scenario  # noqa: E501

        Clones the specified Scenario to a new Scenario with the provided name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clone_scenario(id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of scenario (required)
        :param str name: Name of the new scenario (required)
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
        return self.clone_scenario_with_http_info(id, name, **kwargs)  # noqa: E501

    def clone_scenario_with_http_info(self, id, name, **kwargs):  # noqa: E501
        """Clone Scenario  # noqa: E501

        Clones the specified Scenario to a new Scenario with the provided name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clone_scenario_with_http_info(id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of scenario (required)
        :param str name: Name of the new scenario (required)
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

        all_params = ['id', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clone_scenario" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `clone_scenario`")  # noqa: E501
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in local_var_params or  # noqa: E501
                                                        local_var_params['name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `name` when calling `clone_scenario`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'name' in local_var_params and local_var_params['name'] is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501

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
            '/api/scenarios/{id}/clone', 'PUT',
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

    def create_scenario(self, **kwargs):  # noqa: E501
        """Create Scenario  # noqa: E501

        Creates a single Scenario.<br> <br> All existing Assets used in creation must contain their Asset ID, while Composite Assets to be constructed must contain a valid Asset ID for each element contained.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_scenario(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param InputScenario input_scenario: The Scenario to create
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
        return self.create_scenario_with_http_info(**kwargs)  # noqa: E501

    def create_scenario_with_http_info(self, **kwargs):  # noqa: E501
        """Create Scenario  # noqa: E501

        Creates a single Scenario.<br> <br> All existing Assets used in creation must contain their Asset ID, while Composite Assets to be constructed must contain a valid Asset ID for each element contained.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_scenario_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param InputScenario input_scenario: The Scenario to create
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

        all_params = ['input_scenario']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_scenario" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'input_scenario' in local_var_params:
            body_params = local_var_params['input_scenario']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'Username']  # noqa: E501

        return self.api_client.call_api(
            '/api/scenarios/createscenario', 'PUT',
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

    def create_system_entire(self, **kwargs):  # noqa: E501
        """Create System  # noqa: E501

        Creates a single System.<br> <br> All existing Assets used in creation must contain their Asset ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_system_entire(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param InputSystemModule input_system_module: The System to create
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
        return self.create_system_entire_with_http_info(**kwargs)  # noqa: E501

    def create_system_entire_with_http_info(self, **kwargs):  # noqa: E501
        """Create System  # noqa: E501

        Creates a single System.<br> <br> All existing Assets used in creation must contain their Asset ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_system_entire_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param InputSystemModule input_system_module: The System to create
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

        all_params = ['input_system_module']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_system_entire" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'input_system_module' in local_var_params:
            body_params = local_var_params['input_system_module']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'Username']  # noqa: E501

        return self.api_client.call_api(
            '/api/systems/createsystem', 'PUT',
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

    def delete_asset(self, id, **kwargs):  # noqa: E501
        """Delete asset  # noqa: E501

        Delete a single Asset with the given ID.<br/> <br/> <em>Optionally, this call can be allowed to delete if the asset has dependent assets.</em>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_asset(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of asset to delete (required)
        :param bool force: Allow delete if there are dependent assets
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
        return self.delete_asset_with_http_info(id, **kwargs)  # noqa: E501

    def delete_asset_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete asset  # noqa: E501

        Delete a single Asset with the given ID.<br/> <br/> <em>Optionally, this call can be allowed to delete if the asset has dependent assets.</em>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_asset_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of asset to delete (required)
        :param bool force: Allow delete if there are dependent assets
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
                    " to method delete_asset" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `delete_asset`")  # noqa: E501

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
            '/api/assets/{id}', 'DELETE',
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

    def get_bindings_for_deployment1(self, id, **kwargs):  # noqa: E501
        """List Bindings  # noqa: E501

        Returns a collection of the possible Virtualization Realm bindings for a single scenario.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bindings_for_deployment1(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of scenario (required)
        :param int virtualization_realm_id: ID of preferred virtualization realm
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[VirtualizationRealmBinding]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_bindings_for_deployment1_with_http_info(id, **kwargs)  # noqa: E501

    def get_bindings_for_deployment1_with_http_info(self, id, **kwargs):  # noqa: E501
        """List Bindings  # noqa: E501

        Returns a collection of the possible Virtualization Realm bindings for a single scenario.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bindings_for_deployment1_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of scenario (required)
        :param int virtualization_realm_id: ID of preferred virtualization realm
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[VirtualizationRealmBinding], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'virtualization_realm_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bindings_for_deployment1" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `get_bindings_for_deployment1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'virtualization_realm_id' in local_var_params and local_var_params['virtualization_realm_id'] is not None:  # noqa: E501
            query_params.append(('virtualizationRealmId', local_var_params['virtualization_realm_id']))  # noqa: E501

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
            '/api/scenarios/{id}/bindings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[VirtualizationRealmBinding]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_scenario(self, id, **kwargs):  # noqa: E501
        """Retrieve Scenario  # noqa: E501

        Returns a single Scenario by the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scenario(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of scenario (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: FullScenario
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_scenario_with_http_info(id, **kwargs)  # noqa: E501

    def get_scenario_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve Scenario  # noqa: E501

        Returns a single Scenario by the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scenario_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of scenario (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(FullScenario, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_scenario" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `get_scenario`")  # noqa: E501

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
            '/api/scenarios/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FullScenario',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_scenarios(self, **kwargs):  # noqa: E501
        """List Scenarios  # noqa: E501

        Returns a collection of the user's relevant Scenarios matching a specified query.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scenarios(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[int] categoryids: Category ID(s) to filter by. Multiple categories can be provided with comma-separated strings.
        :param int maxresults: Maximum number of results to return
        :param int page: Requested page number
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[MinimalScenario]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_scenarios_with_http_info(**kwargs)  # noqa: E501

    def get_scenarios_with_http_info(self, **kwargs):  # noqa: E501
        """List Scenarios  # noqa: E501

        Returns a collection of the user's relevant Scenarios matching a specified query.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scenarios_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[int] categoryids: Category ID(s) to filter by. Multiple categories can be provided with comma-separated strings.
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
        :return: tuple(list[MinimalScenario], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['categoryids', 'maxresults', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scenarios" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'categoryids' in local_var_params and local_var_params['categoryids'] is not None:  # noqa: E501
            query_params.append(('categoryids', local_var_params['categoryids']))  # noqa: E501
            collection_formats['categoryids'] = 'multi'  # noqa: E501
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
            '/api/scenarios', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MinimalScenario]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_scenarios_expanded(self, **kwargs):  # noqa: E501
        """List all Scenarios, including Project Assets  # noqa: E501

        Returns a collection of all relevant Scenarios matching a specified query, including those from the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scenarios_expanded(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param bool community: Include community assets
        :param list[int] categoryids: Category ID(s) to filter by. Multiple categories can be provided with comma-separated strings.
        :param int maxresults: Maximum number of results to return
        :param int page: Requested page number
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[BasicScenario]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_scenarios_expanded_with_http_info(**kwargs)  # noqa: E501

    def get_scenarios_expanded_with_http_info(self, **kwargs):  # noqa: E501
        """List all Scenarios, including Project Assets  # noqa: E501

        Returns a collection of all relevant Scenarios matching a specified query, including those from the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scenarios_expanded_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param bool community: Include community assets
        :param list[int] categoryids: Category ID(s) to filter by. Multiple categories can be provided with comma-separated strings.
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
        :return: tuple(list[BasicScenario], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['community', 'categoryids', 'maxresults', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scenarios_expanded" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'community' in local_var_params and local_var_params['community'] is not None:  # noqa: E501
            query_params.append(('community', local_var_params['community']))  # noqa: E501
        if 'categoryids' in local_var_params and local_var_params['categoryids'] is not None:  # noqa: E501
            query_params.append(('categoryids', local_var_params['categoryids']))  # noqa: E501
            collection_formats['categoryids'] = 'multi'  # noqa: E501
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
            '/api/scenarios/expanded', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[BasicScenario]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_dependent_assets(self, id, **kwargs):  # noqa: E501
        """List all Dependent Assets  # noqa: E501

        Returns a collection of the Composite Assets that include the specified Asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_dependent_assets(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of asset (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[BasicAsset]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_dependent_assets_with_http_info(id, **kwargs)  # noqa: E501

    def list_dependent_assets_with_http_info(self, id, **kwargs):  # noqa: E501
        """List all Dependent Assets  # noqa: E501

        Returns a collection of the Composite Assets that include the specified Asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_dependent_assets_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of asset (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[BasicAsset], status_code(int), headers(HTTPHeaderDict))
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
                    " to method list_dependent_assets" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `list_dependent_assets`")  # noqa: E501

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
            '/api/assets/{id}/dependent', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[BasicAsset]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def publish_scenario_to_composition(self, id, **kwargs):  # noqa: E501
        """Publish Scenario  # noqa: E501

        Publishes the specified Scenario as a Composition, with the provided Run Options for launching.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.publish_scenario_to_composition(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: (required)
        :param InputComposition input_composition: The composition definition used when launching the deployment
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
        return self.publish_scenario_to_composition_with_http_info(id, **kwargs)  # noqa: E501

    def publish_scenario_to_composition_with_http_info(self, id, **kwargs):  # noqa: E501
        """Publish Scenario  # noqa: E501

        Publishes the specified Scenario as a Composition, with the provided Run Options for launching.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.publish_scenario_to_composition_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: (required)
        :param InputComposition input_composition: The composition definition used when launching the deployment
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

        all_params = ['id', 'input_composition']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method publish_scenario_to_composition" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `publish_scenario_to_composition`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'input_composition' in local_var_params:
            body_params = local_var_params['input_composition']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'Username']  # noqa: E501

        return self.api_client.call_api(
            '/api/scenarios/{id}/publish', 'POST',
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

    def quick_build(self, id, **kwargs):  # noqa: E501
        """Launch Scenario  # noqa: E501

        Launches a Deployment created from the specified Scenario, with the provided Run Options.<br> <br> A root password can be set within the provided Deployment Run Options, which will override the password for all Hosts.<br> <br> The override of Host passwords may fail due to template password complexity rules and should not be done without consideration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.quick_build(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of scenario (required)
        :param InputDeploymentRunOptions input_deployment_run_options: The deployment run options to use when launching the deployment
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
        return self.quick_build_with_http_info(id, **kwargs)  # noqa: E501

    def quick_build_with_http_info(self, id, **kwargs):  # noqa: E501
        """Launch Scenario  # noqa: E501

        Launches a Deployment created from the specified Scenario, with the provided Run Options.<br> <br> A root password can be set within the provided Deployment Run Options, which will override the password for all Hosts.<br> <br> The override of Host passwords may fail due to template password complexity rules and should not be done without consideration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.quick_build_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of scenario (required)
        :param InputDeploymentRunOptions input_deployment_run_options: The deployment run options to use when launching the deployment
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

        all_params = ['id', 'input_deployment_run_options']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method quick_build" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `quick_build`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'input_deployment_run_options' in local_var_params:
            body_params = local_var_params['input_deployment_run_options']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'Username']  # noqa: E501

        return self.api_client.call_api(
            '/api/scenarios/{id}/launch', 'PUT',
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

    def quick_build1(self, id, **kwargs):  # noqa: E501
        """Launch System  # noqa: E501

        Launches a Deployment created from the specified System, with the provided Run Options.<br> <br> A root password can be set within the provided Deployment Run Options, which will override the password for all Hosts.<br> <br> The override of Host passwords may fail due to template password complexity rules and should not be done without consideration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.quick_build1(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of system (required)
        :param InputDeploymentRunOptions input_deployment_run_options: The deployment run options to use when launching the deployment
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
        return self.quick_build1_with_http_info(id, **kwargs)  # noqa: E501

    def quick_build1_with_http_info(self, id, **kwargs):  # noqa: E501
        """Launch System  # noqa: E501

        Launches a Deployment created from the specified System, with the provided Run Options.<br> <br> A root password can be set within the provided Deployment Run Options, which will override the password for all Hosts.<br> <br> The override of Host passwords may fail due to template password complexity rules and should not be done without consideration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.quick_build1_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of system (required)
        :param InputDeploymentRunOptions input_deployment_run_options: The deployment run options to use when launching the deployment
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

        all_params = ['id', 'input_deployment_run_options']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method quick_build1" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `quick_build1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'input_deployment_run_options' in local_var_params:
            body_params = local_var_params['input_deployment_run_options']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'Username']  # noqa: E501

        return self.api_client.call_api(
            '/api/systems/{id}/launch', 'PUT',
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

    def remove_trusted_project(self, id, trustedid, **kwargs):  # noqa: E501
        """Unassign Trusted Project from Asset  # noqa: E501

        Removes the provided Project from the Asset's list of Trusted Projects.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_trusted_project(id, trustedid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of asset (required)
        :param str trustedid: ID of project to untrust (required)
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
        return self.remove_trusted_project_with_http_info(id, trustedid, **kwargs)  # noqa: E501

    def remove_trusted_project_with_http_info(self, id, trustedid, **kwargs):  # noqa: E501
        """Unassign Trusted Project from Asset  # noqa: E501

        Removes the provided Project from the Asset's list of Trusted Projects.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_trusted_project_with_http_info(id, trustedid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of asset (required)
        :param str trustedid: ID of project to untrust (required)
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

        all_params = ['id', 'trustedid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_trusted_project" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `remove_trusted_project`")  # noqa: E501
        # verify the required parameter 'trustedid' is set
        if self.api_client.client_side_validation and ('trustedid' not in local_var_params or  # noqa: E501
                                                        local_var_params['trustedid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `trustedid` when calling `remove_trusted_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'trustedid' in local_var_params and local_var_params['trustedid'] is not None:  # noqa: E501
            query_params.append(('trustedid', local_var_params['trustedid']))  # noqa: E501

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
            '/api/assets/{id}/removetrustedproject', 'PUT',
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

    def update_asset(self, id, **kwargs):  # noqa: E501
        """Update Asset  # noqa: E501

        Updates the metadata of a single Asset with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_asset(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of asset (required)
        :param InputAssetForUpdate input_asset_for_update: The modified Asset metadata
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
        return self.update_asset_with_http_info(id, **kwargs)  # noqa: E501

    def update_asset_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update Asset  # noqa: E501

        Updates the metadata of a single Asset with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_asset_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of asset (required)
        :param InputAssetForUpdate input_asset_for_update: The modified Asset metadata
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

        all_params = ['id', 'input_asset_for_update']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_asset" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `update_asset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'input_asset_for_update' in local_var_params:
            body_params = local_var_params['input_asset_for_update']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'Username']  # noqa: E501

        return self.api_client.call_api(
            '/api/assets/{id}/update', 'PUT',
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

    def update_asset_state(self, id, state, **kwargs):  # noqa: E501
        """Update State  # noqa: E501

        Updates the state of a single Asset with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_asset_state(id, state, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of asset to delete (required)
        :param str state: The new asset state type (required)
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
        return self.update_asset_state_with_http_info(id, state, **kwargs)  # noqa: E501

    def update_asset_state_with_http_info(self, id, state, **kwargs):  # noqa: E501
        """Update State  # noqa: E501

        Updates the state of a single Asset with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_asset_state_with_http_info(id, state, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of asset to delete (required)
        :param str state: The new asset state type (required)
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

        all_params = ['id', 'state']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_asset_state" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `update_asset_state`")  # noqa: E501
        # verify the required parameter 'state' is set
        if self.api_client.client_side_validation and ('state' not in local_var_params or  # noqa: E501
                                                        local_var_params['state'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `state` when calling `update_asset_state`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'state' in local_var_params and local_var_params['state'] is not None:  # noqa: E501
            query_params.append(('state', local_var_params['state']))  # noqa: E501

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
            '/api/assets/{id}/updatestate', 'PUT',
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

    def update_asset_visibility_query(self, id, visibility, **kwargs):  # noqa: E501
        """Update Visibility  # noqa: E501

        Updates the visibility of a single Asset with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_asset_visibility_query(id, visibility, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of asset to update (required)
        :param str visibility: The new asset visibility type (required)
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
        return self.update_asset_visibility_query_with_http_info(id, visibility, **kwargs)  # noqa: E501

    def update_asset_visibility_query_with_http_info(self, id, visibility, **kwargs):  # noqa: E501
        """Update Visibility  # noqa: E501

        Updates the visibility of a single Asset with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_asset_visibility_query_with_http_info(id, visibility, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of asset to update (required)
        :param str visibility: The new asset visibility type (required)
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

        all_params = ['id', 'visibility']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_asset_visibility_query" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `update_asset_visibility_query`")  # noqa: E501
        # verify the required parameter 'visibility' is set
        if self.api_client.client_side_validation and ('visibility' not in local_var_params or  # noqa: E501
                                                        local_var_params['visibility'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `visibility` when calling `update_asset_visibility_query`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'visibility' in local_var_params and local_var_params['visibility'] is not None:  # noqa: E501
            query_params.append(('visibility', local_var_params['visibility']))  # noqa: E501

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
            '/api/assets/{id}/updatevisibility', 'PUT',
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

    def update_impact_level(self, id, impactlevel, **kwargs):  # noqa: E501
        """Update Impact Level  # noqa: E501

        Updates the Impact Level of a single Asset with the given ID.<br> <br >Maximum Impact Level can only be set to DOD_LEVEL_6 if allowed in the Environment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_impact_level(id, impactlevel, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of asset (required)
        :param str impactlevel: The new asset impact level type. (required)
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
        return self.update_impact_level_with_http_info(id, impactlevel, **kwargs)  # noqa: E501

    def update_impact_level_with_http_info(self, id, impactlevel, **kwargs):  # noqa: E501
        """Update Impact Level  # noqa: E501

        Updates the Impact Level of a single Asset with the given ID.<br> <br >Maximum Impact Level can only be set to DOD_LEVEL_6 if allowed in the Environment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_impact_level_with_http_info(id, impactlevel, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of asset (required)
        :param str impactlevel: The new asset impact level type. (required)
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

        all_params = ['id', 'impactlevel']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_impact_level" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `update_impact_level`")  # noqa: E501
        # verify the required parameter 'impactlevel' is set
        if self.api_client.client_side_validation and ('impactlevel' not in local_var_params or  # noqa: E501
                                                        local_var_params['impactlevel'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `impactlevel` when calling `update_impact_level`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'impactlevel' in local_var_params and local_var_params['impactlevel'] is not None:  # noqa: E501
            query_params.append(('impactlevel', local_var_params['impactlevel']))  # noqa: E501

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
            '/api/assets/{id}/impactlevel', 'PUT',
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

    def update_instance_limit(self, id, limit, **kwargs):  # noqa: E501
        """Update Instance Limit  # noqa: E501

        Updates the instance limit of a single Asset with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_instance_limit(id, limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of asset (required)
        :param int limit: The new asset instance limit (required)
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
        return self.update_instance_limit_with_http_info(id, limit, **kwargs)  # noqa: E501

    def update_instance_limit_with_http_info(self, id, limit, **kwargs):  # noqa: E501
        """Update Instance Limit  # noqa: E501

        Updates the instance limit of a single Asset with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_instance_limit_with_http_info(id, limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of asset (required)
        :param int limit: The new asset instance limit (required)
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

        all_params = ['id', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_instance_limit" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `update_instance_limit`")  # noqa: E501
        # verify the required parameter 'limit' is set
        if self.api_client.client_side_validation and ('limit' not in local_var_params or  # noqa: E501
                                                        local_var_params['limit'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `limit` when calling `update_instance_limit`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501

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
            '/api/assets/{id}/limit', 'PUT',
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

    def update_offline_status(self, id, **kwargs):  # noqa: E501
        """Update Offline Status  # noqa: E501

        Updates the Offline Status of a single Asset with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_offline_status(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of asset to update (required)
        :param bool offline: Set the asset status to offline
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
        return self.update_offline_status_with_http_info(id, **kwargs)  # noqa: E501

    def update_offline_status_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update Offline Status  # noqa: E501

        Updates the Offline Status of a single Asset with the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_offline_status_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of asset to update (required)
        :param bool offline: Set the asset status to offline
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

        all_params = ['id', 'offline']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_offline_status" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `update_offline_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'offline' in local_var_params and local_var_params['offline'] is not None:  # noqa: E501
            query_params.append(('offline', local_var_params['offline']))  # noqa: E501

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
            '/api/assets/{id}/offline', 'PUT',
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
