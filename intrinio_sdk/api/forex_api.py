# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.64.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from intrinio_sdk.api_client import ApiClient


class ForexApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_forex_currencies(self, **kwargs):  # noqa: E501
        """Forex Currencies  # noqa: E501

        Returns a list of forex currencies for which prices are available.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_forex_currencies(_async=True)
        >>> result = thread.get()

        :param async bool
        :return: ApiResponseForexCurrencies
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_forex_currencies_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_forex_currencies_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_forex_currencies_with_http_info(self, **kwargs):  # noqa: E501
        """Forex Currencies  # noqa: E501

        Returns a list of forex currencies for which prices are available.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_forex_currencies_with_http_info(_async=True)
        >>> result = thread.get()

        :param async bool
        :return: ApiResponseForexCurrencies
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_forex_currencies" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/forex/currencies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseForexCurrencies',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_forex_pairs(self, **kwargs):  # noqa: E501
        """Forex Currency Pairs  # noqa: E501

        Returns a list of currency pairs used to request foreign exchange (forex) market price data. The currency that is used as the reference is called quote currency and the currency that is quoted in relation is called the base currency. For example, in the pair code “EURGBP” with a price of 0.88, one Euro (base currency) can be exchanged for 0.88 British Pounds (quote currency).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_forex_pairs(_async=True)
        >>> result = thread.get()

        :param async bool
        :return: ApiResponseForexPairs
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_forex_pairs_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_forex_pairs_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_forex_pairs_with_http_info(self, **kwargs):  # noqa: E501
        """Forex Currency Pairs  # noqa: E501

        Returns a list of currency pairs used to request foreign exchange (forex) market price data. The currency that is used as the reference is called quote currency and the currency that is quoted in relation is called the base currency. For example, in the pair code “EURGBP” with a price of 0.88, one Euro (base currency) can be exchanged for 0.88 British Pounds (quote currency).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_forex_pairs_with_http_info(_async=True)
        >>> result = thread.get()

        :param async bool
        :return: ApiResponseForexPairs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_forex_pairs" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/forex/pairs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseForexPairs',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_forex_prices(self, pair, timeframe, **kwargs):  # noqa: E501
        """Forex Currency Prices  # noqa: E501

        Provides a list of forex price quotes for a given forex currency pair and timeframe.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_forex_prices(pair, timeframe, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str pair: The Forex Currency Pair code (required)
        :param str timeframe: The time interval for the quotes (required)
        :param str timezone: Returns trading times in this timezone
        :param date start_date: Return Forex Prices on or after this date
        :param str start_time: Return Forex Prices at or after this time (24-hour in 'hh:mm' format, UTC timezone)
        :param date end_date: Return Forex Prices on or before this date
        :param str end_time: Return Forex Prices at or before this time (24-hour in 'hh:mm' format, UTC timezone)
        :param int page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseForexPrices
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_forex_prices_with_http_info(pair, timeframe, **kwargs)  # noqa: E501
        else:
            (data) = self.get_forex_prices_with_http_info(pair, timeframe, **kwargs)  # noqa: E501
            return data

    def get_forex_prices_with_http_info(self, pair, timeframe, **kwargs):  # noqa: E501
        """Forex Currency Prices  # noqa: E501

        Provides a list of forex price quotes for a given forex currency pair and timeframe.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_forex_prices_with_http_info(pair, timeframe, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str pair: The Forex Currency Pair code (required)
        :param str timeframe: The time interval for the quotes (required)
        :param str timezone: Returns trading times in this timezone
        :param date start_date: Return Forex Prices on or after this date
        :param str start_time: Return Forex Prices at or after this time (24-hour in 'hh:mm' format, UTC timezone)
        :param date end_date: Return Forex Prices on or before this date
        :param str end_time: Return Forex Prices at or before this time (24-hour in 'hh:mm' format, UTC timezone)
        :param int page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseForexPrices
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pair', 'timeframe', 'timezone', 'start_date', 'start_time', 'end_date', 'end_time', 'page_size', 'next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_forex_prices" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pair' is set
        if ('pair' not in params or
                params['pair'] is None):
            raise ValueError("Missing the required parameter `pair` when calling `get_forex_prices`")  # noqa: E501
        # verify the required parameter 'timeframe' is set
        if ('timeframe' not in params or
                params['timeframe'] is None):
            raise ValueError("Missing the required parameter `timeframe` when calling `get_forex_prices`")  # noqa: E501

        if 'page_size' in params and params['page_size'] > 10000:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_forex_prices`, must be a value less than or equal to `10000`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'pair' in params:
            path_params['pair'] = params['pair']  # noqa: E501
        if 'timeframe' in params:
            path_params['timeframe'] = params['timeframe']  # noqa: E501

        query_params = []
        if 'timezone' in params:
            query_params.append(('timezone', params['timezone']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'start_time' in params:
            query_params.append(('start_time', params['start_time']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('end_time', params['end_time']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
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
            '/forex/prices/{pair}/{timeframe}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseForexPrices',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
