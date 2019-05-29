

[//]: # (CLASS:ZacksAnalystRatingSnapshot)

[//]: # (KIND:object)

### ZacksAnalystRatingSnapshot

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**type** | str | The snapshot type, signifying the age of the ratings data from the snapshot date. &nbsp;
**snapshot_date** | date | The date of the snapshot, when data was recorded. &nbsp;
**rating_date** | date | The date of the latest rating for the snapshot timeframe. This is the effective date of the ratings data. &nbsp;
**mean** | float | The mean (average) weighing of analyst recommendations, from 1 (strong buy) to 5 (strong sell). &nbsp;
**percentile** | float | The percentile of the mean, derived by comparing to all securities rated by analysts as of the rating date, ranging 0.0 (strong buy) to 1.0 (strong sell). &nbsp;
**strong_buys** | int | The number of analysts recommending Strong Buy. &nbsp;
**buys** | int | The number of analysts recommending Buy. &nbsp;
**holds** | int | The number of analysts recommending Hold. &nbsp;
**sells** | int | The number of analysts recommending Sell. &nbsp;
**strong_sells** | int | The number of analysts recommending Strong Sell. &nbsp;
**total** | int | The total number of analysts recommendations. &nbsp;

[//]: # (END_DEFINITION)



