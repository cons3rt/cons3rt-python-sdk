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


class StorageApi(object):
    """NOTE: This class is auto-generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_bucket(self, bucket, **kwargs):  # noqa: E501
        """Create Storage Bucket  # noqa: E501

        Creates a storage bucket as defined by the user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_bucket(bucket, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param Bucket bucket: The bucket creation information (required)
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
        return self.create_bucket_with_http_info(bucket, **kwargs)  # noqa: E501

    def create_bucket_with_http_info(self, bucket, **kwargs):  # noqa: E501
        """Create Storage Bucket  # noqa: E501

        Creates a storage bucket as defined by the user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_bucket_with_http_info(bucket, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param Bucket bucket: The bucket creation information (required)
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

        all_params = ['bucket']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_bucket" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'bucket' is set
        if self.api_client.client_side_validation and ('bucket' not in local_var_params or  # noqa: E501
                                                        local_var_params['bucket'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `bucket` when calling `create_bucket`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'bucket' in local_var_params:
            body_params = local_var_params['bucket']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'Username']  # noqa: E501

        return self.api_client.call_api(
            '/api/buckets', 'POST',
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

    def delete_bucket(self, id, **kwargs):  # noqa: E501
        """Delete Storage Buckets  # noqa: E501

        Deletes an existing storage bucket by identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_bucket(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of bucket (required)
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
        return self.delete_bucket_with_http_info(id, **kwargs)  # noqa: E501

    def delete_bucket_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete Storage Buckets  # noqa: E501

        Deletes an existing storage bucket by identifier  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_bucket_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of bucket (required)
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
                    " to method delete_bucket" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `delete_bucket`")  # noqa: E501

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
            '/api/buckets/{id}', 'DELETE',
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

    def download_file_from_bucket(self, id, file_name, **kwargs):  # noqa: E501
        """Download File From Bucket  # noqa: E501

        Downloads the Asset in the form of a zip file. Download is only available for importable Asset types (i.e. Software, Test, and Container).<br> <br> Based on the background flag, the download will be done in the foreground (false), background (true), or in a location as determined by Asset size (default).<br> <br> If the background flag is set to true (or if no value for the background flag is provided), and the Asset is larger than the site threshold, the Asset will be prepared for download in the background.In that case, an email with a link to retrieve the Asset will be sent.If the Asset is larger than download threshold, it will be prepared for download in the background, and an email with a download link will be sent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_file_from_bucket(id, file_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of bucket (required)
        :param str file_name: The filename within the bucket to download (required)
        :param bool background: Force the download to happen in the background
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
        return self.download_file_from_bucket_with_http_info(id, file_name, **kwargs)  # noqa: E501

    def download_file_from_bucket_with_http_info(self, id, file_name, **kwargs):  # noqa: E501
        """Download File From Bucket  # noqa: E501

        Downloads the Asset in the form of a zip file. Download is only available for importable Asset types (i.e. Software, Test, and Container).<br> <br> Based on the background flag, the download will be done in the foreground (false), background (true), or in a location as determined by Asset size (default).<br> <br> If the background flag is set to true (or if no value for the background flag is provided), and the Asset is larger than the site threshold, the Asset will be prepared for download in the background.In that case, an email with a link to retrieve the Asset will be sent.If the Asset is larger than download threshold, it will be prepared for download in the background, and an email with a download link will be sent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_file_from_bucket_with_http_info(id, file_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of bucket (required)
        :param str file_name: The filename within the bucket to download (required)
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
        :return: tuple(bool, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'file_name', 'background']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_file_from_bucket" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `download_file_from_bucket`")  # noqa: E501
        # verify the required parameter 'file_name' is set
        if self.api_client.client_side_validation and ('file_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['file_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `file_name` when calling `download_file_from_bucket`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'file_name' in local_var_params and local_var_params['file_name'] is not None:  # noqa: E501
            query_params.append(('fileName', local_var_params['file_name']))  # noqa: E501
        if 'background' in local_var_params and local_var_params['background'] is not None:  # noqa: E501
            query_params.append(('background', local_var_params['background']))  # noqa: E501

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
            '/api/buckets/{id}/download', 'GET',
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

    def get_bucket(self, id, **kwargs):  # noqa: E501
        """Retrieve Storage Buckets  # noqa: E501

        returns a storage bucket  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bucket(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of bucket (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Bucket
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_bucket_with_http_info(id, **kwargs)  # noqa: E501

    def get_bucket_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve Storage Buckets  # noqa: E501

        returns a storage bucket  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bucket_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of bucket (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Bucket, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_bucket" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `get_bucket`")  # noqa: E501

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
            '/api/buckets/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Bucket',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_bucket_listing(self, id, **kwargs):  # noqa: E501
        """List Bucket Contents  # noqa: E501

        lists all files contents for an existing bucket  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bucket_listing(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of bucket (required)
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
        return self.get_bucket_listing_with_http_info(id, **kwargs)  # noqa: E501

    def get_bucket_listing_with_http_info(self, id, **kwargs):  # noqa: E501
        """List Bucket Contents  # noqa: E501

        lists all files contents for an existing bucket  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bucket_listing_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of bucket (required)
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
                    " to method get_bucket_listing" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `get_bucket_listing`")  # noqa: E501

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
            '/api/buckets/{id}/listing', 'GET',
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

    def list_available_clouds_for_buckets(self, **kwargs):  # noqa: E501
        """List Clouds Available For Bucket Creation  # noqa: E501

        returns a collection of clouds accessible to the user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_available_clouds_for_buckets(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int maxresults: Maximum number of results to return
        :param int page: Requested page number
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[MinimalCloud]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_available_clouds_for_buckets_with_http_info(**kwargs)  # noqa: E501

    def list_available_clouds_for_buckets_with_http_info(self, **kwargs):  # noqa: E501
        """List Clouds Available For Bucket Creation  # noqa: E501

        returns a collection of clouds accessible to the user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_available_clouds_for_buckets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
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
        :return: tuple(list[MinimalCloud], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['maxresults', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_available_clouds_for_buckets" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/api/buckets/clouds', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MinimalCloud]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_buckets(self, **kwargs):  # noqa: E501
        """List Storage Buckets  # noqa: E501

        returns a collection of storage buckets  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_buckets(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str cloud: ID of the cloud
        :param bool project: Include project buckets
        :param int maxresults: Maximum number of results to return
        :param int page: Requested page number
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[Bucket]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_buckets_with_http_info(**kwargs)  # noqa: E501

    def list_buckets_with_http_info(self, **kwargs):  # noqa: E501
        """List Storage Buckets  # noqa: E501

        returns a collection of storage buckets  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_buckets_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str cloud: ID of the cloud
        :param bool project: Include project buckets
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
        :return: tuple(list[Bucket], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['cloud', 'project', 'maxresults', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_buckets" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cloud' in local_var_params and local_var_params['cloud'] is not None:  # noqa: E501
            query_params.append(('cloud', local_var_params['cloud']))  # noqa: E501
        if 'project' in local_var_params and local_var_params['project'] is not None:  # noqa: E501
            query_params.append(('project', local_var_params['project']))  # noqa: E501
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
            '/api/buckets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Bucket]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def submit_bucket_resource_to_submission_service(self, id, submission_service_id, file_name, **kwargs):  # noqa: E501
        """Submit Bucket Resource to the Project's Submission Service  # noqa: E501

        Publishes a resource in the specified bucket to the requested Submission Service.<br> <br> The requested Project Submission Service will act as a template. Credentials provided when submitting to the Service will override the Project Submission Service's credentials. However, neither the Host nor Port of the Service can be overridden.<br> <br> If the Service's endpoint is an SFTP Host, the Submission will only be able to override the remote path (i.e. if one has not already been defined in this default Submission Service).<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submit_bucket_resource_to_submission_service(id, submission_service_id, file_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of the bucket to publish a resource from (required)
        :param str submission_service_id: ID of project submission service (required)
        :param str file_name: The filename within the bucket to download (required)
        :param InputSubmissionServiceForAssetSubmission input_submission_service_for_asset_submission: Submission service override values
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
        return self.submit_bucket_resource_to_submission_service_with_http_info(id, submission_service_id, file_name, **kwargs)  # noqa: E501

    def submit_bucket_resource_to_submission_service_with_http_info(self, id, submission_service_id, file_name, **kwargs):  # noqa: E501
        """Submit Bucket Resource to the Project's Submission Service  # noqa: E501

        Publishes a resource in the specified bucket to the requested Submission Service.<br> <br> The requested Project Submission Service will act as a template. Credentials provided when submitting to the Service will override the Project Submission Service's credentials. However, neither the Host nor Port of the Service can be overridden.<br> <br> If the Service's endpoint is an SFTP Host, the Submission will only be able to override the remote path (i.e. if one has not already been defined in this default Submission Service).<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submit_bucket_resource_to_submission_service_with_http_info(id, submission_service_id, file_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of the bucket to publish a resource from (required)
        :param str submission_service_id: ID of project submission service (required)
        :param str file_name: The filename within the bucket to download (required)
        :param InputSubmissionServiceForAssetSubmission input_submission_service_for_asset_submission: Submission service override values
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

        all_params = ['id', 'submission_service_id', 'file_name', 'input_submission_service_for_asset_submission']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method submit_bucket_resource_to_submission_service" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `submit_bucket_resource_to_submission_service`")  # noqa: E501
        # verify the required parameter 'submission_service_id' is set
        if self.api_client.client_side_validation and ('submission_service_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['submission_service_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `submission_service_id` when calling `submit_bucket_resource_to_submission_service`")  # noqa: E501
        # verify the required parameter 'file_name' is set
        if self.api_client.client_side_validation and ('file_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['file_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `file_name` when calling `submit_bucket_resource_to_submission_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501
        if 'submission_service_id' in local_var_params:
            path_params['submission_service_id'] = local_var_params['submission_service_id']  # noqa: E501

        query_params = []
        if 'file_name' in local_var_params and local_var_params['file_name'] is not None:  # noqa: E501
            query_params.append(('fileName', local_var_params['file_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'input_submission_service_for_asset_submission' in local_var_params:
            body_params = local_var_params['input_submission_service_for_asset_submission']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'Username']  # noqa: E501

        return self.api_client.call_api(
            '/api/buckets/{id}/submit/{submission_service_id}', 'POST',
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

    def update_bucket(self, id, bucket, **kwargs):  # noqa: E501
        """Update Storage Buckets  # noqa: E501

        updates the configuration information for an existing bucket  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_bucket(id, bucket, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of bucket (required)
        :param Bucket bucket: The bucket creation information (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Bucket
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_bucket_with_http_info(id, bucket, **kwargs)  # noqa: E501

    def update_bucket_with_http_info(self, id, bucket, **kwargs):  # noqa: E501
        """Update Storage Buckets  # noqa: E501

        updates the configuration information for an existing bucket  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_bucket_with_http_info(id, bucket, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of bucket (required)
        :param Bucket bucket: The bucket creation information (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Bucket, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'bucket']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_bucket" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `update_bucket`")  # noqa: E501
        # verify the required parameter 'bucket' is set
        if self.api_client.client_side_validation and ('bucket' not in local_var_params or  # noqa: E501
                                                        local_var_params['bucket'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `bucket` when calling `update_bucket`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'bucket' in local_var_params:
            body_params = local_var_params['bucket']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'Username']  # noqa: E501

        return self.api_client.call_api(
            '/api/buckets/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Bucket',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upload_file_to_bucket(self, id, **kwargs):  # noqa: E501
        """Upload File to Bucket  # noqa: E501

        Uploads a file to a bucket.<br> <br> File must be submitted as multipart-form data, with a file element named \"file\" and a filename field <br> <br> A \"Connection: Keep-Alive\" configuration may be needed for larger sized files, due to the time it takes to copy to the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_file_to_bucket(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of bucket (required)
        :param list[file] file:
        :param str filename:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.upload_file_to_bucket_with_http_info(id, **kwargs)  # noqa: E501

    def upload_file_to_bucket_with_http_info(self, id, **kwargs):  # noqa: E501
        """Upload File to Bucket  # noqa: E501

        Uploads a file to a bucket.<br> <br> File must be submitted as multipart-form data, with a file element named \"file\" and a filename field <br> <br> A \"Connection: Keep-Alive\" configuration may be needed for larger sized files, due to the time it takes to copy to the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_file_to_bucket_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: ID of bucket (required)
        :param list[file] file:
        :param str filename:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(int, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'file', 'filename']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_file_to_bucket" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `upload_file_to_bucket`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in local_var_params:
            local_var_files['file'] = local_var_params['file']  # noqa: E501
            collection_formats['file'] = 'csv'  # noqa: E501
        if 'filename' in local_var_params:
            form_params.append(('filename', local_var_params['filename']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'Username']  # noqa: E501

        return self.api_client.call_api(
            '/api/buckets/{id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
