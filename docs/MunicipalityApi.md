# intrinio_sdk.MunicipalityApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_municipalities**](MunicipalityApi.md#get_all_municipalities) | **GET** /municipalities | All Municipalities
[**get_municipality_by_id**](MunicipalityApi.md#get_municipality_by_id) | **GET** /municipalities/{id} | Municipality by ID
[**get_municipality_financials**](MunicipalityApi.md#get_municipality_financials) | **GET** /municipalities/{id}/financials | Financials for a Municipality


# **get_all_municipalities**
> ApiResponseMunicipalities get_all_municipalities(has_financials=has_financials, government_name=government_name, government_type=government_type, area_name=area_name, area_type=area_type, city=city, state=state, zipcode=zipcode, population_greater_than=population_greater_than, population_less_than=population_less_than, enrollment_greater_than=enrollment_greater_than, enrollment_less_than=enrollment_less_than, next_page=next_page)

All Municipalities

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

municipality_api = intrinio_sdk.MunicipalityApi()

has_financials = true # bool | Return municipalities with financials (optional)
government_name = 'government_name_example' # str | Return municipalities with a government name matching the given query (optional)
government_type = 'government_type_example' # str | Return municipalities with the given government type (optional)
area_name = 'area_name_example' # str | Return municipalities with an area name matching the given query (optional)
area_type = 'area_type_example' # str | Return municipalities with the given area type (optional)
city = 'city_example' # str | Return municipalities in the given city (optional)
state = 'state_example' # str | Return municipalities in the given state (optional)
zipcode = 8.14 # float | Return municipalities in the given zipcode (optional)
population_greater_than = 8.14 # float | Return municipalities with a population greater than the given number (optional)
population_less_than = 8.14 # float | Return municipalities with a population less than the given number (optional)
enrollment_greater_than = 8.14 # float | Return municipalities with an enrollment greater than the given number (optional)
enrollment_less_than = 8.14 # float | Return municipalities with an enrollment less than the given number (optional)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = municipality_api.get_all_municipalities(has_financials=has_financials, government_name=government_name, government_type=government_type, area_name=area_name, area_type=area_type, city=city, state=state, zipcode=zipcode, population_greater_than=population_greater_than, population_less_than=population_less_than, enrollment_greater_than=enrollment_greater_than, enrollment_less_than=enrollment_less_than, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MunicipalityApi->get_all_municipalities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **has_financials** | **bool**| Return municipalities with financials | [optional] 
 **government_name** | **str**| Return municipalities with a government name matching the given query | [optional] 
 **government_type** | **str**| Return municipalities with the given government type | [optional] 
 **area_name** | **str**| Return municipalities with an area name matching the given query | [optional] 
 **area_type** | **str**| Return municipalities with the given area type | [optional] 
 **city** | **str**| Return municipalities in the given city | [optional] 
 **state** | **str**| Return municipalities in the given state | [optional] 
 **zipcode** | **float**| Return municipalities in the given zipcode | [optional] 
 **population_greater_than** | **float**| Return municipalities with a population greater than the given number | [optional] 
 **population_less_than** | **float**| Return municipalities with a population less than the given number | [optional] 
 **enrollment_greater_than** | **float**| Return municipalities with an enrollment greater than the given number | [optional] 
 **enrollment_less_than** | **float**| Return municipalities with an enrollment less than the given number | [optional] 
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseMunicipalities**](ApiResponseMunicipalities.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_municipality_by_id**
> Municipality get_municipality_by_id(id)

Municipality by ID

Returns the Municipality with the given ID

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

municipality_api = intrinio_sdk.MunicipalityApi()

id = 'mun_Xn7x4z' # str | An Intrinio ID of a Municipality

try:
    api_response = municipality_api.get_municipality_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MunicipalityApi->get_municipality_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An Intrinio ID of a Municipality | 

### Return type

[**Municipality**](Municipality.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_municipality_financials**
> ApiResponseMunicipalitiyFinancials get_municipality_financials(id, fiscal_year=fiscal_year)

Financials for a Municipality

Returns financial statement data for the Municipality with the given ID

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

municipality_api = intrinio_sdk.MunicipalityApi()

id = 'mun_Xn7x4z' # str | An Intrinio ID of a Municipality
fiscal_year = 8.14 # float | Return financials for the given fiscal year (optional)

try:
    api_response = municipality_api.get_municipality_financials(id, fiscal_year=fiscal_year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MunicipalityApi->get_municipality_financials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An Intrinio ID of a Municipality | 
 **fiscal_year** | **float**| Return financials for the given fiscal year | [optional] 

### Return type

[**ApiResponseMunicipalitiyFinancials**](ApiResponseMunicipalitiyFinancials.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

