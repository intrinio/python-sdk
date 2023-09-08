# intrinio_sdk.MarketApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_market_status**](MarketApi.md#get_market_status) | **GET** /market/status | Market Status



[//]: # (START_OPERATION)

[//]: # (CLASS:MarketApi)

[//]: # (METHOD:get_market_status)

[//]: # (RETURN_TYPE:MarketStatusResult)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:MarketStatusResult.md)

[//]: # (OPERATION:get_market_status_v2)

[//]: # (ENDPOINT:/market/status)

[//]: # (DOCUMENT_LINK:MarketApi.md#get_market_status)

## **get_market_status**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_market_status_v2)

[//]: # (START_OVERVIEW)

> MarketStatusResult get_market_status()

#### Market Status


Returns the market status.

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


response = intrinio.MarketApi().get_market_status()
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

[**MarketStatusResult**](MarketStatusResult.md)

[//]: # (END_OPERATION)

