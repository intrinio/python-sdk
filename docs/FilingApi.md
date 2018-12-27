# intrinio_sdk.FilingApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_filings**](FilingApi.md#filter_filings) | **GET** /filings/filter | Filter Filings
[**filter_notes**](FilingApi.md#filter_notes) | **GET** /filings/notes/filter | Filter SEC filing notes
[**get_all_filings**](FilingApi.md#get_all_filings) | **GET** /filings | All Filings
[**get_all_notes**](FilingApi.md#get_all_notes) | **GET** /filings/notes | Get All SEC filing notes
[**get_filing_by_id**](FilingApi.md#get_filing_by_id) | **GET** /filings/{id} | Lookup Filing
[**get_note**](FilingApi.md#get_note) | **GET** /filings/notes/{identifier} | Get an SEC filing note by ID
[**get_note_html**](FilingApi.md#get_note_html) | **GET** /filings/notes/{identifier}/html | Returns the content of an SEC filing note as originally filed
[**get_note_text**](FilingApi.md#get_note_text) | **GET** /filings/notes/{identifier}/text | Returns the content of an SEC filing note stripped of HTML
[**search_notes**](FilingApi.md#search_notes) | **GET** /filings/notes/search | Search Filing Notes


# **filter_filings**
> ApiResponseFilings filter_filings(company, report_type=report_type, start_date=start_date, end_date=end_date, next_page=next_page)

Filter Filings

Returns Filings that match the specified filters

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

filing_api = intrinio_sdk.FilingApi()

company = 'AAPL' # str | Filings for the given `company` identifier (ticker, CIK, LEI, Intrinio ID)
report_type = '' # str | Filter by report type (optional)
start_date = '2015-01-01' # date | Filed on or after the given date (optional)
end_date = '2019-01-01' # date | Filed before or after the given date (optional)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = filing_api.filter_filings(company, report_type=report_type, start_date=start_date, end_date=end_date, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilingApi->filter_filings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company** | **str**| Filings for the given &#x60;company&#x60; identifier (ticker, CIK, LEI, Intrinio ID) | 
 **report_type** | **str**| Filter by report type | [optional] 
 **start_date** | **date**| Filed on or after the given date | [optional] 
 **end_date** | **date**| Filed before or after the given date | [optional] 
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseFilings**](ApiResponseFilings.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filter_notes**
> ApiResponseFilingNotes filter_notes(company=company, report_type=report_type, filing_start_date=filing_start_date, filing_end_date=filing_end_date, period_ended_start_date=period_ended_start_date, period_ended_end_date=period_ended_end_date, next_page=next_page)

Filter SEC filing notes

Returns SEC filing notes matching the supplied criteria

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

filing_api = intrinio_sdk.FilingApi()

company = 'AAPL' # str | A Company identifier (Ticker, CIK, LEI, Intrinio ID) (optional)
report_type = '10-Q' # str | Notes contained in filings that match the given report type (optional)
filing_start_date = '2018-07-15' # date | Limit search to filings on or after this date (optional)
filing_end_date = '2018-11-15' # date | Limit search to filings on or before this date (optional)
period_ended_start_date = '2018-07-15' # date | Limit search to filings with a period end date on or after this date (optional)
period_ended_end_date = '2018-11-15' # date | Limit search to filings with a period end date on or before this date (optional)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = filing_api.filter_notes(company=company, report_type=report_type, filing_start_date=filing_start_date, filing_end_date=filing_end_date, period_ended_start_date=period_ended_start_date, period_ended_end_date=period_ended_end_date, next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilingApi->filter_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company** | **str**| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | [optional] 
 **report_type** | **str**| Notes contained in filings that match the given report type | [optional] 
 **filing_start_date** | **date**| Limit search to filings on or after this date | [optional] 
 **filing_end_date** | **date**| Limit search to filings on or before this date | [optional] 
 **period_ended_start_date** | **date**| Limit search to filings with a period end date on or after this date | [optional] 
 **period_ended_end_date** | **date**| Limit search to filings with a period end date on or before this date | [optional] 
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseFilingNotes**](ApiResponseFilingNotes.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_filings**
> ApiResponseFilings get_all_filings(next_page=next_page)

All Filings

Returns all Filings

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

filing_api = intrinio_sdk.FilingApi()

next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = filing_api.get_all_filings(next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilingApi->get_all_filings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseFilings**](ApiResponseFilings.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_notes**
> ApiResponseFilingNotes get_all_notes(next_page=next_page)

Get All SEC filing notes

Return All notes from SEC Filings, most-recent first

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

filing_api = intrinio_sdk.FilingApi()

next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
    api_response = filing_api.get_all_notes(next_page=next_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilingApi->get_all_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_page** | **str**| Gets the next page of data from a previous API call | [optional] 

### Return type

[**ApiResponseFilingNotes**](ApiResponseFilingNotes.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filing_by_id**
> Filing get_filing_by_id(id)

Lookup Filing

Returns the Filing with the given `identifier`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

filing_api = intrinio_sdk.FilingApi()

id = 'fil_7Kn2P6' # str | The Intrinio ID of the Filing

try:
    api_response = filing_api.get_filing_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilingApi->get_filing_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Intrinio ID of the Filing | 

### Return type

[**Filing**](Filing.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_note**
> FilingNote get_note(identifier, content_format=content_format)

Get an SEC filing note by ID

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

filing_api = intrinio_sdk.FilingApi()

identifier = 'xbn_3fghz' # str | The Intrinio ID of the filing note
content_format = 'text' # str | Returns content in html (as filed) or plain text (optional) (default to text)

try:
    api_response = filing_api.get_note(identifier, content_format=content_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilingApi->get_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The Intrinio ID of the filing note | 
 **content_format** | **str**| Returns content in html (as filed) or plain text | [optional] [default to text]

### Return type

[**FilingNote**](FilingNote.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_note_html**
> str get_note_html(identifier)

Returns the content of an SEC filing note as originally filed

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

filing_api = intrinio_sdk.FilingApi()

identifier = 'xbn_3fghz' # str | The Intrinio ID of the filing note

try:
    api_response = filing_api.get_note_html(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilingApi->get_note_html: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The Intrinio ID of the filing note | 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_note_text**
> str get_note_text(identifier)

Returns the content of an SEC filing note stripped of HTML

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

filing_api = intrinio_sdk.FilingApi()

identifier = 'xbn_3fghz' # str | The Intrinio ID of the filing note

try:
    api_response = filing_api.get_note_text(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilingApi->get_note_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The Intrinio ID of the filing note | 

### Return type

**str**

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_notes**
> ApiResponseFilingNotesSearch search_notes(query, filing_start_date=filing_start_date, filing_end_date=filing_end_date, page_size=page_size)

Search Filing Notes

Searches SEC filing notes using the text in `query`

### Example
```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

filing_api = intrinio_sdk.FilingApi()

query = 'inflation' # str | Search for notes that contain all or parts of this text
filing_start_date = '2018-07-15' # date | Limit search to filings on or after this date (optional)
filing_end_date = '2018-11-30' # date | Limit search to filings on or before this date (optional)
page_size = 100 # float | The number of results to return (optional) (default to 100)

try:
    api_response = filing_api.search_notes(query, filing_start_date=filing_start_date, filing_end_date=filing_end_date, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilingApi->search_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search for notes that contain all or parts of this text | 
 **filing_start_date** | **date**| Limit search to filings on or after this date | [optional] 
 **filing_end_date** | **date**| Limit search to filings on or before this date | [optional] 
 **page_size** | **float**| The number of results to return | [optional] [default to 100]

### Return type

[**ApiResponseFilingNotesSearch**](ApiResponseFilingNotesSearch.md)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

