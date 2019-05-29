

[//]: # (CLASS:EarningsRecord)

[//]: # (KIND:object)

### EarningsRecord

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**quarter** | str | The letter “Q” followed by the quarter number the earnings information applies to &nbsp;
**time_of_day** | str | Indicates the time of the announcement &nbsp;
**broadcast_url** | str | Link for Conference Call recording &nbsp;
**transcript_url** | str | Link to the earnings release transcript &nbsp;
**transcript_quarter** | str | The letter “Q” followed by the quarter number the earnings transcript applies to &nbsp;
**transcript_fiscal_year** | str | Fiscal year in YYYY format for the earnings transcript &nbsp;
**conference_call_date** | date | Date of the conference call &nbsp;
**conference_call_time** | str | Published time of the conference call &nbsp;
**conference_call_phone_number** | str | Publicly available phone number for replay conference call &nbsp;
**conference_call_passcode** | str | Passcode for replay conference call &nbsp;
**last_confirmation_date** | date | Date of last earnings date update by a WSH analyst &nbsp;
**board_of_directors_meeting_date** | date | Date of Board/Shareholder Meeting &nbsp;
**board_of_directors_meeting_type** | str | The type of meeting - \&quot;B\&quot; indicates a Board of Directors meeting and \&quot;S\&quot; indicates a Shareholder meeting &nbsp;
**company_website** | str | Website link for the company &nbsp;
**q1_date** | date | Earnings Date for 1st quarter &nbsp;
**q2_date** | date | Earnings Date for 2nd quarter &nbsp;
**q3_date** | date | Earnings Date for 3rd quarter &nbsp;
**q4_date** | date | Earnings Date for 4th quarter &nbsp;
**type** | str | The nature of the next reported earnings date - \&quot;V\&quot; indicates a Verified date, \&quot;T\&quot; indicates that the date was gathered from the company, but is still considered Tentative, and \&quot;I\&quot; indicates that the date is forecased or Inferred &nbsp;
**next_earnings_date** | date | Next earnings date &nbsp;
**next_earnings_quarter** | str | The quarter of the next earnings release &nbsp;
**next_earnings_fiscal_year** | int | The fiscal year associated with next earnings date and next earnings quarter &nbsp;
**security** | [**SecuritySummary**](SecuritySummary.md) |  &nbsp;

[//]: # (END_DEFINITION)


[//]: # (CONTAINED_CLASS:SecuritySummary)



