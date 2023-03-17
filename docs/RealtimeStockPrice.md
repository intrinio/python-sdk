

[//]: # (CLASS:RealtimeStockPrice)

[//]: # (KIND:object)

### RealtimeStockPrice

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**last_price** | float | The price of the last trade. &nbsp;
**last_time** | datetime | The date and time when the last trade occurred. &nbsp;
**last_size** | float | The size of the last trade. &nbsp;
**bid_price** | float | The price of the top bid order. &nbsp;
**bid_size** | float | The size of the top bid order. &nbsp;
**ask_price** | float | The price of the top ask order. &nbsp;
**ask_size** | float | The size of the top ask order. &nbsp;
**open_price** | float | The price at the open of the trading day. &nbsp;
**close_price** | float | The price at the close of the trading day. (IEX only) &nbsp;
**high_price** | float | The high price for the trading day. &nbsp;
**low_price** | float | The low price for the trading day. &nbsp;
**exchange_volume** | float | The number of shares exchanged during the trading day on the exchange. &nbsp;
**market_volume** | float | The number of shares exchanged during the trading day for the whole market. &nbsp;
**updated_on** | datetime | The date and time when the data was last updated. &nbsp;
**source** | str | The source of the data. &nbsp;
**listing_venue** | str | The venue the price came from. &nbsp;
**sales_conditions** | str | The condition for the sale. &nbsp;
**quote_conditions** | str | The condition for the quote. &nbsp;
**market_center_code** | str | The market center character code. &nbsp;
**is_darkpool** | bool | Whether or not the current trade is from a darkpool or not. &nbsp;
**security** | [**RealtimeStockPriceSecurity**](RealtimeStockPriceSecurity.md) |  &nbsp;

[//]: # (END_DEFINITION)


[//]: # (CONTAINED_CLASS:RealtimeStockPriceSecurity)



