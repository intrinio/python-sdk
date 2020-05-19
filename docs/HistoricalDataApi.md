# intrinio_sdk.HistoricalDataApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_historical_data**](HistoricalDataApi.md#get_historical_data) | **GET** /historical_data/{identifier}/{tag} | Historical Data



[//]: # (START_OPERATION)

[//]: # (CLASS:HistoricalDataApi)

[//]: # (METHOD:get_historical_data)

[//]: # (RETURN_TYPE:ApiResponseHistoricalData)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseHistoricalData.md)

[//]: # (OPERATION:get_historical_data_v2)

[//]: # (ENDPOINT:/historical_data/{identifier}/{tag})

[//]: # (DOCUMENT_LINK:HistoricalDataApi.md#get_historical_data)

## **get_historical_data**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_historical_data_v2)

[//]: # (START_OVERVIEW)

> ApiResponseHistoricalData get_historical_data(identifier, tag, frequency=frequency, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)

#### Historical Data


$$v2_historical_data_description$$

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

historical_data_api = intrinio_sdk.HistoricalDataApi()

identifier = '$$v2_historical_data_identifier_default$$' # str | $$v2_historical_data_identifier_description$$
tag = '$$v2_historical_data_item_default$$' # str | $$v2_historical_data_item_description$$
frequency = 'daily' # str | Return historical data in the given frequency (optional) (default to daily)
type = '' # str | Filter by type, when applicable (optional)
start_date = '2015-01-01' # date | Get historical data on or after this date (optional)
end_date = '' # date | Get historical date on or before this date (optional)
sort_order = 'desc' # str | Sort by date `asc` or `desc` (optional) (default to desc)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
  api_response = historical_data_api.get_historical_data(identifier, tag, frequency=frequency, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling HistoricalDataApi->get_historical_data: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| $$v2_historical_data_identifier_description$$ |   &nbsp;
 **tag** | str| $$v2_historical_data_item_description$$ |   &nbsp;
 **frequency** | str| Return historical data in the given frequency | [optional] [default to daily]  &nbsp;
 **type** | str| Filter by type, when applicable | [optional]   &nbsp;
 **start_date** | date| Get historical data on or after this date | [optional]   &nbsp;
 **end_date** | date| Get historical date on or before this date | [optional]   &nbsp;
 **sort_order** | str| Sort by date &#x60;asc&#x60; or &#x60;desc&#x60; | [optional] [default to desc]  &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseHistoricalData**](ApiResponseHistoricalData.md)

[//]: # (END_OPERATION)

