# intrinio_sdk.DataPointApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_point_number**](DataPointApi.md#get_data_point_number) | **GET** /data_point/{identifier}/{tag}/number | Data Point (Number)
[**get_data_point_text**](DataPointApi.md#get_data_point_text) | **GET** /data_point/{identifier}/{tag}/text | Data Point (Text)


# **get_data_point_number**
> float get_data_point_number(identifier, tag)

Data Point (Number)

$$v2_data_point_number_description$$

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

data_point_api = intrinio_sdk.DataPointApi()

identifier = '$$v2_data_point_identifier_default$$' # str | $$v2_data_point_identifier_description$$
tag = '$$v2_data_point_item_number_default$$' # str | $$v2_data_point_item_description$$

try:
    api_response = data_point_api.get_data_point_number(identifier, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataPointApi->get_data_point_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| $$v2_data_point_identifier_description$$ | 
 **tag** | **str**| $$v2_data_point_item_description$$ | 

### Return type

**float**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_point_text**
> str get_data_point_text(identifier, tag)

Data Point (Text)

$$v2_data_point_text_description$$

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

data_point_api = intrinio_sdk.DataPointApi()

identifier = '$$v2_data_point_identifier_default$$' # str | $$v2_data_point_identifier_description$$
tag = '$$v2_data_point_item_text_default$$' # str | $$v2_data_point_item_description$$

try:
    api_response = data_point_api.get_data_point_text(identifier, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataPointApi->get_data_point_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| $$v2_data_point_identifier_description$$ | 
 **tag** | **str**| $$v2_data_point_item_description$$ | 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

