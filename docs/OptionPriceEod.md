

[//]: # (CLASS:OptionPriceEod)

[//]: # (KIND:object)

### OptionPriceEod

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**date** | str | The date of the price, in the format YYYY-MM-DD &nbsp;
**close** | float | The closing price of the options contract. &nbsp;
**close_bid** | float | The closing bid price of the options contract. &nbsp;
**close_ask** | float | The closing ask price of the options contract. &nbsp;
**volume** | int | The cumulative volume of this options contract that traded that day. &nbsp;
**open** | float | The price at the beginning of the period &nbsp;
**open_ask** | float | The ask at the beginning of the period &nbsp;
**open_bid** | float | The bid at the beginning of the period &nbsp;
**open_interest** | int | The total number of this options contract that are still open. &nbsp;
**high** | float | The highest price over the span of the period &nbsp;
**low** | float | The highest price over the span of the period &nbsp;
**mark** | float | The mid price between the latest bid and ask spread &nbsp;
**ask_high** | float | The highest ask over the span of the period &nbsp;
**ask_low** | float | The lowest ask over the span of the period &nbsp;
**bid_high** | float | The highest bid over the span of the period &nbsp;
**bid_low** | object | The lowest bid over the span of the period &nbsp;
**implied_volatility** | float | The implied volatility of the contract calculated using the Black-Scholes Model. &nbsp;
**delta** | float | Delta represents the rate of change between the option&#39;s price and a $1 change in the underlying asset&#39;s price. &nbsp;
**gamma** | float | Gamma represents the rate of change between an option&#39;s delta and the underlying asset&#39;s price. &nbsp;
**theta** | float | Theta represents the rate of change between the option price and time, or time sensitivity - sometimes known as an option&#39;s time decay. &nbsp;
**vega** | float | Vega represents the rate of change between an option&#39;s value and the underlying asset&#39;s implied volatility. &nbsp;

[//]: # (END_DEFINITION)



