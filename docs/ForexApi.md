# intrinio_sdk.ForexApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_forex_currencies**](ForexApi.md#get_forex_currencies) | **GET** /forex/currencies | Forex Currencies
[**get_forex_pairs**](ForexApi.md#get_forex_pairs) | **GET** /forex/pairs | Forex Currency Pairs
[**get_forex_prices**](ForexApi.md#get_forex_prices) | **GET** /forex/prices/{pair}/{timeframe} | Forex Currency Prices


# **get_forex_currencies**
> ApiResponseForexCurrencies get_forex_currencies()

Forex Currencies

Returns a list of forex currencies for which prices are available.

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

forex_api = intrinio_sdk.ForexApi()


try:
    api_response = forex_api.get_forex_currencies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForexApi->get_forex_currencies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiResponseForexCurrencies**](ApiResponseForexCurrencies.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forex_pairs**
> ApiResponseForexPairs get_forex_pairs()

Forex Currency Pairs

Returns a list of currency pairs used to request foreign exchange (forex) market price data. The currency that is used as the reference is called quote currency and the currency that is quoted in relation is called the base currency. For example, in the pair code “EURGBP” with a price of 0.88, one Euro (base currency) can be exchanged for 0.88 British Pounds (quote currency).

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

forex_api = intrinio_sdk.ForexApi()


try:
    api_response = forex_api.get_forex_pairs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForexApi->get_forex_pairs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiResponseForexPairs**](ApiResponseForexPairs.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forex_prices**
> ApiResponseForexPrices get_forex_prices(pair, timeframe, timezone=timezone, start_date=start_date, start_time=start_time, end_date=end_date, end_time=end_time, page_size=page_size, next_page=next_page)

Forex Currency Prices

Provides a list of forex price quotes for a given forex currency pair and timeframe.

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

forex_api = intrinio_sdk.ForexApi()

pair = 'EURUSD' # str | The Forex Currency Pair code
timeframe = 'D1' # str | The time interval for the quotes
timezone = 'UTC' # str | Returns trading times in this timezone (optional) (default to UTC)
start_date = '2018-01-01' # str | Return Forex Prices on or after this date (optional)
start_time = '14:20:00' # str | Return Forex Prices at or after this time (24-hour) (optional)
end_date = '2019-01-01' # str | Return Forex Prices on or before this date (optional)
end_time = '21:01:21' # str | Return Forex Prices at or before this time (24-hour) (optional)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = forex_api.get_forex_prices(pair, timeframe, timezone=timezone, start_date=start_date, start_time=start_time, end_date=end_date, end_time=end_time, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForexApi->get_forex_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| The Forex Currency Pair code | 
 **timeframe** | **str**| The time interval for the quotes | 
 **timezone** | **str**| Returns trading times in this timezone | [optional] [default to UTC]
 **start_date** | **str**| Return Forex Prices on or after this date | [optional] 
 **start_time** | **str**| Return Forex Prices at or after this time (24-hour) | [optional] 
 **end_date** | **str**| Return Forex Prices on or before this date | [optional] 
 **end_time** | **str**| Return Forex Prices at or before this time (24-hour) | [optional] 
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseForexPrices**](ApiResponseForexPrices.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

