# intrinio_sdk.StockExchangeApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_stock_exchanges**](StockExchangeApi.md#get_all_stock_exchanges) | **GET** /stock_exchanges | All Stock Exchanges
[**get_stock_exchange_betas**](StockExchangeApi.md#get_stock_exchange_betas) | **GET** /stock_exchanges/{identifier}/betas | Security Betas
[**get_stock_exchange_by_id**](StockExchangeApi.md#get_stock_exchange_by_id) | **GET** /stock_exchanges/{identifier} | Lookup Stock Exchange
[**get_stock_exchange_gainers**](StockExchangeApi.md#get_stock_exchange_gainers) | **GET** /stock_exchanges/{identifier}/gainers | Top Gainers by Exchange
[**get_stock_exchange_losers**](StockExchangeApi.md#get_stock_exchange_losers) | **GET** /stock_exchanges/{identifier}/losers | Top Losers by Exchange
[**get_stock_exchange_price_adjustments**](StockExchangeApi.md#get_stock_exchange_price_adjustments) | **GET** /stock_exchanges/{identifier}/prices/adjustments | Stock Price Adjustments by Exchange
[**get_stock_exchange_price_adjustments_dividends**](StockExchangeApi.md#get_stock_exchange_price_adjustments_dividends) | **GET** /stock_exchanges/{identifier}/prices/adjustments/dividends | Dividends by date for exchange
[**get_stock_exchange_price_adjustments_splits**](StockExchangeApi.md#get_stock_exchange_price_adjustments_splits) | **GET** /stock_exchanges/{identifier}/prices/adjustments/splits | Splits by date for exchange
[**get_stock_exchange_prices**](StockExchangeApi.md#get_stock_exchange_prices) | **GET** /stock_exchanges/{identifier}/prices | Stock Prices by Exchange
[**get_stock_exchange_quote**](StockExchangeApi.md#get_stock_exchange_quote) | **GET** /stock_exchanges/{identifier}/quote | Realtime Quote Prices by Exchange
[**get_stock_exchange_realtime_prices**](StockExchangeApi.md#get_stock_exchange_realtime_prices) | **GET** /stock_exchanges/{identifier}/prices/realtime | Realtime Stock Prices by Exchange
[**get_stock_exchange_securities**](StockExchangeApi.md#get_stock_exchange_securities) | **GET** /stock_exchanges/{identifier}/securities | Securities by Exchange



[//]: # (START_OPERATION)

[//]: # (CLASS:StockExchangeApi)

[//]: # (METHOD:get_all_stock_exchanges)

[//]: # (RETURN_TYPE:ApiResponseStockExchanges)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseStockExchanges.md)

[//]: # (OPERATION:get_all_stock_exchanges_v2)

[//]: # (ENDPOINT:/stock_exchanges)

[//]: # (DOCUMENT_LINK:StockExchangeApi.md#get_all_stock_exchanges)

## **get_all_stock_exchanges**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_all_stock_exchanges_v2)

[//]: # (START_OVERVIEW)

> ApiResponseStockExchanges get_all_stock_exchanges(city=city, country=country, country_code=country_code, page_size=page_size)

#### All Stock Exchanges


Returns all Stock Exchanges matching the specified parameters

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

city = 'New York'
country = 'UNITED STATES OF AMERICA'
country_code = 'US'
page_size = 100

response = intrinio.StockExchangeApi().get_all_stock_exchanges(city=city, country=country, country_code=country_code, page_size=page_size)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city** | str| Filter by city | [optional]   &nbsp;
 **country** | str| Filter by country | [optional]   &nbsp;
 **country_code** | str| Filter by ISO country code | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseStockExchanges**](ApiResponseStockExchanges.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:StockExchangeApi)

[//]: # (METHOD:get_stock_exchange_betas)

[//]: # (RETURN_TYPE:ApiResponseStockExchangeBetas)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseStockExchangeBetas.md)

[//]: # (OPERATION:get_stock_exchange_betas_v2)

[//]: # (ENDPOINT:/stock_exchanges/{identifier}/betas)

[//]: # (DOCUMENT_LINK:StockExchangeApi.md#get_stock_exchange_betas)

## **get_stock_exchange_betas**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_stock_exchange_betas_v2)

[//]: # (START_OVERVIEW)

> ApiResponseStockExchangeBetas get_stock_exchange_betas(identifier, type=type, date=date, page_size=page_size, next_page=next_page)

#### Security Betas


Returns security beta data in the Stock Exchange with the given `identifier`

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

identifier = 'USCOMP'
type = 'weekly'
date = "2024-04-24"
page_size = 100
next_page = ''

response = intrinio.StockExchangeApi().get_stock_exchange_betas(identifier, type=type, date=date, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Stock Exchange identifier (MIC or Intrinio ID) |   &nbsp;
 **type** | str| Only of the given type | [optional] [default to weekly]  &nbsp;
 **date** | [**object**](.md)| Return data for this period end date. | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseStockExchangeBetas**](ApiResponseStockExchangeBetas.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:StockExchangeApi)

[//]: # (METHOD:get_stock_exchange_by_id)

[//]: # (RETURN_TYPE:StockExchange)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:StockExchange.md)

[//]: # (OPERATION:get_stock_exchange_by_id_v2)

[//]: # (ENDPOINT:/stock_exchanges/{identifier})

[//]: # (DOCUMENT_LINK:StockExchangeApi.md#get_stock_exchange_by_id)

## **get_stock_exchange_by_id**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_stock_exchange_by_id_v2)

[//]: # (START_OVERVIEW)

> StockExchange get_stock_exchange_by_id(identifier)

#### Lookup Stock Exchange


Returns the Stock Exchange with the given `identifier`

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

identifier = 'USCOMP'

response = intrinio.StockExchangeApi().get_stock_exchange_by_id(identifier)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Stock Exchange identifier (MIC or Intrinio ID) |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**StockExchange**](StockExchange.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:StockExchangeApi)

[//]: # (METHOD:get_stock_exchange_gainers)

[//]: # (RETURN_TYPE:ApiResponseStockExchangeMovers)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseStockExchangeMovers.md)

[//]: # (OPERATION:get_stock_exchange_gainers_v2)

[//]: # (ENDPOINT:/stock_exchanges/{identifier}/gainers)

[//]: # (DOCUMENT_LINK:StockExchangeApi.md#get_stock_exchange_gainers)

## **get_stock_exchange_gainers**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_stock_exchange_gainers_v2)

[//]: # (START_OVERVIEW)

> ApiResponseStockExchangeMovers get_stock_exchange_gainers(identifier, min_price=min_price, page_size=page_size, source=source)

#### Top Gainers by Exchange


Returns securities with the highest gain percent change traded on the chosen stock exchange.

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

identifier = 'USCOMP'
min_price = 8.14
page_size = 100
source = 'delayed_sip'

response = intrinio.StockExchangeApi().get_stock_exchange_gainers(identifier, min_price=min_price, page_size=page_size, source=source)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Stock Exchange identifier (MIC or Intrinio ID) |   &nbsp;
 **min_price** | float| The minimum price filter | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **source** | str| Return the realtime price from the specified source instead of the most recent. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseStockExchangeMovers**](ApiResponseStockExchangeMovers.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:StockExchangeApi)

[//]: # (METHOD:get_stock_exchange_losers)

[//]: # (RETURN_TYPE:ApiResponseStockExchangeMovers)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseStockExchangeMovers.md)

[//]: # (OPERATION:get_stock_exchange_losers_v2)

[//]: # (ENDPOINT:/stock_exchanges/{identifier}/losers)

[//]: # (DOCUMENT_LINK:StockExchangeApi.md#get_stock_exchange_losers)

## **get_stock_exchange_losers**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_stock_exchange_losers_v2)

[//]: # (START_OVERVIEW)

> ApiResponseStockExchangeMovers get_stock_exchange_losers(identifier, min_price=min_price, page_size=page_size, source=source)

#### Top Losers by Exchange


Returns securities with the highest loss percent change traded on the chosen stock exchange.

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

identifier = 'USCOMP'
min_price = 8.14
page_size = 100
source = 'delayed_sip'

response = intrinio.StockExchangeApi().get_stock_exchange_losers(identifier, min_price=min_price, page_size=page_size, source=source)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Stock Exchange identifier (MIC or Intrinio ID) |   &nbsp;
 **min_price** | float| The minimum price filter | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **source** | str| Return the realtime price from the specified source instead of the most recent. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseStockExchangeMovers**](ApiResponseStockExchangeMovers.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:StockExchangeApi)

[//]: # (METHOD:get_stock_exchange_price_adjustments)

[//]: # (RETURN_TYPE:ApiResponseStockExchangeStockPriceAdjustments)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseStockExchangeStockPriceAdjustments.md)

[//]: # (OPERATION:get_stock_exchange_price_adjustments_v2)

[//]: # (ENDPOINT:/stock_exchanges/{identifier}/prices/adjustments)

[//]: # (DOCUMENT_LINK:StockExchangeApi.md#get_stock_exchange_price_adjustments)

## **get_stock_exchange_price_adjustments**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_stock_exchange_price_adjustments_v2)

[//]: # (START_OVERVIEW)

> ApiResponseStockExchangeStockPriceAdjustments get_stock_exchange_price_adjustments(identifier, date=date, page_size=page_size, next_page=next_page)

#### Stock Price Adjustments by Exchange


Returns stock price adjustments for the Stock Exchange with the given `identifier`

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

identifier = 'USCOMP'
date = '2018-08-14'
page_size = 100
next_page = ''

response = intrinio.StockExchangeApi().get_stock_exchange_price_adjustments(identifier, date=date, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Stock Exchange identifier (MIC or Intrinio ID) |   &nbsp;
 **date** | date| The date for which to return price adjustments | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseStockExchangeStockPriceAdjustments**](ApiResponseStockExchangeStockPriceAdjustments.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:StockExchangeApi)

[//]: # (METHOD:get_stock_exchange_price_adjustments_dividends)

[//]: # (RETURN_TYPE:ApiResponseStockExchangeStockPriceAdjustments)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseStockExchangeStockPriceAdjustments.md)

[//]: # (OPERATION:get_stock_exchange_price_adjustments_dividends_v2)

[//]: # (ENDPOINT:/stock_exchanges/{identifier}/prices/adjustments/dividends)

[//]: # (DOCUMENT_LINK:StockExchangeApi.md#get_stock_exchange_price_adjustments_dividends)

## **get_stock_exchange_price_adjustments_dividends**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_stock_exchange_price_adjustments_dividends_v2)

[//]: # (START_OVERVIEW)

> ApiResponseStockExchangeStockPriceAdjustments get_stock_exchange_price_adjustments_dividends(identifier, date=date, page_size=page_size, next_page=next_page)

#### Dividends by date for exchange


Returns dividend adjustments for the Stock Exchange with the given `identifier`

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

identifier = 'USCOMP'
date = '2025-06-01'
page_size = 100
next_page = ''

response = intrinio.StockExchangeApi().get_stock_exchange_price_adjustments_dividends(identifier, date=date, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Stock Exchange identifier (MIC or Intrinio ID) |   &nbsp;
 **date** | date| The date for which to return dividends | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseStockExchangeStockPriceAdjustments**](ApiResponseStockExchangeStockPriceAdjustments.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:StockExchangeApi)

[//]: # (METHOD:get_stock_exchange_price_adjustments_splits)

[//]: # (RETURN_TYPE:ApiResponseStockExchangeStockPriceAdjustments)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseStockExchangeStockPriceAdjustments.md)

[//]: # (OPERATION:get_stock_exchange_price_adjustments_splits_v2)

[//]: # (ENDPOINT:/stock_exchanges/{identifier}/prices/adjustments/splits)

[//]: # (DOCUMENT_LINK:StockExchangeApi.md#get_stock_exchange_price_adjustments_splits)

## **get_stock_exchange_price_adjustments_splits**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_stock_exchange_price_adjustments_splits_v2)

[//]: # (START_OVERVIEW)

> ApiResponseStockExchangeStockPriceAdjustments get_stock_exchange_price_adjustments_splits(identifier, date=date, page_size=page_size, next_page=next_page)

#### Splits by date for exchange


Returns split adjustments for the Stock Exchange with the given `identifier`

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

identifier = 'USCOMP'
date = '2025-06-01'
page_size = 100
next_page = ''

response = intrinio.StockExchangeApi().get_stock_exchange_price_adjustments_splits(identifier, date=date, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Stock Exchange identifier (MIC or Intrinio ID) |   &nbsp;
 **date** | date| The date for which to return splits | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseStockExchangeStockPriceAdjustments**](ApiResponseStockExchangeStockPriceAdjustments.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:StockExchangeApi)

[//]: # (METHOD:get_stock_exchange_prices)

[//]: # (RETURN_TYPE:ApiResponseStockExchangeStockPrices)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseStockExchangeStockPrices.md)

[//]: # (OPERATION:get_stock_exchange_prices_v2)

[//]: # (ENDPOINT:/stock_exchanges/{identifier}/prices)

[//]: # (DOCUMENT_LINK:StockExchangeApi.md#get_stock_exchange_prices)

## **get_stock_exchange_prices**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_stock_exchange_prices_v2)

[//]: # (START_OVERVIEW)

> ApiResponseStockExchangeStockPrices get_stock_exchange_prices(identifier, date=date, start_date=start_date, end_date=end_date, page_size=page_size, next_page=next_page, tickers=tickers, next_page2=next_page2)

#### Stock Prices by Exchange


Returns end-of-day stock prices for Securities on the Stock Exchange with `identifier` and on the `price_date` (or the latest date that prices are available)

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

identifier = 'USCOMP'
date = '2018-08-14'
start_date = '2020-08-14'
end_date = '2022-08-14'
page_size = 100
next_page = ''
tickers = ['AAPL,MSFT,NVDA']
next_page2 = ''

response = intrinio.StockExchangeApi().get_stock_exchange_prices(identifier, date=date, start_date=start_date, end_date=end_date, page_size=page_size, next_page=next_page, tickers=tickers, next_page2=next_page2)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Stock Exchange identifier (MIC or Intrinio ID) |   &nbsp;
 **date** | date| The date for which to return prices. May not be used with the start_date and end_date parameters. | [optional]   &nbsp;
 **start_date** | date| The start of the date range you&#39;re querying. May not be used with date parameter. | [optional]   &nbsp;
 **end_date** | date| The end of the date range you&#39;re querying. May not be used with date parameter. | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
 **tickers** | [**list[str]**](str.md)| The comma-delimited list of ticker symbols to filter down to. If not provided, the entire stock exchange is returned. | [optional]   &nbsp;
 **next_page2** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseStockExchangeStockPrices**](ApiResponseStockExchangeStockPrices.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:StockExchangeApi)

[//]: # (METHOD:get_stock_exchange_quote)

[//]: # (RETURN_TYPE:ApiResponseStockExchangeQuote)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseStockExchangeQuote.md)

[//]: # (OPERATION:get_stock_exchange_quote_v2)

[//]: # (ENDPOINT:/stock_exchanges/{identifier}/quote)

[//]: # (DOCUMENT_LINK:StockExchangeApi.md#get_stock_exchange_quote)

## **get_stock_exchange_quote**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_stock_exchange_quote_v2)

[//]: # (START_OVERVIEW)

> ApiResponseStockExchangeQuote get_stock_exchange_quote(identifier, tickers, source=source, active_only=active_only)

#### Realtime Quote Prices by Exchange


Returns many popular metrics for securities from a given exchange 'identifier' from multiple products conveniently in one API. Realtime stock price data requires at least one realtime product subscription (IEX, NASDAQ Basic, and/or Delayed SIP).  If you are subscribed to multiple realtime stock price products, the api will return the most recent realtime stock price. Previous close price and percent change fields require both an EoD US Stock Price subscription and a realtime stock price subscription. Market_cap, price_to_earnings, and dividendyield data fields require a fundamentals subscription.

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

identifier = 'USCOMP'
tickers = ['AAPL,MSFT,NVDA']
source = 'delayed_sip'
active_only = ''

response = intrinio.StockExchangeApi().get_stock_exchange_quote(identifier, tickers, source=source, active_only=active_only)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Stock Exchange identifier (MIC or Intrinio ID) |   &nbsp;
 **tickers** | [**list[str]**](str.md)| The comma-delimited list of ticker symbols to return quotes for. |   &nbsp;
 **source** | str| Return the realtime price from the specified source instead of the most recent. | [optional]   &nbsp;
 **active_only** | bool| Returns prices only from the most recent trading day. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseStockExchangeQuote**](ApiResponseStockExchangeQuote.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:StockExchangeApi)

[//]: # (METHOD:get_stock_exchange_realtime_prices)

[//]: # (RETURN_TYPE:ApiResponseStockExchangeRealtimeStockPrices)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseStockExchangeRealtimeStockPrices.md)

[//]: # (OPERATION:get_stock_exchange_realtime_prices_v2)

[//]: # (ENDPOINT:/stock_exchanges/{identifier}/prices/realtime)

[//]: # (DOCUMENT_LINK:StockExchangeApi.md#get_stock_exchange_realtime_prices)

## **get_stock_exchange_realtime_prices**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_stock_exchange_realtime_prices_v2)

[//]: # (START_OVERVIEW)

> ApiResponseStockExchangeRealtimeStockPrices get_stock_exchange_realtime_prices(identifier, source=source, active_only=active_only, traded_today=traded_today, page_size=page_size, tickers=tickers, next_page=next_page)

#### Realtime Stock Prices by Exchange


Returns realtime stock prices for the Stock Exchange with the given `identifier`

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

identifier = 'USCOMP'
source = ['iex,delayed_sip']
active_only = ''
traded_today = ''
page_size = 100
tickers = ['AAPL,MSFT,NVDA']
next_page = ''

response = intrinio.StockExchangeApi().get_stock_exchange_realtime_prices(identifier, source=source, active_only=active_only, traded_today=traded_today, page_size=page_size, tickers=tickers, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Stock Exchange identifier (MIC or Intrinio ID) |   &nbsp;
 **source** | [**list[str]**](str.md)| Return realtime prices from the specified comma-delimited data sources. If no source is specified, all sources available to user are used. | [optional]   &nbsp;
 **active_only** | bool| Returns prices only from the most recent trading day. | [optional]   &nbsp;
 **traded_today** | bool| Returns prices only from securities which have traded on the most recent trading day. | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **tickers** | [**list[str]**](str.md)| The comma-delimited list of ticker symbols to filter to. If not provided, the entire stock exchange is returned. | [optional]   &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseStockExchangeRealtimeStockPrices**](ApiResponseStockExchangeRealtimeStockPrices.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:StockExchangeApi)

[//]: # (METHOD:get_stock_exchange_securities)

[//]: # (RETURN_TYPE:ApiResponseStockExchangeSecurities)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseStockExchangeSecurities.md)

[//]: # (OPERATION:get_stock_exchange_securities_v2)

[//]: # (ENDPOINT:/stock_exchanges/{identifier}/securities)

[//]: # (DOCUMENT_LINK:StockExchangeApi.md#get_stock_exchange_securities)

## **get_stock_exchange_securities**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_stock_exchange_securities_v2)

[//]: # (START_OVERVIEW)

> ApiResponseStockExchangeSecurities get_stock_exchange_securities(identifier, page_size=page_size, next_page=next_page)

#### Securities by Exchange


Returns Securities traded on the Stock Exchange with `identifier`

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

identifier = 'USCOMP'
page_size = 100
next_page = ''

response = intrinio.StockExchangeApi().get_stock_exchange_securities(identifier, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Stock Exchange identifier (MIC or Intrinio ID) |   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseStockExchangeSecurities**](ApiResponseStockExchangeSecurities.md)

[//]: # (END_OPERATION)

