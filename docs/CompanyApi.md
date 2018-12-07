# intrinio_sdk.CompanyApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_companies**](CompanyApi.md#filter_companies) | **GET** /companies/filter | Filter Companies
[**filter_company_fundamentals**](CompanyApi.md#filter_company_fundamentals) | **GET** /companies/{identifier}/fundamentals/filter | Filter Fundamentals for a Company
[**get_all_companies**](CompanyApi.md#get_all_companies) | **GET** /companies | Get All Companies
[**get_all_company_news**](CompanyApi.md#get_all_company_news) | **GET** /companies/news | Get All Company News
[**get_company**](CompanyApi.md#get_company) | **GET** /companies/{identifier} | Get a Company by ID
[**get_company_data_point_number**](CompanyApi.md#get_company_data_point_number) | **GET** /companies/{identifier}/data_point/{tag}/number | Get Company Data Point (Number)
[**get_company_data_point_text**](CompanyApi.md#get_company_data_point_text) | **GET** /companies/{identifier}/data_point/{tag}/text | Get Company Data Point (Text)
[**get_company_filings**](CompanyApi.md#get_company_filings) | **GET** /companies/{identifier}/filings | Get Filings for a Company
[**get_company_fundamentals**](CompanyApi.md#get_company_fundamentals) | **GET** /companies/{identifier}/fundamentals | Get All Fundamentals for a Company
[**get_company_historical_data**](CompanyApi.md#get_company_historical_data) | **GET** /companies/{identifier}/historical_data/{tag} | Get Company Historical Data
[**get_company_news**](CompanyApi.md#get_company_news) | **GET** /companies/{identifier}/news | Get News for a Company
[**get_company_securities**](CompanyApi.md#get_company_securities) | **GET** /companies/{identifier}/securities | Get Securities by Company
[**lookup_company_fundamental**](CompanyApi.md#lookup_company_fundamental) | **GET** /companies/{identifier}/fundamentals/lookup/{statement_code}/{fiscal_year}/{fiscal_period} | Lookup a Fundamental for a Company
[**search_companies**](CompanyApi.md#search_companies) | **GET** /companies/search | Search Companies


# **filter_companies**
> ApiResponseCompanies filter_companies(last_filing_date=last_filing_date, sic=sic, template=template, sector=sector, industry_category=industry_category, industry_group=industry_group, next_page=next_page)

Filter Companies

Returns Companies matching the specified filters

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

last_filing_date = '2013-10-20' # date | Last filing date (optional)
sic = 'sic_example' # str | Standard Industrial Classification code (optional)
template = 'template_example' # str | Template (optional)
sector = 'sector_example' # str | Industry sector (optional)
industry_category = 'industry_category_example' # str | Industry category (optional)
industry_group = 'industry_group_example' # str | Industry group (optional)
next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = company_api.filter_companies(last_filing_date=last_filing_date, sic=sic, template=template, sector=sector, industry_category=industry_category, industry_group=industry_group, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->filter_companies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_filing_date** | **date**| Last filing date | [optional] 
 **sic** | **str**| Standard Industrial Classification code | [optional] 
 **template** | **str**| Template | [optional] 
 **sector** | **str**| Industry sector | [optional] 
 **industry_category** | **str**| Industry category | [optional] 
 **industry_group** | **str**| Industry group | [optional] 
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseCompanies**](ApiResponseCompanies.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_company_fundamentals**
> ApiResponseCompanyFundamentals filter_company_fundamentals(identifier, filed_after=filed_after, filed_before=filed_before, reported_only=reported_only, fiscal_year=fiscal_year, statement_code=statement_code, type=type, start_date=start_date, end_date=end_date, next_page=next_page)

Filter Fundamentals for a Company

Returns Fundamentals for the Company with the given `identifier` and matching the specified filters

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

identifier = 'identifier_example' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
filed_after = '2013-10-20' # date | Filed on or after this date (optional)
filed_before = '2013-10-20' # date | Filed on or before this date (optional)
reported_only = true # bool | Only as-reported fundamentals (optional)
fiscal_year = 56 # int | Only for the given fiscal year (optional)
statement_code = 'statement_code_example' # str | Only of the given statement code (optional)
type = 'type_example' # str | Only of the given type (optional)
start_date = '2013-10-20' # date | Only on or after the given date (optional)
end_date = '2013-10-20' # date | Only on or after the given date (optional)
next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = company_api.filter_company_fundamentals(identifier, filed_after=filed_after, filed_before=filed_before, reported_only=reported_only, fiscal_year=fiscal_year, statement_code=statement_code, type=type, start_date=start_date, end_date=end_date, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->filter_company_fundamentals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | 
 **filed_after** | **date**| Filed on or after this date | [optional] 
 **filed_before** | **date**| Filed on or before this date | [optional] 
 **reported_only** | **bool**| Only as-reported fundamentals | [optional] 
 **fiscal_year** | **int**| Only for the given fiscal year | [optional] 
 **statement_code** | **str**| Only of the given statement code | [optional] 
 **type** | **str**| Only of the given type | [optional] 
 **start_date** | **date**| Only on or after the given date | [optional] 
 **end_date** | **date**| Only on or after the given date | [optional] 
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseCompanyFundamentals**](ApiResponseCompanyFundamentals.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_companies**
> ApiResponseCompanies get_all_companies(next_page=next_page)

Get All Companies

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = company_api.get_all_companies(next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_all_companies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseCompanies**](ApiResponseCompanies.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_company_news**
> ApiResponseNews get_all_company_news(next_page=next_page)

Get All Company News

Returns all news for all companies

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = company_api.get_all_company_news(next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_all_company_news: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseNews**](ApiResponseNews.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company**
> Company get_company(identifier)

Get a Company by ID

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

identifier = 'identifier_example' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)

try:
    api_response = company_api.get_company(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | 

### Return type

[**Company**](Company.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_data_point_number**
> DataPointNumber get_company_data_point_number(identifier, tag)

Get Company Data Point (Number)

Returns a numeric value for the given `tag` for the Company with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

identifier = 'identifier_example' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
tag = 'tag_example' # str | An Intrinio data tag

try:
    api_response = company_api.get_company_data_point_number(identifier, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company_data_point_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag | 

### Return type

[**DataPointNumber**](DataPointNumber.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_data_point_text**
> DataPointText get_company_data_point_text(identifier, tag)

Get Company Data Point (Text)

Returns a text value for the given `tag` for the Company with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

identifier = 'identifier_example' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
tag = 'tag_example' # str | An Intrinio data tag

try:
    api_response = company_api.get_company_data_point_text(identifier, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company_data_point_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag | 

### Return type

[**DataPointText**](DataPointText.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_filings**
> ApiResponseCompanyFilings get_company_filings(identifier, next_page=next_page)

Get Filings for a Company

Returns a complete list of SEC filings for the Company with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

identifier = 'identifier_example' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = company_api.get_company_filings(identifier, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company_filings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | 
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseCompanyFilings**](ApiResponseCompanyFilings.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_fundamentals**
> ApiResponseCompanyFundamentals get_company_fundamentals(identifier, next_page=next_page)

Get All Fundamentals for a Company

Returns all Fundamentals for the Company with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

identifier = 'identifier_example' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = company_api.get_company_fundamentals(identifier, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company_fundamentals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | 
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseCompanyFundamentals**](ApiResponseCompanyFundamentals.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_historical_data**
> ApiResponseCompanyHistoricalData get_company_historical_data(identifier, tag, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, next_page=next_page)

Get Company Historical Data

Returns historical values for the given `tag` and the Company with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

identifier = 'identifier_example' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
tag = 'tag_example' # str | Item
type = 'type_example' # str | Filter by type, when applicable (optional)
start_date = '2013-10-20' # date | Get historical data on or after this date (optional)
end_date = '2013-10-20' # date | Get historical data on or before this date (optional)
sort_order = 'desc' # str | Sort by date `asc` or `desc` (optional) (default to desc)
next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = company_api.get_company_historical_data(identifier, tag, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company_historical_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | 
 **tag** | **str**| Item | 
 **type** | **str**| Filter by type, when applicable | [optional] 
 **start_date** | **date**| Get historical data on or after this date | [optional] 
 **end_date** | **date**| Get historical data on or before this date | [optional] 
 **sort_order** | **str**| Sort by date &#x60;asc&#x60; or &#x60;desc&#x60; | [optional] [default to desc]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseCompanyHistoricalData**](ApiResponseCompanyHistoricalData.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_news**
> ApiResponseCompanyNews get_company_news(identifier, next_page=next_page)

Get News for a Company

Returns news for the Company with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

identifier = 'identifier_example' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = company_api.get_company_news(identifier, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company_news: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | 
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseCompanyNews**](ApiResponseCompanyNews.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_securities**
> ApiResponseCompanySecurities get_company_securities(identifier, next_page=next_page)

Get Securities by Company

Return Securities for the Company with `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

identifier = 'identifier_example' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
next_page = 'next_page_example' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = company_api.get_company_securities(identifier, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company_securities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | 
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseCompanySecurities**](ApiResponseCompanySecurities.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lookup_company_fundamental**
> Fundamental lookup_company_fundamental(identifier, statement_code, fiscal_period, fiscal_year)

Lookup a Fundamental for a Company

Returns the Fundamental for the Company with the given `identifier` and with the given parameters

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

identifier = 'identifier_example' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
statement_code = 'statement_code_example' # str | The statement code
fiscal_period = 'fiscal_period_example' # str | The fiscal period
fiscal_year = 56 # int | The fiscal year

try:
    api_response = company_api.lookup_company_fundamental(identifier, statement_code, fiscal_period, fiscal_year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->lookup_company_fundamental: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | 
 **statement_code** | **str**| The statement code | 
 **fiscal_period** | **str**| The fiscal period | 
 **fiscal_year** | **int**| The fiscal year | 

### Return type

[**Fundamental**](Fundamental.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_companies**
> ApiResponseCompanies search_companies(query)

Search Companies

Searches for Companies matching the text `query`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

query = 'query_example' # str | Search parameters

try:
    api_response = company_api.search_companies(query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->search_companies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search parameters | 

### Return type

[**ApiResponseCompanies**](ApiResponseCompanies.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

