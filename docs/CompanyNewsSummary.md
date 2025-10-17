

[//]: # (CLASS:CompanyNewsSummary)

[//]: # (KIND:object)

### CompanyNewsSummary

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**id** | str | The Intrinio ID for the news article &nbsp;
**title** | str | The title of the news article &nbsp;
**publication_date** | datetime | The publication date of the news article &nbsp;
**companies** | [**list[CompanySummary]**](CompanySummary.md) | The Companies to which the new article pertains &nbsp;
**securities** | [**list[SecuritySummary]**](SecuritySummary.md) | The Securities to which the new article pertains &nbsp;
**url** | str | The url of the news article &nbsp;
**summary** | str | A summary of the news article &nbsp;
**source** | str | The news source. &nbsp;
**topics** | [**list[NewsTopic]**](NewsTopic.md) |  &nbsp;
**copyright** | str | The copyright of the news article &nbsp;
**language** | str | The language code of the news article &nbsp;
**word_count** | int | The word count of the news article &nbsp;
**spam** | bool | Whether the news article is marked as spam or not &nbsp;
**business_relevance** | float | How strongly correlated the news article is to the business &nbsp;
**article_sentiment** | str | The news sentiment. &nbsp;
**article_sentiment_confidence** | float | The confidence score of the sentiment rating &nbsp;
**issuer** | str | The issuer of the story. &nbsp;
**issuer_name** | str | The issuer of the story. &nbsp;
**issuer_company** | [**CompanySummary**](CompanySummary.md) | The company that issued the story. &nbsp;
**issuer_security** | [**SecuritySummary**](SecuritySummary.md) | The security that issued the story. &nbsp;

[//]: # (END_DEFINITION)


[//]: # (CONTAINED_CLASS:CompanySummary)


[//]: # (CONTAINED_CLASS:SecuritySummary)


[//]: # (CONTAINED_CLASS:NewsTopic)


[//]: # (CONTAINED_CLASS:CompanySummary)


[//]: # (CONTAINED_CLASS:SecuritySummary)



