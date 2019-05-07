# intrinio_sdk.CompanyApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_companies**](CompanyApi.md#get_all_companies) | **GET** /companies | All Companies
[**get_all_company_news**](CompanyApi.md#get_all_company_news) | **GET** /companies/news | All News
[**get_company**](CompanyApi.md#get_company) | **GET** /companies/{identifier} | Lookup Company
[**get_company_data_point_number**](CompanyApi.md#get_company_data_point_number) | **GET** /companies/{identifier}/data_point/{tag}/number | Data Point (Number) for Company
[**get_company_data_point_text**](CompanyApi.md#get_company_data_point_text) | **GET** /companies/{identifier}/data_point/{tag}/text | Data Point (Text) for Company
[**get_company_filings**](CompanyApi.md#get_company_filings) | **GET** /companies/{identifier}/filings | All Filings by Company
[**get_company_fundamentals**](CompanyApi.md#get_company_fundamentals) | **GET** /companies/{identifier}/fundamentals | All Fundamentals by Company
[**get_company_historical_data**](CompanyApi.md#get_company_historical_data) | **GET** /companies/{identifier}/historical_data/{tag} | Historical Data for Company
[**get_company_news**](CompanyApi.md#get_company_news) | **GET** /companies/{identifier}/news | All News by Company
[**get_company_securities**](CompanyApi.md#get_company_securities) | **GET** /companies/{identifier}/securities | All Securities by Company
[**lookup_company_fundamental**](CompanyApi.md#lookup_company_fundamental) | **GET** /companies/{identifier}/fundamentals/lookup/{statement_code}/{fiscal_year}/{fiscal_period} | Lookup Fundamental by Company
[**search_companies**](CompanyApi.md#search_companies) | **GET** /companies/search | Search Companies



[//]: # (START_OPERATION)

[//]: # (OPERATION:get_all_companies_v2)

[//]: # (ENDPOINT:/companies)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_all_companies)

## **get_all_companies**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_all_companies_v2)

> ApiResponseCompanies get_all_companies(latest_filing_date=latest_filing_date, sic=sic, template=template, sector=sector, industry_category=industry_category, industry_group=industry_group, page_size=page_size, next_page=next_page)

#### All Companies


Returns all Companies. When parameters are specified, returns matching companies.

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

latest_filing_date = '' # date | Last filing date (optional)
sic = '' # str | Standard Industrial Classification code (optional)
template = '' # str | Template (optional)
sector = '' # str | Industry sector (optional)
industry_category = '' # str | Industry category (optional)
industry_group = '' # str | Industry group (optional)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = company_api.get_all_companies(latest_filing_date=latest_filing_date, sic=sic, template=template, sector=sector, industry_category=industry_category, industry_group=industry_group, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_all_companies: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latest_filing_date** | **date**| Last filing date | [optional] 
 **sic** | **str**| Standard Industrial Classification code | [optional] 
 **template** | **str**| Template | [optional] 
 **sector** | **str**| Industry sector | [optional] 
 **industry_category** | **str**| Industry category | [optional] 
 **industry_group** | **str**| Industry group | [optional] 
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 
<br/>
### Return type

[**ApiResponseCompanies**](ApiResponseCompanies.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_all_company_news_v2)

[//]: # (ENDPOINT:/companies/news)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_all_company_news)

## **get_all_company_news**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_all_company_news_v2)

> ApiResponseNews get_all_company_news(page_size=page_size, next_page=next_page)

#### All News


Returns all News for all Companies

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = company_api.get_all_company_news(page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_all_company_news: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 
<br/>
### Return type

[**ApiResponseNews**](ApiResponseNews.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_company_v2)

[//]: # (ENDPOINT:/companies/{identifier})

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_company)

## **get_company**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_company_v2)

> Company get_company(identifier)

#### Lookup Company


Returns the Company with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

identifier = 'AAPL' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)

try:
    api_response = company_api.get_company(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | 
<br/>
### Return type

[**Company**](Company.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_company_data_point_number_v2)

[//]: # (ENDPOINT:/companies/{identifier}/data_point/{tag}/number)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_company_data_point_number)

## **get_company_data_point_number**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_company_data_point_number_v2)

> float get_company_data_point_number(identifier, tag)

#### Data Point (Number) for Company


Returns a numeric value for the given `tag` for the Company with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

identifier = 'AAPL' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
tag = 'marketcap' # str | An Intrinio data tag ID or code (<a href='https://data.intrinio.com/data-tags'>reference</a>)

try:
    api_response = company_api.get_company_data_point_number(identifier, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company_data_point_number: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code (&lt;a href&#x3D;&#39;https://data.intrinio.com/data-tags&#39;&gt;reference&lt;/a&gt;) | 
<br/>
### Return type

**float**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_company_data_point_text_v2)

[//]: # (ENDPOINT:/companies/{identifier}/data_point/{tag}/text)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_company_data_point_text)

## **get_company_data_point_text**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_company_data_point_text_v2)

> str get_company_data_point_text(identifier, tag)

#### Data Point (Text) for Company


Returns a text value for the given `tag` for the Company with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

identifier = 'AAPL' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
tag = 'ceo' # str | An Intrinio data tag ID or code (<a href='https://data.intrinio.com/data-tags'>reference</a>)

try:
    api_response = company_api.get_company_data_point_text(identifier, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company_data_point_text: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code (&lt;a href&#x3D;&#39;https://data.intrinio.com/data-tags&#39;&gt;reference&lt;/a&gt;) | 
<br/>
### Return type

**str**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_company_filings_v2)

[//]: # (ENDPOINT:/companies/{identifier}/filings)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_company_filings)

## **get_company_filings**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_company_filings_v2)

> ApiResponseCompanyFilings get_company_filings(identifier, page_size=page_size, next_page=next_page)

#### All Filings by Company


Returns a complete list of SEC filings for the Company with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

identifier = 'AAPL' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = company_api.get_company_filings(identifier, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company_filings: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | 
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 
<br/>
### Return type

[**ApiResponseCompanyFilings**](ApiResponseCompanyFilings.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_company_fundamentals_v2)

[//]: # (ENDPOINT:/companies/{identifier}/fundamentals)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_company_fundamentals)

## **get_company_fundamentals**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_company_fundamentals_v2)

> ApiResponseCompanyFundamentals get_company_fundamentals(identifier, filed_after=filed_after, filed_before=filed_before, reported_only=reported_only, fiscal_year=fiscal_year, statement_code=statement_code, type=type, start_date=start_date, end_date=end_date, page_size=page_size, next_page=next_page)

#### All Fundamentals by Company


Returns all Fundamentals for the Company with the given `identifier`. Returns Fundamentals matching parameters when supplied.

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

identifier = 'AAPL' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
filed_after = '' # date | Filed on or after this date (optional)
filed_before = '' # date | Filed on or before this date (optional)
reported_only = False # bool | Only as-reported fundamentals (optional)
fiscal_year = "~null" # int | Only for the given fiscal year (optional)
statement_code = '' # str | Only of the given statement code (optional)
type = '' # str | Only of the given type (optional)
start_date = '' # date | Only on or after the given date (optional)
end_date = '' # date | Only on or before the given date (optional)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = company_api.get_company_fundamentals(identifier, filed_after=filed_after, filed_before=filed_before, reported_only=reported_only, fiscal_year=fiscal_year, statement_code=statement_code, type=type, start_date=start_date, end_date=end_date, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company_fundamentals: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

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
 **end_date** | **date**| Only on or before the given date | [optional] 
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 
<br/>
### Return type

[**ApiResponseCompanyFundamentals**](ApiResponseCompanyFundamentals.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_company_historical_data_v2)

[//]: # (ENDPOINT:/companies/{identifier}/historical_data/{tag})

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_company_historical_data)

## **get_company_historical_data**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_company_historical_data_v2)

> ApiResponseCompanyHistoricalData get_company_historical_data(identifier, tag, frequency=frequency, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)

#### Historical Data for Company


Returns historical values for the given `tag` and the Company with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

identifier = 'AAPL' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
tag = 'marketcap' # str | An Intrinio data tag ID or code (<a href='https://data.intrinio.com/data-tags'>reference</a>)
frequency = 'daily' # str | Return historical data in the given frequency (optional) (default to daily)
type = '' # str | Filter by type, when applicable (optional)
start_date = '2018-01-01' # date | Get historical data on or after this date (optional)
end_date = '' # date | Get historical data on or before this date (optional)
sort_order = 'desc' # str | Sort by date `asc` or `desc` (optional) (default to desc)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = company_api.get_company_historical_data(identifier, tag, frequency=frequency, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company_historical_data: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | 
 **tag** | **str**| An Intrinio data tag ID or code (&lt;a href&#x3D;&#39;https://data.intrinio.com/data-tags&#39;&gt;reference&lt;/a&gt;) | 
 **frequency** | **str**| Return historical data in the given frequency | [optional] [default to daily]
 **type** | **str**| Filter by type, when applicable | [optional] 
 **start_date** | **date**| Get historical data on or after this date | [optional] 
 **end_date** | **date**| Get historical data on or before this date | [optional] 
 **sort_order** | **str**| Sort by date &#x60;asc&#x60; or &#x60;desc&#x60; | [optional] [default to desc]
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 
<br/>
### Return type

[**ApiResponseCompanyHistoricalData**](ApiResponseCompanyHistoricalData.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_company_news_v2)

[//]: # (ENDPOINT:/companies/{identifier}/news)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_company_news)

## **get_company_news**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_company_news_v2)

> ApiResponseCompanyNews get_company_news(identifier, page_size=page_size, next_page=next_page)

#### All News by Company


Returns news for the Company with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

identifier = 'AAPL' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = company_api.get_company_news(identifier, page_size=page_size, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company_news: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | 
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 
<br/>
### Return type

[**ApiResponseCompanyNews**](ApiResponseCompanyNews.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:get_company_securities_v2)

[//]: # (ENDPOINT:/companies/{identifier}/securities)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_company_securities)

## **get_company_securities**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/get_company_securities_v2)

> ApiResponseCompanySecurities get_company_securities(identifier, next_page=next_page)

#### All Securities by Company


Returns Securities for the Company with the given `identifier`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

identifier = 'AAPL' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = company_api.get_company_securities(identifier, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company_securities: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | 
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 
<br/>
### Return type

[**ApiResponseCompanySecurities**](ApiResponseCompanySecurities.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:lookup_company_fundamental_v2)

[//]: # (ENDPOINT:/companies/{identifier}/fundamentals/lookup/{statement_code}/{fiscal_year}/{fiscal_period})

[//]: # (DOCUMENT_LINK:CompanyApi.md#lookup_company_fundamental)

## **lookup_company_fundamental**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/lookup_company_fundamental_v2)

> Fundamental lookup_company_fundamental(identifier, statement_code, fiscal_period, fiscal_year)

#### Lookup Fundamental by Company


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

company_api = intrinio_sdk.CompanyApi()

identifier = 'AAPL' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID)
statement_code = 'income_statement' # str | The statement code
fiscal_period = 'FY' # str | The fiscal period
fiscal_year = 2017 # int | The fiscal year

try:
    api_response = company_api.lookup_company_fundamental(identifier, statement_code, fiscal_period, fiscal_year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->lookup_company_fundamental: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | 
 **statement_code** | **str**| The statement code | 
 **fiscal_period** | **str**| The fiscal period | 
 **fiscal_year** | **int**| The fiscal year | 
<br/>
### Return type

[**Fundamental**](Fundamental.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (OPERATION:search_companies_v2)

[//]: # (ENDPOINT:/companies/search)

[//]: # (DOCUMENT_LINK:CompanyApi.md#search_companies)

## **search_companies**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/api_v2/search_companies_v2)

> ApiResponseCompaniesSearch search_companies(query, page_size=page_size)

#### Search Companies


Searches for Companies matching the text `query`

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company_api = intrinio_sdk.CompanyApi()

query = 'Apple' # str | Search parameters
page_size = 100 # int | The number of results to return (optional) (default to 100)

try:
    api_response = company_api.search_companies(query, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->search_companies: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search parameters | 
 **page_size** | **int**| The number of results to return | [optional] [default to 100]
<br/>
### Return type

[**ApiResponseCompaniesSearch**](ApiResponseCompaniesSearch.md)

[//]: # (END_OPERATION)

