# intrinio_sdk.InsiderTransactionFilingsApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_insider_transaction_filings**](InsiderTransactionFilingsApi.md#get_all_insider_transaction_filings) | **GET** /insider_transaction_filings | All Insider Transactions Filings



[//]: # (START_OPERATION)

[//]: # (CLASS:InsiderTransactionFilingsApi)

[//]: # (METHOD:get_all_insider_transaction_filings)

[//]: # (RETURN_TYPE:ApiResponseOwnerInsiderTransactionFilings)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseOwnerInsiderTransactionFilings.md)

[//]: # (OPERATION:get_all_insider_transaction_filings_v2)

[//]: # (ENDPOINT:/insider_transaction_filings)

[//]: # (DOCUMENT_LINK:InsiderTransactionFilingsApi.md#get_all_insider_transaction_filings)

## **get_all_insider_transaction_filings**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_all_insider_transaction_filings_v2)

[//]: # (START_OVERVIEW)

> ApiResponseOwnerInsiderTransactionFilings get_all_insider_transaction_filings(start_date=start_date, end_date=end_date, page_size=page_size, sort_by=sort_by, next_page=next_page)

#### All Insider Transactions Filings


Returns all insider transactions filings fitting the optional supplied start and end date.

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

start_date = '2015-01-01'
end_date = ''
page_size = 100
sort_by = 'updated_on'
next_page = ''

response = intrinio.InsiderTransactionFilingsApi().get_all_insider_transaction_filings(start_date=start_date, end_date=end_date, page_size=page_size, sort_by=sort_by, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | date| Filed on or after the given date | [optional]   &nbsp;
 **end_date** | date| Filed before or after the given date | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **sort_by** | str| The field to sort by.  Default is &#39;filing_date&#39;.  Valid values are - &#39;filing_date&#39;, &#39;updated_on&#39;. | [optional]   &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseOwnerInsiderTransactionFilings**](ApiResponseOwnerInsiderTransactionFilings.md)

[//]: # (END_OPERATION)

