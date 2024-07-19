

[//]: # (CLASS:Security)

[//]: # (KIND:object)

### Security

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**id** | str | The Intrinio ID for the Security &nbsp;
**company_id** | str | The Intrinio ID for the company for which the Security is issued &nbsp;
**name** | str | The name of the Security &nbsp;
**type** | str | The Security&#39;s type &nbsp;
**code** | str | A 2-3 digit code classifying the Security (&lt;a href&#x3D;\&quot;https://docs.intrinio.com/documentation/security_codes\&quot; target&#x3D;\&quot;_blank\&quot;&gt;reference&lt;/a&gt;) &nbsp;
**share_class** | str | The Security&#39;s share class (if applicable) &nbsp;
**currency** | str | The currency in which the Security is traded on the exchange &nbsp;
**round_lot_size** | float | The normal unit of trading &nbsp;
**ticker** | str | The common ticker &nbsp;
**exchange_ticker** | str | The exchange-level ticker &nbsp;
**composite_ticker** | str | The country-composite ticker &nbsp;
**alternate_tickers** | list[str] | Alternate formats of the common ticker &nbsp;
**figi** | str | The exchange-level OpenFIGI identifier &nbsp;
**cik** | str | Central Index Key issued by the SEC, which is the unique identifier for all owner filings &nbsp;
**composite_figi** | str | The country-composite OpenFIGI identifier &nbsp;
**share_class_figi** | str | The global-composite OpenFIGI identifier &nbsp;
**figi_uniqueid** | str | The OpenFIGI unique ID &nbsp;
**active** | bool | If true, the Security is active and has been recently traded &nbsp;
**etf** | bool | If true, this Security is an ETF &nbsp;
**delisted** | bool | If true, the Security is no longer traded on the exchange &nbsp;
**primary_listing** | bool | If true, the Security is the primary issue for the company, otherwise it is a secondary issue on a secondary stock exchange &nbsp;
**primary_security** | bool | If true, the Security is considered by Intrinio to be the primary Security for its company &nbsp;
**first_stock_price** | date | The date of the first recorded stock price &nbsp;
**last_stock_price** | date | The date of the last recorded stock price (or the most recent trading day) &nbsp;
**last_stock_price_adjustment** | date | The date of the last stock price adjustment (dividend, split, etc) &nbsp;
**last_corporate_action** | date | The date of the last corporate action &nbsp;
**previous_tickers** | list[str] | Previous tickers used by this security &nbsp;
**listing_exchange_mic** | str | The MIC code of the exchange on which this security primarily trades &nbsp;

[//]: # (END_DEFINITION)



