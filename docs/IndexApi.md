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



[//]: # (START_OPERATION)

[//]: # (OPERATION:get_all_economic_indices_v2)

[//]: # (ENDPOINT:/indices/economic)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_all_economic_indices)

## **get_all_economic_indices**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_all_economic_indices_v2)

> ApiResponseEconomicIndices get_all_economic_indices(page_size=page_size, next_page=next_page)

#### All Economic Indices



### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = index_api.get_all_economic_indices(page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_all_economic_indices: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 
<br/>
### Return type

[**ApiResponseEconomicIndices**](ApiResponseEconomicIndices.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_all_sic_indices_v2)

[//]: # (ENDPOINT:/indices/sic)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_all_sic_indices)

## **get_all_sic_indices**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_all_sic_indices_v2)

> ApiResponseSICIndices get_all_sic_indices(page_size=page_size, next_page=next_page)

#### All SIC Indices



### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = index_api.get_all_sic_indices(page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_all_sic_indices: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 
<br/>
### Return type

[**ApiResponseSICIndices**](ApiResponseSICIndices.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_all_stock_market_indices_v2)

[//]: # (ENDPOINT:/indices/stock_market)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_all_stock_market_indices)

## **get_all_stock_market_indices**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_all_stock_market_indices_v2)

> ApiResponseStockMarketIndices get_all_stock_market_indices(page_size=page_size, next_page=next_page)

#### All Stock Market Indices



### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = index_api.get_all_stock_market_indices(page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_all_stock_market_indices: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 
<br/>
### Return type

[**ApiResponseStockMarketIndices**](ApiResponseStockMarketIndices.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_economic_index_by_id_v2)

[//]: # (ENDPOINT:/indices/economic/{identifier})

[//]: # (DOCUMENT_LINK:IndexApi.md#get_economic_index_by_id)

## **get_economic_index_by_id**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_economic_index_by_id_v2)

> EconomicIndex get_economic_index_by_id(identifier)

#### Lookup Economic Index



### Example
[//]: # (START_CODE_EXAMPLE)

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
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 
<br/>
### Return type

[**EconomicIndex**](EconomicIndex.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_economic_index_data_point_number_v2)

[//]: # (ENDPOINT:/indices/economic/{identifier}/data_point/{tag}/number)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_economic_index_data_point_number)

## **get_economic_index_data_point_number**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_economic_index_data_point_number_v2)

> float get_economic_index_data_point_number(identifier, tag)

#### Data Point (Number) for an Economic Index


Returns a numeric value for the given `tag` for the Economic Index with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

identifier = '$GDP' # str | An Index Identifier (symbol, Intrinio ID)
tag = 'level' # str | An Intrinio data tag <a href='https://data.intrinio.com/data-tags/economic'>reference</a>

try:
    api_response = index_api.get_economic_index_data_point_number(identifier, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_economic_index_data_point_number: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag &lt;a href&#x3D;&#39;https://data.intrinio.com/data-tags/economic&#39;&gt;reference&lt;/a&gt; | 
<br/>
### Return type

**float**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_economic_index_data_point_text_v2)

[//]: # (ENDPOINT:/indices/economic/{identifier}/data_point/{tag}/text)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_economic_index_data_point_text)

## **get_economic_index_data_point_text**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_economic_index_data_point_text_v2)

> str get_economic_index_data_point_text(identifier, tag)

#### Data Point (Text) for an Economic Index


Returns a text value for the given `tag` for the Economic Index with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

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
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code-name | 
<br/>
### Return type

**str**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_economic_index_historical_data_v2)

[//]: # (ENDPOINT:/indices/economic/{identifier}/historical_data/{tag})

[//]: # (DOCUMENT_LINK:IndexApi.md#get_economic_index_historical_data)

## **get_economic_index_historical_data**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_economic_index_historical_data_v2)

> ApiResponseEconomicIndexHistoricalData get_economic_index_historical_data(identifier, tag, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)

#### Historical Data for an Economic Index


Returns historical values for the given `tag` and the Economic Index with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

identifier = '$GDP' # str | An Index Identifier (symbol, Intrinio ID)
tag = 'level' # str | An Intrinio data tag <a href='https://data.intrinio.com/data-tags/economic'>reference</a>
type = '' # str | Filter by type, when applicable (optional)
start_date = '2018-01-01' # date | Get historical data on or after this date (optional)
end_date = '' # date | Get historical data on or before this date (optional)
sort_order = 'desc' # str | Sort by date `asc` or `desc` (optional) (default to desc)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = index_api.get_economic_index_historical_data(identifier, tag, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_economic_index_historical_data: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag &lt;a href&#x3D;&#39;https://data.intrinio.com/data-tags/economic&#39;&gt;reference&lt;/a&gt; | 
 **type** | **str**| Filter by type, when applicable | [optional] 
 **start_date** | **date**| Get historical data on or after this date | [optional] 
 **end_date** | **date**| Get historical data on or before this date | [optional] 
 **sort_order** | **str**| Sort by date &#x60;asc&#x60; or &#x60;desc&#x60; | [optional] [default to desc]
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 
<br/>
### Return type

[**ApiResponseEconomicIndexHistoricalData**](ApiResponseEconomicIndexHistoricalData.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_sic_index_by_id_v2)

[//]: # (ENDPOINT:/indices/sic/{identifier})

[//]: # (DOCUMENT_LINK:IndexApi.md#get_sic_index_by_id)

## **get_sic_index_by_id**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_sic_index_by_id_v2)

> SICIndex get_sic_index_by_id(identifier)

#### Lookup SIC Index



### Example
[//]: # (START_CODE_EXAMPLE)

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
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 
<br/>
### Return type

[**SICIndex**](SICIndex.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_sic_index_data_point_number_v2)

[//]: # (ENDPOINT:/indices/sic/{identifier}/data_point/{tag}/number)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_sic_index_data_point_number)

## **get_sic_index_data_point_number**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_sic_index_data_point_number_v2)

> float get_sic_index_data_point_number(identifier, tag)

#### Data Point (Number) for an SIC Index


Returns a numeric value for the given `tag` for the SIC Index with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

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
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code-name | 
<br/>
### Return type

**float**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_sic_index_data_point_text_v2)

[//]: # (ENDPOINT:/indices/sic/{identifier}/data_point/{tag}/text)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_sic_index_data_point_text)

## **get_sic_index_data_point_text**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_sic_index_data_point_text_v2)

> str get_sic_index_data_point_text(identifier, tag)

#### Data Point (Text) for an SIC Index


Returns a text value for the given `tag` for the SIC Index with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

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
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code-name | 
<br/>
### Return type

**str**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_sic_index_historical_data_v2)

[//]: # (ENDPOINT:/indices/sic/{identifier}/historical_data/{tag})

[//]: # (DOCUMENT_LINK:IndexApi.md#get_sic_index_historical_data)

## **get_sic_index_historical_data**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_sic_index_historical_data_v2)

> ApiResponseSICIndexHistoricalData get_sic_index_historical_data(identifier, tag, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)

#### Historical Data for an SIC Index


Returns historical values for the given `tag` and the SIC Index with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

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
end_date = '' # date | Get historical data on or before this date (optional)
sort_order = 'desc' # str | Sort by date `asc` or `desc` (optional) (default to desc)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = index_api.get_sic_index_historical_data(identifier, tag, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_sic_index_historical_data: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code-name | 
 **type** | **str**| Filter by type, when applicable | [optional] 
 **start_date** | **date**| Get historical data on or after this date | [optional] 
 **end_date** | **date**| Get historical data on or before this date | [optional] 
 **sort_order** | **str**| Sort by date &#x60;asc&#x60; or &#x60;desc&#x60; | [optional] [default to desc]
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 
<br/>
### Return type

[**ApiResponseSICIndexHistoricalData**](ApiResponseSICIndexHistoricalData.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_stock_market_index_by_id_v2)

[//]: # (ENDPOINT:/indices/stock_market/{identifier})

[//]: # (DOCUMENT_LINK:IndexApi.md#get_stock_market_index_by_id)

## **get_stock_market_index_by_id**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_stock_market_index_by_id_v2)

> StockMarketIndex get_stock_market_index_by_id(identifier)

#### Lookup Stock Market Index



### Example
[//]: # (START_CODE_EXAMPLE)

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
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 
<br/>
### Return type

[**StockMarketIndex**](StockMarketIndex.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_stock_market_index_data_point_number_v2)

[//]: # (ENDPOINT:/indices/stock_market/{identifier}/data_point/{tag}/number)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_stock_market_index_data_point_number)

## **get_stock_market_index_data_point_number**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_stock_market_index_data_point_number_v2)

> float get_stock_market_index_data_point_number(identifier, tag)

#### Data Point (Number) for Stock Market Index


Returns a numeric value for the given `tag` for the Stock Market Index with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

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
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code-name | 
<br/>
### Return type

**float**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_stock_market_index_data_point_text_v2)

[//]: # (ENDPOINT:/indices/stock_market/{identifier}/data_point/{tag}/text)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_stock_market_index_data_point_text)

## **get_stock_market_index_data_point_text**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_stock_market_index_data_point_text_v2)

> str get_stock_market_index_data_point_text(identifier, tag)

#### Data Point (Text) for Stock Market Index


Returns a text value for the given `tag` for the Stock Market Index with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

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
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code-name | 
<br/>
### Return type

**str**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_stock_market_index_historical_data_v2)

[//]: # (ENDPOINT:/indices/stock_market/{identifier}/historical_data/{tag})

[//]: # (DOCUMENT_LINK:IndexApi.md#get_stock_market_index_historical_data)

## **get_stock_market_index_historical_data**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_stock_market_index_historical_data_v2)

> ApiResponseStockMarketIndexHistoricalData get_stock_market_index_historical_data(identifier, tag, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)

#### Historical Data for Stock Market Index


Returns historical values for the given `tag` and the Stock Market Index with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

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
end_date = '' # date | Get historical data on or before this date (optional)
sort_order = 'desc' # str | Sort by date `asc` or `desc` (optional) (default to desc)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = index_api.get_stock_market_index_historical_data(identifier, tag, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->get_stock_market_index_historical_data: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An Index Identifier (symbol, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code-name | 
 **type** | **str**| Filter by type, when applicable | [optional] 
 **start_date** | **date**| Get historical data on or after this date | [optional] 
 **end_date** | **date**| Get historical data on or before this date | [optional] 
 **sort_order** | **str**| Sort by date &#x60;asc&#x60; or &#x60;desc&#x60; | [optional] [default to desc]
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 
<br/>
### Return type

[**ApiResponseStockMarketIndexHistoricalData**](ApiResponseStockMarketIndexHistoricalData.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:search_economic_indices_v2)

[//]: # (ENDPOINT:/indices/economic/search)

[//]: # (DOCUMENT_LINK:IndexApi.md#search_economic_indices)

## **search_economic_indices**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/search_economic_indices_v2)

> ApiResponseEconomicIndicesSearch search_economic_indices(query, page_size=page_size)

#### Search Economic Indices


Searches for indices using the text in `query`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

query = 'GDP' # str | Search query
page_size = 100 # int | The number of results to return (optional) (default to 100)

try:
    api_response = index_api.search_economic_indices(query, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->search_economic_indices: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query | 
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
<br/>
### Return type

[**ApiResponseEconomicIndicesSearch**](ApiResponseEconomicIndicesSearch.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:search_sic_indices_v2)

[//]: # (ENDPOINT:/indices/sic/search)

[//]: # (DOCUMENT_LINK:IndexApi.md#search_sic_indices)

## **search_sic_indices**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/search_sic_indices_v2)

> ApiResponseSICIndicesSearch search_sic_indices(query, page_size=page_size)

#### Search SIC Indices


Searches for indices using the text in `query`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

query = 'agriculture' # str | Search query
page_size = 100 # int | The number of results to return (optional) (default to 100)

try:
    api_response = index_api.search_sic_indices(query, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->search_sic_indices: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query | 
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
<br/>
### Return type

[**ApiResponseSICIndicesSearch**](ApiResponseSICIndicesSearch.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:search_stock_markets_indices_v2)

[//]: # (ENDPOINT:/indices/stock_market/search)

[//]: # (DOCUMENT_LINK:IndexApi.md#search_stock_markets_indices)

## **search_stock_markets_indices**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/search_stock_markets_indices_v2)

> ApiResponseStockMarketIndicesSearch search_stock_markets_indices(query, page_size=page_size)

#### Search Stock Market Indices


Searches for indices using the text in `query`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

index_api = intrinio_sdk.IndexApi()

query = 'dow' # str | Search query
page_size = 100 # int | The number of results to return (optional) (default to 100)

try:
    api_response = index_api.search_stock_markets_indices(query, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IndexApi->search_stock_markets_indices: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query | 
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
<br/>
### Return type

[**ApiResponseStockMarketIndicesSearch**](ApiResponseStockMarketIndicesSearch.md)

[//]: # (END_OPERATION)

