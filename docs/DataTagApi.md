# intrinio_sdk.DataTagApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_data_tags**](DataTagApi.md#get_all_data_tags) | **GET** /data_tags | All Data Tags
[**get_data_tag_by_id**](DataTagApi.md#get_data_tag_by_id) | **GET** /data_tags/{identifier} | Lookup Data Tag
[**search_data_tags**](DataTagApi.md#search_data_tags) | **GET** /data_tags/search | Search Data Tags



[//]: # (START_OPERATION)

[//]: # (CLASS:DataTagApi)

[//]: # (METHOD:get_all_data_tags)

[//]: # (RETURN_TYPE:ApiResponseDataTags)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseDataTags.md)

[//]: # (OPERATION:get_all_data_tags_v2)

[//]: # (ENDPOINT:/data_tags)

[//]: # (DOCUMENT_LINK:DataTagApi.md#get_all_data_tags)

## **get_all_data_tags**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_all_data_tags_v2)

[//]: # (START_OVERVIEW)

> ApiResponseDataTags get_all_data_tags(tag=tag, type=type, parent=parent, statement_code=statement_code, fs_template=fs_template, page_size=page_size, next_page=next_page)

#### All Data Tags


Returns all Data Tags. Returns Data Tags matching parameters when specified.

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

tag = '\"~null\"'
type = '\"~null\"'
parent = '\"~null\"'
statement_code = '\"income_statement\"'
fs_template = 'industrial'
page_size = 100
next_page = '\"~null\"'

response = intrinio.DataTagApi().get_all_data_tags(tag=tag, type=type, parent=parent, statement_code=statement_code, fs_template=fs_template, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | str| Tag | [optional]   &nbsp;
 **type** | str| Type | [optional]   &nbsp;
 **parent** | str| ID of tag parent | [optional]   &nbsp;
 **statement_code** | str| Statement Code | [optional]   &nbsp;
 **fs_template** | str| Template | [optional] [default to industrial]  &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseDataTags**](ApiResponseDataTags.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:DataTagApi)

[//]: # (METHOD:get_data_tag_by_id)

[//]: # (RETURN_TYPE:DataTag)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:DataTag.md)

[//]: # (OPERATION:get_data_tag_by_id_v2)

[//]: # (ENDPOINT:/data_tags/{identifier})

[//]: # (DOCUMENT_LINK:DataTagApi.md#get_data_tag_by_id)

## **get_data_tag_by_id**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_data_tag_by_id_v2)

[//]: # (START_OVERVIEW)

> DataTag get_data_tag_by_id(identifier)

#### Lookup Data Tag


Returns the Data Tag with the given `identifier`

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

identifier = '\"marketcap\"'

response = intrinio.DataTagApi().get_data_tag_by_id(identifier)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| The Intrinio ID or the code-name of the Data Tag |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**DataTag**](DataTag.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:DataTagApi)

[//]: # (METHOD:search_data_tags)

[//]: # (RETURN_TYPE:ApiResponseDataTagsSearch)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseDataTagsSearch.md)

[//]: # (OPERATION:search_data_tags_v2)

[//]: # (ENDPOINT:/data_tags/search)

[//]: # (DOCUMENT_LINK:DataTagApi.md#search_data_tags)

## **search_data_tags**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/search_data_tags_v2)

[//]: # (START_OVERVIEW)

> ApiResponseDataTagsSearch search_data_tags(query, page_size=page_size)

#### Search Data Tags


Searches for Data Tags matching the text `query`

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

query = '\"revenue\"'
page_size = 100

response = intrinio.DataTagApi().search_data_tags(query, page_size=page_size)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | str|  |   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseDataTagsSearch**](ApiResponseDataTagsSearch.md)

[//]: # (END_OPERATION)

