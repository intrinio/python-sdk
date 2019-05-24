# ZacksAnalystRatingSnapshot

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The snapshot type, signifying the age of the ratings data from the snapshot date. | [optional] 
**snapshot_date** | **date** | The date of the snapshot, when data was recorded. | [optional] 
**rating_date** | **date** | The date of the latest rating for the snapshot timeframe. This is the effective date of the ratings data. | [optional] 
**mean** | **float** | The mean (average) weighing of analyst recommendations, from 1 (strong buy) to 5 (strong sell). | [optional] 
**percentile** | **float** | The percentile of the mean, derived by comparing to all securities rated by analysts as of the rating date, ranging 0.0 (strong buy) to 1.0 (strong sell). | [optional] 
**strong_buys** | **int** | The number of analysts recommending Strong Buy. | [optional] 
**buys** | **int** | The number of analysts recommending Buy. | [optional] 
**holds** | **int** | The number of analysts recommending Hold. | [optional] 
**sells** | **int** | The number of analysts recommending Sell. | [optional] 
**strong_sells** | **int** | The number of analysts recommending Strong Sell. | [optional] 
**total** | **int** | The total number of analysts recommendations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


