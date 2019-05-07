## StockPriceSummary

### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **date** | The calendar date that the stock price represents. For non-daily stock prices, this represents the last day in the period (end of the week, month, quarter, year, etc) | [optional] 
**intraperiod** | **bool** | If true, the stock price represents an unfinished period (be it day, week, quarter, month, or year), meaning that the close price is the latest price available, not the official close price for the period | [optional] 
**frequency** | **str** | The type of period that the stock price represents | [optional] 
**open** | **float** | The price at the beginning of the period | [optional] 
**high** | **float** | The highest price over the span of the period | [optional] 
**low** | **float** | The lowest price over the span of the period | [optional] 
**close** | **float** | The price at the end of the period | [optional] 
**volume** | **float** | The number of shares exchanged during the period | [optional] 
**adj_open** | **float** | The price at the beginning of the period, adjusted for splits and dividends | [optional] 
**adj_high** | **float** | The highest price over the span of the period, adjusted for splits and dividends | [optional] 
**adj_low** | **float** | The lowest price over the span of the period, adjusted for splits and dividends | [optional] 
**adj_close** | **float** | The price at the end of the period, adjusted for splits and dividends | [optional] 
**adj_volume** | **float** | The number of shares exchanged during the period, adjusted for splits and dividends | [optional] 



