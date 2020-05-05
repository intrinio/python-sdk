

[//]: # (CLASS:ZacksInstitutionalHoldingOwnerDetail)

[//]: # (KIND:object)

### ZacksInstitutionalHoldingOwnerDetail

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**name** | str | The owner&#39;s name &nbsp;
**cik** | str | The Central Index Key (CIK) assigned to the company by the SEC as a unique identifier, used in SEC filings &nbsp;
**address** | str | The owner&#39;s address &nbsp;
**city_state** | str | The owner&#39;s city and state (City, ST) &nbsp;
**location_code** | str | The owner&#39;s location code. (&#39;D&#39; &#x3D; Domestic, &#39;C&#39; &#x3D; Canadian, &#39;F&#39; &#x3D; Foreign) &nbsp;
**phone_number** | str | The owner&#39;s phone number &nbsp;
**postal_code** | str | The owner&#39;s postal code &nbsp;
**url** | str | The owner&#39;s website url &nbsp;
**investment_style** | str | The owner&#39;s investment style (&#39;I&#39; &#x3D; Income, &#39;V&#39; &#x3D; Value, &#39;G&#39; &#x3D; Growth, &#39;B&#39; &#x3D;  Growth at a Reasonable Price, &#39;A&#39; &#x3D; Aggressive Growth, &#39;P&#39; &#x3D; Passive/Index, &#39;D&#39; &#x3D; Deep Value) &nbsp;
**number_of_holdings** | float | Count of equity holdings only, doesn&#39;t include bonds or other funds held &nbsp;
**total_holdings_value** | float | Market value of equity holdings in 1,000s. Sum of shares held times last close price. &nbsp;
**portfolio_turnover_percent** | float | Annual portfolio turnover in terms of percentage of total value. &nbsp;
**is_fund** | str | If &#39;Y&#39;, the owner is a fund? (&#39;Y&#39; &#x3D; Yes, &#39;N&#39; &#x3D; No) &nbsp;
**fund_ticker** | str | Fund ticker if the institution is a fund &nbsp;
**has_fund_manager** | str | Does the fund have a manager. (&#39;Y&#39; &#x3D; Yes, &#39;N&#39; &#x3D; No) &nbsp;
**fund_manager_city** | str | The fund manager&#39;s city &nbsp;
**fund_manager_name** | str | The fund manager&#39;s name &nbsp;
**fund_manager_state** | str | The fund manager&#39;s state &nbsp;
**files_13f** | str | If &#39;Y&#39;, the company files the SEC 13F report. (&#39;Y&#39; &#x3D; Yes, &#39;N&#39; &#x3D; No) &nbsp;
**is_etf** | str | If &#39;Y&#39;, the owner is an ETF. (&#39;Y&#39; &#x3D; Yes, &#39;N&#39; &#x3D; No) &nbsp;
**last_updated_on** | date | The the last updated date &nbsp;

[//]: # (END_DEFINITION)



