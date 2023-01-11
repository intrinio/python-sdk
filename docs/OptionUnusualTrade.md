

[//]: # (CLASS:OptionUnusualTrade)

[//]: # (KIND:object)

### OptionUnusualTrade

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**symbol** | str | The underlying option security symbol for the trade &nbsp;
**timestamp** | date | The UTC timestamp of order placement &nbsp;
**type** | str | The type of unusual trade &nbsp;
**total_value** | float | The aggregated value of all option contract premiums included in the trade &nbsp;
**total_size** | float | The total number of contracts involved in a single transaction &nbsp;
**average_price** | float | The average premium paid per option contract &nbsp;
**contract** | str | The option contract symbol &nbsp;
**ask_at_execution** | float | Ask price at execution &nbsp;
**bid_at_execution** | float | Bid price at execution &nbsp;
**sentiment** | str | Bullish, Bearish, or Neutral Sentiment is estimated based on whether the trade was executed at the bid, ask, or mark price. &nbsp;
**underlying_price_at_execution** | float | Price of the underlying security at execution of trade &nbsp;

[//]: # (END_DEFINITION)



