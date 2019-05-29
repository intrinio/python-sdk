

[//]: # (CLASS:ZacksEPSSurprise)

[//]: # (KIND:object)

### ZacksEPSSurprise

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**id** | str | The Intrinio ID for the record &nbsp;
**fiscal_year** | float | The company’s fiscal year for the reported period &nbsp;
**fiscal_quarter** | str | The company’s fiscal quarter for the reported period &nbsp;
**calendar_year** | float | The closest calendar year for the company’s fiscal year &nbsp;
**calendar_quarter** | str | The closest calendar quarter for the company’s fiscal year &nbsp;
**actual_reported_date** | date | The actual report date for the earnings release &nbsp;
**actual_reported_time** | str | The actual report time for the earnings release &nbsp;
**actual_reported_code** | str | The code cooresponding to the earnings release  BTO &#x3D; BEFORE THE OPEN | DTM &#x3D; DURING THE MARKET | AMC &#x3D; AFTER MARKET CLOSE &nbsp;
**actual_reported_desc** | str | The description for the type of earnings release &nbsp;
**eps_actual** | float | The actual Non-GAAP EPS figure released by the company, interpreted by Zacks. &nbsp;
**eps_actual_zacks_adj** | float | The adjustments Zacks made to get to Non-GAAP EPS to reconcile with GAAP EPS. &nbsp;
**eps_mean_estimate** | float | The pre-earnings release mean EPS estimate for the company &nbsp;
**eps_amount_diff** | float | The EPS surprise amount difference &nbsp;
**eps_percent_diff** | float | The EPS surprise percent difference &nbsp;
**eps_count_estimate** | float | The pre-earnings release number of estimates by analysts &nbsp;
**eps_std_dev_estimate** | float | The pre-earnings release standard deviation of EPS estimates &nbsp;
**security** | [**SecuritySummary**](SecuritySummary.md) | The Security of the Zacks EPS Surprise &nbsp;

[//]: # (END_DEFINITION)


[//]: # (CONTAINED_CLASS:SecuritySummary)



