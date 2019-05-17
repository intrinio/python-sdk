### StockPriceAdjustmentSummary

#### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **date** | The date on which the adjustment occurred. The adjustment should be applied to all stock prices before this date. | [optional] 
**factor** | **float** | The factor by which to multiply stock prices before this date, in order to calculate historically-adjusted stock prices. | [optional] 
**dividend** | **float** | The dividend amount, if a dividend was paid. | [optional] 
**dividend_currency** | **str** | The currency of the dividend, if known. | [optional] 
**split_ratio** | **float** | The ratio of the stock split, if a stock split occurred. | [optional] 



