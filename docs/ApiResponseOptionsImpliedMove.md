

[//]: # (CLASS:ApiResponseOptionsImpliedMove)

[//]: # (KIND:object)

### ApiResponseOptionsImpliedMove

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**implied_move** | [**OptionImpliedMoveData**](OptionImpliedMoveData.md) | The data pertaining to the implied move. &nbsp;
**messages** | list[str] | Any messages or warnings about the data &nbsp;
**underlying_price** | float | The price of the underlying instrument. &nbsp;
**expiration** | str | The date on which the Option expires. The Option becomes invalid after this date and cannot be exercised. &nbsp;
**atm_strike** | float | The at-the-money strike price for the implied move calculation. &nbsp;
**straddle_price** | float | The straddle price for the implied move calculation. &nbsp;
**symbol** | str | The symbol for the underlying instrument. &nbsp;

[//]: # (END_DEFINITION)


[//]: # (CONTAINED_CLASS:OptionImpliedMoveData)



