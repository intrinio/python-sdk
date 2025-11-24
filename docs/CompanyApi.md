# intrinio_sdk.CompanyApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_expected_earnings_dates**](CompanyApi.md#all_expected_earnings_dates) | **GET** /companies/upcoming_earnings | All Expected Earnings Dates
[**expected_earnings_dates_by_company**](CompanyApi.md#expected_earnings_dates_by_company) | **GET** /companies/{identifier}/upcoming_earnings | Expected Earnings Dates by Company
[**get_all_companies**](CompanyApi.md#get_all_companies) | **GET** /companies | All Companies
[**get_all_companies_daily_metrics**](CompanyApi.md#get_all_companies_daily_metrics) | **GET** /companies/daily_metrics | All Companies daily metrics
[**get_all_company_news**](CompanyApi.md#get_all_company_news) | **GET** /companies/news | All News
[**get_company**](CompanyApi.md#get_company) | **GET** /companies/{identifier} | Lookup Company
[**get_company_answers**](CompanyApi.md#get_company_answers) | **GET** /companies/{identifier}/answers | Company Answers
[**get_company_daily_metrics**](CompanyApi.md#get_company_daily_metrics) | **GET** /companies/{identifier}/daily_metrics | Company metrics by Company
[**get_company_data_point_number**](CompanyApi.md#get_company_data_point_number) | **GET** /companies/{identifier}/data_point/{tag}/number | Data Point (Number) for Company
[**get_company_data_point_text**](CompanyApi.md#get_company_data_point_text) | **GET** /companies/{identifier}/data_point/{tag}/text | Data Point (Text) for Company
[**get_company_filings**](CompanyApi.md#get_company_filings) | **GET** /companies/{identifier}/filings | All Filings by Company
[**get_company_fundamentals**](CompanyApi.md#get_company_fundamentals) | **GET** /companies/{identifier}/fundamentals | All Fundamentals by Company
[**get_company_historical_data**](CompanyApi.md#get_company_historical_data) | **GET** /companies/{identifier}/historical_data/{tag} | Historical Data for Company
[**get_company_ipos**](CompanyApi.md#get_company_ipos) | **GET** /companies/ipos | IPOs
[**get_company_news**](CompanyApi.md#get_company_news) | **GET** /companies/{identifier}/news | All News by Company
[**get_company_news_body**](CompanyApi.md#get_company_news_body) | **GET** /companies/news/body | News Article Body
[**get_company_public_float**](CompanyApi.md#get_company_public_float) | **GET** /companies/{identifier}/public_float | Get Company&#39;s public float
[**get_company_securities**](CompanyApi.md#get_company_securities) | **GET** /companies/{identifier}/securities | All Securities by Company
[**insider_transaction_filings_by_company**](CompanyApi.md#insider_transaction_filings_by_company) | **GET** /companies/{identifier}/insider_transaction_filings | Insider Transaction Filings by Company
[**latest_insider_transaction_filing_by_company**](CompanyApi.md#latest_insider_transaction_filing_by_company) | **GET** /companies/{identifier}/insider_transaction_filings/latest | Latest Insider Transaction Filing by Company
[**lookup_company_fundamental**](CompanyApi.md#lookup_company_fundamental) | **GET** /companies/{identifier}/fundamentals/lookup/{statement_code}/{fiscal_year}/{fiscal_period} | Lookup Fundamental by Company
[**recognize_company**](CompanyApi.md#recognize_company) | **GET** /companies/recognize | Recognize Company
[**search_companies**](CompanyApi.md#search_companies) | **GET** /companies/search | Search Companies
[**shares_outstanding_by_company**](CompanyApi.md#shares_outstanding_by_company) | **GET** /companies/{identifier}/shares_outstanding | Shares Outstanding by Company



[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:all_expected_earnings_dates)

[//]: # (RETURN_TYPE:ApiResponseAllExpectedEarningsDates)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseAllExpectedEarningsDates.md)

[//]: # (OPERATION:all_expected_earnings_dates_v2)

[//]: # (ENDPOINT:/companies/upcoming_earnings)

[//]: # (DOCUMENT_LINK:CompanyApi.md#all_expected_earnings_dates)

## **all_expected_earnings_dates**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/all_expected_earnings_dates_v2)

[//]: # (START_OVERVIEW)

> ApiResponseAllExpectedEarningsDates all_expected_earnings_dates(tickers=tickers, fiscal_year=fiscal_year, fiscal_period=fiscal_period, expected_date_after=expected_date_after, expected_date_before=expected_date_before, page_size=page_size, next_page=next_page)

#### All Expected Earnings Dates


Returns expected earnings announcement dates for all companies, optionally filtered by tickers. Results are always sorted by expected date ascending and include company identification.

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

tickers = ''
fiscal_year = ''
fiscal_period = ''
expected_date_after = 'today'
expected_date_before = ''
page_size = 100
next_page = ''

response = intrinio.CompanyApi().all_expected_earnings_dates(tickers=tickers, fiscal_year=fiscal_year, fiscal_period=fiscal_period, expected_date_after=expected_date_after, expected_date_before=expected_date_before, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tickers** | str| Comma-delimited list of tickers to filter results | [optional]   &nbsp;
 **fiscal_year** | int| Filter by fiscal year | [optional]   &nbsp;
 **fiscal_period** | str| Filter by fiscal period (Q1, Q2, Q3, FY) | [optional]   &nbsp;
 **expected_date_after** | date| Returns expected dates on or after this date. Defaults to today if not provided. | [optional] [default to today]  &nbsp;
 **expected_date_before** | date| Returns expected dates before this date. | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseAllExpectedEarningsDates**](ApiResponseAllExpectedEarningsDates.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:expected_earnings_dates_by_company)

[//]: # (RETURN_TYPE:ApiResponseCompanyExpectedEarningsDates)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseCompanyExpectedEarningsDates.md)

[//]: # (OPERATION:expected_earnings_dates_by_company_v2)

[//]: # (ENDPOINT:/companies/{identifier}/upcoming_earnings)

[//]: # (DOCUMENT_LINK:CompanyApi.md#expected_earnings_dates_by_company)

## **expected_earnings_dates_by_company**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/expected_earnings_dates_by_company_v2)

[//]: # (START_OVERVIEW)

> ApiResponseCompanyExpectedEarningsDates expected_earnings_dates_by_company(identifier, fiscal_year=fiscal_year, fiscal_period=fiscal_period, expected_date_after=expected_date_after, expected_date_before=expected_date_before, page_size=page_size, next_page=next_page)

#### Expected Earnings Dates by Company


Returns expected earnings announcement dates for a company's fiscal periods with confidence intervals and historical filing date ranges.

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

identifier = 'AAPL'
fiscal_year = ''
fiscal_period = ''
expected_date_after = 'today'
expected_date_before = ''
page_size = 100
next_page = ''

response = intrinio.CompanyApi().expected_earnings_dates_by_company(identifier, fiscal_year=fiscal_year, fiscal_period=fiscal_period, expected_date_after=expected_date_after, expected_date_before=expected_date_before, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Company identifier (Ticker, CIK, LEI, Intrinio ID) |   &nbsp;
 **fiscal_year** | int| Filter by fiscal year | [optional]   &nbsp;
 **fiscal_period** | str| Filter by fiscal period (Q1, Q2, Q3, FY) | [optional]   &nbsp;
 **expected_date_after** | date| Returns expected dates on or after this date. Defaults to today if not provided. | [optional] [default to today]  &nbsp;
 **expected_date_before** | date| Returns expected dates before this date. | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseCompanyExpectedEarningsDates**](ApiResponseCompanyExpectedEarningsDates.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:get_all_companies)

[//]: # (RETURN_TYPE:ApiResponseCompanies)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseCompanies.md)

[//]: # (OPERATION:get_all_companies_v2)

[//]: # (ENDPOINT:/companies)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_all_companies)

## **get_all_companies**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_all_companies_v2)

[//]: # (START_OVERVIEW)

> ApiResponseCompanies get_all_companies(latest_filing_date=latest_filing_date, sic=sic, template=template, sector=sector, industry_category=industry_category, industry_group=industry_group, has_fundamentals=has_fundamentals, has_stock_prices=has_stock_prices, thea_enabled=thea_enabled, page_size=page_size, next_page=next_page)

#### All Companies


Returns all Companies. When parameters are specified, returns matching companies.

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

latest_filing_date = ''
sic = ''
template = ''
sector = ''
industry_category = ''
industry_group = ''
has_fundamentals = True
has_stock_prices = True
thea_enabled = ''
page_size = 100
next_page = ''

response = intrinio.CompanyApi().get_all_companies(latest_filing_date=latest_filing_date, sic=sic, template=template, sector=sector, industry_category=industry_category, industry_group=industry_group, has_fundamentals=has_fundamentals, has_stock_prices=has_stock_prices, thea_enabled=thea_enabled, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latest_filing_date** | date| Return companies whose latest 10-Q or 10-K was filed on or after this date | [optional]   &nbsp;
 **sic** | str| Return companies with the given Standard Industrial Classification code | [optional]   &nbsp;
 **template** | str| Return companies with the given financial statement template | [optional]   &nbsp;
 **sector** | str| Return companies in the given industry sector | [optional]   &nbsp;
 **industry_category** | str| Return companies in the given industry category | [optional]   &nbsp;
 **industry_group** | str| Return companies in the given industry group | [optional]   &nbsp;
 **has_fundamentals** | bool| Return only companies that have fundamentals when True | [optional]   &nbsp;
 **has_stock_prices** | bool| Return only companies that have stock prices when True | [optional]   &nbsp;
 **thea_enabled** | bool| Return companies whose have been read by our Thea NLP and are ready for our company answers endpoint | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseCompanies**](ApiResponseCompanies.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:get_all_companies_daily_metrics)

[//]: # (RETURN_TYPE:ApiResponseCompanyDailyMetrics)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseCompanyDailyMetrics.md)

[//]: # (OPERATION:get_all_companies_daily_metrics_v2)

[//]: # (ENDPOINT:/companies/daily_metrics)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_all_companies_daily_metrics)

## **get_all_companies_daily_metrics**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_all_companies_daily_metrics_v2)

[//]: # (START_OVERVIEW)

> ApiResponseCompanyDailyMetrics get_all_companies_daily_metrics(on_date=on_date, page_size=page_size, next_page=next_page, next_page2=next_page2)

#### All Companies daily metrics


Returns the company metrics for a date.

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

on_date = '2013-10-20'
page_size = 100
next_page = ''
next_page2 = ''

response = intrinio.CompanyApi().get_all_companies_daily_metrics(on_date=on_date, page_size=page_size, next_page=next_page, next_page2=next_page2)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_date** | date| Date of the metric | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
 **next_page2** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseCompanyDailyMetrics**](ApiResponseCompanyDailyMetrics.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:get_all_company_news)

[//]: # (RETURN_TYPE:ApiResponseNews)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseNews.md)

[//]: # (OPERATION:get_all_company_news_v2)

[//]: # (ENDPOINT:/companies/news)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_all_company_news)

## **get_all_company_news**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_all_company_news_v2)

[//]: # (START_OVERVIEW)

> ApiResponseNews get_all_company_news(specific_source=specific_source, page_size=page_size, sentiment=sentiment, topic=topic, company=company, security=security, start_date=start_date, end_date=end_date, language=language, word_count_greater_than=word_count_greater_than, word_count_less_than=word_count_less_than, is_spam=is_spam, business_relevance_greater_than=business_relevance_greater_than, business_relevance_less_than=business_relevance_less_than, next_page=next_page)

#### All News


Returns the latest news article links, headlines and summaries for all US traded companies allowing you to keep a pulse on companies and their business operations.

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

specific_source = ''
page_size = 100
sentiment = ''
topic = ''
company = 'AAPL'
security = 'AAPL'
start_date = ''
end_date = ''
language = ''
word_count_greater_than = ''
word_count_less_than = ''
is_spam = ''
business_relevance_greater_than = ''
business_relevance_less_than = ''
next_page = ''

response = intrinio.CompanyApi().get_all_company_news(specific_source=specific_source, page_size=page_size, sentiment=sentiment, topic=topic, company=company, security=security, start_date=start_date, end_date=end_date, language=language, word_count_greater_than=word_count_greater_than, word_count_less_than=word_count_less_than, is_spam=is_spam, business_relevance_greater_than=business_relevance_greater_than, business_relevance_less_than=business_relevance_less_than, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specific_source** | str| Only news from this source. Defaults to highest available if not present. | [optional]   &nbsp;
 **page_size** | int| The maximum number of results to return. | [optional] [default to 100]  &nbsp;
 **sentiment** | str| Filter by sentiment.  Unsupported for yahoo source. | [optional]   &nbsp;
 **topic** | str| Filter by topic.  Unsupported for yahoo source. | [optional]   &nbsp;
 **company** | str| Filter by &#x60;company&#x60; identifier (ticker, CIK, LEI, Intrinio ID) | [optional]   &nbsp;
 **security** | str| Filter by &#x60;security&#x60; identifier (ticker, figi, isin, cusip, Intrinio ID).  Unsupported for yahoo source. | [optional]   &nbsp;
 **start_date** | date| Limit news stories to those on or after this date. Defaults to yesterday if unspecified. | [optional]   &nbsp;
 **end_date** | date| Limit news stories to those on or before this date. | [optional]   &nbsp;
 **language** | str| Filter by language.  Unsupported for yahoo source. | [optional]   &nbsp;
 **word_count_greater_than** | int| News stories will have a word count greater than this value.  Unsupported for yahoo source. | [optional]   &nbsp;
 **word_count_less_than** | int| News stories will have a word count less than this value.  Unsupported for yahoo source. | [optional]   &nbsp;
 **is_spam** | bool| Filter whether it is marked as spam or not.  Unsupported for yahoo source. | [optional]   &nbsp;
 **business_relevance_greater_than** | float| News stories will have a business relevance score more than this value.  Unsupported for yahoo source. | [optional]   &nbsp;
 **business_relevance_less_than** | float| News stories will have a business relevance score less than this value.  Unsupported for yahoo source. | [optional]   &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseNews**](ApiResponseNews.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:get_company)

[//]: # (RETURN_TYPE:Company)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:Company.md)

[//]: # (OPERATION:get_company_v2)

[//]: # (ENDPOINT:/companies/{identifier})

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_company)

## **get_company**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_company_v2)

[//]: # (START_OVERVIEW)

> Company get_company(identifier)

#### Lookup Company


Returns company reference and metadata such as tickers, CIK, and a unique company identifier, as well as company metadata such as business description, employee count, and company URL.

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

identifier = 'AAPL'

response = intrinio.CompanyApi().get_company(identifier)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Company identifier (Ticker, CIK, LEI, Intrinio ID) |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**Company**](Company.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:get_company_answers)

[//]: # (RETURN_TYPE:ApiResponseCompanyAnswers)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseCompanyAnswers.md)

[//]: # (OPERATION:get_company_answers_v2)

[//]: # (ENDPOINT:/companies/{identifier}/answers)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_company_answers)

## **get_company_answers**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_company_answers_v2)

[//]: # (START_OVERVIEW)

> ApiResponseCompanyAnswers get_company_answers(identifier, query)

#### Company Answers


Returns answers for a question about the Company with the given `identifier`

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

identifier = 'AAPL'
query = 'What do they believe in?'

response = intrinio.CompanyApi().get_company_answers(identifier, query)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Company identifier (Ticker, CIK, LEI, Intrinio ID) |   &nbsp;
 **query** | str| The query to ask the Thea API |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseCompanyAnswers**](ApiResponseCompanyAnswers.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:get_company_daily_metrics)

[//]: # (RETURN_TYPE:ApiResponseCompanyDailyMetrics)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseCompanyDailyMetrics.md)

[//]: # (OPERATION:get_company_daily_metrics_v2)

[//]: # (ENDPOINT:/companies/{identifier}/daily_metrics)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_company_daily_metrics)

## **get_company_daily_metrics**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_company_daily_metrics_v2)

[//]: # (START_OVERVIEW)

> ApiResponseCompanyDailyMetrics get_company_daily_metrics(identifier, on_date=on_date, page_size=page_size, next_page=next_page, next_page2=next_page2)

#### Company metrics by Company


Returns the latest company metrics.

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

identifier = 'AAPL'
on_date = '2013-10-20'
page_size = 100
next_page = ''
next_page2 = ''

response = intrinio.CompanyApi().get_company_daily_metrics(identifier, on_date=on_date, page_size=page_size, next_page=next_page, next_page2=next_page2)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Company identifier (Ticker, CIK, LEI, Intrinio ID) |   &nbsp;
 **on_date** | date| Date of the metric | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
 **next_page2** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseCompanyDailyMetrics**](ApiResponseCompanyDailyMetrics.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:get_company_data_point_number)

[//]: # (RETURN_TYPE:float)

[//]: # (RETURN_TYPE_KIND:primitive)

[//]: # (RETURN_TYPE_DOC:)

[//]: # (OPERATION:get_company_data_point_number_v2)

[//]: # (ENDPOINT:/companies/{identifier}/data_point/{tag}/number)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_company_data_point_number)

## **get_company_data_point_number**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_company_data_point_number_v2)

[//]: # (START_OVERVIEW)

> float get_company_data_point_number(identifier, tag)

#### Data Point (Number) for Company


Returns latest value for calculations, metrics, and financial data points for a company.

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

identifier = '$$v2_company_data_point_identifier_default$$'
tag = '$$v2_company_data_point_item_number_default$$'

response = intrinio.CompanyApi().get_company_data_point_number(identifier, tag)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| $$v2_company_data_point_identifier_description$$ |   &nbsp;
 **tag** | str| $$v2_company_data_point_item_description$$ |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

**float**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:get_company_data_point_text)

[//]: # (RETURN_TYPE:str)

[//]: # (RETURN_TYPE_KIND:primitive)

[//]: # (RETURN_TYPE_DOC:)

[//]: # (OPERATION:get_company_data_point_text_v2)

[//]: # (ENDPOINT:/companies/{identifier}/data_point/{tag}/text)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_company_data_point_text)

## **get_company_data_point_text**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_company_data_point_text_v2)

[//]: # (START_OVERVIEW)

> str get_company_data_point_text(identifier, tag)

#### Data Point (Text) for Company


Returns latest value for metadata items for a company.

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

identifier = '$$v2_company_data_point_identifier_default$$'
tag = '$$v2_company_data_point_item_text_default$$'

response = intrinio.CompanyApi().get_company_data_point_text(identifier, tag)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| $$v2_company_data_point_identifier_description$$ |   &nbsp;
 **tag** | str| $$v2_company_data_point_item_description$$ |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

**str**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:get_company_filings)

[//]: # (RETURN_TYPE:ApiResponseCompanyFilings)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseCompanyFilings.md)

[//]: # (OPERATION:get_company_filings_v2)

[//]: # (ENDPOINT:/companies/{identifier}/filings)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_company_filings)

## **get_company_filings**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_company_filings_v2)

[//]: # (START_OVERVIEW)

> ApiResponseCompanyFilings get_company_filings(identifier, report_type=report_type, start_date=start_date, end_date=end_date, thea_enabled=thea_enabled, page_size=page_size, next_page=next_page)

#### All Filings by Company


Returns a complete list of SEC filings for the Company with the given `identifier`

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

identifier = 'AAPL'
report_type = ''
start_date = '2015-01-01'
end_date = ''
thea_enabled = ''
page_size = 100
next_page = ''

response = intrinio.CompanyApi().get_company_filings(identifier, report_type=report_type, start_date=start_date, end_date=end_date, thea_enabled=thea_enabled, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Company identifier (Ticker, CIK, LEI, Intrinio ID) |   &nbsp;
 **report_type** | str| Filter by &lt;a href&#x3D;\&quot;https://docs.intrinio.com/documentation/sec_filing_report_types\&quot; target&#x3D;\&quot;_blank\&quot;&gt;report type&lt;/a&gt;. Separate values with commas to return multiple report types. | [optional]   &nbsp;
 **start_date** | date| Filed on or after the given date | [optional]   &nbsp;
 **end_date** | date| Filed before or after the given date | [optional]   &nbsp;
 **thea_enabled** | bool| Return filings that have been read by our Thea NLP and are ready for our answers endpoint | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseCompanyFilings**](ApiResponseCompanyFilings.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:get_company_fundamentals)

[//]: # (RETURN_TYPE:ApiResponseCompanyFundamentals)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseCompanyFundamentals.md)

[//]: # (OPERATION:get_company_fundamentals_v2)

[//]: # (ENDPOINT:/companies/{identifier}/fundamentals)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_company_fundamentals)

## **get_company_fundamentals**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_company_fundamentals_v2)

[//]: # (START_OVERVIEW)

> ApiResponseCompanyFundamentals get_company_fundamentals(identifier, filed_after=filed_after, filed_before=filed_before, reported_only=reported_only, fiscal_year=fiscal_year, statement_code=statement_code, type=type, fundamental_type=fundamental_type, start_date=start_date, end_date=end_date, updated_after=updated_after, latest_only=latest_only, updated_before=updated_before, page_size=page_size, next_page=next_page)

#### All Fundamentals by Company


Returns a list of fundamentals with unique fundamental IDs associated with a particular company. Useful to obtain all historical and/or latest fundamental IDs for a given company to then use to loop through and pull all fundamental data available.

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

identifier = 'AAPL'
filed_after = ''
filed_before = ''
reported_only = False
fiscal_year = ''
statement_code = ''
type = ''
fundamental_type = ''
start_date = ''
end_date = ''
updated_after = '2022-12-01'
latest_only = True
updated_before = '2022-12-01'
page_size = 100
next_page = ''

response = intrinio.CompanyApi().get_company_fundamentals(identifier, filed_after=filed_after, filed_before=filed_before, reported_only=reported_only, fiscal_year=fiscal_year, statement_code=statement_code, type=type, fundamental_type=fundamental_type, start_date=start_date, end_date=end_date, updated_after=updated_after, latest_only=latest_only, updated_before=updated_before, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Company identifier (Ticker, CIK, LEI, Intrinio ID) |   &nbsp;
 **filed_after** | date| Filed on or after this date | [optional]   &nbsp;
 **filed_before** | date| Filed on or before this date | [optional]   &nbsp;
 **reported_only** | bool| Only as-reported fundamentals | [optional]   &nbsp;
 **fiscal_year** | int| Only for the given fiscal year | [optional]   &nbsp;
 **statement_code** | str| Only of the given statement code | [optional]   &nbsp;
 **type** | str| Only of the given type | [optional]   &nbsp;
 **fundamental_type** | str| Only of the given fundamental type | [optional]   &nbsp;
 **start_date** | date| Only on or after the given date | [optional]   &nbsp;
 **end_date** | date| Only on or before the given date | [optional]   &nbsp;
 **updated_after** | date| Only include fundamentals where it was updated after this date. | [optional]   &nbsp;
 **latest_only** | bool| Only the most-recently reported fundamental for the period | [optional]   &nbsp;
 **updated_before** | date| Only include fundamentals where it was updated before this date. | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseCompanyFundamentals**](ApiResponseCompanyFundamentals.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:get_company_historical_data)

[//]: # (RETURN_TYPE:ApiResponseCompanyHistoricalData)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseCompanyHistoricalData.md)

[//]: # (OPERATION:get_company_historical_data_v2)

[//]: # (ENDPOINT:/companies/{identifier}/historical_data/{tag})

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_company_historical_data)

## **get_company_historical_data**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_company_historical_data_v2)

[//]: # (START_OVERVIEW)

> ApiResponseCompanyHistoricalData get_company_historical_data(identifier, tag, frequency=frequency, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)

#### Historical Data for Company


$$v2_company_historical_data_description$$

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

identifier = '$$v2_company_historical_data_identifier_default$$'
tag = '$$v2_company_historical_data_item_default$$'
frequency = 'daily'
type = ''
start_date = '2018-01-01'
end_date = ''
sort_order = 'desc'
page_size = 100
next_page = ''

response = intrinio.CompanyApi().get_company_historical_data(identifier, tag, frequency=frequency, type=type, start_date=start_date, end_date=end_date, sort_order=sort_order, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| $$v2_company_historical_data_identifier_description$$ |   &nbsp;
 **tag** | str| $$v2_company_historical_data_item_description$$ |   &nbsp;
 **frequency** | str| Return historical data in the given frequency | [optional] [default to daily]  &nbsp;
 **type** | str| Return historical data for given fiscal period type | [optional]   &nbsp;
 **start_date** | date| Return historical data on or after this date | [optional]   &nbsp;
 **end_date** | date| Return historical data on or before this date | [optional]   &nbsp;
 **sort_order** | str| Sort by date &#x60;asc&#x60; or &#x60;desc&#x60; | [optional] [default to desc]  &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseCompanyHistoricalData**](ApiResponseCompanyHistoricalData.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:get_company_ipos)

[//]: # (RETURN_TYPE:ApiResponseInitialPublicOfferings)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseInitialPublicOfferings.md)

[//]: # (OPERATION:get_company_ipos_v2)

[//]: # (ENDPOINT:/companies/ipos)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_company_ipos)

## **get_company_ipos**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_company_ipos_v2)

[//]: # (START_OVERVIEW)

> ApiResponseInitialPublicOfferings get_company_ipos(ticker=ticker, status=status, start_date=start_date, end_date=end_date, offer_amount_greater_than=offer_amount_greater_than, offer_amount_less_than=offer_amount_less_than, page_size=page_size, next_page=next_page)

#### IPOs


Returns a list of historical, current, and upcoming initial public offerings (IPOs) across the major US Exchanges. Includes relevant information such as the IPO status, the offer amount, the total share count and target share price.

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

ticker = 'UBER'
status = ''
start_date = ''
end_date = ''
offer_amount_greater_than = ''
offer_amount_less_than = ''
page_size = 100
next_page = ''

response = intrinio.CompanyApi().get_company_ipos(ticker=ticker, status=status, start_date=start_date, end_date=end_date, offer_amount_greater_than=offer_amount_greater_than, offer_amount_less_than=offer_amount_less_than, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | str| Return IPOs with the given ticker (typically the IPO for the company) | [optional]   &nbsp;
 **status** | str| Return IPOs with the given status. Upcoming IPOs are scheduled to occur in the future. Priced IPOs have occurred and the company should be trading publicly. Withdrawn IPOs were planned to occurr but were withdrawn beforehand | [optional]   &nbsp;
 **start_date** | date| Return IPOs on or after the given date | [optional]   &nbsp;
 **end_date** | date| Return IPOs on or before the given date | [optional]   &nbsp;
 **offer_amount_greater_than** | int| Return IPOs with an offer dollar amount greater than the given amount | [optional]   &nbsp;
 **offer_amount_less_than** | int| Return IPOs with an offer dollar amount less than the given amount | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseInitialPublicOfferings**](ApiResponseInitialPublicOfferings.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:get_company_news)

[//]: # (RETURN_TYPE:ApiResponseCompanyNews)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseCompanyNews.md)

[//]: # (OPERATION:get_company_news_v2)

[//]: # (ENDPOINT:/companies/{identifier}/news)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_company_news)

## **get_company_news**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_company_news_v2)

[//]: # (START_OVERVIEW)

> ApiResponseCompanyNews get_company_news(identifier, specific_source=specific_source, page_size=page_size, sentiment=sentiment, topic=topic, security=security, start_date=start_date, end_date=end_date, language=language, word_count_greater_than=word_count_greater_than, word_count_less_than=word_count_less_than, is_spam=is_spam, business_relevance_greater_than=business_relevance_greater_than, business_relevance_less_than=business_relevance_less_than, next_page=next_page)

#### All News by Company


Returns the latest and historical news article links, headlines and summaries for a specified US traded company.

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

identifier = 'AAPL'
specific_source = ''
page_size = 100
sentiment = ''
topic = ''
security = 'AAPL'
start_date = ''
end_date = ''
language = ''
word_count_greater_than = ''
word_count_less_than = ''
is_spam = ''
business_relevance_greater_than = ''
business_relevance_less_than = ''
next_page = ''

response = intrinio.CompanyApi().get_company_news(identifier, specific_source=specific_source, page_size=page_size, sentiment=sentiment, topic=topic, security=security, start_date=start_date, end_date=end_date, language=language, word_count_greater_than=word_count_greater_than, word_count_less_than=word_count_less_than, is_spam=is_spam, business_relevance_greater_than=business_relevance_greater_than, business_relevance_less_than=business_relevance_less_than, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Company identifier (Ticker, CIK, LEI, Intrinio ID) |   &nbsp;
 **specific_source** | str| Only news from this source. Defaults to highest available if not present. | [optional]   &nbsp;
 **page_size** | int| The maximum number of results to return | [optional] [default to 100]  &nbsp;
 **sentiment** | str| Filter by sentiment.  Unsupported for yahoo source. | [optional]   &nbsp;
 **topic** | str| Filter by topic.  Unsupported for yahoo source. | [optional]   &nbsp;
 **security** | str| Filter by &#x60;security&#x60; identifier (ticker, figi, isin, cusip, Intrinio ID).  Unsupported for yahoo source. | [optional]   &nbsp;
 **start_date** | date| Limit news stories to those on or after this date. Defaults to yesterday if unspecified. | [optional]   &nbsp;
 **end_date** | date| Limit news stories to those on or before this date | [optional]   &nbsp;
 **language** | str| Filter by language.  Unsupported for yahoo source. | [optional]   &nbsp;
 **word_count_greater_than** | int| News stories will have a word count greater than this value.  Unsupported for yahoo source. | [optional]   &nbsp;
 **word_count_less_than** | int| News stories will have a word count less than this value.  Unsupported for yahoo source. | [optional]   &nbsp;
 **is_spam** | bool| Filter whether it is marked as spam or not.  Unsupported for yahoo source. | [optional]   &nbsp;
 **business_relevance_greater_than** | float| News stories will have a business relevance score more than this value.  Unsupported for yahoo source. | [optional]   &nbsp;
 **business_relevance_less_than** | float| News stories will have a business relevance score less than this value.  Unsupported for yahoo source. | [optional]   &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseCompanyNews**](ApiResponseCompanyNews.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:get_company_news_body)

[//]: # (RETURN_TYPE:ApiResponseCompanyNewsBody)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseCompanyNewsBody.md)

[//]: # (OPERATION:get_company_news_body_v2)

[//]: # (ENDPOINT:/companies/news/body)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_company_news_body)

## **get_company_news_body**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_company_news_body_v2)

[//]: # (START_OVERVIEW)

> ApiResponseCompanyNewsBody get_company_news_body(news_story_id, publication_date, specific_source=specific_source, next_page=next_page)

#### News Article Body


Returns the body of a news article for moody sources.  This endpoint requires additional authorization beyond basic news access and is for your internal use only - no display. Please see a representative for details.

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

news_story_id = 'new_aBcDef'
publication_date = ''
specific_source = ''
next_page = ''

response = intrinio.CompanyApi().get_company_news_body(news_story_id, publication_date, specific_source=specific_source, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **news_story_id** | str| The identifier of the news story. |   &nbsp;
 **publication_date** | datetime| The DateTime of the story. |   &nbsp;
 **specific_source** | str| Only news from this source. Defaults to highest available if not present. | [optional]   &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseCompanyNewsBody**](ApiResponseCompanyNewsBody.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:get_company_public_float)

[//]: # (RETURN_TYPE:ApiResponseCompanyPublicFloatResult)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseCompanyPublicFloatResult.md)

[//]: # (OPERATION:get_company_public_float_v2)

[//]: # (ENDPOINT:/companies/{identifier}/public_float)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_company_public_float)

## **get_company_public_float**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_company_public_float_v2)

[//]: # (START_OVERVIEW)

> ApiResponseCompanyPublicFloatResult get_company_public_float(identifier, float_date_greater_than=float_date_greater_than, float_date_less_than=float_date_less_than, next_page=next_page, next_page2=next_page2)

#### Get Company's public float


Returns a list of public float data tied to a given company identifier.

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

identifier = 'AAPL'
float_date_greater_than = ''
float_date_less_than = ''
next_page = ''
next_page2 = ''

response = intrinio.CompanyApi().get_company_public_float(identifier, float_date_greater_than=float_date_greater_than, float_date_less_than=float_date_less_than, next_page=next_page, next_page2=next_page2)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Company identifier (Ticker, CIK, LEI, Intrinio ID) |   &nbsp;
 **float_date_greater_than** | date| The lower-bound date for the data being requested. | [optional]   &nbsp;
 **float_date_less_than** | date| The upper-bound date for the data being requested. | [optional]   &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
 **next_page2** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseCompanyPublicFloatResult**](ApiResponseCompanyPublicFloatResult.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:get_company_securities)

[//]: # (RETURN_TYPE:ApiResponseCompanySecurities)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseCompanySecurities.md)

[//]: # (OPERATION:get_company_securities_v2)

[//]: # (ENDPOINT:/companies/{identifier}/securities)

[//]: # (DOCUMENT_LINK:CompanyApi.md#get_company_securities)

## **get_company_securities**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_company_securities_v2)

[//]: # (START_OVERVIEW)

> ApiResponseCompanySecurities get_company_securities(identifier, next_page=next_page)

#### All Securities by Company


Returns a list of underlying securities with associated reference data tied to a given company identifier.

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

identifier = 'AAPL'
next_page = ''

response = intrinio.CompanyApi().get_company_securities(identifier, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Company identifier (Ticker, CIK, LEI, Intrinio ID) |   &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseCompanySecurities**](ApiResponseCompanySecurities.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:insider_transaction_filings_by_company)

[//]: # (RETURN_TYPE:ApiResponseInsiderTransactionFilings)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseInsiderTransactionFilings.md)

[//]: # (OPERATION:insider_transaction_filings_by_company_v2)

[//]: # (ENDPOINT:/companies/{identifier}/insider_transaction_filings)

[//]: # (DOCUMENT_LINK:CompanyApi.md#insider_transaction_filings_by_company)

## **insider_transaction_filings_by_company**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/insider_transaction_filings_by_company_v2)

[//]: # (START_OVERVIEW)

> ApiResponseInsiderTransactionFilings insider_transaction_filings_by_company(identifier, start_date=start_date, end_date=end_date, ownership_type=ownership_type, next_page=next_page, page_size=page_size, sort_by=sort_by, next_page2=next_page2)

#### Insider Transaction Filings by Company


Returns a list of all insider transaction filings in a company. Criteria for being an insider include being a director, officer, or 10%+ owner in the company. Transactions are detailed for both non-derivative and derivative transactions by the insider.

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

identifier = 'AAPL'
start_date = '2018-01-01'
end_date = '2019-01-01'
ownership_type = 'D'
next_page = ''
page_size = 1000
sort_by = 'updated_on'
next_page2 = ''

response = intrinio.CompanyApi().insider_transaction_filings_by_company(identifier, start_date=start_date, end_date=end_date, ownership_type=ownership_type, next_page=next_page, page_size=page_size, sort_by=sort_by, next_page2=next_page2)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Company identifier (Ticker, CIK, LEI, Intrinio ID) |   &nbsp;
 **start_date** | date| Return Company&#39;s insider transaction filings on or after this date | [optional]   &nbsp;
 **end_date** | date| Return Company&#39;s insider transaction filings on or before this date | [optional]   &nbsp;
 **ownership_type** | str| The type of ownership to return transaction filings for. &#39;D&#39; is for direct transactions. &#39;I&#39; is for indirect transactions. Omit for both types. | [optional]   &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 1000]  &nbsp;
 **sort_by** | str| The field to sort by.  Default is &#39;filing_date&#39;. | [optional]   &nbsp;
 **next_page2** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseInsiderTransactionFilings**](ApiResponseInsiderTransactionFilings.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:latest_insider_transaction_filing_by_company)

[//]: # (RETURN_TYPE:InsiderTransactionFiling)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:InsiderTransactionFiling.md)

[//]: # (OPERATION:latest_insider_transaction_filing_by_company_v2)

[//]: # (ENDPOINT:/companies/{identifier}/insider_transaction_filings/latest)

[//]: # (DOCUMENT_LINK:CompanyApi.md#latest_insider_transaction_filing_by_company)

## **latest_insider_transaction_filing_by_company**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/latest_insider_transaction_filing_by_company_v2)

[//]: # (START_OVERVIEW)

> InsiderTransactionFiling latest_insider_transaction_filing_by_company(identifier, next_page=next_page)

#### Latest Insider Transaction Filing by Company


Returns the latest insider transaction filing for a company.

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

identifier = 'AAPL'
next_page = ''

response = intrinio.CompanyApi().latest_insider_transaction_filing_by_company(identifier, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Company identifier (Ticker, CIK, LEI, Intrinio ID) |   &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**InsiderTransactionFiling**](InsiderTransactionFiling.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:lookup_company_fundamental)

[//]: # (RETURN_TYPE:Fundamental)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:Fundamental.md)

[//]: # (OPERATION:lookup_company_fundamental_v2)

[//]: # (ENDPOINT:/companies/{identifier}/fundamentals/lookup/{statement_code}/{fiscal_year}/{fiscal_period})

[//]: # (DOCUMENT_LINK:CompanyApi.md#lookup_company_fundamental)

## **lookup_company_fundamental**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/lookup_company_fundamental_v2)

[//]: # (START_OVERVIEW)

> Fundamental lookup_company_fundamental(identifier, statement_code, fiscal_period, fiscal_year)

#### Lookup Fundamental by Company


Returns the Fundamental for the Company with the given `identifier` and with the given parameters

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

identifier = 'AAPL'
statement_code = 'income_statement'
fiscal_period = 'FY'
fiscal_year = 2017

response = intrinio.CompanyApi().lookup_company_fundamental(identifier, statement_code, fiscal_period, fiscal_year)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Company identifier (Ticker, CIK, LEI, Intrinio ID) |   &nbsp;
 **statement_code** | str| The statement code |   &nbsp;
 **fiscal_period** | str| The fiscal period |   &nbsp;
 **fiscal_year** | int| The fiscal year |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**Fundamental**](Fundamental.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:recognize_company)

[//]: # (RETURN_TYPE:ApiResponseCompanyRecognize)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseCompanyRecognize.md)

[//]: # (OPERATION:recognize_company_v2)

[//]: # (ENDPOINT:/companies/recognize)

[//]: # (DOCUMENT_LINK:CompanyApi.md#recognize_company)

## **recognize_company**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/recognize_company_v2)

[//]: # (START_OVERVIEW)

> ApiResponseCompanyRecognize recognize_company(text)

#### Recognize Company


Returns a list of companies recognized by the Thea API in the given `text` query string parameter.

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

text = 'Apple'

response = intrinio.CompanyApi().recognize_company(text)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | str| The text sent to the Thea API to analyze |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseCompanyRecognize**](ApiResponseCompanyRecognize.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:search_companies)

[//]: # (RETURN_TYPE:ApiResponseCompaniesSearch)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseCompaniesSearch.md)

[//]: # (OPERATION:search_companies_v2)

[//]: # (ENDPOINT:/companies/search)

[//]: # (DOCUMENT_LINK:CompanyApi.md#search_companies)

## **search_companies**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/search_companies_v2)

[//]: # (START_OVERVIEW)

> ApiResponseCompaniesSearch search_companies(query, active=active, mode=mode, page_size=page_size)

#### Search Companies


Search the companies database and return a list of companies matching the text query parameter passed through. Query parameter searches across the company ticker and name.

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

query = 'Apple'
active = True
mode = ''
page_size = 100

response = intrinio.CompanyApi().search_companies(query, active=active, mode=mode, page_size=page_size)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | str| Search parameters |   &nbsp;
 **active** | bool| When True, return companies that are actively traded (having stock prices within the past 14 days). When False, return companies that are not actively traded or never have been traded. Not setting this value returns all. Not used when mode is set. | [optional]   &nbsp;
 **mode** | str| When set, changes search mode to the specified mode. | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseCompaniesSearch**](ApiResponseCompaniesSearch.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:CompanyApi)

[//]: # (METHOD:shares_outstanding_by_company)

[//]: # (RETURN_TYPE:ApiResponseCompanySharesOutstanding)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseCompanySharesOutstanding.md)

[//]: # (OPERATION:shares_outstanding_by_company_v2)

[//]: # (ENDPOINT:/companies/{identifier}/shares_outstanding)

[//]: # (DOCUMENT_LINK:CompanyApi.md#shares_outstanding_by_company)

## **shares_outstanding_by_company**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/shares_outstanding_by_company_v2)

[//]: # (START_OVERVIEW)

> ApiResponseCompanySharesOutstanding shares_outstanding_by_company(identifier, end_date_greater_than=end_date_greater_than, end_date_less_than=end_date_less_than)

#### Shares Outstanding by Company


Returns the shares outstanding reported on the front cover of the SEC 10-K and 10-Q filings.

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

identifier = 'AAPL'
end_date_greater_than = ''
end_date_less_than = ''

response = intrinio.CompanyApi().shares_outstanding_by_company(identifier, end_date_greater_than=end_date_greater_than, end_date_less_than=end_date_less_than)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Company identifier (Ticker, CIK, LEI, Intrinio ID) |   &nbsp;
 **end_date_greater_than** | date| Returns shares outstanding after this date. | [optional]   &nbsp;
 **end_date_less_than** | date| Returns shares outstanding before this date. | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseCompanySharesOutstanding**](ApiResponseCompanySharesOutstanding.md)

[//]: # (END_OPERATION)

