## ApiResponseCryptoBook

### Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bids** | [**list[CryptoBookEntry]**](CryptoBookEntry.md) | The bid prices and their respective sizes, in descending order of price. | [optional] 
**asks** | [**list[CryptoBookEntry]**](CryptoBookEntry.md) | The ask prices and their respective sizes, in ascending order of price. | [optional] 
**pair** | [**CryptoPairSummary**](CryptoPairSummary.md) |  | [optional] 
**exchange** | [**CryptoExchangeSummary**](CryptoExchangeSummary.md) |  | [optional] 
**last_updated** | **str** | The UTC timestamp of when the order book was last updated. | [optional] 



