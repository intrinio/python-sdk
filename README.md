# Intrinio Python SDK

To get an API key, [sign up here](https://intrinio.com/).

Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.

- API version: 2.2.0
- Package version: 2.1.0


## Requirements.

Python 2.7 and 3.4+

## Installation

```sh
pip install intrinio-sdk
```

Then import the package:
```python
import intrinio_sdk 
```

## Installation from Github

```sh
pip install git+https://github.com/intrinio/python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/intrinio/python-sdk.git`)

Then import the package:
```python
import intrinio_sdk 
```

## Installation from python-sdk repo

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import intrinio_sdk
```

## SDK Code Examples

Code examples for Intrinio SDKs are available at https://github.com/intrinio/sdk-code-samples

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
*CompanyApi* | [**get_all_companies**](docs/CompanyApi.md#get_all_companies) | **GET** /companies | All Companies
*CompanyApi* | [**get_all_company_news**](docs/CompanyApi.md#get_all_company_news) | **GET** /companies/news | All News
*CompanyApi* | [**get_company**](docs/CompanyApi.md#get_company) | **GET** /companies/{identifier} | Lookup Company
*CompanyApi* | [**get_company_data_point_number**](docs/CompanyApi.md#get_company_data_point_number) | **GET** /companies/{identifier}/data_point/{tag}/number | Data Point (Number) for Company
*CompanyApi* | [**get_company_data_point_text**](docs/CompanyApi.md#get_company_data_point_text) | **GET** /companies/{identifier}/data_point/{tag}/text | Data Point (Text) for Company
*CompanyApi* | [**get_company_filings**](docs/CompanyApi.md#get_company_filings) | **GET** /companies/{identifier}/filings | All Filings by Company
*CompanyApi* | [**get_company_fundamentals**](docs/CompanyApi.md#get_company_fundamentals) | **GET** /companies/{identifier}/fundamentals | All Fundamentals by Company
*CompanyApi* | [**get_company_historical_data**](docs/CompanyApi.md#get_company_historical_data) | **GET** /companies/{identifier}/historical_data/{tag} | Historical Data for Company
*CompanyApi* | [**get_company_news**](docs/CompanyApi.md#get_company_news) | **GET** /companies/{identifier}/news | All News by Company
*CompanyApi* | [**get_company_securities**](docs/CompanyApi.md#get_company_securities) | **GET** /companies/{identifier}/securities | All Securities by Company
*CompanyApi* | [**lookup_company_fundamental**](docs/CompanyApi.md#lookup_company_fundamental) | **GET** /companies/{identifier}/fundamentals/lookup/{statement_code}/{fiscal_year}/{fiscal_period} | Lookup Fundamental by Company
*CompanyApi* | [**search_companies**](docs/CompanyApi.md#search_companies) | **GET** /companies/search | Search Companies
*DataPointApi* | [**get_data_point_number**](docs/DataPointApi.md#get_data_point_number) | **GET** /data_point/{identifier}/{tag}/number | Data Point (Number)
*DataPointApi* | [**get_data_point_text**](docs/DataPointApi.md#get_data_point_text) | **GET** /data_point/{identifier}/{tag}/text | Data Point (Text)
*DataTagApi* | [**get_all_data_tags**](docs/DataTagApi.md#get_all_data_tags) | **GET** /data_tags | All Data Tags
*DataTagApi* | [**get_data_tag_by_id**](docs/DataTagApi.md#get_data_tag_by_id) | **GET** /data_tags/{identifier} | Lookup Data Tag
*DataTagApi* | [**search_data_tags**](docs/DataTagApi.md#search_data_tags) | **GET** /data_tags/search | Search Data Tags
*FilingApi* | [**get_all_filings**](docs/FilingApi.md#get_all_filings) | **GET** /filings | All Filings
*FilingApi* | [**get_all_notes**](docs/FilingApi.md#get_all_notes) | **GET** /filings/notes | All Filing Notes
*FilingApi* | [**get_filing_by_id**](docs/FilingApi.md#get_filing_by_id) | **GET** /filings/{id} | Lookup Filing
*FilingApi* | [**get_note**](docs/FilingApi.md#get_note) | **GET** /filings/notes/{identifier} | Filing Note by ID
*FilingApi* | [**get_note_html**](docs/FilingApi.md#get_note_html) | **GET** /filings/notes/{identifier}/html | Filing Note HTML
*FilingApi* | [**get_note_text**](docs/FilingApi.md#get_note_text) | **GET** /filings/notes/{identifier}/text | Filing Note Text
*FilingApi* | [**search_notes**](docs/FilingApi.md#search_notes) | **GET** /filings/notes/search | Search Filing Notes
*ForexApi* | [**get_forex_currencies**](docs/ForexApi.md#get_forex_currencies) | **GET** /forex/currencies | Forex Currencies
*ForexApi* | [**get_forex_pairs**](docs/ForexApi.md#get_forex_pairs) | **GET** /forex/pairs | Forex Currency Pairs
*ForexApi* | [**get_forex_prices**](docs/ForexApi.md#get_forex_prices) | **GET** /forex/prices/{pair}/{timeframe} | Forex Currency Prices
*FundamentalsApi* | [**get_fundamental_by_id**](docs/FundamentalsApi.md#get_fundamental_by_id) | **GET** /fundamentals/{id} | Fundamental by ID
*FundamentalsApi* | [**get_fundamental_reported_financials**](docs/FundamentalsApi.md#get_fundamental_reported_financials) | **GET** /fundamentals/{id}/reported_financials | Reported Financials
*FundamentalsApi* | [**get_fundamental_standardized_financials**](docs/FundamentalsApi.md#get_fundamental_standardized_financials) | **GET** /fundamentals/{id}/standardized_financials | Standardized Financials
*FundamentalsApi* | [**lookup_fundamental**](docs/FundamentalsApi.md#lookup_fundamental) | **GET** /fundamentals/lookup/{identifier}/{statement_code}/{fiscal_year}/{fiscal_period} | Lookup Fundamental
*HistoricalDataApi* | [**get_historical_data**](docs/HistoricalDataApi.md#get_historical_data) | **GET** /historical_data/{identifier}/{tag} | Historical Data
*IndexApi* | [**get_all_economic_indices**](docs/IndexApi.md#get_all_economic_indices) | **GET** /indices/economic | All Economic Indices
*IndexApi* | [**get_all_sic_indices**](docs/IndexApi.md#get_all_sic_indices) | **GET** /indices/sic | All SIC Indices
*IndexApi* | [**get_all_stock_market_indices**](docs/IndexApi.md#get_all_stock_market_indices) | **GET** /indices/stock_market | All Stock Market Indices
*IndexApi* | [**get_economic_index_by_id**](docs/IndexApi.md#get_economic_index_by_id) | **GET** /indices/economic/{identifier} | Lookup Economic Index
*IndexApi* | [**get_economic_index_data_point_number**](docs/IndexApi.md#get_economic_index_data_point_number) | **GET** /indices/economic/{identifier}/data_point/{tag}/number | Data Point (Number) for an Economic Index
*IndexApi* | [**get_economic_index_data_point_text**](docs/IndexApi.md#get_economic_index_data_point_text) | **GET** /indices/economic/{identifier}/data_point/{tag}/text | Data Point (Text) for an Economic Index
*IndexApi* | [**get_economic_index_historical_data**](docs/IndexApi.md#get_economic_index_historical_data) | **GET** /indices/economic/{identifier}/historical_data/{tag} | Historical Data for an Economic Index
*IndexApi* | [**get_sic_index_by_id**](docs/IndexApi.md#get_sic_index_by_id) | **GET** /indices/sic/{identifier} | Lookup SIC Index
*IndexApi* | [**get_sic_index_data_point_number**](docs/IndexApi.md#get_sic_index_data_point_number) | **GET** /indices/sic/{identifier}/data_point/{tag}/number | Data Point (Number) for an SIC Index
*IndexApi* | [**get_sic_index_data_point_text**](docs/IndexApi.md#get_sic_index_data_point_text) | **GET** /indices/sic/{identifier}/data_point/{tag}/text | Data Point (Text) for an SIC Index
*IndexApi* | [**get_sic_index_historical_data**](docs/IndexApi.md#get_sic_index_historical_data) | **GET** /indices/sic/{identifier}/historical_data/{tag} | Historical Data for an SIC Index
*IndexApi* | [**get_stock_market_index_by_id**](docs/IndexApi.md#get_stock_market_index_by_id) | **GET** /indices/stock_market/{identifier} | Lookup Stock Market Index
*IndexApi* | [**get_stock_market_index_data_point_number**](docs/IndexApi.md#get_stock_market_index_data_point_number) | **GET** /indices/stock_market/{identifier}/data_point/{tag}/number | Data Point (Number) for Stock Market Index
*IndexApi* | [**get_stock_market_index_data_point_text**](docs/IndexApi.md#get_stock_market_index_data_point_text) | **GET** /indices/stock_market/{identifier}/data_point/{tag}/text | Data Point (Text) for Stock Market Index
*IndexApi* | [**get_stock_market_index_historical_data**](docs/IndexApi.md#get_stock_market_index_historical_data) | **GET** /indices/stock_market/{identifier}/historical_data/{tag} | Historical Data for Stock Market Index
*IndexApi* | [**search_economic_indices**](docs/IndexApi.md#search_economic_indices) | **GET** /indices/economic/search | Search Economic Indices
*IndexApi* | [**search_sic_indices**](docs/IndexApi.md#search_sic_indices) | **GET** /indices/sic/search | Search SIC Indices
*IndexApi* | [**search_stock_markets_indices**](docs/IndexApi.md#search_stock_markets_indices) | **GET** /indices/stock_market/search | Search Stock Market Indices
*MunicipalityApi* | [**get_all_municipalities**](docs/MunicipalityApi.md#get_all_municipalities) | **GET** /municipalities | All Municipalities
*MunicipalityApi* | [**get_municipality_by_id**](docs/MunicipalityApi.md#get_municipality_by_id) | **GET** /municipalities/{id} | Municipality by ID
*MunicipalityApi* | [**get_municipality_financials**](docs/MunicipalityApi.md#get_municipality_financials) | **GET** /municipalities/{id}/financials | Financials for a Municipality
*SecurityApi* | [**get_all_securities**](docs/SecurityApi.md#get_all_securities) | **GET** /securities | All Securities
*SecurityApi* | [**get_security_by_id**](docs/SecurityApi.md#get_security_by_id) | **GET** /securities/{identifier} | Lookup Security
*SecurityApi* | [**get_security_data_point_number**](docs/SecurityApi.md#get_security_data_point_number) | **GET** /securities/{identifier}/data_point/{tag}/number | Data Point (Number) for Security
*SecurityApi* | [**get_security_data_point_text**](docs/SecurityApi.md#get_security_data_point_text) | **GET** /securities/{identifier}/data_point/{tag}/text | Data Point (Text) for Security
*SecurityApi* | [**get_security_historical_data**](docs/SecurityApi.md#get_security_historical_data) | **GET** /securities/{identifier}/historical_data/{tag} | Historical Data for Security
*SecurityApi* | [**get_security_intraday_prices**](docs/SecurityApi.md#get_security_intraday_prices) | **GET** /securities/{identifier}/prices/intraday | Intraday Stock Prices for Security
*SecurityApi* | [**get_security_latest_dividend_record**](docs/SecurityApi.md#get_security_latest_dividend_record) | **GET** /securities/{identifier}/dividends/latest | Lastest Dividend Record for Security
*SecurityApi* | [**get_security_latest_earnings_record**](docs/SecurityApi.md#get_security_latest_earnings_record) | **GET** /securities/{identifier}/earnings/latest | Lastest Earnings Record for Security
*SecurityApi* | [**get_security_realtime_price**](docs/SecurityApi.md#get_security_realtime_price) | **GET** /securities/{identifier}/prices/realtime | Realtime Stock Price for Security
*SecurityApi* | [**get_security_stock_price_adjustments**](docs/SecurityApi.md#get_security_stock_price_adjustments) | **GET** /securities/{identifier}/prices/adjustments | Stock Price Adjustments by Security
*SecurityApi* | [**get_security_stock_prices**](docs/SecurityApi.md#get_security_stock_prices) | **GET** /securities/{identifier}/prices | Stock Prices by Security
*SecurityApi* | [**screen_securities**](docs/SecurityApi.md#screen_securities) | **POST** /securities/screen | Screen Securities
*SecurityApi* | [**search_securities**](docs/SecurityApi.md#search_securities) | **GET** /securities/search | Search Securities
*StockExchangeApi* | [**get_all_stock_exchanges**](docs/StockExchangeApi.md#get_all_stock_exchanges) | **GET** /stock_exchanges | All Stock Exchanges
*StockExchangeApi* | [**get_stock_exchange_by_id**](docs/StockExchangeApi.md#get_stock_exchange_by_id) | **GET** /stock_exchanges/{identifier} | Lookup Stock Exchange
*StockExchangeApi* | [**get_stock_exchange_price_adjustments**](docs/StockExchangeApi.md#get_stock_exchange_price_adjustments) | **GET** /stock_exchanges/{identifier}/prices/adjustments | Stock Price Adjustments by Exchange
*StockExchangeApi* | [**get_stock_exchange_prices**](docs/StockExchangeApi.md#get_stock_exchange_prices) | **GET** /stock_exchanges/{identifier}/prices | Stock Prices by Exchange
*StockExchangeApi* | [**get_stock_exchange_realtime_prices**](docs/StockExchangeApi.md#get_stock_exchange_realtime_prices) | **GET** /stock_exchanges/{identifier}/prices/realtime | Realtime Stock Prices by Exchange
*StockExchangeApi* | [**get_stock_exchange_securities**](docs/StockExchangeApi.md#get_stock_exchange_securities) | **GET** /stock_exchanges/{identifier}/securities | Securities by Exchange


## Documentation For Models

 - [ApiResponseCompanies](docs/ApiResponseCompanies.md)
 - [ApiResponseCompaniesSearch](docs/ApiResponseCompaniesSearch.md)
 - [ApiResponseCompanyFilings](docs/ApiResponseCompanyFilings.md)
 - [ApiResponseCompanyFundamentals](docs/ApiResponseCompanyFundamentals.md)
 - [ApiResponseCompanyHistoricalData](docs/ApiResponseCompanyHistoricalData.md)
 - [ApiResponseCompanyNews](docs/ApiResponseCompanyNews.md)
 - [ApiResponseCompanySecurities](docs/ApiResponseCompanySecurities.md)
 - [ApiResponseDataTags](docs/ApiResponseDataTags.md)
 - [ApiResponseDataTagsSearch](docs/ApiResponseDataTagsSearch.md)
 - [ApiResponseEconomicIndexHistoricalData](docs/ApiResponseEconomicIndexHistoricalData.md)
 - [ApiResponseEconomicIndices](docs/ApiResponseEconomicIndices.md)
 - [ApiResponseEconomicIndicesSearch](docs/ApiResponseEconomicIndicesSearch.md)
 - [ApiResponseFilingNotes](docs/ApiResponseFilingNotes.md)
 - [ApiResponseFilingNotesSearch](docs/ApiResponseFilingNotesSearch.md)
 - [ApiResponseFilings](docs/ApiResponseFilings.md)
 - [ApiResponseForexCurrencies](docs/ApiResponseForexCurrencies.md)
 - [ApiResponseForexPairs](docs/ApiResponseForexPairs.md)
 - [ApiResponseForexPrices](docs/ApiResponseForexPrices.md)
 - [ApiResponseHistoricalData](docs/ApiResponseHistoricalData.md)
 - [ApiResponseMunicipalities](docs/ApiResponseMunicipalities.md)
 - [ApiResponseMunicipalitiyFinancials](docs/ApiResponseMunicipalitiyFinancials.md)
 - [ApiResponseNews](docs/ApiResponseNews.md)
 - [ApiResponseReportedFinancials](docs/ApiResponseReportedFinancials.md)
 - [ApiResponseSICIndexHistoricalData](docs/ApiResponseSICIndexHistoricalData.md)
 - [ApiResponseSICIndices](docs/ApiResponseSICIndices.md)
 - [ApiResponseSICIndicesSearch](docs/ApiResponseSICIndicesSearch.md)
 - [ApiResponseSecurities](docs/ApiResponseSecurities.md)
 - [ApiResponseSecuritiesSearch](docs/ApiResponseSecuritiesSearch.md)
 - [ApiResponseSecurityHistoricalData](docs/ApiResponseSecurityHistoricalData.md)
 - [ApiResponseSecurityIntradayPrices](docs/ApiResponseSecurityIntradayPrices.md)
 - [ApiResponseSecurityStockPriceAdjustments](docs/ApiResponseSecurityStockPriceAdjustments.md)
 - [ApiResponseSecurityStockPrices](docs/ApiResponseSecurityStockPrices.md)
 - [ApiResponseStandardizedFinancials](docs/ApiResponseStandardizedFinancials.md)
 - [ApiResponseStockExchangeRealtimeStockPrices](docs/ApiResponseStockExchangeRealtimeStockPrices.md)
 - [ApiResponseStockExchangeSecurities](docs/ApiResponseStockExchangeSecurities.md)
 - [ApiResponseStockExchangeStockPriceAdjustments](docs/ApiResponseStockExchangeStockPriceAdjustments.md)
 - [ApiResponseStockExchangeStockPrices](docs/ApiResponseStockExchangeStockPrices.md)
 - [ApiResponseStockExchanges](docs/ApiResponseStockExchanges.md)
 - [ApiResponseStockMarketIndexHistoricalData](docs/ApiResponseStockMarketIndexHistoricalData.md)
 - [ApiResponseStockMarketIndices](docs/ApiResponseStockMarketIndices.md)
 - [ApiResponseStockMarketIndicesSearch](docs/ApiResponseStockMarketIndicesSearch.md)
 - [Company](docs/Company.md)
 - [CompanyFiling](docs/CompanyFiling.md)
 - [CompanyNews](docs/CompanyNews.md)
 - [CompanyNewsSummary](docs/CompanyNewsSummary.md)
 - [CompanySummary](docs/CompanySummary.md)
 - [DataTag](docs/DataTag.md)
 - [DataTagSummary](docs/DataTagSummary.md)
 - [DividendRecord](docs/DividendRecord.md)
 - [EarningsRecord](docs/EarningsRecord.md)
 - [EconomicIndex](docs/EconomicIndex.md)
 - [EconomicIndexSummary](docs/EconomicIndexSummary.md)
 - [Filing](docs/Filing.md)
 - [FilingNote](docs/FilingNote.md)
 - [FilingNoteFiling](docs/FilingNoteFiling.md)
 - [FilingNoteSummary](docs/FilingNoteSummary.md)
 - [FilingSummary](docs/FilingSummary.md)
 - [ForexCurrency](docs/ForexCurrency.md)
 - [ForexPair](docs/ForexPair.md)
 - [ForexPrice](docs/ForexPrice.md)
 - [Fundamental](docs/Fundamental.md)
 - [FundamentalSummary](docs/FundamentalSummary.md)
 - [HistoricalData](docs/HistoricalData.md)
 - [IntradayStockPrice](docs/IntradayStockPrice.md)
 - [Municipality](docs/Municipality.md)
 - [MunicipalityFinancial](docs/MunicipalityFinancial.md)
 - [RealtimeStockPrice](docs/RealtimeStockPrice.md)
 - [RealtimeStockPriceSecurity](docs/RealtimeStockPriceSecurity.md)
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

