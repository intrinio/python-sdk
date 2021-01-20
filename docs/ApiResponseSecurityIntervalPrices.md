

[//]: # (CLASS:ApiResponseSecurityIntervalPrices)

[//]: # (KIND:object)

### ApiResponseSecurityIntervalPrices

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**intervals** | [**list[StockPriceInterval]**](StockPriceInterval.md) | Open, High, Low, Close, and Volume for a particular interval &nbsp;
**security** | [**SecuritySummary**](SecuritySummary.md) | The Security resolved from the given identifier &nbsp;
**source** | str | The source of the data &nbsp;
**next_page** | str | The token required to request the next page of the data. If null, no further results are available. &nbsp;

[//]: # (END_DEFINITION)


[//]: # (CONTAINED_CLASS:StockPriceInterval)


[//]: # (CONTAINED_CLASS:SecuritySummary)



