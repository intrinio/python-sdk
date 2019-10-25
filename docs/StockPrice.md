

[//]: # (CLASS:StockPrice)

[//]: # (KIND:object)

### StockPrice

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**_date** | date | The calendar date that the stock price represents. For non-daily stock prices, this represents the last day in the period (end of the week, month, quarter, year, etc) &nbsp;
**intraperiod** | bool | If true, the stock price represents an unfinished period (be it day, week, quarter, month, or year), meaning that the close price is the latest price available, not the official close price for the period &nbsp;
**frequency** | str | The type of period that the stock price represents &nbsp;
**open** | float | The price at the beginning of the period &nbsp;
**high** | float | The highest price over the span of the period &nbsp;
**low** | float | The lowest price over the span of the period &nbsp;
**close** | float | The price at the end of the period &nbsp;
**volume** | float | The number of shares exchanged during the period &nbsp;
**adj_open** | float | The price at the beginning of the period, adjusted for splits and dividends &nbsp;
**adj_high** | float | The highest price over the span of the period, adjusted for splits and dividends &nbsp;
**adj_low** | float | The lowest price over the span of the period, adjusted for splits and dividends &nbsp;
**adj_close** | float | The price at the end of the period, adjusted for splits and dividends &nbsp;
**adj_volume** | float | The number of shares exchanged during the period, adjusted for splits and dividends &nbsp;
**security** | [**SecuritySummary**](SecuritySummary.md) | The Security of the stock price &nbsp;

[//]: # (END_DEFINITION)


[//]: # (CONTAINED_CLASS:SecuritySummary)



