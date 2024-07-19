# intrinio_sdk.MunicipalityApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_municipalities**](MunicipalityApi.md#get_all_municipalities) | **GET** /municipalities | All Municipalities
[**get_municipality_by_id**](MunicipalityApi.md#get_municipality_by_id) | **GET** /municipalities/{id} | Municipality by ID
[**get_municipality_financials**](MunicipalityApi.md#get_municipality_financials) | **GET** /municipalities/{id}/financials | Financials for a Municipality



[//]: # (START_OPERATION)

[//]: # (CLASS:MunicipalityApi)

[//]: # (METHOD:get_all_municipalities)

[//]: # (RETURN_TYPE:ApiResponseMunicipalities)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseMunicipalities.md)

[//]: # (OPERATION:get_all_municipalities_v2)

[//]: # (ENDPOINT:/municipalities)

[//]: # (DOCUMENT_LINK:MunicipalityApi.md#get_all_municipalities)

## **get_all_municipalities**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_all_municipalities_v2)

[//]: # (START_OVERVIEW)

> ApiResponseMunicipalities get_all_municipalities(has_financials=has_financials, government_name=government_name, government_type=government_type, area_name=area_name, area_type=area_type, city=city, state=state, zipcode=zipcode, population_greater_than=population_greater_than, population_less_than=population_less_than, enrollment_greater_than=enrollment_greater_than, enrollment_less_than=enrollment_less_than, next_page=next_page)

#### All Municipalities


Returns all Municipalities. When parameters are specified, returns matching municipalities.

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

has_financials = ''
government_name = ''
government_type = ''
area_name = ''
area_type = ''
city = ''
state = ''
zipcode = ''
population_greater_than = ''
population_less_than = ''
enrollment_greater_than = ''
enrollment_less_than = ''
next_page = ''

response = intrinio.MunicipalityApi().get_all_municipalities(has_financials=has_financials, government_name=government_name, government_type=government_type, area_name=area_name, area_type=area_type, city=city, state=state, zipcode=zipcode, population_greater_than=population_greater_than, population_less_than=population_less_than, enrollment_greater_than=enrollment_greater_than, enrollment_less_than=enrollment_less_than, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **has_financials** | bool| Return municipalities with financials | [optional]   &nbsp;
 **government_name** | str| Return municipalities with a government name matching the given query | [optional]   &nbsp;
 **government_type** | str| Return municipalities with the given government type | [optional]   &nbsp;
 **area_name** | str| Return municipalities with an area name matching the given query | [optional]   &nbsp;
 **area_type** | str| Return municipalities with the given area type | [optional]   &nbsp;
 **city** | str| Return municipalities in the given city | [optional]   &nbsp;
 **state** | str| Return municipalities in the given state | [optional]   &nbsp;
 **zipcode** | float| Return municipalities in the given zipcode | [optional]   &nbsp;
 **population_greater_than** | float| Return municipalities with a population greater than the given number | [optional]   &nbsp;
 **population_less_than** | float| Return municipalities with a population less than the given number | [optional]   &nbsp;
 **enrollment_greater_than** | float| Return municipalities with an enrollment greater than the given number | [optional]   &nbsp;
 **enrollment_less_than** | float| Return municipalities with an enrollment less than the given number | [optional]   &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseMunicipalities**](ApiResponseMunicipalities.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:MunicipalityApi)

[//]: # (METHOD:get_municipality_by_id)

[//]: # (RETURN_TYPE:Municipality)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:Municipality.md)

[//]: # (OPERATION:get_municipality_by_id_v2)

[//]: # (ENDPOINT:/municipalities/{id})

[//]: # (DOCUMENT_LINK:MunicipalityApi.md#get_municipality_by_id)

## **get_municipality_by_id**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_municipality_by_id_v2)

[//]: # (START_OVERVIEW)

> Municipality get_municipality_by_id(id)

#### Municipality by ID


Returns the Municipality with the given ID

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

id = 'mun_Xn7x4z'

response = intrinio.MunicipalityApi().get_municipality_by_id(id)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | str| An Intrinio ID of a Municipality |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**Municipality**](Municipality.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:MunicipalityApi)

[//]: # (METHOD:get_municipality_financials)

[//]: # (RETURN_TYPE:ApiResponseMunicipalitiyFinancials)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseMunicipalitiyFinancials.md)

[//]: # (OPERATION:get_municipality_financials_v2)

[//]: # (ENDPOINT:/municipalities/{id}/financials)

[//]: # (DOCUMENT_LINK:MunicipalityApi.md#get_municipality_financials)

## **get_municipality_financials**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_municipality_financials_v2)

[//]: # (START_OVERVIEW)

> ApiResponseMunicipalitiyFinancials get_municipality_financials(id, fiscal_year=fiscal_year)

#### Financials for a Municipality


Returns financial statement data for the Municipality with the given ID

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

id = 'mun_Xn7x4z'
fiscal_year = 2017

response = intrinio.MunicipalityApi().get_municipality_financials(id, fiscal_year=fiscal_year)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | str| An Intrinio ID of a Municipality |   &nbsp;
 **fiscal_year** | float| Return financials for the given fiscal year | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseMunicipalitiyFinancials**](ApiResponseMunicipalitiyFinancials.md)

[//]: # (END_OPERATION)

