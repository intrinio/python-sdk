# intrinio_sdk.DataPointApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_point_number**](DataPointApi.md#get_data_point_number) | **GET** /data_point/{identifier}/{tag}/number | Data Point (Number)
[**get_data_point_text**](DataPointApi.md#get_data_point_text) | **GET** /data_point/{identifier}/{tag}/text | Data Point (Text)



[//]: # (START_OPERATION)

[//]: # (CLASS:DataPointApi)

[//]: # (METHOD:get_data_point_number)

[//]: # (RETURN_TYPE:float)

[//]: # (RETURN_TYPE_KIND:primitive)

[//]: # (RETURN_TYPE_DOC:)

[//]: # (OPERATION:get_data_point_number_v2)

[//]: # (ENDPOINT:/data_point/{identifier}/{tag}/number)

[//]: # (DOCUMENT_LINK:DataPointApi.md#get_data_point_number)

## **get_data_point_number**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_data_point_number_v2)

[//]: # (START_OVERVIEW)

> float get_data_point_number(identifier, tag)

#### Data Point (Number)


Returns a numeric value for the given `tag` and the entity with the given `identifier`

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

identifier = 'AAPL'
tag = 'marketcap'

response = intrinio.DataPointApi().get_data_point_number(identifier, tag)
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
<br/>

[//]: # (END_PARAMETERS)

### Return type

**float**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:DataPointApi)

[//]: # (METHOD:get_data_point_text)

[//]: # (RETURN_TYPE:str)

[//]: # (RETURN_TYPE_KIND:primitive)

[//]: # (RETURN_TYPE_DOC:)

[//]: # (OPERATION:get_data_point_text_v2)

[//]: # (ENDPOINT:/data_point/{identifier}/{tag}/text)

[//]: # (DOCUMENT_LINK:DataPointApi.md#get_data_point_text)

## **get_data_point_text**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_data_point_text_v2)

[//]: # (START_OVERVIEW)

> str get_data_point_text(identifier, tag)

#### Data Point (Text)


Returns a text value for the given `tag` for the Security with the given `identifier`

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

identifier = 'AAPL'
tag = 'ceo'

response = intrinio.DataPointApi().get_data_point_text(identifier, tag)
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
<br/>

[//]: # (END_PARAMETERS)

### Return type

**str**

[//]: # (END_OPERATION)

