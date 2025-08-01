

[//]: # (CLASS:Fundamental)

[//]: # (KIND:object)

### Fundamental

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**id** | str | The Intrinio ID of the Fundamental &nbsp;
**statement_code** | str | The code of the financial statement that the Fundamental represents &nbsp;
**fiscal_year** | float | The fiscal year &nbsp;
**fiscal_period** | str | The fiscal period &nbsp;
**type** | str | The type of Fundamental &nbsp;
**start_date** | date | The period start date &nbsp;
**end_date** | date | The period start date &nbsp;
**filing_date** | datetime | The date and time when the Fundamental was filed with the SEC &nbsp;
**is_latest** | bool | Is this the latest fundamental available based on the company&#39;s most recent filings? Use the Lookup Fundamental endpoint to find the latest fundamental (&lt;a href&#x3D;\&quot;https://docs.intrinio.com/documentation/web_api/lookup_fundamental_v2\&quot; target&#x3D;\&quot;_blank\&quot;&gt;reference&lt;/a&gt;) &nbsp;
**updated_date** | datetime | The date and time when the fundamental was last updated &nbsp;
**first_calculable** | datetime | The date and time when the fundamental was first calculable &nbsp;
**earnings_disclosed_at** | datetime | The date and time when the earnings information was first disclosed via 8-K filing &nbsp;
**company** | [**CompanySummary**](CompanySummary.md) | The Company that the Fundamental was belongs to &nbsp;

[//]: # (END_DEFINITION)


[//]: # (CONTAINED_CLASS:CompanySummary)



