

[//]: # (CLASS:ApiResponseSecurityTradingStatus)

[//]: # (KIND:object)

### ApiResponseSecurityTradingStatus

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**trading_status** | str | The trading status of the security. &nbsp;
**trading_status_reason** | str | The exchange supplied reason for its current status. &nbsp;
**trading_status_updated_on** | datetime | The time the exchange reported that it changed its trading status. &nbsp;
**security** | [**SecuritySummary**](SecuritySummary.md) | The Security resolved from the given identifier &nbsp;
**market_status** | str | The status of the market. &nbsp;
**messages** | list[str] | A list of messages related to the request, such as warnings or errors. &nbsp;

[//]: # (END_DEFINITION)


[//]: # (CONTAINED_CLASS:SecuritySummary)



