# intrinio_sdk.OptionsApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_options_tickers**](OptionsApi.md#get_all_options_tickers) | **GET** /options/tickers | Options Tickers
[**get_option_expirations_realtime**](OptionsApi.md#get_option_expirations_realtime) | **GET** /options/expirations/{symbol}/realtime | Option Expirations Realtime
[**get_options**](OptionsApi.md#get_options) | **GET** /options/{symbol} | Options
[**get_options_by_symbol_realtime**](OptionsApi.md#get_options_by_symbol_realtime) | **GET** /options/{symbol}/realtime | Options by Symbol Realtime
[**get_options_chain**](OptionsApi.md#get_options_chain) | **GET** /options/chain/{symbol}/{expiration} | Options Chain
[**get_options_chain_realtime**](OptionsApi.md#get_options_chain_realtime) | **GET** /options/chain/{symbol}/{expiration}/realtime | Options Chain Realtime
[**get_options_expirations**](OptionsApi.md#get_options_expirations) | **GET** /options/expirations/{symbol} | Options Expirations
[**get_options_prices**](OptionsApi.md#get_options_prices) | **GET** /options/prices/{identifier} | Option Prices
[**get_options_prices_batch_realtime**](OptionsApi.md#get_options_prices_batch_realtime) | **POST** /options/prices/realtime/batch | Option Prices Batch Realtime
[**get_options_prices_realtime**](OptionsApi.md#get_options_prices_realtime) | **GET** /options/prices/{identifier}/realtime | Option Prices Realtime
[**get_options_stats_realtime**](OptionsApi.md#get_options_stats_realtime) | **GET** /options/prices/{identifier}/realtime/stats | Option Stats Realtime



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

> ApiResponseOptionsTickers get_all_options_tickers()

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


response = intrinio.OptionsApi().get_all_options_tickers()
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)

This endpoint does not need any parameter.
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsTickers**](ApiResponseOptionsTickers.md)

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

> ApiResponseOptionsExpirations get_option_expirations_realtime(symbol, after=after, before=before, source=source)

#### Option Expirations Realtime


Returns all realtime option contract expiration dates for a given symbol.

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

response = intrinio.OptionsApi().get_option_expirations_realtime(symbol, after=after, before=before, source=source)
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
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsExpirations**](ApiResponseOptionsExpirations.md)

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


Returns the master list of option contracts for a given symbol.

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

> ApiResponseOptionsRealtime get_options_by_symbol_realtime(symbol, type=type, strike=strike, strike_greater_than=strike_greater_than, strike_less_than=strike_less_than, expiration=expiration, expiration_after=expiration_after, expiration_before=expiration_before, source=source)

#### Options by Symbol Realtime


Returns the master list of realtime option contracts for a given symbol.

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

response = intrinio.OptionsApi().get_options_by_symbol_realtime(symbol, type=type, source=source)
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


Returns all options contracts and their prices for the given symbol and expiration date.

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

> ApiResponseOptionsChainRealtime get_options_chain_realtime(symbol, expiration, source=source, type=type, strike=strike, strike_greater_than=strike_greater_than, strike_less_than=strike_less_than, volume_greater_than=volume_greater_than, volume_less_than=volume_less_than, open_interest_greater_than=open_interest_greater_than, open_interest_less_than=open_interest_less_than, moneyness=moneyness)

#### Options Chain Realtime


Returns all realtime options contracts and their prices for the given symbol and expiration date.

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

response = intrinio.OptionsApi().get_options_chain_realtime(symbol, expiration, source=source, type=type, moneyness=moneyness)
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


Returns all option contract expiration dates for a given symbol.

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

> ApiResponseOptionsPricesBatchRealtime get_options_prices_batch_realtime(body, source=source)

#### Option Prices Batch Realtime


Returns options prices for a supplied list of option symbols.

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
body = {
  "contracts": [
    "A220121P00055000",
    "A220121P00057500",
    "A220121P00060000"
  ]
}

response = intrinio.OptionsApi().get_options_prices_batch_realtime(body, source=source)
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
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsPricesBatchRealtime**](ApiResponseOptionsPricesBatchRealtime.md)

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

> ApiResponseOptionsPriceRealtime get_options_prices_realtime(identifier, source=source)

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

identifier = 'AAPL230120C00090000'
source = ''

response = intrinio.OptionsApi().get_options_prices_realtime(identifier, source=source)
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
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsPriceRealtime**](ApiResponseOptionsPriceRealtime.md)

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

> ApiResponseOptionsStatsRealtime get_options_stats_realtime(identifier, source=source)

#### Option Stats Realtime


Returns all option stats (greeks and implied volatility) and factors used to calculate them, for a given option contract identifier.

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

response = intrinio.OptionsApi().get_options_stats_realtime(identifier, source=source)
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
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsStatsRealtime**](ApiResponseOptionsStatsRealtime.md)

[//]: # (END_OPERATION)

