# intrinio_sdk.ZacksApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_zacks_analyst_ratings**](ZacksApi.md#get_zacks_analyst_ratings) | **GET** /zacks/analyst_ratings | Zacks Analyst Ratings
[**get_zacks_eps_surprises**](ZacksApi.md#get_zacks_eps_surprises) | **GET** /zacks/eps_surprises | Zacks EPS Surprises
[**get_zacks_sales_surprises**](ZacksApi.md#get_zacks_sales_surprises) | **GET** /zacks/sales_surprises | Zacks Sales Surprises



[//]: # (START_OPERATION)

[//]: # (CLASS:ZacksApi)

[//]: # (METHOD:get_zacks_analyst_ratings)

[//]: # (RETURN_TYPE:ApiResponseZacksAnalystRatings)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseZacksAnalystRatings.md)

[//]: # (OPERATION:get_zacks_analyst_ratings_v2)

[//]: # (ENDPOINT:/zacks/analyst_ratings)

[//]: # (DOCUMENT_LINK:ZacksApi.md#get_zacks_analyst_ratings)

## **get_zacks_analyst_ratings**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_zacks_analyst_ratings_v2)

[//]: # (START_OVERVIEW)

> ApiResponseZacksAnalystRatings get_zacks_analyst_ratings(identifier=identifier, start_date=start_date, end_date=end_date, mean_greater=mean_greater, mean_less=mean_less, strong_buys_greater=strong_buys_greater, strong_buys_less=strong_buys_less, buys_greater=buys_greater, buys_less=buys_less, holds_greater=holds_greater, holds_less=holds_less, sells_greater=sells_greater, sells_less=sells_less, strong_sells_greater=strong_sells_greater, strong_sells_less=strong_sells_less, total_greater=total_greater, total_less=total_less, page_size=page_size, next_page=next_page)

#### Zacks Analyst Ratings


Returns buy, sell, and hold recommendations from analysts at brokerages for all companies in the Zacks universe. Zack’s storied research team aggregates and validates the ratings from professional analysts.

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

zacks_api = intrinio_sdk.ZacksApi()

identifier = 'AAPL' # str | A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID) (optional)
start_date = '' # str | Limit ratings to those on or after this date (optional)
end_date = '' # str | Limit ratings to those on or before this date (optional)
mean_greater = "~null" # float | Return only records with a mean (average) higher than this value (optional)
mean_less = "~null" # float | Return only records with a mean (average) lower than this value (optional)
strong_buys_greater = "~null" # int | Return only records with more than this many Strong Buy recommendations (optional)
strong_buys_less = "~null" # int | Return only records with fewer than this many Strong Buy recommendations (optional)
buys_greater = "~null" # int | Return only records with more than this many Buy recommendations (optional)
buys_less = "~null" # int | Return only records with fewer than this many Buy recommendations (optional)
holds_greater = "~null" # int | Return only records with more than this many Hold recommendations (optional)
holds_less = "~null" # int | Return only records with fewer than this many Hold recommendations (optional)
sells_greater = "~null" # int | Return only records with more than this many Sell recommendations (optional)
sells_less = "~null" # int | Return only records with fewer than this many Sell recommendations (optional)
strong_sells_greater = "~null" # int | Return only records with more than this many Strong Sell recommendations (optional)
strong_sells_less = "~null" # int | Return only records with fewer than this many Strong Sell recommendations (optional)
total_greater = "~null" # int | Return only records with more than this many recommendations, regardless of type (optional)
total_less = "~null" # int | Return only records with fewer than this many recommendations, regardless of type (optional)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
  api_response = zacks_api.get_zacks_analyst_ratings(identifier=identifier, start_date=start_date, end_date=end_date, mean_greater=mean_greater, mean_less=mean_less, strong_buys_greater=strong_buys_greater, strong_buys_less=strong_buys_less, buys_greater=buys_greater, buys_less=buys_less, holds_greater=holds_greater, holds_less=holds_less, sells_greater=sells_greater, sells_less=sells_less, strong_sells_greater=strong_sells_greater, strong_sells_less=strong_sells_less, total_greater=total_greater, total_less=total_less, page_size=page_size, next_page=next_page)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling ZacksApi->get_zacks_analyst_ratings: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID) | [optional]   &nbsp;
 **start_date** | str| Limit ratings to those on or after this date | [optional]   &nbsp;
 **end_date** | str| Limit ratings to those on or before this date | [optional]   &nbsp;
 **mean_greater** | float| Return only records with a mean (average) higher than this value | [optional]   &nbsp;
 **mean_less** | float| Return only records with a mean (average) lower than this value | [optional]   &nbsp;
 **strong_buys_greater** | int| Return only records with more than this many Strong Buy recommendations | [optional]   &nbsp;
 **strong_buys_less** | int| Return only records with fewer than this many Strong Buy recommendations | [optional]   &nbsp;
 **buys_greater** | int| Return only records with more than this many Buy recommendations | [optional]   &nbsp;
 **buys_less** | int| Return only records with fewer than this many Buy recommendations | [optional]   &nbsp;
 **holds_greater** | int| Return only records with more than this many Hold recommendations | [optional]   &nbsp;
 **holds_less** | int| Return only records with fewer than this many Hold recommendations | [optional]   &nbsp;
 **sells_greater** | int| Return only records with more than this many Sell recommendations | [optional]   &nbsp;
 **sells_less** | int| Return only records with fewer than this many Sell recommendations | [optional]   &nbsp;
 **strong_sells_greater** | int| Return only records with more than this many Strong Sell recommendations | [optional]   &nbsp;
 **strong_sells_less** | int| Return only records with fewer than this many Strong Sell recommendations | [optional]   &nbsp;
 **total_greater** | int| Return only records with more than this many recommendations, regardless of type | [optional]   &nbsp;
 **total_less** | int| Return only records with fewer than this many recommendations, regardless of type | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseZacksAnalystRatings**](ApiResponseZacksAnalystRatings.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:ZacksApi)

[//]: # (METHOD:get_zacks_eps_surprises)

[//]: # (RETURN_TYPE:ApiResponseZacksEPSSurprises)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseZacksEPSSurprises.md)

[//]: # (OPERATION:get_zacks_eps_surprises_v2)

[//]: # (ENDPOINT:/zacks/eps_surprises)

[//]: # (DOCUMENT_LINK:ZacksApi.md#get_zacks_eps_surprises)

## **get_zacks_eps_surprises**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_zacks_eps_surprises_v2)

[//]: # (START_OVERVIEW)

> ApiResponseZacksEPSSurprises get_zacks_eps_surprises(start_date=start_date, end_date=end_date, eps_actual_greater=eps_actual_greater, eps_actual_less=eps_actual_less, eps_mean_estimate_greater=eps_mean_estimate_greater, eps_mean_estimate_less=eps_mean_estimate_less, eps_amount_diff_greater=eps_amount_diff_greater, eps_amount_diff_less=eps_amount_diff_less, eps_percent_diff_greater=eps_percent_diff_greater, eps_percent_diff_less=eps_percent_diff_less, eps_count_estimate_greater=eps_count_estimate_greater, eps_count_estimate_less=eps_count_estimate_less, eps_std_dev_estimate_greater=eps_std_dev_estimate_greater, eps_std_dev_estimate_less=eps_std_dev_estimate_less, page_size=page_size, next_page=next_page)

#### Zacks EPS Surprises


Returns Zacks eps surprise data for all Securities.

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

zacks_api = intrinio_sdk.ZacksApi()

start_date = '' # str | Limit EPS surprises to those on or after this date (optional)
end_date = '' # str | Limit EPS surprises to those on or before this date (optional)
eps_actual_greater = "~null" # float | Return only records with an actual EPS higher than this value (optional)
eps_actual_less = "~null" # float | Return only records with an actual EPS lower than this value (optional)
eps_mean_estimate_greater = "~null" # float | Return only records with an EPS mean estimate greater than this value (optional)
eps_mean_estimate_less = "~null" # float | Return only records with an EPS mean estimate lower than this value (optional)
eps_amount_diff_greater = "~null" # float | Return only records with an EPS amount difference greater than this value (optional)
eps_amount_diff_less = "~null" # float | Return only records with an EPS amount difference less than this value (optional)
eps_percent_diff_greater = "~null" # float | Return only records with an EPS percent difference greater than this value (optional)
eps_percent_diff_less = "~null" # float | Return only records with an EPS percent difference less than this value (optional)
eps_count_estimate_greater = "~null" # float | Return only records with an EPS count estimate greater than this value (optional)
eps_count_estimate_less = "~null" # float | Return only records with an EPS count estimate less than this value (optional)
eps_std_dev_estimate_greater = "~null" # float | Return only records with an EPS standard deviation greater than this value (optional)
eps_std_dev_estimate_less = "~null" # float | Return only records with an EPS standard deviation less than this value (optional)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
  api_response = zacks_api.get_zacks_eps_surprises(start_date=start_date, end_date=end_date, eps_actual_greater=eps_actual_greater, eps_actual_less=eps_actual_less, eps_mean_estimate_greater=eps_mean_estimate_greater, eps_mean_estimate_less=eps_mean_estimate_less, eps_amount_diff_greater=eps_amount_diff_greater, eps_amount_diff_less=eps_amount_diff_less, eps_percent_diff_greater=eps_percent_diff_greater, eps_percent_diff_less=eps_percent_diff_less, eps_count_estimate_greater=eps_count_estimate_greater, eps_count_estimate_less=eps_count_estimate_less, eps_std_dev_estimate_greater=eps_std_dev_estimate_greater, eps_std_dev_estimate_less=eps_std_dev_estimate_less, page_size=page_size, next_page=next_page)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling ZacksApi->get_zacks_eps_surprises: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | str| Limit EPS surprises to those on or after this date | [optional]   &nbsp;
 **end_date** | str| Limit EPS surprises to those on or before this date | [optional]   &nbsp;
 **eps_actual_greater** | float| Return only records with an actual EPS higher than this value | [optional]   &nbsp;
 **eps_actual_less** | float| Return only records with an actual EPS lower than this value | [optional]   &nbsp;
 **eps_mean_estimate_greater** | float| Return only records with an EPS mean estimate greater than this value | [optional]   &nbsp;
 **eps_mean_estimate_less** | float| Return only records with an EPS mean estimate lower than this value | [optional]   &nbsp;
 **eps_amount_diff_greater** | float| Return only records with an EPS amount difference greater than this value | [optional]   &nbsp;
 **eps_amount_diff_less** | float| Return only records with an EPS amount difference less than this value | [optional]   &nbsp;
 **eps_percent_diff_greater** | float| Return only records with an EPS percent difference greater than this value | [optional]   &nbsp;
 **eps_percent_diff_less** | float| Return only records with an EPS percent difference less than this value | [optional]   &nbsp;
 **eps_count_estimate_greater** | float| Return only records with an EPS count estimate greater than this value | [optional]   &nbsp;
 **eps_count_estimate_less** | float| Return only records with an EPS count estimate less than this value | [optional]   &nbsp;
 **eps_std_dev_estimate_greater** | float| Return only records with an EPS standard deviation greater than this value | [optional]   &nbsp;
 **eps_std_dev_estimate_less** | float| Return only records with an EPS standard deviation less than this value | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseZacksEPSSurprises**](ApiResponseZacksEPSSurprises.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:ZacksApi)

[//]: # (METHOD:get_zacks_sales_surprises)

[//]: # (RETURN_TYPE:ApiResponseZacksSalesSurprises)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseZacksSalesSurprises.md)

[//]: # (OPERATION:get_zacks_sales_surprises_v2)

[//]: # (ENDPOINT:/zacks/sales_surprises)

[//]: # (DOCUMENT_LINK:ZacksApi.md#get_zacks_sales_surprises)

## **get_zacks_sales_surprises**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_zacks_sales_surprises_v2)

[//]: # (START_OVERVIEW)

> ApiResponseZacksSalesSurprises get_zacks_sales_surprises(start_date=start_date, end_date=end_date, sales_actual_greater=sales_actual_greater, sales_actual_less=sales_actual_less, sales_mean_estimate_greater=sales_mean_estimate_greater, sales_mean_estimate_less=sales_mean_estimate_less, sales_amount_diff_greater=sales_amount_diff_greater, sales_amount_diff_less=sales_amount_diff_less, sales_percent_diff_greater=sales_percent_diff_greater, sales_percent_diff_less=sales_percent_diff_less, sales_count_estimate_greater=sales_count_estimate_greater, sales_count_estimate_less=sales_count_estimate_less, sales_std_dev_estimate_greater=sales_std_dev_estimate_greater, sales_std_dev_estimate_less=sales_std_dev_estimate_less, page_size=page_size, next_page=next_page)

#### Zacks Sales Surprises


Returns Zacks sales surprise data for all Securities.

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

zacks_api = intrinio_sdk.ZacksApi()

start_date = '' # str | Limit sales surprises to those on or after this date (optional)
end_date = '' # str | Limit sales surprises to those on or before this date (optional)
sales_actual_greater = "~null" # float | Return only records with an actual sales higher than this value (optional)
sales_actual_less = "~null" # float | Return only records with an actual sales lower than this value (optional)
sales_mean_estimate_greater = "~null" # float | Return only records with a sales mean estimate greater than this value (optional)
sales_mean_estimate_less = "~null" # float | Return only records with a sales mean estimate lower than this value (optional)
sales_amount_diff_greater = "~null" # float | Return only records with a sales amount difference greater than this value (optional)
sales_amount_diff_less = "~null" # float | Return only records with a sales amount difference less than this value (optional)
sales_percent_diff_greater = "~null" # float | Return only records with a sales percent difference greater than this value (optional)
sales_percent_diff_less = "~null" # float | Return only records with a sales percent difference less than this value (optional)
sales_count_estimate_greater = "~null" # float | Return only records with a sales count estimate greater than this value (optional)
sales_count_estimate_less = "~null" # float | Return only records with a sales count estimate less than this value (optional)
sales_std_dev_estimate_greater = "~null" # float | Return only records with a sales standard deviation greater than this value (optional)
sales_std_dev_estimate_less = "~null" # float | Return only records with a sales standard deviation less than this value (optional)
page_size = 100 # int | The number of results to return (optional) (default to 100)
next_page = '' # str | Gets the next page of data from a previous API call (optional)

try:
  api_response = zacks_api.get_zacks_sales_surprises(start_date=start_date, end_date=end_date, sales_actual_greater=sales_actual_greater, sales_actual_less=sales_actual_less, sales_mean_estimate_greater=sales_mean_estimate_greater, sales_mean_estimate_less=sales_mean_estimate_less, sales_amount_diff_greater=sales_amount_diff_greater, sales_amount_diff_less=sales_amount_diff_less, sales_percent_diff_greater=sales_percent_diff_greater, sales_percent_diff_less=sales_percent_diff_less, sales_count_estimate_greater=sales_count_estimate_greater, sales_count_estimate_less=sales_count_estimate_less, sales_std_dev_estimate_greater=sales_std_dev_estimate_greater, sales_std_dev_estimate_less=sales_std_dev_estimate_less, page_size=page_size, next_page=next_page)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling ZacksApi->get_zacks_sales_surprises: %s\n" % e)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(api_response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | str| Limit sales surprises to those on or after this date | [optional]   &nbsp;
 **end_date** | str| Limit sales surprises to those on or before this date | [optional]   &nbsp;
 **sales_actual_greater** | float| Return only records with an actual sales higher than this value | [optional]   &nbsp;
 **sales_actual_less** | float| Return only records with an actual sales lower than this value | [optional]   &nbsp;
 **sales_mean_estimate_greater** | float| Return only records with a sales mean estimate greater than this value | [optional]   &nbsp;
 **sales_mean_estimate_less** | float| Return only records with a sales mean estimate lower than this value | [optional]   &nbsp;
 **sales_amount_diff_greater** | float| Return only records with a sales amount difference greater than this value | [optional]   &nbsp;
 **sales_amount_diff_less** | float| Return only records with a sales amount difference less than this value | [optional]   &nbsp;
 **sales_percent_diff_greater** | float| Return only records with a sales percent difference greater than this value | [optional]   &nbsp;
 **sales_percent_diff_less** | float| Return only records with a sales percent difference less than this value | [optional]   &nbsp;
 **sales_count_estimate_greater** | float| Return only records with a sales count estimate greater than this value | [optional]   &nbsp;
 **sales_count_estimate_less** | float| Return only records with a sales count estimate less than this value | [optional]   &nbsp;
 **sales_std_dev_estimate_greater** | float| Return only records with a sales standard deviation greater than this value | [optional]   &nbsp;
 **sales_std_dev_estimate_less** | float| Return only records with a sales standard deviation less than this value | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseZacksSalesSurprises**](ApiResponseZacksSalesSurprises.md)

[//]: # (END_OPERATION)

