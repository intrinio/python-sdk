# intrinio_sdk.SecurityApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_securities**](SecurityApi.md#get_all_securities) | **GET** /securities | Get All Securiites
[**get_security_by_id**](SecurityApi.md#get_security_by_id) | **GET** /securities/{identifier} | Get a Security by ID
[**get_security_data_point_number**](SecurityApi.md#get_security_data_point_number) | **GET** /securities/{identifier}/data_point/{item}/number | Get Security Data Point (Number)
[**get_security_data_point_text**](SecurityApi.md#get_security_data_point_text) | **GET** /securities/{identifier}/data_point/{item}/text | Get Security Data Point (Text)
[**get_security_historical_data**](SecurityApi.md#get_security_historical_data) | **GET** /securities/{identifier}/historical_data/{item} | Get Security Historical Data
[**get_security_stock_prices**](SecurityApi.md#get_security_stock_prices) | **GET** /securities/{identifier}/prices | Get Stock Prices for Security
[**screen_securities**](SecurityApi.md#screen_securities) | **POST** /securities/screen | Screen Securities
[**search_securities**](SecurityApi.md#search_securities) | **GET** /securities/search | Search Securities


# **get_all_securities**
> list[SecuritySummary] get_all_securities(next_page=next_page)

Get All Securiites

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'

security_api = intrinio_sdk.SecurityApi()

next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = security_api.get_all_securities(next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_all_securities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**list[SecuritySummary]**](SecuritySummary.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_by_id**
> Security get_security_by_id(identifier)

Get a Security by ID

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'

security_api = intrinio_sdk.SecurityApi()

identifier = 'identifier_example' # str | A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)

try:
    api_response = security_api.get_security_by_id(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_security_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID) | 

### Return type

[**Security**](Security.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_data_point_number**
> DataPointNumber get_security_data_point_number(identifier, item)

Get Security Data Point (Number)

Returns a numeric value for the given `item` for the Security with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'

security_api = intrinio_sdk.SecurityApi()

identifier = 'identifier_example' # str | A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)
item = 'item_example' # str | An Intrinio data tag or other item

try:
    api_response = security_api.get_security_data_point_number(identifier, item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_security_data_point_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID) | 
 **item** | **str**| An Intrinio data tag or other item | 

### Return type

[**DataPointNumber**](DataPointNumber.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_data_point_text**
> DataPointText get_security_data_point_text(identifier, item)

Get Security Data Point (Text)

Returns a text value for the given `item` for the Security with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'

security_api = intrinio_sdk.SecurityApi()

identifier = 'identifier_example' # str | A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)
item = 'item_example' # str | An Intrinio data tag or other item

try:
    api_response = security_api.get_security_data_point_text(identifier, item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_security_data_point_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID) | 
 **item** | **str**| An Intrinio data tag or other item | 

### Return type

[**DataPointText**](DataPointText.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_historical_data**
> list[HistoricalData] get_security_historical_data(identifier, item, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, next_page=next_page)

Get Security Historical Data

Returns historical values for the given `item` and the Security with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'

security_api = intrinio_sdk.SecurityApi()

identifier = 'identifier_example' # str | A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)
item = 'item_example' # str | An Intrinio data tag or other item
type = 'type_example' # str | Filter by type, when applicable (optional)
start_date = '2013-10-20' # date | Get historical data on or after this date (optional)
end_date = '2013-10-20' # date | Get historical date on or before this date (optional)
sort_order = 'desc' # str | Sort by date `asc` or `desc` (optional) (default to desc)
next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = security_api.get_security_historical_data(identifier, item, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_security_historical_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID) | 
 **item** | **str**| An Intrinio data tag or other item | 
 **type** | **str**| Filter by type, when applicable | [optional] 
 **start_date** | **date**| Get historical data on or after this date | [optional] 
 **end_date** | **date**| Get historical date on or before this date | [optional] 
 **sort_order** | **str**| Sort by date &#x60;asc&#x60; or &#x60;desc&#x60; | [optional] [default to desc]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**list[HistoricalData]**](HistoricalData.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_stock_prices**
> list[StockPriceSummary] get_security_stock_prices(identifier, start_date=start_date, end_date=end_date, frequency=frequency, next_page=next_page)

Get Stock Prices for Security

Return stock prices for the Security with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'

security_api = intrinio_sdk.SecurityApi()

identifier = 'identifier_example' # str | A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)
start_date = '2013-10-20' # date | Return prices on or after the date (optional)
end_date = '2013-10-20' # date | Return prices on or beore the date (optional)
frequency = 'daily' # str | Return stock prices in the given frequency (optional) (default to daily)
next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = security_api.get_security_stock_prices(identifier, start_date=start_date, end_date=end_date, frequency=frequency, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_security_stock_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID) | 
 **start_date** | **date**| Return prices on or after the date | [optional] 
 **end_date** | **date**| Return prices on or beore the date | [optional] 
 **frequency** | **str**| Return stock prices in the given frequency | [optional] [default to daily]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**list[StockPriceSummary]**](StockPriceSummary.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **screen_securities**
> list[SecurityScreenResult] screen_securities(logic=logic, order_column=order_column, order_direction=order_direction, primary_only=primary_only, next_page=next_page)

Screen Securities

Screen securities using complex logic

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'

security_api = intrinio_sdk.SecurityApi()

logic = intrinio_sdk.SecurityScreenGroup() # SecurityScreenGroup | The logic to screen with, consisting of operators, clauses, and nested groups (optional)
order_column = 'order_column_example' # str | Results returned sorted by this column (optional)
order_direction = 'asc' # str | Sort order to use with the order_column (optional) (default to asc)
primary_only = false # bool | Return only primary securities (optional) (default to false)
next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = security_api.screen_securities(logic=logic, order_column=order_column, order_direction=order_direction, primary_only=primary_only, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->screen_securities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logic** | [**SecurityScreenGroup**](SecurityScreenGroup.md)| The logic to screen with, consisting of operators, clauses, and nested groups | [optional] 
 **order_column** | **str**| Results returned sorted by this column | [optional] 
 **order_direction** | **str**| Sort order to use with the order_column | [optional] [default to asc]
 **primary_only** | **bool**| Return only primary securities | [optional] [default to false]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**list[SecurityScreenResult]**](SecurityScreenResult.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_securities**
> list[SecuritySummary] search_securities(query, next_page=next_page)

Search Securities

Searches for Securities matching the text `query`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.configuration.api_key['api-key'] = 'YOUR_API_KEY'

security_api = intrinio_sdk.SecurityApi()

query = 'query_example' # str | 
next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = security_api.search_securities(query, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->search_securities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**list[SecuritySummary]**](SecuritySummary.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

