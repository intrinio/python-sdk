# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://docs.intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.34.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from intrinio_sdk.api_client import ApiClient


class MunicipalityApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_municipalities(self, **kwargs):  # noqa: E501
        """All Municipalities  # noqa: E501

        Returns all Municipalities. When parameters are specified, returns matching municipalities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_municipalities(_async=True)
        >>> result = thread.get()

        :param async bool
        :param bool has_financials: Return municipalities with financials
        :param str government_name: Return municipalities with a government name matching the given query
        :param str government_type: Return municipalities with the given government type
        :param str area_name: Return municipalities with an area name matching the given query
        :param str area_type: Return municipalities with the given area type
        :param str city: Return municipalities in the given city
        :param str state: Return municipalities in the given state
        :param float zipcode: Return municipalities in the given zipcode
        :param float population_greater_than: Return municipalities with a population greater than the given number
        :param float population_less_than: Return municipalities with a population less than the given number
        :param float enrollment_greater_than: Return municipalities with an enrollment greater than the given number
        :param float enrollment_less_than: Return municipalities with an enrollment less than the given number
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseMunicipalities
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_all_municipalities_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_municipalities_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_municipalities_with_http_info(self, **kwargs):  # noqa: E501
        """All Municipalities  # noqa: E501

        Returns all Municipalities. When parameters are specified, returns matching municipalities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_all_municipalities_with_http_info(_async=True)
        >>> result = thread.get()

        :param async bool
        :param bool has_financials: Return municipalities with financials
        :param str government_name: Return municipalities with a government name matching the given query
        :param str government_type: Return municipalities with the given government type
        :param str area_name: Return municipalities with an area name matching the given query
        :param str area_type: Return municipalities with the given area type
        :param str city: Return municipalities in the given city
        :param str state: Return municipalities in the given state
        :param float zipcode: Return municipalities in the given zipcode
        :param float population_greater_than: Return municipalities with a population greater than the given number
        :param float population_less_than: Return municipalities with a population less than the given number
        :param float enrollment_greater_than: Return municipalities with an enrollment greater than the given number
        :param float enrollment_less_than: Return municipalities with an enrollment less than the given number
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseMunicipalities
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['has_financials', 'government_name', 'government_type', 'area_name', 'area_type', 'city', 'state', 'zipcode', 'population_greater_than', 'population_less_than', 'enrollment_greater_than', 'enrollment_less_than', 'next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_municipalities" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'has_financials' in params:
            query_params.append(('has_financials', params['has_financials']))  # noqa: E501
        if 'government_name' in params:
            query_params.append(('government_name', params['government_name']))  # noqa: E501
        if 'government_type' in params:
            query_params.append(('government_type', params['government_type']))  # noqa: E501
        if 'area_name' in params:
            query_params.append(('area_name', params['area_name']))  # noqa: E501
        if 'area_type' in params:
            query_params.append(('area_type', params['area_type']))  # noqa: E501
        if 'city' in params:
            query_params.append(('city', params['city']))  # noqa: E501
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501
        if 'zipcode' in params:
            query_params.append(('zipcode', params['zipcode']))  # noqa: E501
        if 'population_greater_than' in params:
            query_params.append(('population_greater_than', params['population_greater_than']))  # noqa: E501
        if 'population_less_than' in params:
            query_params.append(('population_less_than', params['population_less_than']))  # noqa: E501
        if 'enrollment_greater_than' in params:
            query_params.append(('enrollment_greater_than', params['enrollment_greater_than']))  # noqa: E501
        if 'enrollment_less_than' in params:
            query_params.append(('enrollment_less_than', params['enrollment_less_than']))  # noqa: E501
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
            '/municipalities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseMunicipalities',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_municipality_by_id(self, id, **kwargs):  # noqa: E501
        """Municipality by ID  # noqa: E501

        Returns the Municipality with the given ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_municipality_by_id(id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: An Intrinio ID of a Municipality (required)
        :return: Municipality
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_municipality_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_municipality_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_municipality_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Municipality by ID  # noqa: E501

        Returns the Municipality with the given ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_municipality_by_id_with_http_info(id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: An Intrinio ID of a Municipality (required)
        :return: Municipality
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_municipality_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_municipality_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/municipalities/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Municipality',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_municipality_financials(self, id, **kwargs):  # noqa: E501
        """Financials for a Municipality  # noqa: E501

        Returns financial statement data for the Municipality with the given ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_municipality_financials(id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: An Intrinio ID of a Municipality (required)
        :param float fiscal_year: Return financials for the given fiscal year
        :return: ApiResponseMunicipalitiyFinancials
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_municipality_financials_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_municipality_financials_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_municipality_financials_with_http_info(self, id, **kwargs):  # noqa: E501
        """Financials for a Municipality  # noqa: E501

        Returns financial statement data for the Municipality with the given ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_municipality_financials_with_http_info(id, _async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: An Intrinio ID of a Municipality (required)
        :param float fiscal_year: Return financials for the given fiscal year
        :return: ApiResponseMunicipalitiyFinancials
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'fiscal_year']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_municipality_financials" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_municipality_financials`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'fiscal_year' in params:
            query_params.append(('fiscal_year', params['fiscal_year']))  # noqa: E501

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
            '/municipalities/{id}/financials', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseMunicipalitiyFinancials',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
