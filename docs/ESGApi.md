# intrinio_sdk.ESGApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_esg_companies**](ESGApi.md#get_esg_companies) | **GET** /esg/companies | ESG Companies
[**get_esg_company_comprehensive_ratings**](ESGApi.md#get_esg_company_comprehensive_ratings) | **GET** /esg/{identifier}/comprehensive | ESG Company Comprehensive Ratings History
[**get_esg_company_ratings**](ESGApi.md#get_esg_company_ratings) | **GET** /esg/{identifier} | ESG Company Ratings History
[**get_esg_latest**](ESGApi.md#get_esg_latest) | **GET** /esg | ESG Latest
[**get_esg_latest_comprehensive**](ESGApi.md#get_esg_latest_comprehensive) | **GET** /esg/comprehensive | ESG Latest Comprehensive



[//]: # (START_OPERATION)

[//]: # (CLASS:ESGApi)

[//]: # (METHOD:get_esg_companies)

[//]: # (RETURN_TYPE:ApiResponseESGCompanies)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseESGCompanies.md)

[//]: # (OPERATION:get_esg_companies_v2)

[//]: # (ENDPOINT:/esg/companies)

[//]: # (DOCUMENT_LINK:ESGApi.md#get_esg_companies)

## **get_esg_companies**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_esg_companies_v2)

[//]: # (START_OVERVIEW)

> ApiResponseESGCompanies get_esg_companies(country=country, industry=industry, ticker=ticker, page_size=page_size, next_page=next_page)

#### ESG Companies



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

country = '\"Canada\"'
industry = '\"Retail\"'
ticker = '\"SHOP\"'
page_size = 100
next_page = '\"~null\"'

response = intrinio.ESGApi().get_esg_companies(country=country, industry=industry, ticker=ticker, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | str|  | [optional]   &nbsp;
 **industry** | str|  | [optional]   &nbsp;
 **ticker** | str|  | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseESGCompanies**](ApiResponseESGCompanies.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:ESGApi)

[//]: # (METHOD:get_esg_company_comprehensive_ratings)

[//]: # (RETURN_TYPE:ApiResponseESGCompanyComprehensiveRatingHistory)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseESGCompanyComprehensiveRatingHistory.md)

[//]: # (OPERATION:get_esg_company_comprehensive_ratings_v2)

[//]: # (ENDPOINT:/esg/{identifier}/comprehensive)

[//]: # (DOCUMENT_LINK:ESGApi.md#get_esg_company_comprehensive_ratings)

## **get_esg_company_comprehensive_ratings**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_esg_company_comprehensive_ratings_v2)

[//]: # (START_OVERVIEW)

> ApiResponseESGCompanyComprehensiveRatingHistory get_esg_company_comprehensive_ratings(identifier, page_size=page_size, next_page=next_page)

#### ESG Company Comprehensive Ratings History



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
page_size = 100
next_page = '\"~null\"'

response = intrinio.ESGApi().get_esg_company_comprehensive_ratings(identifier, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| ISIN, Intrinio ID, or Ticker |   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseESGCompanyComprehensiveRatingHistory**](ApiResponseESGCompanyComprehensiveRatingHistory.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:ESGApi)

[//]: # (METHOD:get_esg_company_ratings)

[//]: # (RETURN_TYPE:ApiResponseESGCompanyRatingHistory)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseESGCompanyRatingHistory.md)

[//]: # (OPERATION:get_esg_company_ratings_v2)

[//]: # (ENDPOINT:/esg/{identifier})

[//]: # (DOCUMENT_LINK:ESGApi.md#get_esg_company_ratings)

## **get_esg_company_ratings**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_esg_company_ratings_v2)

[//]: # (START_OVERVIEW)

> ApiResponseESGCompanyRatingHistory get_esg_company_ratings(identifier, page_size=page_size, next_page=next_page)

#### ESG Company Ratings History



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
page_size = 100
next_page = '\"~null\"'

response = intrinio.ESGApi().get_esg_company_ratings(identifier, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| ISIN, Intrinio ID, or Ticker |   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseESGCompanyRatingHistory**](ApiResponseESGCompanyRatingHistory.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:ESGApi)

[//]: # (METHOD:get_esg_latest)

[//]: # (RETURN_TYPE:ApiResponseESGLatest)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseESGLatest.md)

[//]: # (OPERATION:get_esg_latest_v2)

[//]: # (ENDPOINT:/esg)

[//]: # (DOCUMENT_LINK:ESGApi.md#get_esg_latest)

## **get_esg_latest**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_esg_latest_v2)

[//]: # (START_OVERVIEW)

> ApiResponseESGLatest get_esg_latest(country=country, page_size=page_size, next_page=next_page)

#### ESG Latest



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

country = '\"USA\"'
page_size = 100
next_page = '\"~null\"'

response = intrinio.ESGApi().get_esg_latest(country=country, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | str|  | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseESGLatest**](ApiResponseESGLatest.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:ESGApi)

[//]: # (METHOD:get_esg_latest_comprehensive)

[//]: # (RETURN_TYPE:ApiResponseESGLatestComprehensive)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseESGLatestComprehensive.md)

[//]: # (OPERATION:get_esg_latest_comprehensive_v2)

[//]: # (ENDPOINT:/esg/comprehensive)

[//]: # (DOCUMENT_LINK:ESGApi.md#get_esg_latest_comprehensive)

## **get_esg_latest_comprehensive**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_esg_latest_comprehensive_v2)

[//]: # (START_OVERVIEW)

> ApiResponseESGLatestComprehensive get_esg_latest_comprehensive(country=country, page_size=page_size, next_page=next_page)

#### ESG Latest Comprehensive



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

country = '\"USA\"'
page_size = 100
next_page = '\"~null\"'

response = intrinio.ESGApi().get_esg_latest_comprehensive(country=country, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | str|  | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseESGLatestComprehensive**](ApiResponseESGLatestComprehensive.md)

[//]: # (END_OPERATION)

