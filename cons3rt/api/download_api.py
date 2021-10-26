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


class DownloadApi(object):
    """NOTE: This class is auto-generated. Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

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
