# intrinio_sdk.StockExchangeApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_stock_exchanges**](StockExchangeApi.md#filter_stock_exchanges) | **GET** /stock_exchanges/filter | Filter Stock Exchanges
[**get_all_stock_exchanges**](StockExchangeApi.md#get_all_stock_exchanges) | **GET** /stock_exchanges | Get All Stock Exchanges
[**get_stock_exchange_by_id**](StockExchangeApi.md#get_stock_exchange_by_id) | **GET** /stock_exchanges/{identifier} | Get Stock Exchange by ID
[**get_stock_exchange_prices**](StockExchangeApi.md#get_stock_exchange_prices) | **GET** /stock_exchanges/{identifier}/prices | Get Stock Prices by Exchange
[**get_stock_exchange_securities**](StockExchangeApi.md#get_stock_exchange_securities) | **GET** /stock_exchanges/{identifier}/securities | Get Securities by Exchange


# **filter_stock_exchanges**
> list[StockExchange] filter_stock_exchanges(city=city, country=country, country_code=country_code, next_page=next_page)

Filter Stock Exchanges

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'

stock_exchange_api = intrinio_sdk.StockExchangeApi()

city = 'city_example' # str | Filter by city (optional)
country = 'country_example' # str | Filter by country (optional)
country_code = 'country_code_example' # str | Filter by ISO country code (optional)
next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = stock_exchange_api.filter_stock_exchanges(city=city, country=country, country_code=country_code, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockExchangeApi->filter_stock_exchanges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city** | **str**| Filter by city | [optional] 
 **country** | **str**| Filter by country | [optional] 
 **country_code** | **str**| Filter by ISO country code | [optional] 
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**list[StockExchange]**](StockExchange.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_stock_exchanges**
> list[StockExchange] get_all_stock_exchanges(next_page=next_page)

Get All Stock Exchanges

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'

stock_exchange_api = intrinio_sdk.StockExchangeApi()

next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = stock_exchange_api.get_all_stock_exchanges(next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockExchangeApi->get_all_stock_exchanges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**list[StockExchange]**](StockExchange.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stock_exchange_by_id**
> StockExchange get_stock_exchange_by_id(identifier)

Get Stock Exchange by ID

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'

stock_exchange_api = intrinio_sdk.StockExchangeApi()

identifier = 'identifier_example' # str | A Stock Exchange identifier (MIC or Intrinio ID)

try:
    api_response = stock_exchange_api.get_stock_exchange_by_id(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockExchangeApi->get_stock_exchange_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Stock Exchange identifier (MIC or Intrinio ID) | 

### Return type

[**StockExchange**](StockExchange.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stock_exchange_prices**
> list[StockPrice] get_stock_exchange_prices(identifier, date=date, next_page=next_page)

Get Stock Prices by Exchange

Return daily Stock Prices for Securities on the Stock Exchange with `identifier` and on the `price_date` (or the latest date that prices are available)

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'

stock_exchange_api = intrinio_sdk.StockExchangeApi()

identifier = 'identifier_example' # str | A Stock Exchange identifier (MIC or Intrinio ID)
date = '2013-10-20' # date | The date for which to return prices (optional)
next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = stock_exchange_api.get_stock_exchange_prices(identifier, date=date, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockExchangeApi->get_stock_exchange_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Stock Exchange identifier (MIC or Intrinio ID) | 
 **date** | **date**| The date for which to return prices | [optional] 
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**list[StockPrice]**](StockPrice.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stock_exchange_securities**
> list[Security] get_stock_exchange_securities(identifier, next_page=next_page)

Get Securities by Exchange

Return Securities on the Stock Exchange with `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'

stock_exchange_api = intrinio_sdk.StockExchangeApi()

identifier = 'identifier_example' # str | A Stock Exchange identifier (MIC or Intrinio ID)
next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = stock_exchange_api.get_stock_exchange_securities(identifier, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockExchangeApi->get_stock_exchange_securities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Stock Exchange identifier (MIC or Intrinio ID) | 
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**list[Security]**](Security.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

