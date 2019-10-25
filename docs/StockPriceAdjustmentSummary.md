

[//]: # (CLASS:StockPriceAdjustmentSummary)

[//]: # (KIND:object)

### StockPriceAdjustmentSummary

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**_date** | date | The date on which the adjustment occurred. The adjustment should be applied to all stock prices before this date. &nbsp;
**factor** | float | The factor by which to multiply stock prices before this date, in order to calculate historically-adjusted stock prices. &nbsp;
**dividend** | float | The dividend amount, if a dividend was paid. &nbsp;
**dividend_currency** | str | The currency of the dividend, if known. &nbsp;
**split_ratio** | float | The ratio of the stock split, if a stock split occurred. &nbsp;

[//]: # (END_DEFINITION)



