# intrinio_sdk.OptionsApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_options**](OptionsApi.md#get_options) | **GET** /options/{symbol} | Options
[**get_options_chain**](OptionsApi.md#get_options_chain) | **GET** /options/chain/{symbol}/{expiration} | Options Chain
[**get_options_expirations**](OptionsApi.md#get_options_expirations) | **GET** /options/expirations/{symbol} | Options Expirations
[**get_options_prices**](OptionsApi.md#get_options_prices) | **GET** /options/prices/{identifier} | Option Prices



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

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_options_v2)

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
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = options_api.get_options(symbol, type=type, strike=strike, strike_greater_than=strike_greater_than, strike_less_than=strike_less_than, expiration=expiration, expiration_after=expiration_after, expiration_before=expiration_before, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptionsApi->get_options: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The option symbol, corresponding to the underlying security. |   &nbsp;
 **type** | **str**| The option contract type. | [optional]   &nbsp;
 **strike** | **float**| The strike price of the option contract. This will return options contracts with strike price equal to this price. | [optional]   &nbsp;
 **strike_greater_than** | **float**| The strike price of the option contract. This will return options contracts with strike prices greater than this price. | [optional]   &nbsp;
 **strike_less_than** | **float**| The strike price of the option contract. This will return options contracts with strike prices less than this price. | [optional]   &nbsp;
 **expiration** | **str**| The expiration date of the option contract. This will return options contracts with expiration dates on this date. | [optional]   &nbsp;
 **expiration_after** | **str**| The expiration date of the option contract. This will return options contracts with expiration dates after this date. | [optional]   &nbsp;
 **expiration_before** | **str**| The expiration date of the option contract. This will return options contracts with expiration dates before this date. | [optional]   &nbsp;
 **page_size** | **int**| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptions**](ApiResponseOptions.md)

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

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_options_chain_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOptionsChain get_options_chain(symbol, expiration, type=type, strike=strike, strike_greater_than=strike_greater_than, strike_less_than=strike_less_than, moneyness=moneyness, page_size=page_size)

#### Options Chain


Returns all options contracts and their prices for the given symbol and expiration date.

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

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
page_size = 100 # int | The number of results to return (optional) (default to 100)

try:
    api_response = options_api.get_options_chain(symbol, expiration, type=type, strike=strike, strike_greater_than=strike_greater_than, strike_less_than=strike_less_than, moneyness=moneyness, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptionsApi->get_options_chain: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The option symbol, corresponding to the underlying security. |   &nbsp;
 **expiration** | **str**| The expiration date of the options contract |   &nbsp;
 **type** | **str**| The option contract type. | [optional]   &nbsp;
 **strike** | **float**| The strike price of the option contract. This will return options contracts with strike price equal to this price. | [optional]   &nbsp;
 **strike_greater_than** | **float**| The strike price of the option contract. This will return options contracts with strike prices greater than this price. | [optional]   &nbsp;
 **strike_less_than** | **float**| The strike price of the option contract. This will return options contracts with strike prices less than this price. | [optional]   &nbsp;
 **moneyness** | **str**| The moneyness of the options contracts to return. &#39;all&#39; will return all options contracts. &#39;in_the_money&#39; will return options contracts that are in the money (call options with strike prices below the current price, put options with strike prices above the current price). &#39;out_of_they_money&#39; will return options contracts that are out of the money (call options with strike prices above the current price, put options with strike prices below the current price). &#39;near_the_money&#39; will return options contracts that are $0.50 or less away from being in the money. | [optional]   &nbsp;
 **page_size** | **int**| The number of results to return | [optional] [default to 100]  &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionsChain**](ApiResponseOptionsChain.md)

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

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_options_expirations_v2)

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
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The option symbol, corresponding to the underlying security. |   &nbsp;
 **after** | **str**| Return option contract expiration dates after this date. | [optional]   &nbsp;
 **before** | **str**| Return option contract expiration dates before this date. | [optional]   &nbsp;
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

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_options_prices_v2)

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
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

options_api = intrinio_sdk.OptionsApi()

identifier = 'null' # str | The Intrinio ID or code of the options contract to request prices for.
start_date = '2019-01-01' # str | Return option contract prices on or after this date. (optional)
end_date = '2019-12-31' # str | Return option contract prices on or before this date. (optional)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = options_api.get_options_prices(identifier, start_date=start_date, end_date=end_date, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptionsApi->get_options_prices: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The Intrinio ID or code of the options contract to request prices for. |   &nbsp;
 **start_date** | **str**| Return option contract prices on or after this date. | [optional]   &nbsp;
 **end_date** | **str**| Return option contract prices on or before this date. | [optional]   &nbsp;
 **page_size** | **int**| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOptionPrices**](ApiResponseOptionPrices.md)

[//]: # (END_OPERATION)

