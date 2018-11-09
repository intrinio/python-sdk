# Intrinio Python SDK

WARNING: THIS IS IS A BETA - DO NOT USE IN PRODUCTION.

To request a beta access key, [sign up here](https://intrinio.com/api-v2-beta).

Welcome to the Intrinio API! Through our Marketplace, we offer a wide selection of financial data feeds sourced by our own proprietary processes as well as from many data vendors. The primary application of the Intrinio API is for use in third-party applications and integrations or for end-users utilizing the Excel add-in and Google Sheets add-on. The Intrinio API uses HTTPS verbs and a RESTful endpoint structure, which makes it easy to request data from Intrinio. Responses are delivered in JSON format. If you need additional help in using the API, go to our home page (https://intrinio.com) and click on the chat icon in the lower right corner.

- API version: 2.0.2
- Package version: 0.9.1


## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### Option 1: pip install

You can install directly from GitHub:

```sh
pip install git+https://github.com/intrinio/python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/intrinio/python-sdk.git`)

Then import the package:
```python
import intrinio_sdk 
```

### Option 2: Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import intrinio_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'YOUR_API_KEY' 

company_api = intrinio_sdk.CompanyApi()

try:
    api_response = company_api.filter_companies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->filter_companies: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api-v2.intrinio.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CompanyApi* | [**filter_companies**](docs/CompanyApi.md#filter_companies) | **GET** /companies/filter | Filter Companies
*CompanyApi* | [**filter_company_fundamentals**](docs/CompanyApi.md#filter_company_fundamentals) | **GET** /companies/{identifier}/fundamentals/filter | Filter Fundamentals for a Company
*CompanyApi* | [**get_all_companies**](docs/CompanyApi.md#get_all_companies) | **GET** /companies | Get All Companies
*CompanyApi* | [**get_all_company_news**](docs/CompanyApi.md#get_all_company_news) | **GET** /companies/news | Get All Company News
*CompanyApi* | [**get_company**](docs/CompanyApi.md#get_company) | **GET** /companies/{identifier} | Get a Company by ID
*CompanyApi* | [**get_company_data_point_number**](docs/CompanyApi.md#get_company_data_point_number) | **GET** /companies/{identifier}/data_point/{tag}/number | Get Company Data Point (Number)
*CompanyApi* | [**get_company_data_point_text**](docs/CompanyApi.md#get_company_data_point_text) | **GET** /companies/{identifier}/data_point/{tag}/text | Get Company Data Point (Text)
*CompanyApi* | [**get_company_filings**](docs/CompanyApi.md#get_company_filings) | **GET** /companies/{identifier}/filings | Get Filings for a Company
*CompanyApi* | [**get_company_fundamentals**](docs/CompanyApi.md#get_company_fundamentals) | **GET** /companies/{identifier}/fundamentals | Get All Fundamentals for a Company
*CompanyApi* | [**get_company_historical_data**](docs/CompanyApi.md#get_company_historical_data) | **GET** /companies/{identifier}/historical_data/{tag} | Get Company Historical Data
*CompanyApi* | [**get_company_news**](docs/CompanyApi.md#get_company_news) | **GET** /companies/{identifier}/news | Get News for a Company
*CompanyApi* | [**get_company_securities**](docs/CompanyApi.md#get_company_securities) | **GET** /companies/{identifier}/securities | Get Securities by Company
*CompanyApi* | [**lookup_company_fundamental**](docs/CompanyApi.md#lookup_company_fundamental) | **GET** /companies/{identifier}/fundamentals/lookup/{statement_code}/{fiscal_year}/{fiscal_period} | Lookup a Fundamental for a Company
*CompanyApi* | [**search_companies**](docs/CompanyApi.md#search_companies) | **GET** /companies/search | Search Companies
*DataPointApi* | [**get_data_point_number**](docs/DataPointApi.md#get_data_point_number) | **GET** /data_point/{identifier}/{tag}/number | Get a Data Point (Number)
*DataPointApi* | [**get_data_point_text**](docs/DataPointApi.md#get_data_point_text) | **GET** /data_point/{identifier}/{tag}/text | Get a Data Point (Text)
*DataTagApi* | [**filter_data_tags**](docs/DataTagApi.md#filter_data_tags) | **GET** /data_tags/filter | Filter Data Tags
*DataTagApi* | [**get_all_data_tags**](docs/DataTagApi.md#get_all_data_tags) | **GET** /data_tags | Get All Data Tags
*DataTagApi* | [**get_data_tag_by_id**](docs/DataTagApi.md#get_data_tag_by_id) | **GET** /data_tags/{identifier} | Get a Data Tag by ID
*DataTagApi* | [**search_data_tags**](docs/DataTagApi.md#search_data_tags) | **GET** /data_tags/search | Search Data Tags
*FilingApi* | [**filter_filings**](docs/FilingApi.md#filter_filings) | **GET** /filings/filter | Filter Filings
*FilingApi* | [**get_all_filings**](docs/FilingApi.md#get_all_filings) | **GET** /filings | Get All Filings
*FilingApi* | [**get_filing_by_id**](docs/FilingApi.md#get_filing_by_id) | **GET** /filings/{id} | Get a Filing by ID
*FundamentalsApi* | [**get_fundamental_by_id**](docs/FundamentalsApi.md#get_fundamental_by_id) | **GET** /fundamentals/{id} | Get a Fundamental by ID
*FundamentalsApi* | [**get_fundamental_reported_financials**](docs/FundamentalsApi.md#get_fundamental_reported_financials) | **GET** /fundamentals/{id}/reported_financials | Get Reported Financials for a Fundamental
*FundamentalsApi* | [**get_fundamental_standardized_financials**](docs/FundamentalsApi.md#get_fundamental_standardized_financials) | **GET** /fundamentals/{id}/standardized_financials | Get Standardized Financials for a Fundamental
*FundamentalsApi* | [**lookup_fundamental**](docs/FundamentalsApi.md#lookup_fundamental) | **GET** /fundamentals/lookup/{identifier}/{statement_code}/{fiscal_year}/{fiscal_period} | Lookup a Fundamental
*HistoricalDataApi* | [**get_historical_data**](docs/HistoricalDataApi.md#get_historical_data) | **GET** /historical_data/{identifier}/{tag} | Get Historical Data
*IndexApi* | [**get_all_economic_indices**](docs/IndexApi.md#get_all_economic_indices) | **GET** /indices/economic | Get All Economic Indices
*IndexApi* | [**get_all_sic_indices**](docs/IndexApi.md#get_all_sic_indices) | **GET** /indices/sic | Get All SIC Indices
*IndexApi* | [**get_all_stock_market_indices**](docs/IndexApi.md#get_all_stock_market_indices) | **GET** /indices/stock_market | Get All Stock Market Indices
*IndexApi* | [**get_economic_index_by_id**](docs/IndexApi.md#get_economic_index_by_id) | **GET** /indices/economic/{identifier} | Get an Economic Index by ID
*IndexApi* | [**get_economic_index_data_point_number**](docs/IndexApi.md#get_economic_index_data_point_number) | **GET** /indices/economic/{identifier}/data_point/{tag}/number | Get Economic Index Data Point (Number)
*IndexApi* | [**get_economic_index_data_point_text**](docs/IndexApi.md#get_economic_index_data_point_text) | **GET** /indices/economic/{identifier}/data_point/{tag}/text | Get Economic Index Data Point (Text)
*IndexApi* | [**get_economic_index_historical_data**](docs/IndexApi.md#get_economic_index_historical_data) | **GET** /indices/economic/{identifier}/historical_data/{tag} | Get Economic Index Historical Data
*IndexApi* | [**get_sic_index_by_id**](docs/IndexApi.md#get_sic_index_by_id) | **GET** /indices/sic/{identifier} | Get an SIC Index by ID
*IndexApi* | [**get_sic_index_data_point_number**](docs/IndexApi.md#get_sic_index_data_point_number) | **GET** /indices/sic/{identifier}/data_point/{tag}/number | Get SIC Index Data Point (Number)
*IndexApi* | [**get_sic_index_data_point_text**](docs/IndexApi.md#get_sic_index_data_point_text) | **GET** /indices/sic/{identifier}/data_point/{tag}/text | Get SIC Index Data Point (Text)
*IndexApi* | [**get_sic_index_historical_data**](docs/IndexApi.md#get_sic_index_historical_data) | **GET** /indices/sic/{identifier}/historical_data/{tag} | Get SIC Index Historical Data
*IndexApi* | [**get_stock_market_index_by_id**](docs/IndexApi.md#get_stock_market_index_by_id) | **GET** /indices/stock_market/{identifier} | Get a Stock Market Index by ID
*IndexApi* | [**get_stock_market_index_data_point_number**](docs/IndexApi.md#get_stock_market_index_data_point_number) | **GET** /indices/stock_market/{identifier}/data_point/{tag}/number | Get Stock Market Index Data Point (Number)
*IndexApi* | [**get_stock_market_index_data_point_text**](docs/IndexApi.md#get_stock_market_index_data_point_text) | **GET** /indices/stock_market/{identifier}/data_point/{tag}/text | Get Stock Market Index Data Point (Text)
*IndexApi* | [**get_stock_market_index_historical_data**](docs/IndexApi.md#get_stock_market_index_historical_data) | **GET** /indices/stock_market/{identifier}/historical_data/{tag} | Get Stock Market Index Historical Data
*IndexApi* | [**search_economic_indices**](docs/IndexApi.md#search_economic_indices) | **GET** /indices/economic/search | Search Economic Indices
*IndexApi* | [**search_sic_indices**](docs/IndexApi.md#search_sic_indices) | **GET** /indices/sic/search | Search SIC Indices
*IndexApi* | [**search_stock_markets_indices**](docs/IndexApi.md#search_stock_markets_indices) | **GET** /indices/stock_market/search | Search Stock Market Indices
*SecurityApi* | [**get_all_securities**](docs/SecurityApi.md#get_all_securities) | **GET** /securities | Get All Securiites
*SecurityApi* | [**get_security_by_id**](docs/SecurityApi.md#get_security_by_id) | **GET** /securities/{identifier} | Get a Security by ID
*SecurityApi* | [**get_security_data_point_number**](docs/SecurityApi.md#get_security_data_point_number) | **GET** /securities/{identifier}/data_point/{tag}/number | Get Security Data Point (Number)
*SecurityApi* | [**get_security_data_point_text**](docs/SecurityApi.md#get_security_data_point_text) | **GET** /securities/{identifier}/data_point/{tag}/text | Get Security Data Point (Text)
*SecurityApi* | [**get_security_historical_data**](docs/SecurityApi.md#get_security_historical_data) | **GET** /securities/{identifier}/historical_data/{tag} | Get Security Historical Data
*SecurityApi* | [**get_security_stock_price_adjustments**](docs/SecurityApi.md#get_security_stock_price_adjustments) | **GET** /securities/{identifier}/prices/adjustments | Get Stock Price Adjustments for Security
*SecurityApi* | [**get_security_stock_prices**](docs/SecurityApi.md#get_security_stock_prices) | **GET** /securities/{identifier}/prices | Get Stock Prices for Security
*SecurityApi* | [**screen_securities**](docs/SecurityApi.md#screen_securities) | **POST** /securities/screen | Screen Securities
*SecurityApi* | [**search_securities**](docs/SecurityApi.md#search_securities) | **GET** /securities/search | Search Securities
*StockExchangeApi* | [**filter_stock_exchanges**](docs/StockExchangeApi.md#filter_stock_exchanges) | **GET** /stock_exchanges/filter | Filter Stock Exchanges
*StockExchangeApi* | [**get_all_stock_exchanges**](docs/StockExchangeApi.md#get_all_stock_exchanges) | **GET** /stock_exchanges | Get All Stock Exchanges
*StockExchangeApi* | [**get_stock_exchange_by_id**](docs/StockExchangeApi.md#get_stock_exchange_by_id) | **GET** /stock_exchanges/{identifier} | Get Stock Exchange by ID
*StockExchangeApi* | [**get_stock_exchange_price_adjustments**](docs/StockExchangeApi.md#get_stock_exchange_price_adjustments) | **GET** /stock_exchanges/{identifier}/prices/adjustments | Get Stock Price Adjustments by Exchange
*StockExchangeApi* | [**get_stock_exchange_prices**](docs/StockExchangeApi.md#get_stock_exchange_prices) | **GET** /stock_exchanges/{identifier}/prices | Get Stock Prices by Exchange
*StockExchangeApi* | [**get_stock_exchange_securities**](docs/StockExchangeApi.md#get_stock_exchange_securities) | **GET** /stock_exchanges/{identifier}/securities | Get Securities by Exchange


## Documentation For Models

 - [ApiResponseCompanies](docs/ApiResponseCompanies.md)
 - [ApiResponseCompanyFilings](docs/ApiResponseCompanyFilings.md)
 - [ApiResponseCompanyFundamentals](docs/ApiResponseCompanyFundamentals.md)
 - [ApiResponseCompanyHistoricalData](docs/ApiResponseCompanyHistoricalData.md)
 - [ApiResponseCompanyNews](docs/ApiResponseCompanyNews.md)
 - [ApiResponseCompanySecurities](docs/ApiResponseCompanySecurities.md)
 - [ApiResponseDataTags](docs/ApiResponseDataTags.md)
 - [ApiResponseEconomicIndexHistoricalData](docs/ApiResponseEconomicIndexHistoricalData.md)
 - [ApiResponseEconomicIndices](docs/ApiResponseEconomicIndices.md)
 - [ApiResponseFilings](docs/ApiResponseFilings.md)
 - [ApiResponseHistoricalData](docs/ApiResponseHistoricalData.md)
 - [ApiResponseNews](docs/ApiResponseNews.md)
 - [ApiResponseReportedFinancials](docs/ApiResponseReportedFinancials.md)
 - [ApiResponseSICIndexHistoricalData](docs/ApiResponseSICIndexHistoricalData.md)
 - [ApiResponseSICIndices](docs/ApiResponseSICIndices.md)
 - [ApiResponseSecurities](docs/ApiResponseSecurities.md)
 - [ApiResponseSecurityHistoricalData](docs/ApiResponseSecurityHistoricalData.md)
 - [ApiResponseSecurityStockPriceAdjustments](docs/ApiResponseSecurityStockPriceAdjustments.md)
 - [ApiResponseSecurityStockPrices](docs/ApiResponseSecurityStockPrices.md)
 - [ApiResponseStandardizedFinancials](docs/ApiResponseStandardizedFinancials.md)
 - [ApiResponseStockExchangeSecurities](docs/ApiResponseStockExchangeSecurities.md)
 - [ApiResponseStockExchangeStockPriceAdjustments](docs/ApiResponseStockExchangeStockPriceAdjustments.md)
 - [ApiResponseStockExchangeStockPrices](docs/ApiResponseStockExchangeStockPrices.md)
 - [ApiResponseStockMarketIndexHistoricalData](docs/ApiResponseStockMarketIndexHistoricalData.md)
 - [ApiResponseStockMarketIndices](docs/ApiResponseStockMarketIndices.md)
 - [Company](docs/Company.md)
 - [CompanyFiling](docs/CompanyFiling.md)
 - [CompanyNews](docs/CompanyNews.md)
 - [CompanyNewsSummary](docs/CompanyNewsSummary.md)
 - [CompanySummary](docs/CompanySummary.md)
 - [DataPointNumber](docs/DataPointNumber.md)
 - [DataPointText](docs/DataPointText.md)
 - [DataTag](docs/DataTag.md)
 - [DataTagSummary](docs/DataTagSummary.md)
 - [EconomicIndex](docs/EconomicIndex.md)
 - [EconomicIndexSummary](docs/EconomicIndexSummary.md)
 - [Filing](docs/Filing.md)
 - [FilingSummary](docs/FilingSummary.md)
 - [Fundamental](docs/Fundamental.md)
 - [FundamentalSummary](docs/FundamentalSummary.md)
 - [HistoricalData](docs/HistoricalData.md)
 - [ReportedFinancial](docs/ReportedFinancial.md)
 - [ReportedTag](docs/ReportedTag.md)
 - [SICIndex](docs/SICIndex.md)
 - [Security](docs/Security.md)
 - [SecurityScreenClause](docs/SecurityScreenClause.md)
 - [SecurityScreenGroup](docs/SecurityScreenGroup.md)
 - [SecurityScreenResult](docs/SecurityScreenResult.md)
 - [SecurityScreenResultData](docs/SecurityScreenResultData.md)
 - [SecuritySummary](docs/SecuritySummary.md)
 - [StandardizedFinancial](docs/StandardizedFinancial.md)
 - [StockExchange](docs/StockExchange.md)
 - [StockMarketIndex](docs/StockMarketIndex.md)
 - [StockMarketIndexSummary](docs/StockMarketIndexSummary.md)
 - [StockPrice](docs/StockPrice.md)
 - [StockPriceAdjustment](docs/StockPriceAdjustment.md)
 - [StockPriceAdjustmentSummary](docs/StockPriceAdjustmentSummary.md)
 - [StockPriceSummary](docs/StockPriceSummary.md)

