# intrinio_sdk.MutualFundApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_mutual_funds**](MutualFundApi.md#get_all_mutual_funds) | **GET** /mutual_funds | Get All Mutual Funds
[**get_mutual_fund_by_id**](MutualFundApi.md#get_mutual_fund_by_id) | **GET** /mutual_funds/{identifier} | Get a Mutual Fund by ID
[**get_mutual_fund_stats**](MutualFundApi.md#get_mutual_fund_stats) | **GET** /mutual_funds/{identifier}/stats | Get Stats for a Mutual Fund
[**search_mutual_funds**](MutualFundApi.md#search_mutual_funds) | **GET** /mutual_funds/search | Search Mutual Funds


# **get_all_mutual_funds**
> list[MutualFund] get_all_mutual_funds(next_page=next_page)

Get All Mutual Funds

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api-key'] = 'YOUR_API_KEY'

mutual_fund_api = intrinio_sdk.MutualFundApi()

next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = mutual_fund_api.get_all_mutual_funds(next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MutualFundApi->get_all_mutual_funds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**list[MutualFund]**](MutualFund.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mutual_fund_by_id**
> MutualFund get_mutual_fund_by_id(identifier)

Get a Mutual Fund by ID

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api-key'] = 'YOUR_API_KEY'

mutual_fund_api = intrinio_sdk.MutualFundApi()

identifier = 'identifier_example' # str | A Mutual Fund identifier (CUSIP, Intrinio ID)

try:
    api_response = mutual_fund_api.get_mutual_fund_by_id(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MutualFundApi->get_mutual_fund_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Mutual Fund identifier (CUSIP, Intrinio ID) | 

### Return type

[**MutualFund**](MutualFund.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mutual_fund_stats**
> list[MutualFundStat] get_mutual_fund_stats(identifier, start_date=start_date, end_date=end_date, next_page=next_page)

Get Stats for a Mutual Fund

Returns stats for the  Mutual Fund with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api-key'] = 'YOUR_API_KEY'

mutual_fund_api = intrinio_sdk.MutualFundApi()

identifier = 'identifier_example' # str | A Mutual Fund identifier (CUSIP, Intrinio ID)
start_date = '2013-10-20' # date | Return stats on or after the date (optional)
end_date = '2013-10-20' # date | Return stats on or before the date (optional)
next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = mutual_fund_api.get_mutual_fund_stats(identifier, start_date=start_date, end_date=end_date, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MutualFundApi->get_mutual_fund_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Mutual Fund identifier (CUSIP, Intrinio ID) | 
 **start_date** | **date**| Return stats on or after the date | [optional] 
 **end_date** | **date**| Return stats on or before the date | [optional] 
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**list[MutualFundStat]**](MutualFundStat.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_mutual_funds**
> list[MutualFund] search_mutual_funds(query, next_page=next_page)

Search Mutual Funds

Searches for Mutual Funds matching the text `query`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api-key'] = 'YOUR_API_KEY'

mutual_fund_api = intrinio_sdk.MutualFundApi()

query = 'query_example' # str | 
next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = mutual_fund_api.search_mutual_funds(query, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MutualFundApi->search_mutual_funds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**list[MutualFund]**](MutualFund.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

