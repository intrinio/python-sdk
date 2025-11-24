

[//]: # (CLASS:EarningsDateEstimate)

[//]: # (KIND:object)

### EarningsDateEstimate

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**fiscal_year** | int | The fiscal year for the earnings report &nbsp;
**fiscal_period** | str | The fiscal period for the earnings report (Q1, Q2, Q3, Q4, or FY) &nbsp;
**expected_date** | date | The expected date of the earnings announcement &nbsp;
**expected_8k_at** | datetime | The expected timestamp when the 8-K filing will be available &nbsp;
**historically_earliest** | str | The earliest date (MM-DD format) this company has historically announced earnings for this fiscal period &nbsp;
**historically_latest** | str | The latest date (MM-DD format) this company has historically announced earnings for this fiscal period &nbsp;
**confidence_intervals** | [**dict(str, EarningsDateEstimateConfidenceIntervals)**](EarningsDateEstimateConfidenceIntervals.md) | Confidence intervals for the expected date, sorted by confidence level (descending) &nbsp;

[//]: # (END_DEFINITION)


[//]: # (CONTAINED_CLASS:EarningsDateEstimateConfidenceIntervals)



