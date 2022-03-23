

[//]: # (CLASS:InsiderTransactionFiling)

[//]: # (KIND:object)

### InsiderTransactionFiling

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**filing_url** | str | The URL of the filing with the SEC &nbsp;
**issuer_ticker** | str | The ticker of the issuing company. &nbsp;
**issuer_cik** | str | The Central Index Key (CIK) of the issuing company. &nbsp;
**issuer_company** | str | The name of the issuing company. &nbsp;
**transactions** | [**list[InsiderTransaction]**](InsiderTransaction.md) | The insider transactions associated with the filing &nbsp;
**company** | [**CompanySummary**](CompanySummary.md) | The company associated with the filing &nbsp;
**owner** | [**OwnerSummary**](OwnerSummary.md) | The owner associated with the filing &nbsp;

[//]: # (END_DEFINITION)


[//]: # (CONTAINED_CLASS:InsiderTransaction)


[//]: # (CONTAINED_CLASS:CompanySummary)


[//]: # (CONTAINED_CLASS:OwnerSummary)



