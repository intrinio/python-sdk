# intrinio_sdk.StandardizedTagApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_standardized_tags**](StandardizedTagApi.md#filter_standardized_tags) | **GET** /standardized_tags/filter | Filter Standardized Tags
[**get_all_standardized_tags**](StandardizedTagApi.md#get_all_standardized_tags) | **GET** /standardized_tags | Get All Standardized Tags
[**get_standardized_tag_by_id**](StandardizedTagApi.md#get_standardized_tag_by_id) | **GET** /standardized_tags/{tag_id} | Get a Standardized Tag by ID
[**get_standardized_tag_data_point_number**](StandardizedTagApi.md#get_standardized_tag_data_point_number) | **GET** /standardized_tags/{id}/data_point/{identifier}/number | Get Data Point (Number) for The Standardized Tag
[**get_standardized_tag_data_point_text**](StandardizedTagApi.md#get_standardized_tag_data_point_text) | **GET** /standardized_tags/{id}/data_point/{identifier}/text | Get Data Point (Text) for the Standardized Tag
[**get_standardized_tag_historical_data**](StandardizedTagApi.md#get_standardized_tag_historical_data) | **GET** /standardized_tags/{id}/historical_data/{identifier} | Get Historical Data for the Standardized Tag
[**search_standardized_tags**](StandardizedTagApi.md#search_standardized_tags) | **GET** /standardized_tags/search | Search Standardized Tags


# **filter_standardized_tags**
> list[StandardizedTag] filter_standardized_tags(tag=tag, type=type, parent=parent, statement_code=statement_code, fs_template=fs_template, next_page=next_page)

Filter Standardized Tags

Returns Standarized Tags that match the given filters

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'

standardized_tag_api = intrinio_sdk.StandardizedTagApi()

tag = 'tag_example' # str | Tag (optional)
type = 'type_example' # str | Type (optional)
parent = 'parent_example' # str | ID of tag parent (optional)
statement_code = 'statement_code_example' # str | Statement Code (optional)
fs_template = 'industrial' # str | Template (optional) (default to industrial)
next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = standardized_tag_api.filter_standardized_tags(tag=tag, type=type, parent=parent, statement_code=statement_code, fs_template=fs_template, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandardizedTagApi->filter_standardized_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Tag | [optional] 
 **type** | **str**| Type | [optional] 
 **parent** | **str**| ID of tag parent | [optional] 
 **statement_code** | **str**| Statement Code | [optional] 
 **fs_template** | **str**| Template | [optional] [default to industrial]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**list[StandardizedTag]**](StandardizedTag.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_standardized_tags**
> list[StandardizedTag] get_all_standardized_tags(next_page=next_page)

Get All Standardized Tags

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'

standardized_tag_api = intrinio_sdk.StandardizedTagApi()

next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = standardized_tag_api.get_all_standardized_tags(next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandardizedTagApi->get_all_standardized_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**list[StandardizedTag]**](StandardizedTag.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_standardized_tag_by_id**
> StandardizedTag get_standardized_tag_by_id(tag_id)

Get a Standardized Tag by ID

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'

standardized_tag_api = intrinio_sdk.StandardizedTagApi()

tag_id = 'tag_id_example' # str | The Intrinio ID for the tag

try:
    api_response = standardized_tag_api.get_standardized_tag_by_id(tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandardizedTagApi->get_standardized_tag_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| The Intrinio ID for the tag | 

### Return type

[**StandardizedTag**](StandardizedTag.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_standardized_tag_data_point_number**
> DataPointNumber get_standardized_tag_data_point_number(id, identifier)

Get Data Point (Number) for The Standardized Tag

Returns a numeric data point for the Standardized Tag and entity `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'

standardized_tag_api = intrinio_sdk.StandardizedTagApi()

id = 'id_example' # str | The Intrinio Standardized Tag ID or its tag
identifier = 'identifier_example' # str | An identifier for an entity such as a Company, Security, Index, etc (Ticker, FIGI, ISIN, CUSIP, CIK, LEI, Intrinio ID)

try:
    api_response = standardized_tag_api.get_standardized_tag_data_point_number(id, identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandardizedTagApi->get_standardized_tag_data_point_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Intrinio Standardized Tag ID or its tag | 
 **identifier** | **str**| An identifier for an entity such as a Company, Security, Index, etc (Ticker, FIGI, ISIN, CUSIP, CIK, LEI, Intrinio ID) | 

### Return type

[**DataPointNumber**](DataPointNumber.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_standardized_tag_data_point_text**
> DataPointText get_standardized_tag_data_point_text(id, identifier)

Get Data Point (Text) for the Standardized Tag

Returns a text data point for the Standardized Tag and entity `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'

standardized_tag_api = intrinio_sdk.StandardizedTagApi()

id = 'id_example' # str | The Intrinio Standardized Tag ID or its tag
identifier = 'identifier_example' # str | An identifier for an entity such as a Company, Security, Index, etc (Ticker, FIGI, ISIN, CUSIP, CIK, LEI, Intrinio ID)

try:
    api_response = standardized_tag_api.get_standardized_tag_data_point_text(id, identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandardizedTagApi->get_standardized_tag_data_point_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Intrinio Standardized Tag ID or its tag | 
 **identifier** | **str**| An identifier for an entity such as a Company, Security, Index, etc (Ticker, FIGI, ISIN, CUSIP, CIK, LEI, Intrinio ID) | 

### Return type

[**DataPointText**](DataPointText.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_standardized_tag_historical_data**
> list[HistoricalData] get_standardized_tag_historical_data(id, identifier, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, next_page=next_page)

Get Historical Data for the Standardized Tag

Returns historical values for the Standardized Tag and the Entity represented by the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'

standardized_tag_api = intrinio_sdk.StandardizedTagApi()

id = 'id_example' # str | The Intrinio Standardized Tag ID or its tag
identifier = 'identifier_example' # str | An identifier for an entity such as a Company, Security, Index, etc (Ticker, FIGI, ISIN, CUSIP, CIK, LEI, Intrinio ID)
type = 'type_example' # str | Filter by type, when applicable (optional)
start_date = '2013-10-20' # date | Get historical data on or after this date (optional)
end_date = '2013-10-20' # date | Get historical date on or before this date (optional)
sort_order = 'desc' # str | Sort by date `asc` or `desc` (optional) (default to desc)
next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = standardized_tag_api.get_standardized_tag_historical_data(id, identifier, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandardizedTagApi->get_standardized_tag_historical_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Intrinio Standardized Tag ID or its tag | 
 **identifier** | **str**| An identifier for an entity such as a Company, Security, Index, etc (Ticker, FIGI, ISIN, CUSIP, CIK, LEI, Intrinio ID) | 
 **type** | **str**| Filter by type, when applicable | [optional] 
 **start_date** | **date**| Get historical data on or after this date | [optional] 
 **end_date** | **date**| Get historical date on or before this date | [optional] 
 **sort_order** | **str**| Sort by date &#x60;asc&#x60; or &#x60;desc&#x60; | [optional] [default to desc]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**list[HistoricalData]**](HistoricalData.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_standardized_tags**
> list[StandardizedTag] search_standardized_tags(query, next_page=next_page)

Search Standardized Tags

Searches for Standardized Tags matching the text `query`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'

standardized_tag_api = intrinio_sdk.StandardizedTagApi()

query = 'query_example' # str | 
next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = standardized_tag_api.search_standardized_tags(query, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandardizedTagApi->search_standardized_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**list[StandardizedTag]**](StandardizedTag.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

