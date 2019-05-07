## EarningsRecord

### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quarter** | **str** | The letter “Q” followed by the quarter number the earnings information applies to | [optional] 
**time_of_day** | **str** | Indicates the time of the announcement | [optional] 
**broadcast_url** | **str** | Link for Conference Call recording | [optional] 
**transcript_url** | **str** | Link to the earnings release transcript | [optional] 
**transcript_quarter** | **str** | The letter “Q” followed by the quarter number the earnings transcript applies to | [optional] 
**transcript_fiscal_year** | **str** | Fiscal year in YYYY format for the earnings transcript | [optional] 
**conference_call_date** | **date** | Date of the conference call | [optional] 
**conference_call_time** | **str** | Published time of the conference call | [optional] 
**conference_call_phone_number** | **str** | Publicly available phone number for replay conference call | [optional] 
**conference_call_passcode** | **str** | Passcode for replay conference call | [optional] 
**last_confirmation_date** | **date** | Date of last earnings date update by a WSH analyst | [optional] 
**board_of_directors_meeting_date** | **date** | Date of Board/Shareholder Meeting | [optional] 
**board_of_directors_meeting_type** | **str** | The type of meeting - \&quot;B\&quot; indicates a Board of Directors meeting and \&quot;S\&quot; indicates a Shareholder meeting | [optional] 
**company_website** | **str** | Website link for the company | [optional] 
**q1_date** | **date** | Earnings Date for 1st quarter | [optional] 
**q2_date** | **date** | Earnings Date for 2nd quarter | [optional] 
**q3_date** | **date** | Earnings Date for 3rd quarter | [optional] 
**q4_date** | **date** | Earnings Date for 4th quarter | [optional] 
**type** | **str** | The nature of the next reported earnings date - \&quot;V\&quot; indicates a Verified date, \&quot;T\&quot; indicates that the date was gathered from the company, but is still considered Tentative, and \&quot;I\&quot; indicates that the date is forecased or Inferred | [optional] 
**next_earnings_date** | **date** | Next earnings date | [optional] 
**next_earnings_quarter** | **str** | The quarter of the next earnings release | [optional] 
**next_earnings_fiscal_year** | **int** | The fiscal year associated with next earnings date and next earnings quarter | [optional] 
**security** | [**SecuritySummary**](SecuritySummary.md) |  | [optional] 



