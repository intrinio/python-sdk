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


Returns historical values for the given `tag` and the entity represented by the given `identifier`

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

identifier = '\"AAPL\"'
tag = '\"marketcap\"'
frequency = 'daily'
type = '\"~null\"'
start_date = '\"2015-01-01\"'
end_date = '\"~null\"'
sort_order = 'desc'
page_size = 100
next_page = '\"~null\"'

response = intrinio.HistoricalDataApi().get_historical_data(identifier, tag, frequency=frequency, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| An identifier for an entity such as a Company, Security, Index, etc (Ticker, FIGI, ISIN, CUSIP, CIK, LEI, Intrinio ID) |   &nbsp;
 **tag** | str| An Intrinio data tag ID or code (&lt;a href&#x3D;&#39;https://data.intrinio.com/data-tags&#39;&gt;reference&lt;/a&gt;) |   &nbsp;
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

