# intrinio_sdk.OptionsApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_options_tickers**](OptionsApi.md#get_all_options_tickers) | **GET** /options/tickers | Options Tickers
[**get_option_aggregates**](OptionsApi.md#get_option_aggregates) | **GET** /options/aggregates | Total open interest and volume aggregated by ticker
[**get_option_expirations_realtime**](OptionsApi.md#get_option_expirations_realtime) | **GET** /options/expirations/{symbol}/realtime | Options Expirations
[**get_option_strikes_realtime**](OptionsApi.md#get_option_strikes_realtime) | **GET** /options/strikes/{symbol}/{strike}/realtime | Option Strikes Realtime
[**get_option_trades**](OptionsApi.md#get_option_trades) | **GET** /options/trades | Option Trades
[**get_option_trades_by_contract**](OptionsApi.md#get_option_trades_by_contract) | **GET** /options/{identifier}/trades | Option Trades By Contract
[**get_options**](OptionsApi.md#get_options) | **GET** /options/{symbol} | Options
[**get_options_by_symbol_realtime**](OptionsApi.md#get_options_by_symbol_realtime) | **GET** /options/{symbol}/realtime | Options by Symbol Realtime
[**get_options_chain**](OptionsApi.md#get_options_chain) | **GET** /options/chain/{symbol}/{expiration} | Options Chain
[**get_options_chain_eod**](OptionsApi.md#get_options_chain_eod) | **GET** /options/chain/{symbol}/{expiration}/eod | Options Chain EOD
[**get_options_chain_realtime**](OptionsApi.md#get_options_chain_realtime) | **GET** /options/chain/{symbol}/{expiration}/realtime | Options Chain Realtime
[**get_options_expirations**](OptionsApi.md#get_options_expirations) | **GET** /options/expirations/{symbol} | Options Expirations
[**get_options_expirations_eod**](OptionsApi.md#get_options_expirations_eod) | **GET** /options/expirations/{symbol}/eod | Options Expirations
[**get_options_greeks_by_contract**](OptionsApi.md#get_options_greeks_by_contract) | **GET** /options/greeks/{contract}/realtime | Option Greeks &amp; Derived Price by Contract
[**get_options_greeks_by_ticker**](OptionsApi.md#get_options_greeks_by_ticker) | **GET** /options/greeks/by_ticker/{identifier}/realtime | Options Realtime Greeks &amp; Derived Price by Ticker
[**get_options_implied_move_by_symbol**](OptionsApi.md#get_options_implied_move_by_symbol) | **GET** /options/implied_move/{symbol}/{expiration_date} | Options Implied Move By Symbol
[**get_options_interval_by_contract**](OptionsApi.md#get_options_interval_by_contract) | **GET** /options/interval/{identifier} | Options Intervals By Contract
[**get_options_interval_movers**](OptionsApi.md#get_options_interval_movers) | **GET** /options/interval/movers | Options Intervals Movers
[**get_options_interval_movers_change**](OptionsApi.md#get_options_interval_movers_change) | **GET** /options/interval/movers/change | Options Intervals Movers By Change
[**get_options_interval_movers_volume**](OptionsApi.md#get_options_interval_movers_volume) | **GET** /options/interval/movers/volume | Options Intervals Movers By Volume
[**get_options_prices**](OptionsApi.md#get_options_prices) | **GET** /options/prices/{identifier} | Option Prices
[**get_options_prices_batch_realtime**](OptionsApi.md#get_options_prices_batch_realtime) | **POST** /options/prices/realtime/batch | Option Prices Batch Realtime
[**get_options_prices_eod**](OptionsApi.md#get_options_prices_eod) | **GET** /options/prices/{identifier}/eod | Option Prices EOD
[**get_options_prices_eod_by_ticker**](OptionsApi.md#get_options_prices_eod_by_ticker) | **GET** /options/prices/by_ticker/{symbol}/eod | Option Prices End of Day By Ticker
[**get_options_prices_realtime**](OptionsApi.md#get_options_prices_realtime) | **GET** /options/prices/{identifier}/realtime | Option Prices Realtime
[**get_options_prices_realtime_by_ticker**](OptionsApi.md#get_options_prices_realtime_by_ticker) | **GET** /options/prices/by_ticker/{symbol}/realtime | Option Prices Realtime By Ticker
[**get_options_snapshots**](OptionsApi.md#get_options_snapshots) | **GET** /options/snapshots | Option Prices Realtime Snapshot
[**get_options_stats_realtime**](OptionsApi.md#get_options_stats_realtime) | **GET** /options/prices/{identifier}/realtime/stats | Option Stats Realtime
[**get_unusual_activity**](OptionsApi.md#get_unusual_activity) | **GET** /options/unusual_activity/{symbol} | Options Unusual Activity
[**get_unusual_activity_intraday**](OptionsApi.md#get_unusual_activity_intraday) | **GET** /options/unusual_activity/{symbol}/intraday | Options Unusual Activity Intraday
[**get_unusual_activity_universal**](OptionsApi.md#get_unusual_activity_universal) | **GET** /options/unusual_activity | Options Unusual Activity Universal
[**get_unusual_activity_universal_intraday**](OptionsApi.md#get_unusual_activity_universal_intraday) | **GET** /options/unusual_activity/intraday | Options Unusual Activity Universal Intraday



[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_all_options_tickers)

[//]: # (RETURN_TYPE:ApiResponseOptionsTickers)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsTickers.md)

[//]: # (OPERATION:get_all_options_tickers_v2)

[//]: # (ENDPOINT:/options/tickers)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_all_options_tickers)

## **get_all_options_tickers**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_all_options_tickers_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsTickers get_all_options_tickers(use_underlying_symbols=use_underlying_symbols)

#### Options Tickers


Returns all tickers that have existing options contracts.

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

use_underlying_symbols = False

response = intrinio.OptionsApi().get_all_options_tickers(use_underlying_symbols=use_underlying_symbols)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use_underlying_symbols** | bool| Use underlying symbol vs contract symbol | [optional] [default to False]  &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsTickers**](ApiResponseOptionsTickers.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_option_aggregates)

[//]: # (RETURN_TYPE:ApiResponseOptionsAggregates)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsAggregates.md)

[//]: # (OPERATION:get_option_aggregates_v2)

[//]: # (ENDPOINT:/options/aggregates)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_option_aggregates)

## **get_option_aggregates**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_option_aggregates_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsAggregates get_option_aggregates(date=date, page_size=page_size, next_page=next_page)

#### Total open interest and volume aggregated by ticker


Returns total open interest and volume by ticker

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

date = "2024-04-24"
page_size = 100
next_page = ''

response = intrinio.OptionsApi().get_option_aggregates(date=date, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date** | [**object**](.md)| Return aggregated data for this date | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsAggregates**](ApiResponseOptionsAggregates.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_option_expirations_realtime)

[//]: # (RETURN_TYPE:ApiResponseOptionsExpirations)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsExpirations.md)

[//]: # (OPERATION:get_option_expirations_realtime_v2)

[//]: # (ENDPOINT:/options/expirations/{symbol}/realtime)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_option_expirations_realtime)

## **get_option_expirations_realtime**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_option_expirations_realtime_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsExpirations get_option_expirations_realtime(symbol, after=after, before=before, source=source, include_related_symbols=include_related_symbols)

#### Options Expirations


Returns a list of all current and upcoming option contract expiration dates for a particular symbol.

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

symbol = 'MSFT'
after = '2022-01-01'
before = '2023-04-01'
source = ''
include_related_symbols = False

response = intrinio.OptionsApi().get_option_expirations_realtime(symbol, after=after, before=before, source=source, include_related_symbols=include_related_symbols)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | str| The option symbol, corresponding to the underlying security. |   &nbsp;
 **after** | str| Return option contract expiration dates after this date. | [optional]   &nbsp;
 **before** | str| Return option contract expiration dates before this date. | [optional]   &nbsp;
 **source** | str| Realtime or 15-minute delayed contracts. | [optional]   &nbsp;
 **include_related_symbols** | bool| Include related symbols that end in a 1 or 2 because of a corporate action. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsExpirations**](ApiResponseOptionsExpirations.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_option_strikes_realtime)

[//]: # (RETURN_TYPE:ApiResponseOptionsChainRealtime)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsChainRealtime.md)

[//]: # (OPERATION:get_option_strikes_realtime_v2)

[//]: # (ENDPOINT:/options/strikes/{symbol}/{strike}/realtime)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_option_strikes_realtime)

## **get_option_strikes_realtime**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_option_strikes_realtime_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsChainRealtime get_option_strikes_realtime(symbol, strike, source=source, stock_price_source=stock_price_source, model=model, show_extended_price=show_extended_price, include_related_symbols=include_related_symbols)

#### Option Strikes Realtime


Returns a list of the latest top of the order book size and premium (bid / ask), the latest trade size and premium as well as the greeks and implied volatility for all call/put contracts that match the strike and symbol specified.

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

symbol = 'MSFT'
strike = 95
source = ''
stock_price_source = ''
model = ''
show_extended_price = ''
include_related_symbols = False

response = intrinio.OptionsApi().get_option_strikes_realtime(symbol, strike, source=source, stock_price_source=stock_price_source, model=model, show_extended_price=show_extended_price, include_related_symbols=include_related_symbols)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | str| The option symbol, corresponding to the underlying security. |   &nbsp;
 **strike** | float| The strike price of the option contract. This will return options contracts with strike price equal to this price. |   &nbsp;
 **source** | str| Realtime or delayed. | [optional]   &nbsp;
 **stock_price_source** | str| Source for underlying price for calculating Greeks. | [optional]   &nbsp;
 **model** | str| Model for calculating Greek values. Default is black_scholes. | [optional]   &nbsp;
 **show_extended_price** | bool| Whether to include open close high low type fields. | [optional]   &nbsp;
 **include_related_symbols** | bool| Include related symbols that end in a 1 or 2 because of a corporate action. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsChainRealtime**](ApiResponseOptionsChainRealtime.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_option_trades)

[//]: # (RETURN_TYPE:OptionTradesResult)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:OptionTradesResult.md)

[//]: # (OPERATION:get_option_trades_v2)

[//]: # (ENDPOINT:/options/trades)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_option_trades)

## **get_option_trades**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_option_trades_v2)

[//]: # (START_OVERVIEW)

> OptionTradesResult get_option_trades(source=source, start_date=start_date, start_time=start_time, end_date=end_date, end_time=end_time, timezone=timezone, page_size=page_size, min_size=min_size, security=security, next_page=next_page)

#### Option Trades


Returns all trades between start time and end time, up to seven days ago for the specified source.

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

source = ''
start_date = ''
start_time = ''
end_date = ''
end_time = ''
timezone = 'UTC'
page_size = 100
min_size = 100
security = 'AAPL'
next_page = ''

response = intrinio.OptionsApi().get_option_trades(source=source, start_date=start_date, start_time=start_time, end_date=end_date, end_time=end_time, timezone=timezone, page_size=page_size, min_size=min_size, security=security, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | str| The specific source of the data being requested. | [optional]   &nbsp;
 **start_date** | date| The start date for the data being requested. | [optional]   &nbsp;
 **start_time** | str| The start time for the data being requested. | [optional]   &nbsp;
 **end_date** | date| The end date for the data being requested. | [optional]   &nbsp;
 **end_time** | str| The end time for the data being requested. | [optional]   &nbsp;
 **timezone** | str| The timezone the start and end date/times use. | [optional] [default to UTC]  &nbsp;
 **page_size** | int| The maximum number of results to return per page. | [optional] [default to 100]  &nbsp;
 **min_size** | int| Trades must be larger or equal to this size. | [optional]   &nbsp;
 **security** | str| The ticker symbol for which trades are being requested. | [optional]   &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**OptionTradesResult**](OptionTradesResult.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_option_trades_by_contract)

[//]: # (RETURN_TYPE:OptionTradesResult)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:OptionTradesResult.md)

[//]: # (OPERATION:get_option_trades_by_contract_v2)

[//]: # (ENDPOINT:/options/{identifier}/trades)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_option_trades_by_contract)

## **get_option_trades_by_contract**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_option_trades_by_contract_v2)

[//]: # (START_OVERVIEW)

> OptionTradesResult get_option_trades_by_contract(identifier, source=source, start_date=start_date, start_time=start_time, end_date=end_date, end_time=end_time, timezone=timezone, page_size=page_size, min_size=min_size, next_page=next_page)

#### Option Trades By Contract


Returns all trades for a contract between start time and end time, up to seven days ago for the specified source.

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

identifier = 'AAPL__261218C00230000'
source = ''
start_date = ''
start_time = ''
end_date = ''
end_time = ''
timezone = 'UTC'
page_size = 100
min_size = 100
next_page = ''

response = intrinio.OptionsApi().get_option_trades_by_contract(identifier, source=source, start_date=start_date, start_time=start_time, end_date=end_date, end_time=end_time, timezone=timezone, page_size=page_size, min_size=min_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| The option contract for which trades are being requested. |   &nbsp;
 **source** | str| The specific source of the data being requested. | [optional]   &nbsp;
 **start_date** | date| The start date for the data being requested. | [optional]   &nbsp;
 **start_time** | str| The start time for the data being requested. | [optional]   &nbsp;
 **end_date** | date| The end date for the data being requested. | [optional]   &nbsp;
 **end_time** | str| The end time for the data being requested. | [optional]   &nbsp;
 **timezone** | str| The timezone the start and end date/times use. | [optional] [default to UTC]  &nbsp;
 **page_size** | int| The maximum number of results to return per page. | [optional] [default to 100]  &nbsp;
 **min_size** | int| Trades must be larger or equal to this size. | [optional]   &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**OptionTradesResult**](OptionTradesResult.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options)

[//]: # (RETURN_TYPE:ApiResponseOptions)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptions.md)

[//]: # (OPERATION:get_options_v2)

[//]: # (ENDPOINT:/options/{symbol})

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options)

## **get_options**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptions get_options(symbol, type=type, strike=strike, strike_greater_than=strike_greater_than, strike_less_than=strike_less_than, expiration=expiration, expiration_after=expiration_after, expiration_before=expiration_before, page_size=page_size, next_page=next_page)

#### Options


Returns a list of all securities that have options listed and are tradable on a US market exchange. Useful to retrieve the entire universe.  Available via a 3rd party, contact sales for a trial.

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

symbol = 'AAPL'
type = 'put'
page_size = 100
next_page = ''

response = intrinio.OptionsApi().get_options(symbol, type=type, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | str| The option symbol, corresponding to the underlying security. |   &nbsp;
 **type** | str| The option contract type. | [optional]   &nbsp;
 **strike** | float| The strike price of the option contract. This will return options contracts with strike price equal to this price. | [optional]   &nbsp;
 **strike_greater_than** | float| The strike price of the option contract. This will return options contracts with strike prices greater than this price. | [optional]   &nbsp;
 **strike_less_than** | float| The strike price of the option contract. This will return options contracts with strike prices less than this price. | [optional]   &nbsp;
 **expiration** | str| The expiration date of the option contract. This will return options contracts with expiration dates on this date. | [optional]   &nbsp;
 **expiration_after** | str| The expiration date of the option contract. This will return options contracts with expiration dates after this date. | [optional]   &nbsp;
 **expiration_before** | str| The expiration date of the option contract. This will return options contracts with expiration dates before this date. | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptions**](ApiResponseOptions.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options_by_symbol_realtime)

[//]: # (RETURN_TYPE:ApiResponseOptionsRealtime)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsRealtime.md)

[//]: # (OPERATION:get_options_by_symbol_realtime_v2)

[//]: # (ENDPOINT:/options/{symbol}/realtime)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options_by_symbol_realtime)

## **get_options_by_symbol_realtime**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_by_symbol_realtime_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsRealtime get_options_by_symbol_realtime(symbol, type=type, strike=strike, strike_greater_than=strike_greater_than, strike_less_than=strike_less_than, expiration=expiration, expiration_after=expiration_after, expiration_before=expiration_before, source=source, include_related_symbols=include_related_symbols)

#### Options by Symbol Realtime


Returns a list of all securities that have options listed and are tradable on a US market exchange. Useful to retrieve the entire universe.

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

symbol = 'AAPL'
type = 'put'
source = ''
include_related_symbols = False

response = intrinio.OptionsApi().get_options_by_symbol_realtime(symbol, type=type, source=source, include_related_symbols=include_related_symbols)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | str| The option symbol, corresponding to the underlying security. |   &nbsp;
 **type** | str| The option contract type. | [optional]   &nbsp;
 **strike** | float| The strike price of the option contract. This will return options contracts with strike price equal to this price. | [optional]   &nbsp;
 **strike_greater_than** | float| The strike price of the option contract. This will return options contracts with strike prices greater than this price. | [optional]   &nbsp;
 **strike_less_than** | float| The strike price of the option contract. This will return options contracts with strike prices less than this price. | [optional]   &nbsp;
 **expiration** | str| The expiration date of the option contract. This will return options contracts with expiration dates on this date. | [optional]   &nbsp;
 **expiration_after** | str| The expiration date of the option contract. This will return options contracts with expiration dates after this date. | [optional]   &nbsp;
 **expiration_before** | str| The expiration date of the option contract. This will return options contracts with expiration dates before this date. | [optional]   &nbsp;
 **source** | str| Realtime or 15-minute delayed contracts. | [optional]   &nbsp;
 **include_related_symbols** | bool| Include related symbols that end in a 1 or 2 because of a corporate action. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsRealtime**](ApiResponseOptionsRealtime.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options_chain)

[//]: # (RETURN_TYPE:ApiResponseOptionsChain)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsChain.md)

[//]: # (OPERATION:get_options_chain_v2)

[//]: # (ENDPOINT:/options/chain/{symbol}/{expiration})

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options_chain)

## **get_options_chain**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_chain_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsChain get_options_chain(symbol, expiration, date=date, type=type, strike=strike, strike_greater_than=strike_greater_than, strike_less_than=strike_less_than, moneyness=moneyness, page_size=page_size)

#### Options Chain


Returns a list of the historical end-of-day top of the order book size and premium (bid / ask), the latest trade size and premium as well as the greeks and implied volatility for all option contracts currently associated with the option chain.  Available via a 3rd party, contact sales for a trial.

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

symbol = 'MSFT'
expiration = '2019-04-05'
date = ''
type = ''
moneyness = ''
page_size = 100

response = intrinio.OptionsApi().get_options_chain(symbol, expiration, date=date, type=type, moneyness=moneyness, page_size=page_size)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | str| The option symbol, corresponding to the underlying security. |   &nbsp;
 **expiration** | str| The expiration date of the options contract |   &nbsp;
 **date** | date| The date of the option price. Returns option prices on this date. | [optional]   &nbsp;
 **type** | str| The option contract type. | [optional]   &nbsp;
 **strike** | float| The strike price of the option contract. This will return options contracts with strike price equal to this price. | [optional]   &nbsp;
 **strike_greater_than** | float| The strike price of the option contract. This will return options contracts with strike prices greater than this price. | [optional]   &nbsp;
 **strike_less_than** | float| The strike price of the option contract. This will return options contracts with strike prices less than this price. | [optional]   &nbsp;
 **moneyness** | str| The moneyness of the options contracts to return. &#39;all&#39; will return all options contracts. &#39;in_the_money&#39; will return options contracts that are in the money (call options with strike prices below the current price, put options with strike prices above the current price). &#39;out_of_they_money&#39; will return options contracts that are out of the money (call options with strike prices above the current price, put options with strike prices below the current price). &#39;near_the_money&#39; will return options contracts that are $0.50 or less away from being in the money. | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsChain**](ApiResponseOptionsChain.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options_chain_eod)

[//]: # (RETURN_TYPE:ApiResponseOptionsChainEod)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsChainEod.md)

[//]: # (OPERATION:get_options_chain_eod_v2)

[//]: # (ENDPOINT:/options/chain/{symbol}/{expiration}/eod)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options_chain_eod)

## **get_options_chain_eod**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_chain_eod_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsChainEod get_options_chain_eod(symbol, expiration, type=type, strike=strike, strike_greater_than=strike_greater_than, strike_less_than=strike_less_than, date=date, include_related_symbols=include_related_symbols)

#### Options Chain EOD


Returns all EOD options contracts and their prices for the given symbol and expiration date.

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

symbol = 'AAPL'
expiration = '2023-01-20'
type = ''
include_related_symbols = False

response = intrinio.OptionsApi().get_options_chain_eod(symbol, expiration, type=type, include_related_symbols=include_related_symbols)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | str| The option symbol, corresponding to the underlying security. |   &nbsp;
 **expiration** | str| The expiration date of the options contract |   &nbsp;
 **type** | str| The option contract type. | [optional]   &nbsp;
 **strike** | float| The strike price of the option contract. This will return options contracts with strike price equal to this price. | [optional]   &nbsp;
 **strike_greater_than** | float| The strike price of the option contract. This will return options contracts with strike prices greater than this price. | [optional]   &nbsp;
 **strike_less_than** | float| The strike price of the option contract. This will return options contracts with strike prices less than this price. | [optional]   &nbsp;
 **date** | date| The date to retrieve prices for | [optional]   &nbsp;
 **include_related_symbols** | bool| Include related symbols that end in a 1 or 2 because of a corporate action. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsChainEod**](ApiResponseOptionsChainEod.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options_chain_realtime)

[//]: # (RETURN_TYPE:ApiResponseOptionsChainRealtime)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsChainRealtime.md)

[//]: # (OPERATION:get_options_chain_realtime_v2)

[//]: # (ENDPOINT:/options/chain/{symbol}/{expiration}/realtime)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options_chain_realtime)

## **get_options_chain_realtime**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_chain_realtime_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsChainRealtime get_options_chain_realtime(symbol, expiration, source=source, type=type, strike=strike, strike_greater_than=strike_greater_than, strike_less_than=strike_less_than, volume_greater_than=volume_greater_than, volume_less_than=volume_less_than, open_interest_greater_than=open_interest_greater_than, open_interest_less_than=open_interest_less_than, moneyness=moneyness, stock_price_source=stock_price_source, model=model, show_extended_price=show_extended_price, include_related_symbols=include_related_symbols)

#### Options Chain Realtime


Returns a list of the latest National Best Bid & Offer (NBBO) top of the order book size and premium (bid / ask), the latest trade size and premium as well as the greeks and implied volatility for all option contracts currently associated with the option chain.

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

symbol = 'MSFT'
expiration = '2023-01-20'
source = ''
type = ''
moneyness = ''
stock_price_source = ''
model = ''
show_extended_price = ''
include_related_symbols = False

response = intrinio.OptionsApi().get_options_chain_realtime(symbol, expiration, source=source, type=type, moneyness=moneyness, stock_price_source=stock_price_source, model=model, show_extended_price=show_extended_price, include_related_symbols=include_related_symbols)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | str| The option symbol, corresponding to the underlying security. |   &nbsp;
 **expiration** | str| The expiration date of the options contract |   &nbsp;
 **source** | str| Realtime or 15-minute delayed contracts. | [optional]   &nbsp;
 **type** | str| The option contract type. | [optional]   &nbsp;
 **strike** | float| The strike price of the option contract. This will return options contracts with strike price equal to this price. | [optional]   &nbsp;
 **strike_greater_than** | float| The strike price of the option contract. This will return options contracts with strike prices greater than this price. | [optional]   &nbsp;
 **strike_less_than** | float| The strike price of the option contract. This will return options contracts with strike prices less than this price. | [optional]   &nbsp;
 **volume_greater_than** | float| The volume of the option contract. This will return options contracts with volumes greater than this amount. | [optional]   &nbsp;
 **volume_less_than** | float| The volume of the option contract. This will return options contracts with volumes less than this amout. | [optional]   &nbsp;
 **open_interest_greater_than** | float| The open interest of the option contract. This will return options contracts with open interest greater than this amount. | [optional]   &nbsp;
 **open_interest_less_than** | float| The open interest of the option contract. This will return options contracts with open interest less than this amount. | [optional]   &nbsp;
 **moneyness** | str| The moneyness of the options contracts to return. &#39;all&#39; will return all options contracts. &#39;in_the_money&#39; will return options contracts that are in the money (call options with strike prices below the current price, put options with strike prices above the current price). &#39;out_of_they_money&#39; will return options contracts that are out of the money (call options with strike prices above the current price, put options with strike prices below the current price). &#39;near_the_money&#39; will return options contracts that are $0.50 or less away from being in the money.  Requires subscription to realtime stock price data. | [optional]   &nbsp;
 **stock_price_source** | str| Source for underlying price for calculating Greeks. | [optional]   &nbsp;
 **model** | str| Model for calculating Greek values. Default is black_scholes. | [optional]   &nbsp;
 **show_extended_price** | bool| Whether to include open close high low type fields. | [optional]   &nbsp;
 **include_related_symbols** | bool| Include related symbols that end in a 1 or 2 because of a corporate action. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsChainRealtime**](ApiResponseOptionsChainRealtime.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options_expirations)

[//]: # (RETURN_TYPE:ApiResponseOptionsExpirations)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsExpirations.md)

[//]: # (OPERATION:get_options_expirations_v2)

[//]: # (ENDPOINT:/options/expirations/{symbol})

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options_expirations)

## **get_options_expirations**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_expirations_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsExpirations get_options_expirations(symbol, after=after, before=before)

#### Options Expirations


Returns a list of all current and upcoming option contract expiration dates for a particular symbol.  Available via a 3rd party, contact sales for a trial.

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

symbol = 'MSFT'
after = '2019-01-01'
before = '2019-12-31'

response = intrinio.OptionsApi().get_options_expirations(symbol, after=after, before=before)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | str| The option symbol, corresponding to the underlying security. |   &nbsp;
 **after** | str| Return option contract expiration dates after this date. | [optional]   &nbsp;
 **before** | str| Return option contract expiration dates before this date. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsExpirations**](ApiResponseOptionsExpirations.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options_expirations_eod)

[//]: # (RETURN_TYPE:ApiResponseOptionsExpirations)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsExpirations.md)

[//]: # (OPERATION:get_options_expirations_eod_v2)

[//]: # (ENDPOINT:/options/expirations/{symbol}/eod)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options_expirations_eod)

## **get_options_expirations_eod**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_expirations_eod_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsExpirations get_options_expirations_eod(symbol, after=after, before=before, include_related_symbols=include_related_symbols)

#### Options Expirations


Returns a list of all current and upcoming option contract expiration dates for a particular symbol.

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

symbol = 'MSFT'
after = '2019-01-01'
before = '2019-12-31'
include_related_symbols = False

response = intrinio.OptionsApi().get_options_expirations_eod(symbol, after=after, before=before, include_related_symbols=include_related_symbols)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | str| The option symbol, corresponding to the underlying security. |   &nbsp;
 **after** | str| Return option contract expiration dates after this date. | [optional]   &nbsp;
 **before** | str| Return option contract expiration dates before this date. | [optional]   &nbsp;
 **include_related_symbols** | bool| Include related symbols that end in a 1 or 2 because of a corporate action. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsExpirations**](ApiResponseOptionsExpirations.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options_greeks_by_contract)

[//]: # (RETURN_TYPE:ApiResponseOptionsGreekContractRealtime)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsGreekContractRealtime.md)

[//]: # (OPERATION:get_options_greeks_by_contract_v2)

[//]: # (ENDPOINT:/options/greeks/{contract}/realtime)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options_greeks_by_contract)

## **get_options_greeks_by_contract**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_greeks_by_contract_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsGreekContractRealtime get_options_greeks_by_contract(contract, source=source, model=model, iv_mode=iv_mode, stock_price_source=stock_price_source)

#### Option Greeks & Derived Price by Contract


Retrieves realtime options greeks data for a specific options contract

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

contract = 'contract_example'
source = 'source_example'
model = 'black_scholes'
iv_mode = 'iv_mode_example'
stock_price_source = 'stock_price_source_example'

response = intrinio.OptionsApi().get_options_greeks_by_contract(contract, source=source, model=model, iv_mode=iv_mode, stock_price_source=stock_price_source)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | str| The options contract identifier |   &nbsp;
 **source** | str| The data source to use for options data | [optional]   &nbsp;
 **model** | str| The options pricing model to use for greeks calculations | [optional] [default to black_scholes]  &nbsp;
 **iv_mode** | str| The implied volatility calculation mode | [optional]   &nbsp;
 **stock_price_source** | str| The data source to use for underlying stock prices | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsGreekContractRealtime**](ApiResponseOptionsGreekContractRealtime.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options_greeks_by_ticker)

[//]: # (RETURN_TYPE:ApiResponseOptionsGreeksByTickerRealtime)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsGreeksByTickerRealtime.md)

[//]: # (OPERATION:get_options_greeks_by_ticker_v2)

[//]: # (ENDPOINT:/options/greeks/by_ticker/{identifier}/realtime)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options_greeks_by_ticker)

## **get_options_greeks_by_ticker**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_greeks_by_ticker_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsGreeksByTickerRealtime get_options_greeks_by_ticker(identifier, source=source, model=model, iv_mode=iv_mode, stock_price_source=stock_price_source, expiration_start_date=expiration_start_date, expiration_end_date=expiration_end_date, strike=strike, strike_greater_than=strike_greater_than, strike_less_than=strike_less_than, page_size=page_size)

#### Options Realtime Greeks & Derived Price by Ticker


Retrieves realtime options greeks data for all contracts of a given ticker symbol

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

identifier = 'identifier_example'
source = 'source_example'
model = 'black_scholes'
iv_mode = 'iv_mode_example'
stock_price_source = 'stock_price_source_example'
expiration_start_date = '2013-10-20'
expiration_end_date = '2013-10-20'
strike = 3.4
strike_greater_than = 3.4
strike_less_than = 3.4
page_size = 250

response = intrinio.OptionsApi().get_options_greeks_by_ticker(identifier, source=source, model=model, iv_mode=iv_mode, stock_price_source=stock_price_source, expiration_start_date=expiration_start_date, expiration_end_date=expiration_end_date, strike=strike, strike_greater_than=strike_greater_than, strike_less_than=strike_less_than, page_size=page_size)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| The ticker symbol to get options greeks for |   &nbsp;
 **source** | str| The data source to use for options data | [optional]   &nbsp;
 **model** | str| The options pricing model to use for greeks calculations | [optional] [default to black_scholes]  &nbsp;
 **iv_mode** | str| The implied volatility calculation mode | [optional]   &nbsp;
 **stock_price_source** | str| The data source to use for underlying stock prices | [optional]   &nbsp;
 **expiration_start_date** | date| Filter options by expiration date (start) | [optional]   &nbsp;
 **expiration_end_date** | date| Filter options by expiration date (end) | [optional]   &nbsp;
 **strike** | float| Filter options by strike price | [optional]   &nbsp;
 **strike_greater_than** | float| Filter options by minimum strike price | [optional]   &nbsp;
 **strike_less_than** | float| Filter options by maximum strike price | [optional]   &nbsp;
 **page_size** | int| Number of results to return per page | [optional] [default to 250]  &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsGreeksByTickerRealtime**](ApiResponseOptionsGreeksByTickerRealtime.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options_implied_move_by_symbol)

[//]: # (RETURN_TYPE:ApiResponseOptionsImpliedMove)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsImpliedMove.md)

[//]: # (OPERATION:get_options_implied_move_by_symbol_v2)

[//]: # (ENDPOINT:/options/implied_move/{symbol}/{expiration_date})

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options_implied_move_by_symbol)

## **get_options_implied_move_by_symbol**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_implied_move_by_symbol_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsImpliedMove get_options_implied_move_by_symbol(symbol, expiration_date, percentage=percentage, source=source)

#### Options Implied Move By Symbol


Returns the implied move data points for a ticker symbol.

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

symbol = 'TSLA'
expiration_date = '2025-05-30'
percentage = 0.85
source = ''

response = intrinio.OptionsApi().get_options_implied_move_by_symbol(symbol, expiration_date, percentage=percentage, source=source)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | str| The ticker symbol for the contracts. |   &nbsp;
 **expiration_date** | date| The expiration date for the contracts to consider. |   &nbsp;
 **percentage** | [**object**](.md)| Percentage to multiply the straddle by. Defaults to 0.85. | [optional]   &nbsp;
 **source** | str| Realtime or 15-minute delayed contracts. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsImpliedMove**](ApiResponseOptionsImpliedMove.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options_interval_by_contract)

[//]: # (RETURN_TYPE:OptionIntervalsResult)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:OptionIntervalsResult.md)

[//]: # (OPERATION:get_options_interval_by_contract_v2)

[//]: # (ENDPOINT:/options/interval/{identifier})

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options_interval_by_contract)

## **get_options_interval_by_contract**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_interval_by_contract_v2)

[//]: # (START_OVERVIEW)

> OptionIntervalsResult get_options_interval_by_contract(identifier, interval_size, source=source, page_size=page_size, end_time=end_time)

#### Options Intervals By Contract


Returns a list of interval data points for a contract.

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

identifier = 'SPY___230103P00380000'
interval_size = '5m'
source = ''
page_size = 100
end_time = ''

response = intrinio.OptionsApi().get_options_interval_by_contract(identifier, interval_size, source=source, page_size=page_size, end_time=end_time)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| The Intrinio ID or code of the options contract to request intervals for. |   &nbsp;
 **interval_size** | str| The time length of the interval. |   &nbsp;
 **source** | str| Realtime or 15-minute delayed contracts. | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **end_time** | datetime| The inclusive UTC date and time the intervals end at. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**OptionIntervalsResult**](OptionIntervalsResult.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options_interval_movers)

[//]: # (RETURN_TYPE:OptionIntervalsMoversResult)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:OptionIntervalsMoversResult.md)

[//]: # (OPERATION:get_options_interval_movers_v2)

[//]: # (ENDPOINT:/options/interval/movers)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options_interval_movers)

## **get_options_interval_movers**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_interval_movers_v2)

[//]: # (START_OVERVIEW)

> OptionIntervalsMoversResult get_options_interval_movers(source=source, open_time=open_time)

#### Options Intervals Movers


Returns a list of intervals for the biggest movers over the last hour interval.

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

source = ''
open_time = ''

response = intrinio.OptionsApi().get_options_interval_movers(source=source, open_time=open_time)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | str| Realtime or 15-minute delayed contracts. | [optional]   &nbsp;
 **open_time** | datetime| The inclusive UTC date and time the interval opens at. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**OptionIntervalsMoversResult**](OptionIntervalsMoversResult.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options_interval_movers_change)

[//]: # (RETURN_TYPE:OptionIntervalsMoversResult)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:OptionIntervalsMoversResult.md)

[//]: # (OPERATION:get_options_interval_movers_change_v2)

[//]: # (ENDPOINT:/options/interval/movers/change)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options_interval_movers_change)

## **get_options_interval_movers_change**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_interval_movers_change_v2)

[//]: # (START_OVERVIEW)

> OptionIntervalsMoversResult get_options_interval_movers_change(source=source, open_time=open_time)

#### Options Intervals Movers By Change


Returns a list of intervals for the biggest movers by change over the last hour interval.

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

source = ''
open_time = ''

response = intrinio.OptionsApi().get_options_interval_movers_change(source=source, open_time=open_time)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | str| Realtime or 15-minute delayed contracts. | [optional]   &nbsp;
 **open_time** | datetime| The inclusive UTC date and time the interval opens at. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**OptionIntervalsMoversResult**](OptionIntervalsMoversResult.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options_interval_movers_volume)

[//]: # (RETURN_TYPE:OptionIntervalsMoversResult)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:OptionIntervalsMoversResult.md)

[//]: # (OPERATION:get_options_interval_movers_volume_v2)

[//]: # (ENDPOINT:/options/interval/movers/volume)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options_interval_movers_volume)

## **get_options_interval_movers_volume**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_interval_movers_volume_v2)

[//]: # (START_OVERVIEW)

> OptionIntervalsMoversResult get_options_interval_movers_volume(source=source, open_time=open_time)

#### Options Intervals Movers By Volume


Returns a list of intervals for the biggest movers by volume over the last hour interval.

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

source = ''
open_time = ''

response = intrinio.OptionsApi().get_options_interval_movers_volume(source=source, open_time=open_time)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | str| Realtime or 15-minute delayed contracts. | [optional]   &nbsp;
 **open_time** | datetime| The inclusive UTC date and time the interval opens at. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**OptionIntervalsMoversResult**](OptionIntervalsMoversResult.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options_prices)

[//]: # (RETURN_TYPE:ApiResponseOptionPrices)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionPrices.md)

[//]: # (OPERATION:get_options_prices_v2)

[//]: # (ENDPOINT:/options/prices/{identifier})

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options_prices)

## **get_options_prices**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_prices_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionPrices get_options_prices(identifier, start_date=start_date, end_date=end_date, page_size=page_size, next_page=next_page)

#### Option Prices


Returns all price data from inception to expiration for a particular contract.

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

identifier = 'MSFT190405C00118000'
start_date = '2019-01-01'
end_date = '2019-12-31'
page_size = 100
next_page = ''

response = intrinio.OptionsApi().get_options_prices(identifier, start_date=start_date, end_date=end_date, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| The Intrinio ID or code of the options contract to request prices for. |   &nbsp;
 **start_date** | str| Return option contract prices on or after this date. | [optional]   &nbsp;
 **end_date** | str| Return option contract prices on or before this date. | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionPrices**](ApiResponseOptionPrices.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options_prices_batch_realtime)

[//]: # (RETURN_TYPE:ApiResponseOptionsPricesBatchRealtime)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsPricesBatchRealtime.md)

[//]: # (OPERATION:get_options_prices_batch_realtime_v2)

[//]: # (ENDPOINT:/options/prices/realtime/batch)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options_prices_batch_realtime)

## **get_options_prices_batch_realtime**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_prices_batch_realtime_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsPricesBatchRealtime get_options_prices_batch_realtime(body, source=source, show_stats=show_stats, stock_price_source=stock_price_source, model=model, show_extended_price=show_extended_price)

#### Option Prices Batch Realtime


Returns a list of latest price data for up to 250 option contracts per request.

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

source = ''
show_stats = ''
stock_price_source = ''
model = ''
show_extended_price = ''
body = {
  "contracts": [
    "A220121P00055000",
    "A220121P00057500",
    "A220121P00060000"
  ]
}

response = intrinio.OptionsApi().get_options_prices_batch_realtime(body, source=source, show_stats=show_stats, stock_price_source=stock_price_source, model=model, show_extended_price=show_extended_price)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OptionContractsList**](OptionContractsList.md)| The contract symbols for which to return options prices for. |   &nbsp;
 **source** | str| Realtime or 15-minute delayed contracts. | [optional]   &nbsp;
 **show_stats** | bool| Whether to include Greek calculations or not. | [optional]   &nbsp;
 **stock_price_source** | str| Source for underlying price for calculating Greeks. | [optional]   &nbsp;
 **model** | str| Model for calculating Greek values. Default is black_scholes. | [optional]   &nbsp;
 **show_extended_price** | bool| Whether to include open close high low type fields. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsPricesBatchRealtime**](ApiResponseOptionsPricesBatchRealtime.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options_prices_eod)

[//]: # (RETURN_TYPE:ApiResponseOptionsPricesEod)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsPricesEod.md)

[//]: # (OPERATION:get_options_prices_eod_v2)

[//]: # (ENDPOINT:/options/prices/{identifier}/eod)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options_prices_eod)

## **get_options_prices_eod**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_prices_eod_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsPricesEod get_options_prices_eod(identifier, next_page=next_page, start_date=start_date, end_date=end_date)

#### Option Prices EOD


Returns all option prices for a given option contract identifier.

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

identifier = 'AAPL230616P00190000'
next_page = ''

response = intrinio.OptionsApi().get_options_prices_eod(identifier, next_page=next_page, )
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| The Intrinio ID or code of the options contract to request prices for. |   &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
 **start_date** | date| The start date to retrieve prices for | [optional]   &nbsp;
 **end_date** | date| The end date to retrieve prices for | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsPricesEod**](ApiResponseOptionsPricesEod.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options_prices_eod_by_ticker)

[//]: # (RETURN_TYPE:ApiResponseOptionsPricesByTickerEod)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsPricesByTickerEod.md)

[//]: # (OPERATION:get_options_prices_eod_by_ticker_v2)

[//]: # (ENDPOINT:/options/prices/by_ticker/{symbol}/eod)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options_prices_eod_by_ticker)

## **get_options_prices_eod_by_ticker**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_prices_eod_by_ticker_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsPricesByTickerEod get_options_prices_eod_by_ticker(symbol, page_size=page_size, date=date, type=type, strike=strike, strike_greater_than=strike_greater_than, strike_less_than=strike_less_than, include_related_symbols=include_related_symbols, next_page=next_page)

#### Option Prices End of Day By Ticker


Returns a list of end of day pricing information for all option contracts currently associated with the ticker.

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

symbol = 'MSFT'
page_size = 250
date = "2024-01-01"
type = ''
include_related_symbols = False
next_page = ''

response = intrinio.OptionsApi().get_options_prices_eod_by_ticker(symbol, page_size=page_size, date=date, type=type, include_related_symbols=include_related_symbols, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | str| The equities ticker symbol, corresponding to the underlying security. |   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 250]  &nbsp;
 **date** | [**object**](.md)| The date to get pricing data for. Defaults to today in Eastern time zone. | [optional]   &nbsp;
 **type** | str| The option contract type. | [optional]   &nbsp;
 **strike** | float| The strike price of the option contract. This will return options contracts with strike price equal to this price. | [optional]   &nbsp;
 **strike_greater_than** | float| The strike price of the option contract. This will return options contracts with strike prices greater than this price. | [optional]   &nbsp;
 **strike_less_than** | float| The strike price of the option contract. This will return options contracts with strike prices less than this price. | [optional]   &nbsp;
 **include_related_symbols** | bool| Include related symbols that end in a 1 or 2 because of a corporate action. | [optional]   &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsPricesByTickerEod**](ApiResponseOptionsPricesByTickerEod.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options_prices_realtime)

[//]: # (RETURN_TYPE:ApiResponseOptionsPriceRealtime)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsPriceRealtime.md)

[//]: # (OPERATION:get_options_prices_realtime_v2)

[//]: # (ENDPOINT:/options/prices/{identifier}/realtime)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options_prices_realtime)

## **get_options_prices_realtime**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_prices_realtime_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsPriceRealtime get_options_prices_realtime(identifier, source=source, stock_price_source=stock_price_source, model=model, show_extended_price=show_extended_price)

#### Option Prices Realtime


Returns all option prices for a given option contract identifier.

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

identifier = 'AAPL__261218C00230000'
source = ''
stock_price_source = ''
model = ''
show_extended_price = ''

response = intrinio.OptionsApi().get_options_prices_realtime(identifier, source=source, stock_price_source=stock_price_source, model=model, show_extended_price=show_extended_price)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| The Intrinio ID or code of the options contract to request prices for. |   &nbsp;
 **source** | str| Realtime or 15-minute delayed contracts. | [optional]   &nbsp;
 **stock_price_source** | str| Source for underlying price for calculating Greeks. | [optional]   &nbsp;
 **model** | str| Model for calculating Greek values. Default is black_scholes. | [optional]   &nbsp;
 **show_extended_price** | bool| Whether to include open close high low type fields. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsPriceRealtime**](ApiResponseOptionsPriceRealtime.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options_prices_realtime_by_ticker)

[//]: # (RETURN_TYPE:ApiResponseOptionsPricesByTickerRealtime)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsPricesByTickerRealtime.md)

[//]: # (OPERATION:get_options_prices_realtime_by_ticker_v2)

[//]: # (ENDPOINT:/options/prices/by_ticker/{symbol}/realtime)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options_prices_realtime_by_ticker)

## **get_options_prices_realtime_by_ticker**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_prices_realtime_by_ticker_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsPricesByTickerRealtime get_options_prices_realtime_by_ticker(symbol, source=source, iv_mode=iv_mode, next_page=next_page, page_size=page_size, stock_price_source=stock_price_source, model=model, show_extended_price=show_extended_price, expiration_start_date=expiration_start_date, expiration_end_date=expiration_end_date, strike=strike)

#### Option Prices Realtime By Ticker


Returns a list of the latest National Best Bid & Offer (NBBO) top of the order book size and premium (bid / ask), the latest trade size and premium as well as the greeks and implied volatility for all option contracts currently associated with the ticker.

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

symbol = 'MSFT'
source = ''
iv_mode = ''
next_page = ''
page_size = 250
stock_price_source = ''
model = ''
show_extended_price = ''
expiration_start_date = "2024-01-01"
expiration_end_date = "2024-02-02"
strike = 100.0

response = intrinio.OptionsApi().get_options_prices_realtime_by_ticker(symbol, source=source, iv_mode=iv_mode, next_page=next_page, page_size=page_size, stock_price_source=stock_price_source, model=model, show_extended_price=show_extended_price, expiration_start_date=expiration_start_date, expiration_end_date=expiration_end_date, strike=strike)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | str| The equities ticker symbol, corresponding to the underlying security. |   &nbsp;
 **source** | str| Realtime or 15-minute delayed contracts. | [optional]   &nbsp;
 **iv_mode** | str| Change the mode for the implied volatility calculation to out of the money. | [optional]   &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 250]  &nbsp;
 **stock_price_source** | str| Source for underlying price for calculating Greeks. | [optional]   &nbsp;
 **model** | str| Model for calculating Greek values. Default is black_scholes. | [optional]   &nbsp;
 **show_extended_price** | bool| Whether to include open close high low type fields. | [optional]   &nbsp;
 **expiration_start_date** | [**object**](.md)| Filter out contracts that expire before this date. | [optional]   &nbsp;
 **expiration_end_date** | [**object**](.md)| Filter out contracts that expire after this date. | [optional]   &nbsp;
 **strike** | float| Filter out contracts that have this strike price. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsPricesByTickerRealtime**](ApiResponseOptionsPricesByTickerRealtime.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options_snapshots)

[//]: # (RETURN_TYPE:OptionSnapshotsResult)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:OptionSnapshotsResult.md)

[//]: # (OPERATION:get_options_snapshots_v2)

[//]: # (ENDPOINT:/options/snapshots)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options_snapshots)

## **get_options_snapshots**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_snapshots_v2)

[//]: # (START_OVERVIEW)

> OptionSnapshotsResult get_options_snapshots(source=source, at_datetime=at_datetime, with_greeks=with_greeks, stock_price_source=stock_price_source, with_underlying_price=with_underlying_price)

#### Option Prices Realtime Snapshot


Returns all options snapshots for the queried interval with links to download.

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

source = ''
at_datetime = ''
with_greeks = ''
stock_price_source = ''
with_underlying_price = ''

response = intrinio.OptionsApi().get_options_snapshots(source=source, at_datetime=at_datetime, with_greeks=with_greeks, stock_price_source=stock_price_source, with_underlying_price=with_underlying_price)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | str| Realtime or 15-minute delayed contracts. | [optional]   &nbsp;
 **at_datetime** | datetime| The UTC date and time (with url-encoded spaces) the snapshot will cover. | [optional]   &nbsp;
 **with_greeks** | bool| Whether to include Greek calculations fields when available. | [optional]   &nbsp;
 **stock_price_source** | str| Source for underlying price for calculating Greeks. | [optional]   &nbsp;
 **with_underlying_price** | bool| Whether to include the underlying price of the security in the file. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**OptionSnapshotsResult**](OptionSnapshotsResult.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_options_stats_realtime)

[//]: # (RETURN_TYPE:ApiResponseOptionsStatsRealtime)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsStatsRealtime.md)

[//]: # (OPERATION:get_options_stats_realtime_v2)

[//]: # (ENDPOINT:/options/prices/{identifier}/realtime/stats)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_options_stats_realtime)

## **get_options_stats_realtime**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_options_stats_realtime_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsStatsRealtime get_options_stats_realtime(identifier, source=source, show_extended_price=show_extended_price)

#### Option Stats Realtime


Returns all option stats (greeks and implied volatility) as well as the underlying factors used to calculate them, for a particular option contract.

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

identifier = 'AAPL230120C00090000'
source = ''
show_extended_price = ''

response = intrinio.OptionsApi().get_options_stats_realtime(identifier, source=source, show_extended_price=show_extended_price)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| The Intrinio ID or code of the options contract to request prices for. |   &nbsp;
 **source** | str| Realtime or 15-minute delayed contracts. | [optional]   &nbsp;
 **show_extended_price** | bool| Whether to include open close high low type fields. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsStatsRealtime**](ApiResponseOptionsStatsRealtime.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_unusual_activity)

[//]: # (RETURN_TYPE:ApiResponseOptionsUnusualActivity)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsUnusualActivity.md)

[//]: # (OPERATION:get_unusual_activity_v2)

[//]: # (ENDPOINT:/options/unusual_activity/{symbol})

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_unusual_activity)

## **get_unusual_activity**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_unusual_activity_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsUnusualActivity get_unusual_activity(symbol, source=source)

#### Options Unusual Activity


Returns unusual options activity for a particular company across all option chains. Unusual options activity includes large trades, sweeps, and block trades.

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

symbol = 'AAPL'
source = ''

response = intrinio.OptionsApi().get_unusual_activity(symbol, source=source)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | str| The option symbol, corresponding to the underlying security. |   &nbsp;
 **source** | str| Realtime or 15-minute delayed contracts. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsUnusualActivity**](ApiResponseOptionsUnusualActivity.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_unusual_activity_intraday)

[//]: # (RETURN_TYPE:ApiResponseOptionsUnusualActivity)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsUnusualActivity.md)

[//]: # (OPERATION:get_unusual_activity_intraday_v2)

[//]: # (ENDPOINT:/options/unusual_activity/{symbol}/intraday)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_unusual_activity_intraday)

## **get_unusual_activity_intraday**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_unusual_activity_intraday_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsUnusualActivity get_unusual_activity_intraday(symbol, next_page=next_page, page_size=page_size, activity_type=activity_type, sentiment=sentiment, start_date=start_date, end_date=end_date, minimum_total_value=minimum_total_value, maximum_total_value=maximum_total_value)

#### Options Unusual Activity Intraday


Returns unusual trades for a given identifier within the query parameters.

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

symbol = 'AAPL'
next_page = ''
page_size = 1000
activity_type = ''
sentiment = ''
start_date = '2022-02-01'
end_date = '2022-02-03'
minimum_total_value = 100000.0
maximum_total_value = 200000.0

response = intrinio.OptionsApi().get_unusual_activity_intraday(symbol, next_page=next_page, page_size=page_size, activity_type=activity_type, sentiment=sentiment, start_date=start_date, end_date=end_date, minimum_total_value=minimum_total_value, maximum_total_value=maximum_total_value)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | str| The option symbol, corresponding to the underlying security. |   &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 1000]  &nbsp;
 **activity_type** | str| The unusual activity type to query for. | [optional]   &nbsp;
 **sentiment** | str| The sentiment type to query for. | [optional]   &nbsp;
 **start_date** | date| Return unusual activity on or after this date. | [optional]   &nbsp;
 **end_date** | date| Return unusual activity before this date. | [optional]   &nbsp;
 **minimum_total_value** | [**object**](.md)| The inclusive minimum total value for the unusual activity. | [optional]   &nbsp;
 **maximum_total_value** | [**object**](.md)| The inclusive maximum total value for the unusual activity. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsUnusualActivity**](ApiResponseOptionsUnusualActivity.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_unusual_activity_universal)

[//]: # (RETURN_TYPE:ApiResponseOptionsUnusualActivity)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsUnusualActivity.md)

[//]: # (OPERATION:get_unusual_activity_universal_v2)

[//]: # (ENDPOINT:/options/unusual_activity)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_unusual_activity_universal)

## **get_unusual_activity_universal**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_unusual_activity_universal_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsUnusualActivity get_unusual_activity_universal(source=source)

#### Options Unusual Activity Universal


Returns the latest unusual options activity across all US companies with across all option chains. Unusual options activity includes large trades, sweeps, and block trades.

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

source = ''

response = intrinio.OptionsApi().get_unusual_activity_universal(source=source)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | str| Realtime or 15-minute delayed contracts. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsUnusualActivity**](ApiResponseOptionsUnusualActivity.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:OptionsApi)

[//]: # (METHOD:get_unusual_activity_universal_intraday)

[//]: # (RETURN_TYPE:ApiResponseOptionsUnusualActivity)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOptionsUnusualActivity.md)

[//]: # (OPERATION:get_unusual_activity_universal_intraday_v2)

[//]: # (ENDPOINT:/options/unusual_activity/intraday)

[//]: # (DOCUMENT_LINK:OptionsApi.md#get_unusual_activity_universal_intraday)

## **get_unusual_activity_universal_intraday**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_unusual_activity_universal_intraday_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsUnusualActivity get_unusual_activity_universal_intraday(next_page=next_page, page_size=page_size, activity_type=activity_type, sentiment=sentiment, start_date=start_date, end_date=end_date, minimum_total_value=minimum_total_value, maximum_total_value=maximum_total_value)

#### Options Unusual Activity Universal Intraday


Returns unusual trades for all underlying security symbols within the query parameters.

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

next_page = ''
page_size = 1000
activity_type = ''
sentiment = ''
start_date = '2022-02-01'
end_date = '2022-02-03'
minimum_total_value = 100000.0
maximum_total_value = 200000.0

response = intrinio.OptionsApi().get_unusual_activity_universal_intraday(next_page=next_page, page_size=page_size, activity_type=activity_type, sentiment=sentiment, start_date=start_date, end_date=end_date, minimum_total_value=minimum_total_value, maximum_total_value=maximum_total_value)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 1000]  &nbsp;
 **activity_type** | str| The unusual activity type to query for. | [optional]   &nbsp;
 **sentiment** | str| The sentiment type to query for. | [optional]   &nbsp;
 **start_date** | date| Return unusual activity on or after this date. | [optional]   &nbsp;
 **end_date** | date| Return unusual activity before this date. | [optional]   &nbsp;
 **minimum_total_value** | [**object**](.md)| The inclusive minimum total value for the unusual activity. | [optional]   &nbsp;
 **maximum_total_value** | [**object**](.md)| The inclusive maximum total value for the unusual activity. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsUnusualActivity**](ApiResponseOptionsUnusualActivity.md)

[//]: # (END_OPERATION)

