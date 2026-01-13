# intrinio_sdk.AccountApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_current_usage**](AccountApi.md#get_account_current_usage) | **GET** /account | Account Current Usage



[//]: # (START_OPERATION)

[//]: # (CLASS:AccountApi)

[//]: # (METHOD:get_account_current_usage)

[//]: # (RETURN_TYPE:ApiResponseAccountUsages)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseAccountUsages.md)

[//]: # (OPERATION:get_account_current_usage_v2)

[//]: # (ENDPOINT:/account)

[//]: # (DOCUMENT_LINK:AccountApi.md#get_account_current_usage)

## **get_account_current_usage**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_account_current_usage_v2)

[//]: # (START_OVERVIEW)

> ApiResponseAccountUsages get_account_current_usage()

#### Account Current Usage


Returns a list of all access codes available with their current usage.

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


response = intrinio.AccountApi().get_account_current_usage()
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)

This endpoint does not need any parameter.
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseAccountUsages**](ApiResponseAccountUsages.md)

[//]: # (END_OPERATION)

