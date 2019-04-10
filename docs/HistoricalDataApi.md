# intrinio_sdk.HistoricalDataApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_historical_data**](HistoricalDataApi.md#get_historical_data) | **GET** /historical_data/{identifier}/{tag} | Historical Data


# **get_historical_data**
> ApiResponseHistoricalData get_historical_data(identifier, tag, frequency=frequency, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)

Historical Data

Returns historical values for the given `tag` and the entity represented by the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

historical_data_api = intrinio_sdk.HistoricalDataApi()

identifier = 'AAPL' # str | An identifier for an entity such as a Company, Security, Index, etc (Ticker, FIGI, ISIN, CUSIP, CIK, LEI, Intrinio ID)
tag = 'marketcap' # str | An Intrinio data tag ID or code (<a href='https://data.intrinio.com/data-tags'>reference</a>)
frequency = 'daily' # str | Return historical data in the given frequency (optional) (default to daily)
type = '' # str | Filter by type, when applicable (optional)
start_date = '2015-01-01' # date | Get historical data on or after this date (optional)
end_date = '2019-01-01' # date | Get historical date on or before this date (optional)
sort_order = 'desc' # str | Sort by date `asc` or `desc` (optional) (default to desc)
page_size = 100 # float | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = historical_data_api.get_historical_data(identifier, tag, frequency=frequency, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HistoricalDataApi->get_historical_data: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| An identifier for an entity such as a Company, Security, Index, etc (Ticker, FIGI, ISIN, CUSIP, CIK, LEI, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code (&lt;a href&#x3D;&#39;https://data.intrinio.com/data-tags&#39;&gt;reference&lt;/a&gt;) | 
 **frequency** | **str**| Return historical data in the given frequency | [optional] [default to daily]
 **type** | **str**| Filter by type, when applicable | [optional] 
 **start_date** | **date**| Get historical data on or after this date | [optional] 
 **end_date** | **date**| Get historical date on or before this date | [optional] 
 **sort_order** | **str**| Sort by date &#x60;asc&#x60; or &#x60;desc&#x60; | [optional] [default to desc]
 **page_size** | **float**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseHistoricalData**](ApiResponseHistoricalData.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

