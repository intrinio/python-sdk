

[//]: # (CLASS:StockPriceInterval)

[//]: # (KIND:object)

### StockPriceInterval

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**time** | datetime | The timestamp that represents the start of the interval span. &nbsp;
**open** | float | The first traded price during the period &nbsp;
**close** | float | The last traded price during the period &nbsp;
**high** | float | The highest price over the span of the period &nbsp;
**low** | float | The lowest price over the span of the period &nbsp;
**volume** | float | The number of shares exchanged during the period &nbsp;
**close_time** | datetime | The timestamp that represents the end of the interval span. &nbsp;
**interval** | str | The size of the interval. &nbsp;
**average** | float | The average trade price of an individual stock during the interval. &nbsp;
**change** | float | The change ratio from open to close.  ((Close - Open)/Open). &nbsp;
**bid_high** | float | The highest bid price from the interval. &nbsp;
**bid_low** | float | The lowest bid price from the interval. &nbsp;
**bid_close** | float | The last bid price from the interval. &nbsp;
**bid_open** | float | The first bid price from the interval. &nbsp;
**bid_first_time** | datetime | The timestamp that represents the first bid time from the interval span. &nbsp;
**bid_last_time** | datetime | The timestamp that represents the last bid time from the interval span. &nbsp;
**bid_change_percent** | float | The ratio of the close to open bid difference, in percent. &nbsp;
**ask_high** | float | The highest ask price from the interval. &nbsp;
**ask_low** | float | The lowest ask price from the interval. &nbsp;
**ask_close** | float | The last ask price from the interval. &nbsp;
**ask_open** | float | The first ask price from the interval. &nbsp;
**ask_first_time** | datetime | The timestamp that represents the first ask time from the interval span. &nbsp;
**ask_last_time** | datetime | The timestamp that represents the last ask time from the interval span. &nbsp;
**ask_change_percent** | float | The ratio of the close to open ask difference, in percent. &nbsp;

[//]: # (END_DEFINITION)



