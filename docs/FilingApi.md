# intrinio_sdk.FilingApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_filings**](FilingApi.md#filter_filings) | **GET** /filings/filter | Filter Filings
[**get_all_filings**](FilingApi.md#get_all_filings) | **GET** /filings | Get All Filings
[**get_filing_by_id**](FilingApi.md#get_filing_by_id) | **GET** /filings/{id} | Get a Filing by ID


# **filter_filings**
> ApiResponseFilings filter_filings(company, report_type=report_type, start_date=start_date, end_date=end_date, next_page=next_page)

Filter Filings

Returns filings that match the specified filters

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

filing_api = intrinio_sdk.FilingApi()

company = 'company_example' # str | Filings for the given `company` identifier (ticker, CIK, LEI, Intrinio ID)
report_type = 'report_type_example' # str | Filter by report type (optional)
start_date = '2013-10-20' # date | Filed on or after the given date (optional)
end_date = '2013-10-20' # date | Filed before or after the given date (optional)
next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = filing_api.filter_filings(company, report_type=report_type, start_date=start_date, end_date=end_date, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilingApi->filter_filings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company** | **str**| Filings for the given &#x60;company&#x60; identifier (ticker, CIK, LEI, Intrinio ID) | 
 **report_type** | **str**| Filter by report type | [optional] 
 **start_date** | **date**| Filed on or after the given date | [optional] 
 **end_date** | **date**| Filed before or after the given date | [optional] 
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseFilings**](ApiResponseFilings.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_filings**
> ApiResponseFilings get_all_filings(next_page=next_page)

Get All Filings

Returns all filings

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

filing_api = intrinio_sdk.FilingApi()

next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = filing_api.get_all_filings(next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilingApi->get_all_filings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseFilings**](ApiResponseFilings.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filing_by_id**
> Filing get_filing_by_id(id)

Get a Filing by ID

Return the filing with the given ID

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

filing_api = intrinio_sdk.FilingApi()

id = 'id_example' # str | The Intrinio ID of the Filing

try:
    api_response = filing_api.get_filing_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilingApi->get_filing_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Intrinio ID of the Filing | 

### Return type

[**Filing**](Filing.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

