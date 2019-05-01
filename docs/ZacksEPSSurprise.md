# ZacksEPSSurprise

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Intrinio ID for the record | [optional] 
**fiscal_year** | **float** | The company’s fiscal year for the reported period | [optional] 
**fiscal_quarter** | **str** | The company’s fiscal quarter for the reported period | [optional] 
**calendar_year** | **float** | The closest calendar year for the company’s fiscal year | [optional] 
**calendar_quarter** | **str** | The closest calendar quarter for the company’s fiscal year | [optional] 
**actual_reported_date** | **date** | The actual report date for the earnings release | [optional] 
**actual_reported_time** | **str** | The actual report time for the earnings release | [optional] 
**actual_reported_code** | **str** | The code cooresponding to the earnings release  BTO &#x3D; BEFORE THE OPEN | DTM &#x3D; DURING THE MARKET | AMC &#x3D; AFTER MARKET CLOSE | [optional] 
**actual_reported_desc** | **str** | The description for the type of earnings release | [optional] 
**eps_actual** | **float** | The actual Non-GAAP EPS figure released by the company, interpreted by Zacks. | [optional] 
**eps_actual_zacks_adj** | **float** | The adjustments Zacks made to get to Non-GAAP EPS to reconcile with GAAP EPS. | [optional] 
**eps_mean_estimate** | **float** | The pre-earnings release mean EPS estimate for the company | [optional] 
**eps_amount_diff** | **float** | The EPS surprise amount difference | [optional] 
**eps_percent_diff** | **float** | The EPS surprise percent difference | [optional] 
**eps_count_estimate** | **float** | The pre-earnings release number of estimates by analysts | [optional] 
**eps_std_dev_estimate** | **float** | The pre-earnings release standard deviation of EPS estimates | [optional] 
**security** | [**SecuritySummary**](SecuritySummary.md) | The Security of the Zacks EPS Surprise | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


