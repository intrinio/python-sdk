

[//]: # (CLASS:OptionSurfaceDatum)

[//]: # (KIND:object)

### OptionSurfaceDatum

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**strike_price** | float | The actual strike price.  Present when the requesting surface type is raw. &nbsp;
**unix_timestamp** | float | The expiration DateTime.  Present when the requesting surface type is raw. &nbsp;
**forward_natural_log_moneyness** | float | The natural logarithm of forward moneyness, calculated as ln(F / K), where F is the forward underlying price adjusted for risk-free rate and dividend yield over time to expiration, and K is the option strike. Present when the requesting surface type is something other than raw. &nbsp;
**square_root_tau** | float | The square root of tau, where tau is the option’s time to expiration in years using a 365.25-day year basis. Present when the requesting surface type is something other than raw. &nbsp;
**implied_volatility** | float | The implied volatility of the contract calculated using the Black-Scholes Model, and smoothed if the requesting surface type was logarithmic_smoothed. Always present. &nbsp;

[//]: # (END_DEFINITION)



