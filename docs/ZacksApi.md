# intrinio_sdk.ZacksApi

All URIs are relative to *https://api-v2.intrinio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_zacks_analyst_ratings**](ZacksApi.md#get_zacks_analyst_ratings) | **GET** /zacks/analyst_ratings | Zacks Analyst Ratings
[**get_zacks_eps_estimates**](ZacksApi.md#get_zacks_eps_estimates) | **GET** /zacks/eps_estimates | Zacks EPS Estimates
[**get_zacks_eps_growth_rates**](ZacksApi.md#get_zacks_eps_growth_rates) | **GET** /zacks/eps_growth_rates | Zacks EPS Growth Rates
[**get_zacks_eps_surprises**](ZacksApi.md#get_zacks_eps_surprises) | **GET** /zacks/eps_surprises | Zacks EPS Surprises
[**get_zacks_etf_holdings**](ZacksApi.md#get_zacks_etf_holdings) | **GET** /zacks/etf_holdings | Zacks ETF Holdings
[**get_zacks_institutional_holding_companies**](ZacksApi.md#get_zacks_institutional_holding_companies) | **GET** /zacks/institutional_holdings/companies | Zacks Institutional Holding Companies
[**get_zacks_institutional_holding_owners**](ZacksApi.md#get_zacks_institutional_holding_owners) | **GET** /zacks/institutional_holdings/owners | Zacks Institutional Holding Owners
[**get_zacks_institutional_holdings**](ZacksApi.md#get_zacks_institutional_holdings) | **GET** /zacks/institutional_holdings | Zacks Institutional Holdings
[**get_zacks_long_term_growth_rates**](ZacksApi.md#get_zacks_long_term_growth_rates) | **GET** /zacks/long_term_growth_rates | Zacks Long Term Growth Rates
[**get_zacks_sales_surprises**](ZacksApi.md#get_zacks_sales_surprises) | **GET** /zacks/sales_surprises | Zacks Sales Surprises
[**get_zacks_target_price_consensuses**](ZacksApi.md#get_zacks_target_price_consensuses) | **GET** /zacks/target_price_consensuses | Zacks Target Price Consensuses



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
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

identifier = 'AAPL'
start_date = ''
end_date = ''
mean_greater = ''
mean_less = ''
strong_buys_greater = ''
strong_buys_less = ''
buys_greater = ''
buys_less = ''
holds_greater = ''
holds_less = ''
sells_greater = ''
sells_less = ''
strong_sells_greater = ''
strong_sells_less = ''
total_greater = ''
total_less = ''
page_size = 100
next_page = ''

response = intrinio.ZacksApi().get_zacks_analyst_ratings(identifier=identifier, start_date=start_date, end_date=end_date, mean_greater=mean_greater, mean_less=mean_less, strong_buys_greater=strong_buys_greater, strong_buys_less=strong_buys_less, buys_greater=buys_greater, buys_less=buys_less, holds_greater=holds_greater, holds_less=holds_less, sells_greater=sells_greater, sells_less=sells_less, strong_sells_greater=strong_sells_greater, strong_sells_less=strong_sells_less, total_greater=total_greater, total_less=total_less, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID) | [optional]   &nbsp;
 **start_date** | date| Limit ratings to those on or after this date | [optional]   &nbsp;
 **end_date** | date| Limit ratings to those on or before this date | [optional]   &nbsp;
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

[//]: # (METHOD:get_zacks_eps_estimates)

[//]: # (RETURN_TYPE:ApiResponseZacksEPSEstimates)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseZacksEPSEstimates.md)

[//]: # (OPERATION:get_zacks_eps_estimates_v2)

[//]: # (ENDPOINT:/zacks/eps_estimates)

[//]: # (DOCUMENT_LINK:ZacksApi.md#get_zacks_eps_estimates)

## **get_zacks_eps_estimates**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_zacks_eps_estimates_v2)

[//]: # (START_OVERVIEW)

> ApiResponseZacksEPSEstimates get_zacks_eps_estimates(identifier=identifier, start_date=start_date, end_date=end_date, fiscal_year=fiscal_year, fiscal_period=fiscal_period, calendar_year=calendar_year, calendar_period=calendar_period, page_size=page_size, next_page=next_page)

#### Zacks EPS Estimates


Returns Zacks consensus earnings-per-share (EPS) data for all Companies.

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

identifier = 'AAPL'
start_date = ''
end_date = ''
fiscal_year = ''
fiscal_period = ''
calendar_year = ''
calendar_period = ''
page_size = 100
next_page = ''

response = intrinio.ZacksApi().get_zacks_eps_estimates(identifier=identifier, start_date=start_date, end_date=end_date, fiscal_year=fiscal_year, fiscal_period=fiscal_period, calendar_year=calendar_year, calendar_period=calendar_period, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Company identifier (Ticker, CIK, LEI, Intrinio ID) | [optional]   &nbsp;
 **start_date** | date| Limit EPS estimates to those on or after this date | [optional]   &nbsp;
 **end_date** | date| Limit EPS estimates to those on or before this date | [optional]   &nbsp;
 **fiscal_year** | int| Only for the given fiscal year | [optional]   &nbsp;
 **fiscal_period** | str| The fiscal period | [optional]   &nbsp;
 **calendar_year** | int| Only for the given calendar year | [optional]   &nbsp;
 **calendar_period** | str| The calendar period | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseZacksEPSEstimates**](ApiResponseZacksEPSEstimates.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:ZacksApi)

[//]: # (METHOD:get_zacks_eps_growth_rates)

[//]: # (RETURN_TYPE:ApiResponseZacksEPSGrowthRates)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseZacksEPSGrowthRates.md)

[//]: # (OPERATION:get_zacks_eps_growth_rates_v2)

[//]: # (ENDPOINT:/zacks/eps_growth_rates)

[//]: # (DOCUMENT_LINK:ZacksApi.md#get_zacks_eps_growth_rates)

## **get_zacks_eps_growth_rates**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_zacks_eps_growth_rates_v2)

[//]: # (START_OVERVIEW)

> ApiResponseZacksEPSGrowthRates get_zacks_eps_growth_rates(company=company, industry_group_name=industry_group_name, industry_group_number=industry_group_number, page_size=page_size, next_page=next_page)

#### Zacks EPS Growth Rates


Returns the latest Zacks EPS growth rates

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

company = 'AAPL'
industry_group_name = ''
industry_group_number = ''
page_size = 100
next_page = ''

response = intrinio.ZacksApi().get_zacks_eps_growth_rates(company=company, industry_group_name=industry_group_name, industry_group_number=industry_group_number, page_size=page_size, next_page=next_page)
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
 **industry_group_name** | str| Return only growth rates for companies in the given Zacks industry group name | [optional]   &nbsp;
 **industry_group_number** | str| Return only growth rates for companies in the given Zacks industry group number | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseZacksEPSGrowthRates**](ApiResponseZacksEPSGrowthRates.md)

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
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

start_date = ''
end_date = ''
eps_actual_greater = ''
eps_actual_less = ''
eps_mean_estimate_greater = ''
eps_mean_estimate_less = ''
eps_amount_diff_greater = ''
eps_amount_diff_less = ''
eps_percent_diff_greater = ''
eps_percent_diff_less = ''
eps_count_estimate_greater = ''
eps_count_estimate_less = ''
eps_std_dev_estimate_greater = ''
eps_std_dev_estimate_less = ''
page_size = 100
next_page = ''

response = intrinio.ZacksApi().get_zacks_eps_surprises(start_date=start_date, end_date=end_date, eps_actual_greater=eps_actual_greater, eps_actual_less=eps_actual_less, eps_mean_estimate_greater=eps_mean_estimate_greater, eps_mean_estimate_less=eps_mean_estimate_less, eps_amount_diff_greater=eps_amount_diff_greater, eps_amount_diff_less=eps_amount_diff_less, eps_percent_diff_greater=eps_percent_diff_greater, eps_percent_diff_less=eps_percent_diff_less, eps_count_estimate_greater=eps_count_estimate_greater, eps_count_estimate_less=eps_count_estimate_less, eps_std_dev_estimate_greater=eps_std_dev_estimate_greater, eps_std_dev_estimate_less=eps_std_dev_estimate_less, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | date| Limit EPS surprises to those on or after this date | [optional]   &nbsp;
 **end_date** | date| Limit EPS surprises to those on or before this date | [optional]   &nbsp;
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

[//]: # (METHOD:get_zacks_etf_holdings)

[//]: # (RETURN_TYPE:ApiResponseZacksETFHoldings)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseZacksETFHoldings.md)

[//]: # (OPERATION:get_zacks_etf_holdings_v2)

[//]: # (ENDPOINT:/zacks/etf_holdings)

[//]: # (DOCUMENT_LINK:ZacksApi.md#get_zacks_etf_holdings)

## **get_zacks_etf_holdings**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_zacks_etf_holdings_v2)

[//]: # (START_OVERVIEW)

> ApiResponseZacksETFHoldings get_zacks_etf_holdings(etf_ticker=etf_ticker, holding_symbol=holding_symbol, weight_greater=weight_greater, weight_less=weight_less, page_size=page_size, next_page=next_page)

#### Zacks ETF Holdings


Returns Zacks ETF holdings data

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

etf_ticker = ''
holding_symbol = ''
weight_greater = ''
weight_less = ''
page_size = 100
next_page = ''

response = intrinio.ZacksApi().get_zacks_etf_holdings(etf_ticker=etf_ticker, holding_symbol=holding_symbol, weight_greater=weight_greater, weight_less=weight_less, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **etf_ticker** | str| Return holdings of the ETF with the given ticker | [optional]   &nbsp;
 **holding_symbol** | str| Return holdings where the instrument being held has the given trading symbol | [optional]   &nbsp;
 **weight_greater** | float| Return on the holdings with a weight greater than | [optional]   &nbsp;
 **weight_less** | float| Return on the holdings with a weight less than | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseZacksETFHoldings**](ApiResponseZacksETFHoldings.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:ZacksApi)

[//]: # (METHOD:get_zacks_institutional_holding_companies)

[//]: # (RETURN_TYPE:ApiResponseZacksInstitutionalHoldingCompanies)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseZacksInstitutionalHoldingCompanies.md)

[//]: # (OPERATION:get_zacks_institutional_holding_companies_v2)

[//]: # (ENDPOINT:/zacks/institutional_holdings/companies)

[//]: # (DOCUMENT_LINK:ZacksApi.md#get_zacks_institutional_holding_companies)

## **get_zacks_institutional_holding_companies**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_zacks_institutional_holding_companies_v2)

[//]: # (START_OVERVIEW)

> ApiResponseZacksInstitutionalHoldingCompanies get_zacks_institutional_holding_companies(ticker=ticker, page_size=page_size, next_page=next_page)

#### Zacks Institutional Holding Companies


Returns Zacks institutional holding companies data

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

ticker = ''
page_size = 100
next_page = ''

response = intrinio.ZacksApi().get_zacks_institutional_holding_companies(ticker=ticker, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | str| Return companies with the given ticker | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseZacksInstitutionalHoldingCompanies**](ApiResponseZacksInstitutionalHoldingCompanies.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:ZacksApi)

[//]: # (METHOD:get_zacks_institutional_holding_owners)

[//]: # (RETURN_TYPE:ApiResponseZacksInstitutionalHoldingOwners)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseZacksInstitutionalHoldingOwners.md)

[//]: # (OPERATION:get_zacks_institutional_holding_owners_v2)

[//]: # (ENDPOINT:/zacks/institutional_holdings/owners)

[//]: # (DOCUMENT_LINK:ZacksApi.md#get_zacks_institutional_holding_owners)

## **get_zacks_institutional_holding_owners**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_zacks_institutional_holding_owners_v2)

[//]: # (START_OVERVIEW)

> ApiResponseZacksInstitutionalHoldingOwners get_zacks_institutional_holding_owners(cik=cik, page_size=page_size, next_page=next_page)

#### Zacks Institutional Holding Owners


Returns Zacks institutional holding owners data

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

cik = ''
page_size = 100
next_page = ''

response = intrinio.ZacksApi().get_zacks_institutional_holding_owners(cik=cik, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cik** | str| Return owners with the given Central Index Key (CIK) | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseZacksInstitutionalHoldingOwners**](ApiResponseZacksInstitutionalHoldingOwners.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:ZacksApi)

[//]: # (METHOD:get_zacks_institutional_holdings)

[//]: # (RETURN_TYPE:ApiResponseZacksInstitutionalHoldings)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseZacksInstitutionalHoldings.md)

[//]: # (OPERATION:get_zacks_institutional_holdings_v2)

[//]: # (ENDPOINT:/zacks/institutional_holdings)

[//]: # (DOCUMENT_LINK:ZacksApi.md#get_zacks_institutional_holdings)

## **get_zacks_institutional_holdings**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_zacks_institutional_holdings_v2)

[//]: # (START_OVERVIEW)

> ApiResponseZacksInstitutionalHoldings get_zacks_institutional_holdings(ticker=ticker, owner_cik=owner_cik, page_size=page_size, next_page=next_page)

#### Zacks Institutional Holdings


Returns Zacks institutional holdings data

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

ticker = ''
owner_cik = ''
page_size = 100
next_page = ''

response = intrinio.ZacksApi().get_zacks_institutional_holdings(ticker=ticker, owner_cik=owner_cik, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | str| Return holdings where the company being held has the given ticker | [optional]   &nbsp;
 **owner_cik** | str| Return holdings where the owner/holder has the given Central Index Key (CIK) | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseZacksInstitutionalHoldings**](ApiResponseZacksInstitutionalHoldings.md)

[//]: # (END_OPERATION)


[//]: # (START_OPERATION)

[//]: # (CLASS:ZacksApi)

[//]: # (METHOD:get_zacks_long_term_growth_rates)

[//]: # (RETURN_TYPE:ApiResponseZacksLongTermGrowthRates)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseZacksLongTermGrowthRates.md)

[//]: # (OPERATION:get_zacks_long_term_growth_rates_v2)

[//]: # (ENDPOINT:/zacks/long_term_growth_rates)

[//]: # (DOCUMENT_LINK:ZacksApi.md#get_zacks_long_term_growth_rates)

## **get_zacks_long_term_growth_rates**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_zacks_long_term_growth_rates_v2)

[//]: # (START_OVERVIEW)

> ApiResponseZacksLongTermGrowthRates get_zacks_long_term_growth_rates(identifier=identifier, page_size=page_size, next_page=next_page)

#### Zacks Long Term Growth Rates


Returns the latest Zacks long term growth rates

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

identifier = 'AAPL'
page_size = 100
next_page = ''

response = intrinio.ZacksApi().get_zacks_long_term_growth_rates(identifier=identifier, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID) | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseZacksLongTermGrowthRates**](ApiResponseZacksLongTermGrowthRates.md)

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
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

start_date = ''
end_date = ''
sales_actual_greater = ''
sales_actual_less = ''
sales_mean_estimate_greater = ''
sales_mean_estimate_less = ''
sales_amount_diff_greater = ''
sales_amount_diff_less = ''
sales_percent_diff_greater = ''
sales_percent_diff_less = ''
sales_count_estimate_greater = ''
sales_count_estimate_less = ''
sales_std_dev_estimate_greater = ''
sales_std_dev_estimate_less = ''
page_size = 100
next_page = ''

response = intrinio.ZacksApi().get_zacks_sales_surprises(start_date=start_date, end_date=end_date, sales_actual_greater=sales_actual_greater, sales_actual_less=sales_actual_less, sales_mean_estimate_greater=sales_mean_estimate_greater, sales_mean_estimate_less=sales_mean_estimate_less, sales_amount_diff_greater=sales_amount_diff_greater, sales_amount_diff_less=sales_amount_diff_less, sales_percent_diff_greater=sales_percent_diff_greater, sales_percent_diff_less=sales_percent_diff_less, sales_count_estimate_greater=sales_count_estimate_greater, sales_count_estimate_less=sales_count_estimate_less, sales_std_dev_estimate_greater=sales_std_dev_estimate_greater, sales_std_dev_estimate_less=sales_std_dev_estimate_less, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | date| Limit sales surprises to those on or after this date | [optional]   &nbsp;
 **end_date** | date| Limit sales surprises to those on or before this date | [optional]   &nbsp;
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


[//]: # (START_OPERATION)

[//]: # (CLASS:ZacksApi)

[//]: # (METHOD:get_zacks_target_price_consensuses)

[//]: # (RETURN_TYPE:ApiResponseZacksTargetPriceConsensuses)

[//]: # (RETURN_TYPE_KIND:object)

[//]: # (RETURN_TYPE_DOC:ApiResponseZacksTargetPriceConsensuses.md)

[//]: # (OPERATION:get_zacks_target_price_consensuses_v2)

[//]: # (ENDPOINT:/zacks/target_price_consensuses)

[//]: # (DOCUMENT_LINK:ZacksApi.md#get_zacks_target_price_consensuses)

## **get_zacks_target_price_consensuses**

[**View Intrinio API Documentation**](https://docs.intrinio.com/documentation/python/get_zacks_target_price_consensuses_v2)

[//]: # (START_OVERVIEW)

> ApiResponseZacksTargetPriceConsensuses get_zacks_target_price_consensuses(identifier=identifier, industry_group_number=industry_group_number, page_size=page_size, next_page=next_page)

#### Zacks Target Price Consensuses


Returns the latest Zacks target price consensus data

[//]: # (END_OVERVIEW)

### Example
[//]: # (START_CODE_EXAMPLE)

```python
from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

intrinio.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY'

identifier = 'AAPL'
industry_group_number = ''
page_size = 100
next_page = ''

response = intrinio.ZacksApi().get_zacks_target_price_consensuses(identifier=identifier, industry_group_number=industry_group_number, page_size=page_size, next_page=next_page)
print(response)
    
# Note: For a Pandas DataFrame, import Pandas and use pd.DataFrame(response.property_name_dict) 
```
[//]: # (END_CODE_EXAMPLE)

[//]: # (START_DEFINITION)

### Parameters

[//]: # (START_PARAMETERS)


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | str| Filings for the given &#x60;company&#x60; identifier (ticker, CIK, LEI, Intrinio ID) | [optional]   &nbsp;
 **industry_group_number** | str| Return only growth rates for companies in the given Zacks industry group number | [optional]   &nbsp;
 **page_size** | int| The number of results to return | [optional] [default to 100]  &nbsp;
 **next_page** | str| Gets the next page of data from a previous API call | [optional]   &nbsp;
<br/>

[//]: # (END_PARAMETERS)

### Return type

[**ApiResponseZacksTargetPriceConsensuses**](ApiResponseZacksTargetPriceConsensuses.md)

[//]: # (END_OPERATION)

