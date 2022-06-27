# intrinio_sdk.FilingApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_filings**](FilingApi.md#get_all_filings) | **GET** /filings | All Filings
[**get_all_notes**](FilingApi.md#get_all_notes) | **GET** /filings/notes | All Filing Notes
[**get_filing_answers**](FilingApi.md#get_filing_answers) | **GET** /filings/{identifier}/answers | Filing Answers
[**get_filing_by_id**](FilingApi.md#get_filing_by_id) | **GET** /filings/{id} | Lookup Filing
[**get_filing_fundamentals**](FilingApi.md#get_filing_fundamentals) | **GET** /filings/{identifier}/fundamentals | All Fundamentals by Filing
[**get_filing_html**](FilingApi.md#get_filing_html) | **GET** /filings/{identifier}/html | Filing Html
[**get_filing_text**](FilingApi.md#get_filing_text) | **GET** /filings/{identifier}/text | Filing Text
[**get_note**](FilingApi.md#get_note) | **GET** /filings/notes/{identifier} | Filing Note by ID
[**get_note_html**](FilingApi.md#get_note_html) | **GET** /filings/notes/{identifier}/html | Filing Note HTML
[**get_note_text**](FilingApi.md#get_note_text) | **GET** /filings/notes/{identifier}/text | Filing Note Text
[**search_notes**](FilingApi.md#search_notes) | **GET** /filings/notes/search | Search Filing Notes



[//]: # (START_OPERATION)

[//]: # (CLASS:FilingApi)

[//]: # (METHOD:get_all_filings)

[//]: # (RETURN_TYPE:ApiResponseFilings)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseFilings.md)

[//]: # (OPERATION:get_all_filings_v2)

[//]: # (ENDPOINT:/filings)

[//]: # (DOCUMENT_LINK:FilingApi.md#get_all_filings)

## **get_all_filings**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_all_filings_v2)

[//]: # (START_OVERVIEW)

> ApiResponseFilings get_all_filings(company=company, report_type=report_type, start_date=start_date, end_date=end_date, industry_category=industry_category, industry_group=industry_group, thea_enabled=thea_enabled, page_size=page_size, next_page=next_page)

#### All Filings


Returns pertinent filing reference data for a specific company filing or latest filings for all companies. Useful for tracking the latest filings submitted and updating your database accordingly with the new information.

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

company = 'AAPL'
report_type = '10-Q'
start_date = '2015-01-01'
end_date = ''
industry_category = ''
industry_group = ''
thea_enabled = ''
page_size = 100
next_page = ''

response = intrinio.FilingApi().get_all_filings(company=company, report_type=report_type, start_date=start_date, end_date=end_date, industry_category=industry_category, industry_group=industry_group, thea_enabled=thea_enabled, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company** | str| Filings for the given &#x60;company&#x60; identifier (ticker, CIK, LEI, Intrinio ID) | [optional]   &nbsp;
 **report_type** | str| Filter by report type. Separate values with commas to return multiple The filing &lt;a href&#x3D;\&quot;https://docs.intrinio.com/documentation/sec_filing_report_types\&quot; target&#x3D;\&quot;_blank\&quot;&gt;report types&lt;/a&gt;. | [optional]   &nbsp;
 **start_date** | date| Filed on or after the given date | [optional]   &nbsp;
 **end_date** | date| Filed before or after the given date | [optional]   &nbsp;
 **industry_category** | str| Return companies in the given industry category | [optional]   &nbsp;
 **industry_group** | str| Return companies in the given industry group | [optional]   &nbsp;
 **thea_enabled** | bool| Return filings that have been read by our Thea NLP and are ready for our answers endpoint | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseFilings**](ApiResponseFilings.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:FilingApi)

[//]: # (METHOD:get_all_notes)

[//]: # (RETURN_TYPE:ApiResponseFilingNotes)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseFilingNotes.md)

[//]: # (OPERATION:get_all_notes_v2)

[//]: # (ENDPOINT:/filings/notes)

[//]: # (DOCUMENT_LINK:FilingApi.md#get_all_notes)

## **get_all_notes**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_all_notes_v2)

[//]: # (START_OVERVIEW)

> ApiResponseFilingNotes get_all_notes(company=company, report_type=report_type, filing_start_date=filing_start_date, filing_end_date=filing_end_date, period_ended_start_date=period_ended_start_date, period_ended_end_date=period_ended_end_date, page_size=page_size, next_page=next_page)

#### All Filing Notes


Returns a list of the latest XBRL filing note sections from the SEC 10-K and 10-Q statements. The returned Intrinio XBRL filing note ID can then be utilized with the “Filing Note by ID” endpoint to retrieve the contents of the note in HTML or text format.

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

company = 'AAPL'
report_type = '10-Q'
filing_start_date = ''
filing_end_date = ''
period_ended_start_date = ''
period_ended_end_date = ''
page_size = 100
next_page = ''

response = intrinio.FilingApi().get_all_notes(company=company, report_type=report_type, filing_start_date=filing_start_date, filing_end_date=filing_end_date, period_ended_start_date=period_ended_start_date, period_ended_end_date=period_ended_end_date, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company** | str| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | [optional]   &nbsp;
 **report_type** | str| Notes contained in filings that match the given &lt;a href&#x3D;\&quot;https://docs.intrinio.com/documentation/sec_filing_report_types\&quot; target&#x3D;\&quot;_blank\&quot;&gt;report type&lt;/a&gt; | [optional]   &nbsp;
 **filing_start_date** | date| Limit search to filings on or after this date | [optional]   &nbsp;
 **filing_end_date** | date| Limit search to filings on or before this date | [optional]   &nbsp;
 **period_ended_start_date** | date| Limit search to filings with a period end date on or after this date | [optional]   &nbsp;
 **period_ended_end_date** | date| Limit search to filings with a period end date on or before this date | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseFilingNotes**](ApiResponseFilingNotes.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:FilingApi)

[//]: # (METHOD:get_filing_answers)

[//]: # (RETURN_TYPE:ApiResponseFilingAnswers)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseFilingAnswers.md)

[//]: # (OPERATION:get_filing_answers_v2)

[//]: # (ENDPOINT:/filings/{identifier}/answers)

[//]: # (DOCUMENT_LINK:FilingApi.md#get_filing_answers)

## **get_filing_answers**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_filing_answers_v2)

[//]: # (START_OVERVIEW)

> ApiResponseFilingAnswers get_filing_answers(identifier, query)

#### Filing Answers



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

identifier = 'fil_B73xBG'
query = 'What do they believe in?'

response = intrinio.FilingApi().get_filing_answers(identifier, query)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Filing identifier |   &nbsp;
 **query** | str| The query to ask the Thea API |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseFilingAnswers**](ApiResponseFilingAnswers.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:FilingApi)

[//]: # (METHOD:get_filing_by_id)

[//]: # (RETURN_TYPE:Filing)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:Filing.md)

[//]: # (OPERATION:get_filing_by_id_v2)

[//]: # (ENDPOINT:/filings/{id})

[//]: # (DOCUMENT_LINK:FilingApi.md#get_filing_by_id)

## **get_filing_by_id**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_filing_by_id_v2)

[//]: # (START_OVERVIEW)

> Filing get_filing_by_id(id)

#### Lookup Filing


Returns the Filing with the given `identifier`

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

id = 'fil_7Kn2P6'

response = intrinio.FilingApi().get_filing_by_id(id)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | str| The Intrinio ID of the Filing |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**Filing**](Filing.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:FilingApi)

[//]: # (METHOD:get_filing_fundamentals)

[//]: # (RETURN_TYPE:ApiResponseFilingFundamentals)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseFilingFundamentals.md)

[//]: # (OPERATION:get_filing_fundamentals_v2)

[//]: # (ENDPOINT:/filings/{identifier}/fundamentals)

[//]: # (DOCUMENT_LINK:FilingApi.md#get_filing_fundamentals)

## **get_filing_fundamentals**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_filing_fundamentals_v2)

[//]: # (START_OVERVIEW)

> ApiResponseFilingFundamentals get_filing_fundamentals(identifier, statement_code=statement_code, type=type, fiscal_year=fiscal_year, fiscal_period=fiscal_period, start_date=start_date, end_date=end_date, next_page=next_page)

#### All Fundamentals by Filing


Returns a list of fundamentals with unique fundamental IDs associated with a particular `Intrinio Filing ID` (if applicable) that have been updated or created as a result of a company`s latest SEC filing. Useful to ensure your database is up to date with the latest fundamentals.

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

identifier = 'fil_B73xBG'
statement_code = ''
type = ''
fiscal_year = ''
fiscal_period = ''
start_date = ''
end_date = ''
next_page = ''

response = intrinio.FilingApi().get_filing_fundamentals(identifier, statement_code=statement_code, type=type, fiscal_year=fiscal_year, fiscal_period=fiscal_period, start_date=start_date, end_date=end_date, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Filing identifier |   &nbsp;
 **statement_code** | str| Filters fundamentals by statement code | [optional]   &nbsp;
 **type** | str| Filters fundamentals by type | [optional]   &nbsp;
 **fiscal_year** | int| Filters fundamentals by fiscal year | [optional]   &nbsp;
 **fiscal_period** | str| Filters fundamentals by fiscal period | [optional]   &nbsp;
 **start_date** | date| Returns fundamentals on or after the given date | [optional]   &nbsp;
 **end_date** | date| Returns fundamentals on or before the given date | [optional]   &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseFilingFundamentals**](ApiResponseFilingFundamentals.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:FilingApi)

[//]: # (METHOD:get_filing_html)

[//]: # (RETURN_TYPE:str)

[//]: # (RETURN_TYPE_KIND:primitive)

[//]: # (RETURN_TYPE_DOC:)

[//]: # (OPERATION:get_filing_html_v2)

[//]: # (ENDPOINT:/filings/{identifier}/html)

[//]: # (DOCUMENT_LINK:FilingApi.md#get_filing_html)

## **get_filing_html**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_filing_html_v2)

[//]: # (START_OVERVIEW)

> str get_filing_html(identifier)

#### Filing Html


Returns a SEC filing in HTML Format for a specified filing ID.

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

identifier = 'fil_B73xBG'

response = intrinio.FilingApi().get_filing_html(identifier)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Filing identifier |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

**str**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:FilingApi)

[//]: # (METHOD:get_filing_text)

[//]: # (RETURN_TYPE:str)

[//]: # (RETURN_TYPE_KIND:primitive)

[//]: # (RETURN_TYPE_DOC:)

[//]: # (OPERATION:get_filing_text_v2)

[//]: # (ENDPOINT:/filings/{identifier}/text)

[//]: # (DOCUMENT_LINK:FilingApi.md#get_filing_text)

## **get_filing_text**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_filing_text_v2)

[//]: # (START_OVERVIEW)

> str get_filing_text(identifier)

#### Filing Text



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

identifier = 'fil_B73xBG'

response = intrinio.FilingApi().get_filing_text(identifier)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Filing identifier |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

**str**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:FilingApi)

[//]: # (METHOD:get_note)

[//]: # (RETURN_TYPE:FilingNote)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:FilingNote.md)

[//]: # (OPERATION:get_note_v2)

[//]: # (ENDPOINT:/filings/notes/{identifier})

[//]: # (DOCUMENT_LINK:FilingApi.md#get_note)

## **get_note**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_note_v2)

[//]: # (START_OVERVIEW)

> FilingNote get_note(identifier, content_format=content_format)

#### Filing Note by ID


Returns the XBRL filing note contents in HTML or text format for a specified Intrinio XBRL filing note ID.

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

identifier = 'xbn_ydK3QL'
content_format = 'text'

response = intrinio.FilingApi().get_note(identifier, content_format=content_format)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| The Intrinio ID of the filing note |   &nbsp;
 **content_format** | str| Returns content in html (as filed) or plain text | [optional] [default to text]  &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**FilingNote**](FilingNote.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:FilingApi)

[//]: # (METHOD:get_note_html)

[//]: # (RETURN_TYPE:str)

[//]: # (RETURN_TYPE_KIND:primitive)

[//]: # (RETURN_TYPE_DOC:)

[//]: # (OPERATION:get_note_html_v2)

[//]: # (ENDPOINT:/filings/notes/{identifier}/html)

[//]: # (DOCUMENT_LINK:FilingApi.md#get_note_html)

## **get_note_html**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_note_html_v2)

[//]: # (START_OVERVIEW)

> str get_note_html(identifier)

#### Filing Note HTML



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

identifier = 'xbn_ydK3QL'

response = intrinio.FilingApi().get_note_html(identifier)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| The Intrinio ID of the filing note |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

**str**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:FilingApi)

[//]: # (METHOD:get_note_text)

[//]: # (RETURN_TYPE:str)

[//]: # (RETURN_TYPE_KIND:primitive)

[//]: # (RETURN_TYPE_DOC:)

[//]: # (OPERATION:get_note_text_v2)

[//]: # (ENDPOINT:/filings/notes/{identifier}/text)

[//]: # (DOCUMENT_LINK:FilingApi.md#get_note_text)

## **get_note_text**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_note_text_v2)

[//]: # (START_OVERVIEW)

> str get_note_text(identifier)

#### Filing Note Text



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

identifier = 'xbn_ydK3QL'

response = intrinio.FilingApi().get_note_text(identifier)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| The Intrinio ID of the filing note |   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

**str**

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:FilingApi)

[//]: # (METHOD:search_notes)

[//]: # (RETURN_TYPE:ApiResponseFilingNotesSearch)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseFilingNotesSearch.md)

[//]: # (OPERATION:search_notes_v2)

[//]: # (ENDPOINT:/filings/notes/search)

[//]: # (DOCUMENT_LINK:FilingApi.md#search_notes)

## **search_notes**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/search_notes_v2)

[//]: # (START_OVERVIEW)

> ApiResponseFilingNotesSearch search_notes(query, filing_start_date=filing_start_date, filing_end_date=filing_end_date, page_size=page_size)

#### Search Filing Notes


Search the XBRL note database and return a list of XBRL note sections containing text from the text query parameter passed through.

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

query = 'inflation'
filing_start_date = '2018-07-15'
filing_end_date = '2018-11-30'
page_size = 100

response = intrinio.FilingApi().search_notes(query, filing_start_date=filing_start_date, filing_end_date=filing_end_date, page_size=page_size)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | str| Search for notes that contain all or parts of this text |   &nbsp;
 **filing_start_date** | date| Limit search to filings on or after this date | [optional]   &nbsp;
 **filing_end_date** | date| Limit search to filings on or before this date | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseFilingNotesSearch**](ApiResponseFilingNotesSearch.md)

[//]: # (END_OPERATION)

