# intrinio_sdk.OptionsApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_options**](OptionsApi.md#get_options) | **GET** /options/{symbol} | Options
[**get_options_chain**](OptionsApi.md#get_options_chain) | **GET** /options/chain/{symbol}/{expiration} | Options Chain
[**get_options_expirations**](OptionsApi.md#get_options_expirations) | **GET** /options/expirations/{symbol} | Options Expirations
[**get_options_prices**](OptionsApi.md#get_options_prices) | **GET** /options/prices/{identifier} | Option Prices


# **get_options**
> ApiResponseOptions get_options(symbol, type=type, strike=strike, strike_greater_than=strike_greater_than, strike_less_than=strike_less_than, expiration=expiration, expiration_after=expiration_after, expiration_before=expiration_before, page_size=page_size, next_page=next_page)

Options

Returns the master list of option contracts for a given symbol.

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

options_api = intrinio_sdk.OptionsApi()

symbol = 'MSFT' # str | The option symbol, corresponding to the underlying security.
type = 'put' # str | The option contract type. (optional)
strike = 170.0 # float | The strike price of the option contract. This will return options contracts with strike price equal to this price. (optional)
strike_greater_than = 190.0 # float | The strike price of the option contract. This will return options contracts with strike prices greater than this price. (optional)
strike_less_than = 150.0 # float | The strike price of the option contract. This will return options contracts with strike prices less than this price. (optional)
expiration = '2019-03-01' # str | The expiration date of the option contract. This will return options contracts with expiration dates on this date. (optional)
expiration_after = '2019-01-01' # str | The expiration date of the option contract. This will return options contracts with expiration dates after this date. (optional)
expiration_before = '2019-12-31' # str | The expiration date of the option contract. This will return options contracts with expiration dates before this date. (optional)
page_size = 100 # float | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = options_api.get_options(symbol, type=type, strike=strike, strike_greater_than=strike_greater_than, strike_less_than=strike_less_than, expiration=expiration, expiration_after=expiration_after, expiration_before=expiration_before, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptionsApi->get_options: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The option symbol, corresponding to the underlying security. | 
 **type** | **str**| The option contract type. | [optional] 
 **strike** | **float**| The strike price of the option contract. This will return options contracts with strike price equal to this price. | [optional] 
 **strike_greater_than** | **float**| The strike price of the option contract. This will return options contracts with strike prices greater than this price. | [optional] 
 **strike_less_than** | **float**| The strike price of the option contract. This will return options contracts with strike prices less than this price. | [optional] 
 **expiration** | **str**| The expiration date of the option contract. This will return options contracts with expiration dates on this date. | [optional] 
 **expiration_after** | **str**| The expiration date of the option contract. This will return options contracts with expiration dates after this date. | [optional] 
 **expiration_before** | **str**| The expiration date of the option contract. This will return options contracts with expiration dates before this date. | [optional] 
 **page_size** | **float**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseOptions**](ApiResponseOptions.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_options_chain**
> ApiResponseOptionsChain get_options_chain(symbol, expiration, type=type, strike=strike, strike_greater_than=strike_greater_than, strike_less_than=strike_less_than, moneyness=moneyness, page_size=page_size)

Options Chain

Returns all options contracts and their prices for the given symbol and expiration date.

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

options_api = intrinio_sdk.OptionsApi()

symbol = 'MSFT' # str | The option symbol, corresponding to the underlying security.
expiration = '2019-03-06' # str | The expiration date of the options contract
type = 'put' # str | The option contract type. (optional)
strike = 170.0 # float | The strike price of the option contract. This will return options contracts with strike price equal to this price. (optional)
strike_greater_than = 190.0 # float | The strike price of the option contract. This will return options contracts with strike prices greater than this price. (optional)
strike_less_than = 150.0 # float | The strike price of the option contract. This will return options contracts with strike prices less than this price. (optional)
moneyness = 'in_the_money' # str | The moneyness of the options contracts to return. 'all' will return all options contracts. 'in_the_money' will return options contracts that are in the money (call options with strike prices below the current price, put options with strike prices above the current price). 'out_of_they_money' will return options contracts that are out of the money (call options with strike prices above the current price, put options with strike prices below the current price). 'near_the_money' will return options contracts that are $0.50 or less away from being in the money. (optional)
page_size = 100 # float | The number of results to return (optional) (default to 100)

try:
    api_response = options_api.get_options_chain(symbol, expiration, type=type, strike=strike, strike_greater_than=strike_greater_than, strike_less_than=strike_less_than, moneyness=moneyness, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptionsApi->get_options_chain: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The option symbol, corresponding to the underlying security. | 
 **expiration** | **str**| The expiration date of the options contract | 
 **type** | **str**| The option contract type. | [optional] 
 **strike** | **float**| The strike price of the option contract. This will return options contracts with strike price equal to this price. | [optional] 
 **strike_greater_than** | **float**| The strike price of the option contract. This will return options contracts with strike prices greater than this price. | [optional] 
 **strike_less_than** | **float**| The strike price of the option contract. This will return options contracts with strike prices less than this price. | [optional] 
 **moneyness** | **str**| The moneyness of the options contracts to return. &#39;all&#39; will return all options contracts. &#39;in_the_money&#39; will return options contracts that are in the money (call options with strike prices below the current price, put options with strike prices above the current price). &#39;out_of_they_money&#39; will return options contracts that are out of the money (call options with strike prices above the current price, put options with strike prices below the current price). &#39;near_the_money&#39; will return options contracts that are $0.50 or less away from being in the money. | [optional] 
 **page_size** | **float**| The number of results to return | [optional] [default to 100]

### Return type

[**ApiResponseOptionsChain**](ApiResponseOptionsChain.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_options_expirations**
> ApiResponseOptionsExpirations get_options_expirations(symbol, after=after, before=before)

Options Expirations

Returns all option contract expiration dates for a given symbol.

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

options_api = intrinio_sdk.OptionsApi()

symbol = 'MSFT' # str | The option symbol, corresponding to the underlying security.
after = '2019-01-01' # str | Return option contract expiration dates after this date. (optional)
before = '2019-12-31' # str | Return option contract expiration dates before this date. (optional)

try:
    api_response = options_api.get_options_expirations(symbol, after=after, before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptionsApi->get_options_expirations: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The option symbol, corresponding to the underlying security. | 
 **after** | **str**| Return option contract expiration dates after this date. | [optional] 
 **before** | **str**| Return option contract expiration dates before this date. | [optional] 

### Return type

[**ApiResponseOptionsExpirations**](ApiResponseOptionsExpirations.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_options_prices**
> ApiResponseOptionPrices get_options_prices(identifier, start_date=start_date, end_date=end_date, page_size=page_size, next_page=next_page)

Option Prices

Returns all option prices for a given option contract identifier.

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

options_api = intrinio_sdk.OptionsApi()

identifier = 'null' # str | The Intrinio ID or code of the options contract to request prices for.
start_date = '2019-01-01' # str | Return option contract prices on or after this date. (optional)
end_date = '2019-12-31' # str | Return option contract prices on or before this date. (optional)
page_size = 100 # float | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = options_api.get_options_prices(identifier, start_date=start_date, end_date=end_date, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptionsApi->get_options_prices: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The Intrinio ID or code of the options contract to request prices for. | 
 **start_date** | **str**| Return option contract prices on or after this date. | [optional] 
 **end_date** | **str**| Return option contract prices on or before this date. | [optional] 
 **page_size** | **float**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseOptionPrices**](ApiResponseOptionPrices.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

