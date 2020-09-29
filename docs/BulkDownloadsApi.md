# intrinio_sdk.BulkDownloadsApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bulk_download_links**](BulkDownloadsApi.md#get_bulk_download_links) | **GET** /bulk_downloads/links | All Links



[//]: # (START_OPERATION)

[//]: # (CLASS:BulkDownloadsApi)

[//]: # (METHOD:get_bulk_download_links)

[//]: # (RETURN_TYPE:ApiResponseBulkDownloadLinks)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseBulkDownloadLinks.md)

[//]: # (OPERATION:get_bulk_download_links_v2)

[//]: # (ENDPOINT:/bulk_downloads/links)

[//]: # (DOCUMENT_LINK:BulkDownloadsApi.md#get_bulk_download_links)

## **get_bulk_download_links**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_bulk_download_links_v2)

[//]: # (START_OVERVIEW)

> ApiResponseBulkDownloadLinks get_bulk_download_links()

#### All Links


Returns all active bulk downloads for your account with links to download.

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


response = intrinio.BulkDownloadsApi().get_bulk_download_links()
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

[**ApiResponseBulkDownloadLinks**](ApiResponseBulkDownloadLinks.md)

[//]: # (END_OPERATION)

