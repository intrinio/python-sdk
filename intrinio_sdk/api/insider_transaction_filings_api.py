# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.76.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from intrinio_sdk.api_client import ApiClient


class InsiderTransactionFilingsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_insider_transaction_filings(self, **kwargs):  # noqa: E501
        """All Insider Transactions Filings  # noqa: E501

        Returns all insider transactions filings fitting the optional supplied start and end date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_insider_transaction_filings(_async=True)
        >>> result = thread.get()

        :param async bool
        :param date start_date: Filed on or after the given date
        :param date end_date: Filed before or after the given date
        :param int page_size: The number of results to return
        :param str sort_by: The field to sort by.  Default is 'filing_date'.  Valid values are - 'filing_date', 'updated_on'.
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseOwnerInsiderTransactionFilings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_all_insider_transaction_filings_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_insider_transaction_filings_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_insider_transaction_filings_with_http_info(self, **kwargs):  # noqa: E501
        """All Insider Transactions Filings  # noqa: E501

        Returns all insider transactions filings fitting the optional supplied start and end date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_insider_transaction_filings_with_http_info(_async=True)
        >>> result = thread.get()

        :param async bool
        :param date start_date: Filed on or after the given date
        :param date end_date: Filed before or after the given date
        :param int page_size: The number of results to return
        :param str sort_by: The field to sort by.  Default is 'filing_date'.  Valid values are - 'filing_date', 'updated_on'.
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseOwnerInsiderTransactionFilings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'page_size', 'sort_by', 'next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_insider_transaction_filings" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page_size' in params and params['page_size'] > 10000:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_all_insider_transaction_filings`, must be a value less than or equal to `10000`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501
        if 'next_page' in params:
            query_params.append(('next_page', params['next_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/insider_transaction_filings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseOwnerInsiderTransactionFilings',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
