# ZacksSalesSurpriseSummary

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
**last_rev_date** | **date** | The last revision date for the analyst estimates | [optional] 
**sales_actual** | **float** | The actual Non-GAAP sales figure released by the company, interpreted by Zacks. | [optional] 
**sales_actual_zacks_adj** | **float** | The adjustments Zacks made to get to Non-GAAP sales to reconcile with GAAP sales. | [optional] 
**sales_actual_gaap** | **float** | The actual GAAP sales figured released by the company | [optional] 
**sales_mean_estimate** | **float** | The pre-earnings release mean sales estimate for the company sales_count_estimate; the pre-earnings release number of estimates by analysts | [optional] 
**sales_amount_diff** | **float** | The sales surprise amount difference | [optional] 
**sales_percent_diff** | **float** | The sales surprise percent difference | [optional] 
**sales_std_dev_estimate** | **float** | The pre-earnings release standard deviation of sales estimates | [optional] 
**security** | [**SecuritySummary**](SecuritySummary.md) | The Security of the Zacks Sales Surprise | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


