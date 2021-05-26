

[//]: # (CLASS:StockPriceSummary)

[//]: # (KIND:object)

### StockPriceSummary

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**date** | date | The calendar date that the stock price represents. For non-daily stock prices, this represents the last day in the period (end of the week, month, quarter, year, etc) &nbsp;
**intraperiod** | bool | If True, the stock price represents an unfinished period (be it day, week, quarter, month, or year), meaning that the close price is the latest price available, not the official close price for the period &nbsp;
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
**factor** | float | The factor by which to multiply stock prices before this date, in order to calculate historically-adjusted stock prices. &nbsp;
**split_ratio** | float | The ratio of the stock split, if a stock split occurred. &nbsp;
**dividend** | float | The dividend amount, if a dividend was paid. &nbsp;
**change** | float | The difference in price from the last price for this frequency &nbsp;
**percent_change** | float | The percent difference in price from the last price for this frequency &nbsp;
**fifty_two_week_high** | float | The 52 week high price (daily only) &nbsp;
**fifty_two_week_low** | float | The 52 week low price (daily only) &nbsp;

[//]: # (END_DEFINITION)



