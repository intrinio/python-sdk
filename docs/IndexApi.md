# intrinio_sdk.IndexApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_economic_indices**](IndexApi.md#get_all_economic_indices) | **GET** /indices/economic | All Economic Indices
[**get_all_eod_index_prices**](IndexApi.md#get_all_eod_index_prices) | **GET** /indices/prices/eod | All End of Day Index Prices
[**get_all_index_summaries**](IndexApi.md#get_all_index_summaries) | **GET** /indices | All Index Summaries
[**get_all_realtime_index_prices**](IndexApi.md#get_all_realtime_index_prices) | **GET** /indices/prices/realtime | All Realtime Index Prices
[**get_all_sic_indices**](IndexApi.md#get_all_sic_indices) | **GET** /indices/sic | All SIC Indices
[**get_all_stock_market_indices**](IndexApi.md#get_all_stock_market_indices) | **GET** /indices/stock_market | All Stock Market Indices
[**get_economic_index_by_id**](IndexApi.md#get_economic_index_by_id) | **GET** /indices/economic/{identifier} | Lookup Economic Index
[**get_economic_index_data_point_number**](IndexApi.md#get_economic_index_data_point_number) | **GET** /indices/economic/{identifier}/data_point/{tag}/number | Data Point (Number) for an Economic Index
[**get_economic_index_data_point_text**](IndexApi.md#get_economic_index_data_point_text) | **GET** /indices/economic/{identifier}/data_point/{tag}/text | Data Point (Text) for an Economic Index
[**get_economic_index_historical_data**](IndexApi.md#get_economic_index_historical_data) | **GET** /indices/economic/{identifier}/historical_data/{tag} | Historical Data for an Economic Index
[**get_eod_index_price_by_id**](IndexApi.md#get_eod_index_price_by_id) | **GET** /indices/{identifier}/eod | End of Day Index Prices By Identifier
[**get_index_constituents_by_id**](IndexApi.md#get_index_constituents_by_id) | **GET** /indices/{identifier}/constituents | Index Constituents By Index Identifier
[**get_index_intervals**](IndexApi.md#get_index_intervals) | **GET** /indices/{identifier}/intervals | Index Intervals
[**get_index_summary_by_id**](IndexApi.md#get_index_summary_by_id) | **GET** /indices/{identifier} | Index Summary By Identifier
[**get_realtime_index_price_by_id**](IndexApi.md#get_realtime_index_price_by_id) | **GET** /indices/{identifier}/realtime | Realtime Index Price By Identifier
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

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_all_economic_indices)

[//]: # (RETURN_TYPE:ApiResponseEconomicIndices)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseEconomicIndices.md)

[//]: # (OPERATION:get_all_economic_indices_v2)

[//]: # (ENDPOINT:/indices/economic)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_all_economic_indices)

## **get_all_economic_indices**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_all_economic_indices_v2)

[//]: # (START_OVERVIEW)

> ApiResponseEconomicIndices get_all_economic_indices(page_size=page_size, next_page=next_page)

#### All Economic Indices


Returns a list of reference data on more than 200,000 economic indices from the Federal Reserve Economic Data (FRED) database.

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

page_size = 100
next_page = ''

response = intrinio.IndexApi().get_all_economic_indices(page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseEconomicIndices**](ApiResponseEconomicIndices.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_all_eod_index_prices)

[//]: # (RETURN_TYPE:ApiResponseEodIndexPricesAll)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseEodIndexPricesAll.md)

[//]: # (OPERATION:get_all_eod_index_prices_v2)

[//]: # (ENDPOINT:/indices/prices/eod)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_all_eod_index_prices)

## **get_all_eod_index_prices**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_all_eod_index_prices_v2)

[//]: # (START_OVERVIEW)

> ApiResponseEodIndexPricesAll get_all_eod_index_prices(page_size=page_size, start_date=start_date, end_date=end_date)

#### All End of Day Index Prices



[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

page_size = 100
start_date = ''
end_date = ''

response = intrinio.IndexApi().get_all_eod_index_prices(page_size=page_size, start_date=start_date, end_date=end_date)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **start_date** | date| Limit prices to those on or after this date | [optional]   &nbsp;
 **end_date** | date| Limit prices to those on or before this date | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseEodIndexPricesAll**](ApiResponseEodIndexPricesAll.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_all_index_summaries)

[//]: # (RETURN_TYPE:ApiResponseIndices)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseIndices.md)

[//]: # (OPERATION:get_all_index_summaries_v2)

[//]: # (ENDPOINT:/indices)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_all_index_summaries)

## **get_all_index_summaries**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_all_index_summaries_v2)

[//]: # (START_OVERVIEW)

> ApiResponseIndices get_all_index_summaries(page_size=page_size)

#### All Index Summaries



[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

page_size = 100

response = intrinio.IndexApi().get_all_index_summaries(page_size=page_size)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseIndices**](ApiResponseIndices.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_all_realtime_index_prices)

[//]: # (RETURN_TYPE:ApiResponseRealtimeIndexPrices)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseRealtimeIndexPrices.md)

[//]: # (OPERATION:get_all_realtime_index_prices_v2)

[//]: # (ENDPOINT:/indices/prices/realtime)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_all_realtime_index_prices)

## **get_all_realtime_index_prices**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_all_realtime_index_prices_v2)

[//]: # (START_OVERVIEW)

> ApiResponseRealtimeIndexPrices get_all_realtime_index_prices(page_size=page_size)

#### All Realtime Index Prices



[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

page_size = 100

response = intrinio.IndexApi().get_all_realtime_index_prices(page_size=page_size)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseRealtimeIndexPrices**](ApiResponseRealtimeIndexPrices.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_all_sic_indices)

[//]: # (RETURN_TYPE:ApiResponseSICIndices)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseSICIndices.md)

[//]: # (OPERATION:get_all_sic_indices_v2)

[//]: # (ENDPOINT:/indices/sic)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_all_sic_indices)

## **get_all_sic_indices**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_all_sic_indices_v2)

[//]: # (START_OVERVIEW)

> ApiResponseSICIndices get_all_sic_indices(page_size=page_size, next_page=next_page)

#### All SIC Indices



[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

page_size = 100
next_page = ''

response = intrinio.IndexApi().get_all_sic_indices(page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseSICIndices**](ApiResponseSICIndices.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_all_stock_market_indices)

[//]: # (RETURN_TYPE:ApiResponseStockMarketIndices)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseStockMarketIndices.md)

[//]: # (OPERATION:get_all_stock_market_indices_v2)

[//]: # (ENDPOINT:/indices/stock_market)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_all_stock_market_indices)

## **get_all_stock_market_indices**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_all_stock_market_indices_v2)

[//]: # (START_OVERVIEW)

> ApiResponseStockMarketIndices get_all_stock_market_indices(page_size=page_size, next_page=next_page)

#### All Stock Market Indices



[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

page_size = 100
next_page = ''

response = intrinio.IndexApi().get_all_stock_market_indices(page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseStockMarketIndices**](ApiResponseStockMarketIndices.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_economic_index_by_id)

[//]: # (RETURN_TYPE:EconomicIndex)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:EconomicIndex.md)

[//]: # (OPERATION:get_economic_index_by_id_v2)

[//]: # (ENDPOINT:/indices/economic/{identifier})

[//]: # (DOCUMENT_LINK:IndexApi.md#get_economic_index_by_id)

## **get_economic_index_by_id**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_economic_index_by_id_v2)

[//]: # (START_OVERVIEW)

> EconomicIndex get_economic_index_by_id(identifier)

#### Lookup Economic Index


Returns reference data for a specified Federal Reserve Economic Data (FRED) series ID.

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

identifier = '$GDP'

response = intrinio.IndexApi().get_economic_index_by_id(identifier)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| An Index Identifier (symbol, Intrinio ID) |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**EconomicIndex**](EconomicIndex.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_economic_index_data_point_number)

[//]: # (RETURN_TYPE:float)

[//]: # (RETURN_TYPE_KIND:primitive)

[//]: # (RETURN_TYPE_DOC:)

[//]: # (OPERATION:get_economic_index_data_point_number_v2)

[//]: # (ENDPOINT:/indices/economic/{identifier}/data_point/{tag}/number)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_economic_index_data_point_number)

## **get_economic_index_data_point_number**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_economic_index_data_point_number_v2)

[//]: # (START_OVERVIEW)

> float get_economic_index_data_point_number(identifier, tag)

#### Data Point (Number) for an Economic Index


Returns latest data for a specified Federal Reserve Economic Data (FRED) ID.

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

identifier = '$GDP'
tag = 'level'

response = intrinio.IndexApi().get_economic_index_data_point_number(identifier, tag)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| An Index Identifier (symbol, Intrinio ID) |   &nbsp;
 **tag** | str| An Intrinio data tag &lt;a href&#x3D;&#39;https://data.intrinio.com/data-tags/economic&#39;&gt;reference&lt;/a&gt; |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

**float**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_economic_index_data_point_text)

[//]: # (RETURN_TYPE:str)

[//]: # (RETURN_TYPE_KIND:primitive)

[//]: # (RETURN_TYPE_DOC:)

[//]: # (OPERATION:get_economic_index_data_point_text_v2)

[//]: # (ENDPOINT:/indices/economic/{identifier}/data_point/{tag}/text)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_economic_index_data_point_text)

## **get_economic_index_data_point_text**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_economic_index_data_point_text_v2)

[//]: # (START_OVERVIEW)

> str get_economic_index_data_point_text(identifier, tag)

#### Data Point (Text) for an Economic Index


Returns a text value for the given `tag` for the Economic Index with the given `identifier`

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

identifier = '$GDP'
tag = 'level'

response = intrinio.IndexApi().get_economic_index_data_point_text(identifier, tag)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| An Index Identifier (symbol, Intrinio ID) |   &nbsp;
 **tag** | str| An Intrinio data tag ID or code-name |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

**str**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_economic_index_historical_data)

[//]: # (RETURN_TYPE:ApiResponseEconomicIndexHistoricalData)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseEconomicIndexHistoricalData.md)

[//]: # (OPERATION:get_economic_index_historical_data_v2)

[//]: # (ENDPOINT:/indices/economic/{identifier}/historical_data/{tag})

[//]: # (DOCUMENT_LINK:IndexApi.md#get_economic_index_historical_data)

## **get_economic_index_historical_data**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_economic_index_historical_data_v2)

[//]: # (START_OVERVIEW)

> ApiResponseEconomicIndexHistoricalData get_economic_index_historical_data(identifier, tag, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)

#### Historical Data for an Economic Index


Returns historical data for a specified Federal Reserve Economic Data (FRED) ID over a period of time.

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

identifier = '$GDP'
tag = 'level'
type = ''
start_date = '2018-01-01'
end_date = ''
sort_order = 'desc'
page_size = 100
next_page = ''

response = intrinio.IndexApi().get_economic_index_historical_data(identifier, tag, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| An Index Identifier (symbol, Intrinio ID) |   &nbsp;
 **tag** | str| An Intrinio data tag &lt;a href&#x3D;&#39;https://data.intrinio.com/data-tags/economic&#39;&gt;reference&lt;/a&gt; |   &nbsp;
 **type** | str| Filter by type, when applicable | [optional]   &nbsp;
 **start_date** | date| Get historical data on or after this date | [optional]   &nbsp;
 **end_date** | date| Get historical data on or before this date | [optional]   &nbsp;
 **sort_order** | str| Sort by date &#x60;asc&#x60; or &#x60;desc&#x60; | [optional] [default to desc]  &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseEconomicIndexHistoricalData**](ApiResponseEconomicIndexHistoricalData.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_eod_index_price_by_id)

[//]: # (RETURN_TYPE:ApiResponseEodIndexPrices)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseEodIndexPrices.md)

[//]: # (OPERATION:get_eod_index_price_by_id_v2)

[//]: # (ENDPOINT:/indices/{identifier}/eod)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_eod_index_price_by_id)

## **get_eod_index_price_by_id**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_eod_index_price_by_id_v2)

[//]: # (START_OVERVIEW)

> ApiResponseEodIndexPrices get_eod_index_price_by_id(identifier, page_size=page_size, start_date=start_date, end_date=end_date)

#### End of Day Index Prices By Identifier



[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

identifier = 'SPX'
page_size = 100
start_date = ''
end_date = ''

response = intrinio.IndexApi().get_eod_index_price_by_id(identifier, page_size=page_size, start_date=start_date, end_date=end_date)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| The index symbol |   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **start_date** | date| Limit prices to those on or after this date | [optional]   &nbsp;
 **end_date** | date| Limit prices to those on or before this date | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseEodIndexPrices**](ApiResponseEodIndexPrices.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_index_constituents_by_id)

[//]: # (RETURN_TYPE:ApiResponseIndexConstituents)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseIndexConstituents.md)

[//]: # (OPERATION:get_index_constituents_by_id_v2)

[//]: # (ENDPOINT:/indices/{identifier}/constituents)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_index_constituents_by_id)

## **get_index_constituents_by_id**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_index_constituents_by_id_v2)

[//]: # (START_OVERVIEW)

> ApiResponseIndexConstituents get_index_constituents_by_id(identifier)

#### Index Constituents By Index Identifier



[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

identifier = 'DJI'

response = intrinio.IndexApi().get_index_constituents_by_id(identifier)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| The index symbol |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseIndexConstituents**](ApiResponseIndexConstituents.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_index_intervals)

[//]: # (RETURN_TYPE:ApiResponseIndexIntervals)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseIndexIntervals.md)

[//]: # (OPERATION:get_index_intervals_v2)

[//]: # (ENDPOINT:/indices/{identifier}/intervals)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_index_intervals)

## **get_index_intervals**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_index_intervals_v2)

[//]: # (START_OVERVIEW)

> ApiResponseIndexIntervals get_index_intervals(identifier, interval_size, start_date=start_date, start_time=start_time, end_date=end_date, end_time=end_time, timezone=timezone, page_size=page_size)

#### Index Intervals


Returns a list of interval data points for a specified index, including open, close, high, low, volume, and average price. Intervals are available in 60-minute, 30-minute, 15-minute, 10-minute, 5-minute, and 1-minute increments.

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

identifier = 'SPX'
interval_size = '5m'
start_date = '2023-01-01'
start_time = '33300'
end_date = '2023-02-01'
end_time = '33300'
timezone = 'UTC'
page_size = 100

response = intrinio.IndexApi().get_index_intervals(identifier, interval_size, start_date=start_date, start_time=start_time, end_date=end_date, end_time=end_time, timezone=timezone, page_size=page_size)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| The index identifier |   &nbsp;
 **interval_size** | str| The interval size to return in minutes (m) or hour (h). | [default to 5m]  &nbsp;
 **start_date** | date| Return intervals starting at the specified date | [optional]   &nbsp;
 **start_time** | str| Return intervals starting at the specified time on the &#x60;start_date&#x60; (24-hour in &#39;hh:mm:ss&#39; format) | [optional]   &nbsp;
 **end_date** | date| Return intervals stopping at the specified date | [optional]   &nbsp;
 **end_time** | str| Return intervals stopping at the specified time on the &#x60;end_date&#x60; (24-hour in &#39;hh:mm:ss&#39; format) | [optional]   &nbsp;
 **timezone** | str| Interprets the input times in this time zone, as well as returns times in this timezone. | [optional] [default to UTC]  &nbsp;
 **page_size** | int| The number of results to return per page. | [optional] [default to 100]  &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseIndexIntervals**](ApiResponseIndexIntervals.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_index_summary_by_id)

[//]: # (RETURN_TYPE:ApiResponseIndex)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseIndex.md)

[//]: # (OPERATION:get_index_summary_by_id_v2)

[//]: # (ENDPOINT:/indices/{identifier})

[//]: # (DOCUMENT_LINK:IndexApi.md#get_index_summary_by_id)

## **get_index_summary_by_id**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_index_summary_by_id_v2)

[//]: # (START_OVERVIEW)

> ApiResponseIndex get_index_summary_by_id(identifier)

#### Index Summary By Identifier



[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

identifier = 'SPX'

response = intrinio.IndexApi().get_index_summary_by_id(identifier)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| The index symbol |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseIndex**](ApiResponseIndex.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_realtime_index_price_by_id)

[//]: # (RETURN_TYPE:RealtimeIndexPrice)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:RealtimeIndexPrice.md)

[//]: # (OPERATION:get_realtime_index_price_by_id_v2)

[//]: # (ENDPOINT:/indices/{identifier}/realtime)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_realtime_index_price_by_id)

## **get_realtime_index_price_by_id**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_realtime_index_price_by_id_v2)

[//]: # (START_OVERVIEW)

> RealtimeIndexPrice get_realtime_index_price_by_id(identifier)

#### Realtime Index Price By Identifier


Returns the realtime price for an index.

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

identifier = 'SPX'

response = intrinio.IndexApi().get_realtime_index_price_by_id(identifier)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| The index symbol |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**RealtimeIndexPrice**](RealtimeIndexPrice.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_sic_index_by_id)

[//]: # (RETURN_TYPE:SICIndex)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:SICIndex.md)

[//]: # (OPERATION:get_sic_index_by_id_v2)

[//]: # (ENDPOINT:/indices/sic/{identifier})

[//]: # (DOCUMENT_LINK:IndexApi.md#get_sic_index_by_id)

## **get_sic_index_by_id**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_sic_index_by_id_v2)

[//]: # (START_OVERVIEW)

> SICIndex get_sic_index_by_id(identifier)

#### Lookup SIC Index



[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

identifier = '$SIC.2911'

response = intrinio.IndexApi().get_sic_index_by_id(identifier)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| An Index Identifier (symbol, Intrinio ID) |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**SICIndex**](SICIndex.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_sic_index_data_point_number)

[//]: # (RETURN_TYPE:float)

[//]: # (RETURN_TYPE_KIND:primitive)

[//]: # (RETURN_TYPE_DOC:)

[//]: # (OPERATION:get_sic_index_data_point_number_v2)

[//]: # (ENDPOINT:/indices/sic/{identifier}/data_point/{tag}/number)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_sic_index_data_point_number)

## **get_sic_index_data_point_number**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_sic_index_data_point_number_v2)

[//]: # (START_OVERVIEW)

> float get_sic_index_data_point_number(identifier, tag)

#### Data Point (Number) for an SIC Index


Returns a numeric value for the given `tag` for the SIC Index with the given `identifier`

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

identifier = '$SIC.2911'
tag = 'marketcap'

response = intrinio.IndexApi().get_sic_index_data_point_number(identifier, tag)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| An Index Identifier (symbol, Intrinio ID) |   &nbsp;
 **tag** | str| An Intrinio data tag ID or code-name |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

**float**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_sic_index_data_point_text)

[//]: # (RETURN_TYPE:str)

[//]: # (RETURN_TYPE_KIND:primitive)

[//]: # (RETURN_TYPE_DOC:)

[//]: # (OPERATION:get_sic_index_data_point_text_v2)

[//]: # (ENDPOINT:/indices/sic/{identifier}/data_point/{tag}/text)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_sic_index_data_point_text)

## **get_sic_index_data_point_text**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_sic_index_data_point_text_v2)

[//]: # (START_OVERVIEW)

> str get_sic_index_data_point_text(identifier, tag)

#### Data Point (Text) for an SIC Index


Returns a text value for the given `tag` for the SIC Index with the given `identifier`

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

identifier = '$SIC.2911'
tag = 'marketcap'

response = intrinio.IndexApi().get_sic_index_data_point_text(identifier, tag)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| An Index Identifier (symbol, Intrinio ID) |   &nbsp;
 **tag** | str| An Intrinio data tag ID or code-name |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

**str**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_sic_index_historical_data)

[//]: # (RETURN_TYPE:ApiResponseSICIndexHistoricalData)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseSICIndexHistoricalData.md)

[//]: # (OPERATION:get_sic_index_historical_data_v2)

[//]: # (ENDPOINT:/indices/sic/{identifier}/historical_data/{tag})

[//]: # (DOCUMENT_LINK:IndexApi.md#get_sic_index_historical_data)

## **get_sic_index_historical_data**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_sic_index_historical_data_v2)

[//]: # (START_OVERVIEW)

> ApiResponseSICIndexHistoricalData get_sic_index_historical_data(identifier, tag, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)

#### Historical Data for an SIC Index


Returns historical values for the given `tag` and the SIC Index with the given `identifier`

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

identifier = '$SIC.1'
tag = 'marketcap'
type = ''
start_date = '2018-01-01'
end_date = ''
sort_order = 'desc'
page_size = 100
next_page = ''

response = intrinio.IndexApi().get_sic_index_historical_data(identifier, tag, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| An Index Identifier (symbol, Intrinio ID) |   &nbsp;
 **tag** | str| An Intrinio data tag ID or code-name |   &nbsp;
 **type** | str| Filter by type, when applicable | [optional]   &nbsp;
 **start_date** | date| Get historical data on or after this date | [optional]   &nbsp;
 **end_date** | date| Get historical data on or before this date | [optional]   &nbsp;
 **sort_order** | str| Sort by date &#x60;asc&#x60; or &#x60;desc&#x60; | [optional] [default to desc]  &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseSICIndexHistoricalData**](ApiResponseSICIndexHistoricalData.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_stock_market_index_by_id)

[//]: # (RETURN_TYPE:StockMarketIndex)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:StockMarketIndex.md)

[//]: # (OPERATION:get_stock_market_index_by_id_v2)

[//]: # (ENDPOINT:/indices/stock_market/{identifier})

[//]: # (DOCUMENT_LINK:IndexApi.md#get_stock_market_index_by_id)

## **get_stock_market_index_by_id**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_stock_market_index_by_id_v2)

[//]: # (START_OVERVIEW)

> StockMarketIndex get_stock_market_index_by_id(identifier)

#### Lookup Stock Market Index



[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

identifier = '$DJI'

response = intrinio.IndexApi().get_stock_market_index_by_id(identifier)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| An Index Identifier (symbol, Intrinio ID) |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**StockMarketIndex**](StockMarketIndex.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_stock_market_index_data_point_number)

[//]: # (RETURN_TYPE:float)

[//]: # (RETURN_TYPE_KIND:primitive)

[//]: # (RETURN_TYPE_DOC:)

[//]: # (OPERATION:get_stock_market_index_data_point_number_v2)

[//]: # (ENDPOINT:/indices/stock_market/{identifier}/data_point/{tag}/number)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_stock_market_index_data_point_number)

## **get_stock_market_index_data_point_number**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_stock_market_index_data_point_number_v2)

[//]: # (START_OVERVIEW)

> float get_stock_market_index_data_point_number(identifier, tag)

#### Data Point (Number) for Stock Market Index


Returns a numeric value for the given `tag` for the Stock Market Index with the given `identifier`

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

identifier = '$DJI'
tag = 'level'

response = intrinio.IndexApi().get_stock_market_index_data_point_number(identifier, tag)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| An Index Identifier (symbol, Intrinio ID) |   &nbsp;
 **tag** | str| An Intrinio data tag ID or code-name |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

**float**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_stock_market_index_data_point_text)

[//]: # (RETURN_TYPE:str)

[//]: # (RETURN_TYPE_KIND:primitive)

[//]: # (RETURN_TYPE_DOC:)

[//]: # (OPERATION:get_stock_market_index_data_point_text_v2)

[//]: # (ENDPOINT:/indices/stock_market/{identifier}/data_point/{tag}/text)

[//]: # (DOCUMENT_LINK:IndexApi.md#get_stock_market_index_data_point_text)

## **get_stock_market_index_data_point_text**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_stock_market_index_data_point_text_v2)

[//]: # (START_OVERVIEW)

> str get_stock_market_index_data_point_text(identifier, tag)

#### Data Point (Text) for Stock Market Index


Returns a text value for the given `tag` for the Stock Market Index with the given `identifier`

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

identifier = '$DJI'
tag = 'level'

response = intrinio.IndexApi().get_stock_market_index_data_point_text(identifier, tag)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| An Index Identifier (symbol, Intrinio ID) |   &nbsp;
 **tag** | str| An Intrinio data tag ID or code-name |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

**str**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:get_stock_market_index_historical_data)

[//]: # (RETURN_TYPE:ApiResponseStockMarketIndexHistoricalData)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseStockMarketIndexHistoricalData.md)

[//]: # (OPERATION:get_stock_market_index_historical_data_v2)

[//]: # (ENDPOINT:/indices/stock_market/{identifier}/historical_data/{tag})

[//]: # (DOCUMENT_LINK:IndexApi.md#get_stock_market_index_historical_data)

## **get_stock_market_index_historical_data**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_stock_market_index_historical_data_v2)

[//]: # (START_OVERVIEW)

> ApiResponseStockMarketIndexHistoricalData get_stock_market_index_historical_data(identifier, tag, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)

#### Historical Data for Stock Market Index


Returns historical values for the given `tag` and the Stock Market Index with the given `identifier`

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

identifier = '$DJI'
tag = 'level'
type = ''
start_date = '2018-01-01'
end_date = ''
sort_order = 'desc'
page_size = 100
next_page = ''

response = intrinio.IndexApi().get_stock_market_index_historical_data(identifier, tag, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| An Index Identifier (symbol, Intrinio ID) |   &nbsp;
 **tag** | str| An Intrinio data tag ID or code-name |   &nbsp;
 **type** | str| Filter by type, when applicable | [optional]   &nbsp;
 **start_date** | date| Get historical data on or after this date | [optional]   &nbsp;
 **end_date** | date| Get historical data on or before this date | [optional]   &nbsp;
 **sort_order** | str| Sort by date &#x60;asc&#x60; or &#x60;desc&#x60; | [optional] [default to desc]  &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseStockMarketIndexHistoricalData**](ApiResponseStockMarketIndexHistoricalData.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:search_economic_indices)

[//]: # (RETURN_TYPE:ApiResponseEconomicIndicesSearch)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseEconomicIndicesSearch.md)

[//]: # (OPERATION:search_economic_indices_v2)

[//]: # (ENDPOINT:/indices/economic/search)

[//]: # (DOCUMENT_LINK:IndexApi.md#search_economic_indices)

## **search_economic_indices**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/search_economic_indices_v2)

[//]: # (START_OVERVIEW)

> ApiResponseEconomicIndicesSearch search_economic_indices(query, page_size=page_size)

#### Search Economic Indices


Search the Federal Reserve Economic Data (FRED) database and return a list of economic indices matching the text query parameter passed through.

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

query = 'GDP'
page_size = 100

response = intrinio.IndexApi().search_economic_indices(query, page_size=page_size)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | str| Search query |   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseEconomicIndicesSearch**](ApiResponseEconomicIndicesSearch.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:search_sic_indices)

[//]: # (RETURN_TYPE:ApiResponseSICIndicesSearch)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseSICIndicesSearch.md)

[//]: # (OPERATION:search_sic_indices_v2)

[//]: # (ENDPOINT:/indices/sic/search)

[//]: # (DOCUMENT_LINK:IndexApi.md#search_sic_indices)

## **search_sic_indices**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/search_sic_indices_v2)

[//]: # (START_OVERVIEW)

> ApiResponseSICIndicesSearch search_sic_indices(query, page_size=page_size)

#### Search SIC Indices


Searches for indices using the text in `query`

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

query = 'agriculture'
page_size = 100

response = intrinio.IndexApi().search_sic_indices(query, page_size=page_size)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | str| Search query |   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseSICIndicesSearch**](ApiResponseSICIndicesSearch.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:IndexApi)

[//]: # (METHOD:search_stock_markets_indices)

[//]: # (RETURN_TYPE:ApiResponseStockMarketIndicesSearch)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseStockMarketIndicesSearch.md)

[//]: # (OPERATION:search_stock_markets_indices_v2)

[//]: # (ENDPOINT:/indices/stock_market/search)

[//]: # (DOCUMENT_LINK:IndexApi.md#search_stock_markets_indices)

## **search_stock_markets_indices**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/search_stock_markets_indices_v2)

[//]: # (START_OVERVIEW)

> ApiResponseStockMarketIndicesSearch search_stock_markets_indices(query, page_size=page_size)

#### Search Stock Market Indices


Searches for indices using the text in `query`

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().set_api_key('YOUR_API_KEY')
intrinio.ApiClient().allow_retries(True)

query = 'dow'
page_size = 100

response = intrinio.IndexApi().search_stock_markets_indices(query, page_size=page_size)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | str| Search query |   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseStockMarketIndicesSearch**](ApiResponseStockMarketIndicesSearch.md)

[//]: # (END_OPERATION)

