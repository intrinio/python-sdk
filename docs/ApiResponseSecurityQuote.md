

[//]: # (CLASS:ApiResponseSecurityQuote)

[//]: # (KIND:object)

### ApiResponseSecurityQuote

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**security** | [**SecuritySummary**](SecuritySummary.md) | The Security of the stock quote &nbsp;
**last** | float | The price of the latest trade &nbsp;
**last_time** | datetime | The date and time when the last trade occurred. &nbsp;
**source** | str | The source of the pricing data. &nbsp;
**open** | float | The open price from the latest day of trading. &nbsp;
**high** | float | The highest price from the latest day of trading. &nbsp;
**low** | float | The lowest price from the latest day of trading. &nbsp;
**exchange_volume** | float | The volume of the security from the source. &nbsp;
**market_volume** | float | The volume of the security for the entire market. &nbsp;
**eod_fifty_two_week_high** | float | The 52 week high price. &nbsp;
**eod_fifty_two_week_low** | float | The 52 week low price. &nbsp;
**marketcap** | float | The current market cap. &nbsp;
**pricetoearnings** | float | The current price to earnings. &nbsp;
**previous_close** | float | The previous close price. &nbsp;
**previous_close_date** | date | The date of the previous close. &nbsp;
**change** | float | The difference in last price from the last close price &nbsp;
**change_percent** | float | The percent difference in last price from the last close price &nbsp;
**adj_close_5_days_ago** | float | The adjusted close price 5 days ago. &nbsp;
**adj_close_30_days_ago** | float | The adjusted close price 30 days ago. &nbsp;
**adj_close_90_days_ago** | float | The adjusted close price 90 days ago. &nbsp;
**adj_close_180_days_ago** | float | The adjusted close price 180 days ago. &nbsp;
**adj_close_365_days_ago** | float | The adjusted close price 365 days ago. &nbsp;
**adj_close_730_days_ago** | float | The adjusted close price 730 days ago. &nbsp;
**adj_close_1825_days_ago** | float | The adjusted close price 1825 days ago. &nbsp;
**adj_close_year_to_date** | float | The adjusted close price at the start of the calendar year. &nbsp;
**change_percent_5_days** | float | The percent change from the adjusted price 5 days ago to now. &nbsp;
**change_percent_30_days** | float | The percent change from the adjusted price 30 days ago to now. &nbsp;
**change_percent_90_days** | float | The percent change from the adjusted price 90 days ago to now. &nbsp;
**change_percent_180_days** | float | The percent change from the adjusted price 180 days ago to now. &nbsp;
**change_percent_365_days** | float | The percent change from the adjusted price 365 days ago to now. &nbsp;
**change_percent_730_days_ago** | float | The percent change from the adjusted price 730 days ago to now. &nbsp;
**change_percent_1825_days** | float | The percent change from the adjusted price 1825 days ago to now. &nbsp;
**change_percent_year_to_date** | float | The percent change from the adjusted price since the start of the calendar year to now. &nbsp;
**extended_hours_last** | float | The price of the latest trade in pre and post market trading.  Might be null during normal trading &nbsp;
**extended_hours_change** | float | The difference in extended_hours_last price from most recent official close price &nbsp;
**extended_hours_change_percent** | float | The percent difference in extended_hours_last from the most recent official close price &nbsp;

[//]: # (END_DEFINITION)


[//]: # (CONTAINED_CLASS:SecuritySummary)



