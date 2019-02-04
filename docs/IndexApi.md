# intrinio_sdk.IndexApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_economic_indices**](IndexApi.md#get_all_economic_indices) | **GET** /indices/economic | All Economic Indices
[**get_all_sic_indices**](IndexApi.md#get_all_sic_indices) | **GET** /indices/sic | All SIC Indices
[**get_all_stock_market_indices**](IndexApi.md#get_all_stock_market_indices) | **GET** /indices/stock_market | All Stock Market Indices
[**get_economic_index_by_id**](IndexApi.md#get_economic_index_by_id) | **GET** /indices/economic/{identifier} | Lookup Economic Index
[**get_economic_index_data_point_number**](IndexApi.md#get_economic_index_data_point_number) | **GET** /indices/economic/{identifier}/data_point/{tag}/number | Data Point (Number) for an Economic Index
[**get_economic_index_data_point_text**](IndexApi.md#get_economic_index_data_point_text) | **GET** /indices/economic/{identifier}/data_point/{tag}/text | Data Point (Text) for an Economic Index
[**get_economic_index_historical_data**](IndexApi.md#get_economic_index_historical_data) | **GET** /indices/economic/{identifier}/historical_data/{tag} | Historical Data for an Economic Index
[**get_sic_index_by_id**](IndexApi.md#get_sic_index_by_id) | **GET** /indices/sic/{identifier} | Lookup SIC Index
[**get_sic_index_data_point_number**](IndexApi.md#get_sic_index_data_point_number) | **GET** /indices/sic/{identifier}/data_point/{tag}/number | Data Point (Number) for an SIC Index
[**get_sic_index_data_point_text**](IndexApi.md#get_sic_index_data_point_text) | **GET** /indices/sic/{identifier}/data_point/{tag}/text | Data Point (Text) for an SIC Index
[**get_sic_index_historical_data**](IndexApi.md#get_sic_index_historical_data) | **GET** /indices/sic/{identifier}/historical_data/{tag} | Historical Data for an SIC Index
[**get_stock_market_index_by_id**](IndexApi.md#get_stock_market_index_by_id) | **GET** /indices/stock_market/{identifier} | Lookup Stock Market Index
[**get_stock_market_index_data_point_number**](IndexApi.md#get_stock_market_index_data_point_number) | **GET** /indices/stock_market/{identifier}/data_point/{tag}/number | Data Point (Number) for Stock Market Index
[**get_stock_market_index_data_point_text**](IndexApi.md#get_stock_market_index_data_point_text) | **GET** /indices/stock_market/{identifier}/data_point/{tag}/text | Data Point (Text) for Stock Market Index
[**get_stock_market_index_historical_data**](IndexApi.md#get_stock_market_index_historical_data) | **GET** /indices/stock_market/{identifier}/historical_data/{tag} | Historical Data for Stock Market Index
[**search_economic_indices**](IndexApi.md#search_economic_indices) | **GET** /indices/economic/search | Search Economic Indices
[**search_sic_indices**](IndexApi.md#search_sic_indices) | **GET** /indices/sic/search | Search SIC Indices
[**search_stock_markets_indices**](IndexApi.md#search_stock_markets_indices) | **GET** /indices/stock_market/search | Search Stock Market Indices


# **get_all_economic_indices**
> ApiResponseEconomicIndices get_all_economic_indices(page_size=page_size, next_page=next_page)

All Economic Indices

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

page_size = 100 # float | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = index_api.get_all_economic_indices(page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_all_economic_indices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **float**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseEconomicIndices**](ApiResponseEconomicIndices.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_sic_indices**
> ApiResponseSICIndices get_all_sic_indices(page_size=page_size, next_page=next_page)

All SIC Indices

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

page_size = 100 # float | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = index_api.get_all_sic_indices(page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_all_sic_indices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **float**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseSICIndices**](ApiResponseSICIndices.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_stock_market_indices**
> ApiResponseStockMarketIndices get_all_stock_market_indices(page_size=page_size, next_page=next_page)

All Stock Market Indices

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

page_size = 100 # float | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = index_api.get_all_stock_market_indices(page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_all_stock_market_indices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **float**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseStockMarketIndices**](ApiResponseStockMarketIndices.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_economic_index_by_id**
> EconomicIndex get_economic_index_by_id(identifier)

Lookup Economic Index

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

identifier = '$GDP' # str | An Index Identifier (symbol, Intrinio ID)

try:
    api_response = index_api.get_economic_index_by_id(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_economic_index_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 

### Return type

[**EconomicIndex**](EconomicIndex.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_economic_index_data_point_number**
> float get_economic_index_data_point_number(identifier, tag)

Data Point (Number) for an Economic Index

Returns a numeric value for the given `tag` for the Economic Index with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

identifier = '$GDP' # str | An Index Identifier (symbol, Intrinio ID)
tag = 'level' # str | An Intrinio data tag ID or code-name

try:
    api_response = index_api.get_economic_index_data_point_number(identifier, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_economic_index_data_point_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code-name | 

### Return type

**float**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_economic_index_data_point_text**
> str get_economic_index_data_point_text(identifier, tag)

Data Point (Text) for an Economic Index

Returns a text value for the given `tag` for the Economic Index with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

identifier = '$GDP' # str | An Index Identifier (symbol, Intrinio ID)
tag = 'level' # str | An Intrinio data tag ID or code-name

try:
    api_response = index_api.get_economic_index_data_point_text(identifier, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_economic_index_data_point_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code-name | 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_economic_index_historical_data**
> ApiResponseEconomicIndexHistoricalData get_economic_index_historical_data(identifier, tag, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)

Historical Data for an Economic Index

Returns historical values for the given `tag` and the Economic Index with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

identifier = '$GDP' # str | An Index Identifier (symbol, Intrinio ID)
tag = 'level' # str | An Intrinio data tag ID or code-name
type = '' # str | Filter by type, when applicable (optional)
start_date = '2018-01-01' # date | Get historical data on or after this date (optional)
end_date = '2019-01-01' # date | Get historical data on or before this date (optional)
sort_order = 'desc' # str | Sort by date `asc` or `desc` (optional) (default to desc)
page_size = 100 # float | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = index_api.get_economic_index_historical_data(identifier, tag, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_economic_index_historical_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code-name | 
 **type** | **str**| Filter by type, when applicable | [optional] 
 **start_date** | **date**| Get historical data on or after this date | [optional] 
 **end_date** | **date**| Get historical data on or before this date | [optional] 
 **sort_order** | **str**| Sort by date &#x60;asc&#x60; or &#x60;desc&#x60; | [optional] [default to desc]
 **page_size** | **float**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseEconomicIndexHistoricalData**](ApiResponseEconomicIndexHistoricalData.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sic_index_by_id**
> SICIndex get_sic_index_by_id(identifier)

Lookup SIC Index

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

identifier = '$SIC.1' # str | An Index Identifier (symbol, Intrinio ID)

try:
    api_response = index_api.get_sic_index_by_id(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_sic_index_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 

### Return type

[**SICIndex**](SICIndex.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sic_index_data_point_number**
> float get_sic_index_data_point_number(identifier, tag)

Data Point (Number) for an SIC Index

Returns a numeric value for the given `tag` for the SIC Index with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

identifier = '$SIC.1' # str | An Index Identifier (symbol, Intrinio ID)
tag = 'level' # str | An Intrinio data tag ID or code-name

try:
    api_response = index_api.get_sic_index_data_point_number(identifier, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_sic_index_data_point_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code-name | 

### Return type

**float**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sic_index_data_point_text**
> str get_sic_index_data_point_text(identifier, tag)

Data Point (Text) for an SIC Index

Returns a text value for the given `tag` for the SIC Index with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

identifier = '$SIC.1' # str | An Index Identifier (symbol, Intrinio ID)
tag = 'level' # str | An Intrinio data tag ID or code-name

try:
    api_response = index_api.get_sic_index_data_point_text(identifier, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_sic_index_data_point_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code-name | 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sic_index_historical_data**
> ApiResponseSICIndexHistoricalData get_sic_index_historical_data(identifier, tag, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)

Historical Data for an SIC Index

Returns historical values for the given `tag` and the SIC Index with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

identifier = '$SIC.1' # str | An Index Identifier (symbol, Intrinio ID)
tag = 'marketcap' # str | An Intrinio data tag ID or code-name
type = '' # str | Filter by type, when applicable (optional)
start_date = '2018-01-01' # date | Get historical data on or after this date (optional)
end_date = '2019-01-01' # date | Get historical data on or before this date (optional)
sort_order = 'desc' # str | Sort by date `asc` or `desc` (optional) (default to desc)
page_size = 100 # float | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = index_api.get_sic_index_historical_data(identifier, tag, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_sic_index_historical_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code-name | 
 **type** | **str**| Filter by type, when applicable | [optional] 
 **start_date** | **date**| Get historical data on or after this date | [optional] 
 **end_date** | **date**| Get historical data on or before this date | [optional] 
 **sort_order** | **str**| Sort by date &#x60;asc&#x60; or &#x60;desc&#x60; | [optional] [default to desc]
 **page_size** | **float**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseSICIndexHistoricalData**](ApiResponseSICIndexHistoricalData.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stock_market_index_by_id**
> StockMarketIndex get_stock_market_index_by_id(identifier)

Lookup Stock Market Index

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

identifier = '$DJI' # str | An Index Identifier (symbol, Intrinio ID)

try:
    api_response = index_api.get_stock_market_index_by_id(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_stock_market_index_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 

### Return type

[**StockMarketIndex**](StockMarketIndex.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stock_market_index_data_point_number**
> float get_stock_market_index_data_point_number(identifier, tag)

Data Point (Number) for Stock Market Index

Returns a numeric value for the given `tag` for the Stock Market Index with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

identifier = '$DJI' # str | An Index Identifier (symbol, Intrinio ID)
tag = 'level' # str | An Intrinio data tag ID or code-name

try:
    api_response = index_api.get_stock_market_index_data_point_number(identifier, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_stock_market_index_data_point_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code-name | 

### Return type

**float**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stock_market_index_data_point_text**
> str get_stock_market_index_data_point_text(identifier, tag)

Data Point (Text) for Stock Market Index

Returns a text value for the given `tag` for the Stock Market Index with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

identifier = '$DJI' # str | An Index Identifier (symbol, Intrinio ID)
tag = 'level' # str | An Intrinio data tag ID or code-name

try:
    api_response = index_api.get_stock_market_index_data_point_text(identifier, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_stock_market_index_data_point_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code-name | 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stock_market_index_historical_data**
> ApiResponseStockMarketIndexHistoricalData get_stock_market_index_historical_data(identifier, tag, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)

Historical Data for Stock Market Index

Returns historical values for the given `tag` and the Stock Market Index with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

identifier = '$DJI' # str | An Index Identifier (symbol, Intrinio ID)
tag = 'level' # str | An Intrinio data tag ID or code-name
type = '' # str | Filter by type, when applicable (optional)
start_date = '2018-01-01' # date | Get historical data on or after this date (optional)
end_date = '2019-01-01' # date | Get historical data on or before this date (optional)
sort_order = 'desc' # str | Sort by date `asc` or `desc` (optional) (default to desc)
page_size = 100 # float | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = index_api.get_stock_market_index_historical_data(identifier, tag, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_stock_market_index_historical_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code-name | 
 **type** | **str**| Filter by type, when applicable | [optional] 
 **start_date** | **date**| Get historical data on or after this date | [optional] 
 **end_date** | **date**| Get historical data on or before this date | [optional] 
 **sort_order** | **str**| Sort by date &#x60;asc&#x60; or &#x60;desc&#x60; | [optional] [default to desc]
 **page_size** | **float**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseStockMarketIndexHistoricalData**](ApiResponseStockMarketIndexHistoricalData.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_economic_indices**
> ApiResponseEconomicIndicesSearch search_economic_indices(query, page_size=page_size)

Search Economic Indices

Searches for indices using the text in `query`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

query = 'GDP' # str | Search query
page_size = 100 # float | The number of results to return (optional) (default to 100)

try:
    api_response = index_api.search_economic_indices(query, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->search_economic_indices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query | 
 **page_size** | **float**| The number of results to return | [optional] [default to 100]

### Return type

[**ApiResponseEconomicIndicesSearch**](ApiResponseEconomicIndicesSearch.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_sic_indices**
> ApiResponseSICIndicesSearch search_sic_indices(query, page_size=page_size)

Search SIC Indices

Searches for indices using the text in `query`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

query = 'agriculture' # str | Search query
page_size = 100 # float | The number of results to return (optional) (default to 100)

try:
    api_response = index_api.search_sic_indices(query, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->search_sic_indices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query | 
 **page_size** | **float**| The number of results to return | [optional] [default to 100]

### Return type

[**ApiResponseSICIndicesSearch**](ApiResponseSICIndicesSearch.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_stock_markets_indices**
> ApiResponseStockMarketIndicesSearch search_stock_markets_indices(query, page_size=page_size)

Search Stock Market Indices

Searches for indices using the text in `query`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

query = 'dow' # str | Search query
page_size = 100 # float | The number of results to return (optional) (default to 100)

try:
    api_response = index_api.search_stock_markets_indices(query, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->search_stock_markets_indices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query | 
 **page_size** | **float**| The number of results to return | [optional] [default to 100]

### Return type

[**ApiResponseStockMarketIndicesSearch**](ApiResponseStockMarketIndicesSearch.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

