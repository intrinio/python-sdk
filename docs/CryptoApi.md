# intrinio_sdk.CryptoApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_crypto_book_asks**](CryptoApi.md#get_crypto_book_asks) | **GET** /crypto/book/asks | Crypto Book Asks
[**get_crypto_book_bids**](CryptoApi.md#get_crypto_book_bids) | **GET** /crypto/book/bids | Crypto Book Bids
[**get_crypto_book_summary**](CryptoApi.md#get_crypto_book_summary) | **GET** /crypto/book | Crypto Book Summary
[**get_crypto_currencies**](CryptoApi.md#get_crypto_currencies) | **GET** /crypto/currencies | Crypto Currencies
[**get_crypto_exchanges**](CryptoApi.md#get_crypto_exchanges) | **GET** /crypto/exchanges | Crypto Exchanges
[**get_crypto_pairs**](CryptoApi.md#get_crypto_pairs) | **GET** /crypto/pairs | Crypto Pairs
[**get_crypto_prices**](CryptoApi.md#get_crypto_prices) | **GET** /crypto/prices | Crypto Prices
[**get_crypto_snapshot**](CryptoApi.md#get_crypto_snapshot) | **GET** /crypto/snapshot | Crypto Snapshot
[**get_crypto_stats**](CryptoApi.md#get_crypto_stats) | **GET** /crypto/stats | Crypto Stats


# **get_crypto_book_asks**
> ApiResponseCryptoBookAsks get_crypto_book_asks(pair=pair, exchange=exchange, currency=currency)

Crypto Book Asks

Returns the entire ask order book for a given Crypto Currency Pair and Crypto Exchange.

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

crypto_api = intrinio_sdk.CryptoApi()

pair = 'btcusd' # str | Return the order book asks for the given Crypto Currency Pair. (optional)
exchange = 'gemini' # str | Return the order book asks for a Crypto Currency on the given Crypto Exchange. (optional)
currency = 'BTC' # str | Return the order book asks for the given Crypto Currency. (optional)

try:
    api_response = crypto_api.get_crypto_book_asks(pair=pair, exchange=exchange, currency=currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoApi->get_crypto_book_asks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| Return the order book asks for the given Crypto Currency Pair. | [optional] 
 **exchange** | **str**| Return the order book asks for a Crypto Currency on the given Crypto Exchange. | [optional] 
 **currency** | **str**| Return the order book asks for the given Crypto Currency. | [optional] 

### Return type

[**ApiResponseCryptoBookAsks**](ApiResponseCryptoBookAsks.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crypto_book_bids**
> ApiResponseCryptoBookBids get_crypto_book_bids(pair=pair, exchange=exchange, currency=currency)

Crypto Book Bids

Returns the entire bid order book for a given Crypto Currency Pair and Crypto Exchange.

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

crypto_api = intrinio_sdk.CryptoApi()

pair = 'btcusd' # str | Return the order book bids for the given Crypto Currency Pair. (optional)
exchange = 'gemini' # str | Return the order book bids for a Crypto Currency on the given Crypto Exchange. (optional)
currency = 'BTC' # str | Return the order book bids for the given Crypto Currency. (optional)

try:
    api_response = crypto_api.get_crypto_book_bids(pair=pair, exchange=exchange, currency=currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoApi->get_crypto_book_bids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| Return the order book bids for the given Crypto Currency Pair. | [optional] 
 **exchange** | **str**| Return the order book bids for a Crypto Currency on the given Crypto Exchange. | [optional] 
 **currency** | **str**| Return the order book bids for the given Crypto Currency. | [optional] 

### Return type

[**ApiResponseCryptoBookBids**](ApiResponseCryptoBookBids.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crypto_book_summary**
> ApiResponseCryptoBook get_crypto_book_summary(levels=levels, pair=pair, exchange=exchange, currency=currency)

Crypto Book Summary

Returns the order book summary (bid/ask prices and size) for a given Crypto Currency Pair and Crypto Exchange.

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

crypto_api = intrinio_sdk.CryptoApi()

levels = 50 # int | The number of prices/levels to return on each side. For example, the max of 50 levels will return up to 50 bid prices and 50 ask prices. (optional)
pair = 'btcusd' # str | Return the order book summary for the given Crypto Currency Pair. (optional)
exchange = 'gemini' # str | Return the order book summary for a Crypto Currency on the given Crypto Exchange. (optional)
currency = 'BTC' # str | Return the order book summary for the given Crypto Currency. (optional)

try:
    api_response = crypto_api.get_crypto_book_summary(levels=levels, pair=pair, exchange=exchange, currency=currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoApi->get_crypto_book_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **levels** | **int**| The number of prices/levels to return on each side. For example, the max of 50 levels will return up to 50 bid prices and 50 ask prices. | [optional] 
 **pair** | **str**| Return the order book summary for the given Crypto Currency Pair. | [optional] 
 **exchange** | **str**| Return the order book summary for a Crypto Currency on the given Crypto Exchange. | [optional] 
 **currency** | **str**| Return the order book summary for the given Crypto Currency. | [optional] 

### Return type

[**ApiResponseCryptoBook**](ApiResponseCryptoBook.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crypto_currencies**
> ApiResponseCryptoCurrencies get_crypto_currencies(exchange=exchange)

Crypto Currencies

Returns a list of Crypto Currencies for which prices are available.

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

crypto_api = intrinio_sdk.CryptoApi()

exchange = 'gemini' # str | Returns Crypto Currencies traded on the given Crypto Exchange. (optional)

try:
    api_response = crypto_api.get_crypto_currencies(exchange=exchange)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoApi->get_crypto_currencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange** | **str**| Returns Crypto Currencies traded on the given Crypto Exchange. | [optional] 

### Return type

[**ApiResponseCryptoCurrencies**](ApiResponseCryptoCurrencies.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crypto_exchanges**
> ApiResponseCryptoExchanges get_crypto_exchanges(pair=pair)

Crypto Exchanges

Returns a list of Crypto Exchanges for which prices are available.

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

crypto_api = intrinio_sdk.CryptoApi()

pair = 'btcusd' # str | Returns Crypto Currencies traded on the given Crypto Exchange. (optional)

try:
    api_response = crypto_api.get_crypto_exchanges(pair=pair)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoApi->get_crypto_exchanges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| Returns Crypto Currencies traded on the given Crypto Exchange. | [optional] 

### Return type

[**ApiResponseCryptoExchanges**](ApiResponseCryptoExchanges.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crypto_pairs**
> ApiResponseCryptoPairs get_crypto_pairs(exchange=exchange, currency=currency, page_size=page_size, next_page=next_page)

Crypto Pairs

Returns a list of Crypto Currency Pairs for which data is available.

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

crypto_api = intrinio_sdk.CryptoApi()

exchange = 'gemini' # str | Return pairs traded on the given Crypto Exchange. (optional)
currency = 'BTC' # str | Return pairs with one side being the given Crypto Currency. (optional)
page_size = 100 # int | An integer greater than or equal to 1 for specifying the number of results on each page. (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = crypto_api.get_crypto_pairs(exchange=exchange, currency=currency, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoApi->get_crypto_pairs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange** | **str**| Return pairs traded on the given Crypto Exchange. | [optional] 
 **currency** | **str**| Return pairs with one side being the given Crypto Currency. | [optional] 
 **page_size** | **int**| An integer greater than or equal to 1 for specifying the number of results on each page. | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseCryptoPairs**](ApiResponseCryptoPairs.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crypto_prices**
> ApiResponseCryptoPrices get_crypto_prices(timeframe, pair=pair, exchange=exchange, currency=currency, timezone=timezone, start_date=start_date, start_time=start_time, end_date=end_date, end_time=end_time, page_size=page_size, next_page=next_page)

Crypto Prices

Returns a list of available Crypto Currency Prices.

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

crypto_api = intrinio_sdk.CryptoApi()

timeframe = 'h1' # str | The time interval for the prices.
pair = 'btcusd' # str | Return prices for the given Crypto Currency Pair. (optional)
exchange = 'gemini' # str | Return prices for a Crypto Currency on the given Crypto Exchange. (optional)
currency = 'BTC' # str | Return prices for the given Crypto Currency. (optional)
timezone = 'UTC' # str | Return price date/times in this timezone, also interpret start/end date/time parameters in this timezone. (optional) (default to UTC)
start_date = '2018-01-01' # str | Return Crypto Prices on or after this date. (optional)
start_time = '14:20:00' # str | Return Crypto Prices at or after this time (24-hour). (optional)
end_date = '2019-01-01' # str | Return Crypto Prices on or before this date. (optional)
end_time = '21:01:21' # str | Return Crypto Prices at or before this time (24-hour). (optional)
page_size = 100 # int | An integer greater than or equal to 1 for specifying the number of results on each page. (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = crypto_api.get_crypto_prices(timeframe, pair=pair, exchange=exchange, currency=currency, timezone=timezone, start_date=start_date, start_time=start_time, end_date=end_date, end_time=end_time, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoApi->get_crypto_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeframe** | **str**| The time interval for the prices. | 
 **pair** | **str**| Return prices for the given Crypto Currency Pair. | [optional] 
 **exchange** | **str**| Return prices for a Crypto Currency on the given Crypto Exchange. | [optional] 
 **currency** | **str**| Return prices for the given Crypto Currency. | [optional] 
 **timezone** | **str**| Return price date/times in this timezone, also interpret start/end date/time parameters in this timezone. | [optional] [default to UTC]
 **start_date** | **str**| Return Crypto Prices on or after this date. | [optional] 
 **start_time** | **str**| Return Crypto Prices at or after this time (24-hour). | [optional] 
 **end_date** | **str**| Return Crypto Prices on or before this date. | [optional] 
 **end_time** | **str**| Return Crypto Prices at or before this time (24-hour). | [optional] 
 **page_size** | **int**| An integer greater than or equal to 1 for specifying the number of results on each page. | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseCryptoPrices**](ApiResponseCryptoPrices.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crypto_snapshot**
> ApiResponseCryptoSnapshot get_crypto_snapshot(pair=pair, exchange=exchange, currency=currency)

Crypto Snapshot

Returns a market snapshot over that last 24 hours for the given currency pair and exchange.

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

crypto_api = intrinio_sdk.CryptoApi()

pair = 'btcusd' # str | Return the snapshot for the given Crypto Currency Pair. (optional)
exchange = 'gemini' # str | Return the snapshot for a Crypto Currency on the given Crypto Exchange. (optional)
currency = 'BTC' # str | Return the snapshot for the given Crypto Currency. (optional)

try:
    api_response = crypto_api.get_crypto_snapshot(pair=pair, exchange=exchange, currency=currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoApi->get_crypto_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**| Return the snapshot for the given Crypto Currency Pair. | [optional] 
 **exchange** | **str**| Return the snapshot for a Crypto Currency on the given Crypto Exchange. | [optional] 
 **currency** | **str**| Return the snapshot for the given Crypto Currency. | [optional] 

### Return type

[**ApiResponseCryptoSnapshot**](ApiResponseCryptoSnapshot.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crypto_stats**
> ApiResponseCryptoStats get_crypto_stats(exchange=exchange, currency=currency)

Crypto Stats

Returns available stats on Crypto Currencies.

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

crypto_api = intrinio_sdk.CryptoApi()

exchange = 'gemini' # str | Returns stats for Crypto Currencies that trade on the specified Crypto Exchange. (optional)
currency = 'BTC' # str | Returns stats for the specified Crypto Currency. (optional)

try:
    api_response = crypto_api.get_crypto_stats(exchange=exchange, currency=currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CryptoApi->get_crypto_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange** | **str**| Returns stats for Crypto Currencies that trade on the specified Crypto Exchange. | [optional] 
 **currency** | **str**| Returns stats for the specified Crypto Currency. | [optional] 

### Return type

[**ApiResponseCryptoStats**](ApiResponseCryptoStats.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

