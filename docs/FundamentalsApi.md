# intrinio_sdk.FundamentalsApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fundamental_by_id**](FundamentalsApi.md#get_fundamental_by_id) | **GET** /fundamentals/{id} | Fundamental by ID
[**get_fundamental_reported_financials**](FundamentalsApi.md#get_fundamental_reported_financials) | **GET** /fundamentals/{id}/reported_financials | Reported Financials
[**get_fundamental_standardized_financials**](FundamentalsApi.md#get_fundamental_standardized_financials) | **GET** /fundamentals/{id}/standardized_financials | Standardized Financials
[**lookup_fundamental**](FundamentalsApi.md#lookup_fundamental) | **GET** /fundamentals/lookup/{identifier}/{statement_code}/{fiscal_year}/{fiscal_period} | Lookup Fundamental



[//]: # (START_OPERTATION)

[//]: # (ENDPOINT:/fundamentals/{id})

[//]: # (DOC_LINK:FundamentalsApi.md#get_fundamental_by_id)

# **get_fundamental_by_id**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_fundamental_by_id_v2)

> Fundamental get_fundamental_by_id(id)

Fundamental by ID

Returns detailed fundamental data for the given `id`.

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

fundamentals_api = intrinio_sdk.FundamentalsApi()

id = 'fun_ge9LlE' # str | The Intrinio ID for the Fundamental

try:
    api_response = fundamentals_api.get_fundamental_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundamentalsApi->get_fundamental_by_id: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Intrinio ID for the Fundamental | 

### Return type

[**Fundamental**](Fundamental.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERTATION)

[//]: # (ENDPOINT:/fundamentals/{id}/reported_financials)

[//]: # (DOC_LINK:FundamentalsApi.md#get_fundamental_reported_financials)

# **get_fundamental_reported_financials**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_fundamental_reported_financials_v2)

> ApiResponseReportedFinancials get_fundamental_reported_financials(id)

Reported Financials

Returns the As-Reported Financials directly from the financial statements of the XBRL filings from the company

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

fundamentals_api = intrinio_sdk.FundamentalsApi()

id = 'AAPL-income_statement-2018-Q1' # str | The Intrinio ID or lookup code (ticker-statement-year-period) for the Fundamental

try:
    api_response = fundamentals_api.get_fundamental_reported_financials(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundamentalsApi->get_fundamental_reported_financials: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Intrinio ID or lookup code (ticker-statement-year-period) for the Fundamental | 

### Return type

[**ApiResponseReportedFinancials**](ApiResponseReportedFinancials.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERTATION)

[//]: # (ENDPOINT:/fundamentals/{id}/standardized_financials)

[//]: # (DOC_LINK:FundamentalsApi.md#get_fundamental_standardized_financials)

# **get_fundamental_standardized_financials**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_fundamental_standardized_financials_v2)

> ApiResponseStandardizedFinancials get_fundamental_standardized_financials(id)

Standardized Financials

Returns professional-grade historical financial data. This data is standardized, cleansed and verified to ensure the highest quality data sourced directly from the XBRL financial statements. The primary purpose of standardized financials are to facilitate comparability across a single company’s fundamentals and across all companies fundamentals. For example, it is possible to compare total revenues between two companies as of a certain point in time, or within a single company across multiple time periods. This is not possible using the as reported financial statements because of the inherent complexity of reporting standards.

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

fundamentals_api = intrinio_sdk.FundamentalsApi()

id = 'AAPL-income_statement-2018-Q1' # str | The Intrinio ID or lookup code (ticker-statement-year-period) for the Fundamental

try:
    api_response = fundamentals_api.get_fundamental_standardized_financials(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundamentalsApi->get_fundamental_standardized_financials: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Intrinio ID or lookup code (ticker-statement-year-period) for the Fundamental | 

### Return type

[**ApiResponseStandardizedFinancials**](ApiResponseStandardizedFinancials.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERTATION)

[//]: # (ENDPOINT:/fundamentals/lookup/{identifier}/{statement_code}/{fiscal_year}/{fiscal_period})

[//]: # (DOC_LINK:FundamentalsApi.md#lookup_fundamental)

# **lookup_fundamental**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/lookup_fundamental_v2)

> Fundamental lookup_fundamental(identifier, statement_code, fiscal_year, fiscal_period)

Lookup Fundamental

Returns the Fundamental for the Company with the given `identifier` and with the given parameters

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

fundamentals_api = intrinio_sdk.FundamentalsApi()

identifier = 'AAPL' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
statement_code = 'income_statement' # str | The statement code
fiscal_year = 2017 # int | The fiscal year
fiscal_period = 'FY' # str | The fiscal period

try:
    api_response = fundamentals_api.lookup_fundamental(identifier, statement_code, fiscal_year, fiscal_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundamentalsApi->lookup_fundamental: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | 
 **statement_code** | **str**| The statement code | 
 **fiscal_year** | **int**| The fiscal year | 
 **fiscal_period** | **str**| The fiscal period | 

### Return type

[**Fundamental**](Fundamental.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

[//]: # (END_OPERATION)

