# intrinio_sdk.StockExchangeApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_stock_exchanges**](StockExchangeApi.md#get_all_stock_exchanges) | **GET** /stock_exchanges | All Stock Exchanges
[**get_stock_exchange_by_id**](StockExchangeApi.md#get_stock_exchange_by_id) | **GET** /stock_exchanges/{identifier} | Lookup Stock Exchange
[**get_stock_exchange_price_adjustments**](StockExchangeApi.md#get_stock_exchange_price_adjustments) | **GET** /stock_exchanges/{identifier}/prices/adjustments | Stock Price Adjustments by Exchange
[**get_stock_exchange_prices**](StockExchangeApi.md#get_stock_exchange_prices) | **GET** /stock_exchanges/{identifier}/prices | Stock Prices by Exchange
[**get_stock_exchange_realtime_prices**](StockExchangeApi.md#get_stock_exchange_realtime_prices) | **GET** /stock_exchanges/{identifier}/prices/realtime | Realtime Stock Prices by Exchange
[**get_stock_exchange_securities**](StockExchangeApi.md#get_stock_exchange_securities) | **GET** /stock_exchanges/{identifier}/securities | Securities by Exchange



[//]: # (START_OPERATION)

[//]: # (OPERATION:get_all_stock_exchanges_v2)

[//]: # (ENDPOINT:/stock_exchanges)

[//]: # (DOCUMENT_LINK:StockExchangeApi.md#get_all_stock_exchanges)

## **get_all_stock_exchanges**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_all_stock_exchanges_v2)

> ApiResponseStockExchanges get_all_stock_exchanges(city=city, country=country, country_code=country_code, page_size=page_size)

#### All Stock Exchanges


Returns all Stock Exchanges matching the specified parameters

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

stock_exchange_api = intrinio_sdk.StockExchangeApi()

city = 'city_example' # str | Filter by city (optional)
country = 'CHINA' # str | Filter by country (optional)
country_code = 'country_code_example' # str | Filter by ISO country code (optional)
page_size = 100 # int | The number of results to return (optional) (default to 100)

try:
    api_response = stock_exchange_api.get_all_stock_exchanges(city=city, country=country, country_code=country_code, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockExchangeApi->get_all_stock_exchanges: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city** | **str**| Filter by city | [optional] 
 **country** | **str**| Filter by country | [optional] 
 **country_code** | **str**| Filter by ISO country code | [optional] 
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
<br/>
### Return type

[**ApiResponseStockExchanges**](ApiResponseStockExchanges.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_stock_exchange_by_id_v2)

[//]: # (ENDPOINT:/stock_exchanges/{identifier})

[//]: # (DOCUMENT_LINK:StockExchangeApi.md#get_stock_exchange_by_id)

## **get_stock_exchange_by_id**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_stock_exchange_by_id_v2)

> StockExchange get_stock_exchange_by_id(identifier)

#### Lookup Stock Exchange


Returns the Stock Exchange with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

stock_exchange_api = intrinio_sdk.StockExchangeApi()

identifier = 'USCOMP' # str | A Stock Exchange identifier (MIC or Intrinio ID)

try:
    api_response = stock_exchange_api.get_stock_exchange_by_id(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockExchangeApi->get_stock_exchange_by_id: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Stock Exchange identifier (MIC or Intrinio ID) | 
<br/>
### Return type

[**StockExchange**](StockExchange.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_stock_exchange_price_adjustments_v2)

[//]: # (ENDPOINT:/stock_exchanges/{identifier}/prices/adjustments)

[//]: # (DOCUMENT_LINK:StockExchangeApi.md#get_stock_exchange_price_adjustments)

## **get_stock_exchange_price_adjustments**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_stock_exchange_price_adjustments_v2)

> ApiResponseStockExchangeStockPriceAdjustments get_stock_exchange_price_adjustments(identifier, date=date, page_size=page_size, next_page=next_page)

#### Stock Price Adjustments by Exchange


Returns stock price adjustments for the Stock Exchange with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

stock_exchange_api = intrinio_sdk.StockExchangeApi()

identifier = 'USCOMP' # str | A Stock Exchange identifier (MIC or Intrinio ID)
date = '2018-08-14' # date | The date for which to return price adjustments (optional)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = stock_exchange_api.get_stock_exchange_price_adjustments(identifier, date=date, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockExchangeApi->get_stock_exchange_price_adjustments: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Stock Exchange identifier (MIC or Intrinio ID) | 
 **date** | **date**| The date for which to return price adjustments | [optional] 
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 
<br/>
### Return type

[**ApiResponseStockExchangeStockPriceAdjustments**](ApiResponseStockExchangeStockPriceAdjustments.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_stock_exchange_prices_v2)

[//]: # (ENDPOINT:/stock_exchanges/{identifier}/prices)

[//]: # (DOCUMENT_LINK:StockExchangeApi.md#get_stock_exchange_prices)

## **get_stock_exchange_prices**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_stock_exchange_prices_v2)

> ApiResponseStockExchangeStockPrices get_stock_exchange_prices(identifier, date=date, page_size=page_size, next_page=next_page)

#### Stock Prices by Exchange


Returns end-of-day stock prices for Securities on the Stock Exchange with `identifier` and on the `price_date` (or the latest date that prices are available)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

stock_exchange_api = intrinio_sdk.StockExchangeApi()

identifier = 'USCOMP' # str | A Stock Exchange identifier (MIC or Intrinio ID)
date = '2018-08-14' # date | The date for which to return prices (optional)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = stock_exchange_api.get_stock_exchange_prices(identifier, date=date, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockExchangeApi->get_stock_exchange_prices: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Stock Exchange identifier (MIC or Intrinio ID) | 
 **date** | **date**| The date for which to return prices | [optional] 
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 
<br/>
### Return type

[**ApiResponseStockExchangeStockPrices**](ApiResponseStockExchangeStockPrices.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_stock_exchange_realtime_prices_v2)

[//]: # (ENDPOINT:/stock_exchanges/{identifier}/prices/realtime)

[//]: # (DOCUMENT_LINK:StockExchangeApi.md#get_stock_exchange_realtime_prices)

## **get_stock_exchange_realtime_prices**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_stock_exchange_realtime_prices_v2)

> ApiResponseStockExchangeRealtimeStockPrices get_stock_exchange_realtime_prices(identifier, source=source, page_size=page_size, next_page=next_page)

#### Realtime Stock Prices by Exchange


Returns realtime stock prices for the Stock Exchange with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

stock_exchange_api = intrinio_sdk.StockExchangeApi()

identifier = 'USCOMP' # str | A Stock Exchange identifier (MIC or Intrinio ID)
source = '' # str | Return realtime prices from the specified data source (optional)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = stock_exchange_api.get_stock_exchange_realtime_prices(identifier, source=source, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockExchangeApi->get_stock_exchange_realtime_prices: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Stock Exchange identifier (MIC or Intrinio ID) | 
 **source** | **str**| Return realtime prices from the specified data source | [optional] 
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 
<br/>
### Return type

[**ApiResponseStockExchangeRealtimeStockPrices**](ApiResponseStockExchangeRealtimeStockPrices.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_stock_exchange_securities_v2)

[//]: # (ENDPOINT:/stock_exchanges/{identifier}/securities)

[//]: # (DOCUMENT_LINK:StockExchangeApi.md#get_stock_exchange_securities)

## **get_stock_exchange_securities**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_stock_exchange_securities_v2)

> ApiResponseStockExchangeSecurities get_stock_exchange_securities(identifier, page_size=page_size, next_page=next_page)

#### Securities by Exchange


Returns Securities traded on the Stock Exchange with `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

stock_exchange_api = intrinio_sdk.StockExchangeApi()

identifier = 'USCOMP' # str | A Stock Exchange identifier (MIC or Intrinio ID)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = stock_exchange_api.get_stock_exchange_securities(identifier, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockExchangeApi->get_stock_exchange_securities: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Stock Exchange identifier (MIC or Intrinio ID) | 
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 
<br/>
### Return type

[**ApiResponseStockExchangeSecurities**](ApiResponseStockExchangeSecurities.md)

[//]: # (END_OPERATION)

