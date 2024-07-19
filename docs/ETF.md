

[//]: # (CLASS:ETF)

[//]: # (KIND:object)

### ETF

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**id** | str | The Intrinio ID of the ETF &nbsp;
**name** | str | The common name of the ETF &nbsp;
**ticker** | str | The common ticker symbol for the ETF &nbsp;
**figi_ticker** | str | The OpenFIGI ticker for the ETF &nbsp;
**ric** | str | Reuters Instrument Code (RIC) for the ETF &nbsp;
**isin** | str | International Securities Identification Number (ISIN) for the ETF &nbsp;
**sedol** | str | Stock Exchange Daily Official List (SEDOL) for the ETF &nbsp;
**exchange_mic** | str | The exchange Market Identifier Code (MIC) from the International Standards Organization (ISO) &nbsp;
**sponsor** | str | The fund manager (ETF) or issuing bank (ETN) &nbsp;
**type** | str | High-level classification for the ETF based on its intended investment objective &nbsp;
**description** | str | The ETF description as published by the ETF sponsor &nbsp;
**inception_date** | date | Inception Date for the ETF as published by the ETF sponsor &nbsp;
**data_change_date** | date | The last date on which there was a change in a classifications data field for this ETF &nbsp;
**close_date** | date | The date on which this ETF was de-listed if it is no longer listed &nbsp;
**is_live_listed** | bool | If True, the ETF is still listed on an exchange; if False, the ETF is no longer listed &nbsp;
**legal_structure** | str | The legal structure as defined in the prospectus &nbsp;
**intraday_nav_ticker** | str | Intra-day NAV ticker for the Exchange Traded Fund (ETF) &nbsp;
**primary_ticker** | str | The primary ticker field is used for Exchange Traded Products (ETPs) that have multiple listings and share classes. If an ETP has multiple listings or share classes, the same primary ticker is assigned to all the listings and share classes &nbsp;
**primary_ticker_country_code** | str | 2 letter ISO country code for the country of the primary listing &nbsp;
**primary_listing_region** | str | Geographic region in the country of the primary listing falls &nbsp;
**net_expense_ratio** | float | Gross expense net of Fee Waivers, as a percentage of net assets as published by the ETF Sponsor &nbsp;
**asset_class** | str | Captures the underlying nature of the securities in the Exchanged Traded Product (ETP) &nbsp;
**other_asset_types** | str | If &#39;asset_class&#39; field is classified as &#39;Other Asset Types&#39; this field captures the specific category of the underlying assets &nbsp;
**market_cap_range** | str | Equity ETFs are classified as falling into categories based on the description of their investment strategy in the prospectus.  Examples (&#39;Mega Cap&#39;, &#39;Large Cap&#39;, &#39;Mid Cap&#39;, etc.) &nbsp;
**holds_only_nyse_stocks** | bool | If True, the ETF is an equity ETF and holds only stocks listed on NYSE &nbsp;
**holds_only_nasdaq_stocks** | bool | If False, the ETF is an equity ETF and holds only stocks listed on Nasdaq &nbsp;
**growth_value_tilt** | str | Classifies equity ETFs as either &#39;Growth&#39; or Value&#39; based on the stated style tilt in the ETF prospectus. Equity ETFs that do not have a stated style tilt are classified as &#39;Core / Blend&#39; &nbsp;
**growth_type** | str | For ETFs that are classified as &#39;Growth&#39; in &#39;growth_value_tilt&#39;, this field further identifies those where the stocks in the ETF are both selected and weighted based on their growth (style factor) scores &nbsp;
**value_type** | str | For ETFs that are classified as &#39;Value&#39; in &#39;growth_value_tilt&#39;, this field further identifies those where the stocks in the ETF are both selected and weighted based on their value (style factor) scores &nbsp;
**sector** | str | For equity ETFs that aim to provide targeted exposure to a sector or industry, this field identifies the Sector that it provides the exposure to &nbsp;
**industry** | str | For equity ETFs that aim to provide targeted exposure to an industry, this field identifies the Industry that it provides the exposure to. &nbsp;
**sub_industry** | str | For equity ETFs that aim to provide targeted exposure to a sub-industry, this field identifies the sub-industry that it provides the exposure to &nbsp;
**cross_sector_theme** | str | For equity ETFs that aim to provide targeted exposure to a specific investment theme that cuts across GICS sectors, this field identifies the specific cross-sector theme.  Examples (&#39;Agri-business&#39;, &#39;Natural Resources&#39;, &#39;Green Investing&#39;, etc.) &nbsp;
**natural_resources_type** | str | For ETFs that are classified as &#39;Natural Resources&#39; in the &#39;cross_sector_theme&#39; field, this field provides further detail on the type of Natural Resources exposure. &nbsp;
**excludes_financials** | bool | For equity ETFs, identifies those ETFs where the underlying fund holdings will not hold financials stocks, based on the funds intended objective &nbsp;
**excludes_technology** | bool | For equity ETFs, identifies those ETFs where the underlying fund holdings will not hold technology stocks, based on the funds intended objective &nbsp;
**us_or_excludes_us** | str | Takes the value of &#39;Domestic&#39; for US exposure, &#39;International&#39; for non-US exposure and &#39;Global&#39; for exposure that includes all regions including the US &nbsp;
**developed_emerging** | str | This field identifies the stage of development of the markets that the ETF provides exposure to &nbsp;
**specialized_region** | str | This field is populated if the ETF provides targeted exposure to a specific type of geography-based grouping that does not fall into a specific country or continent grouping.  Examples (&#39;BRIC&#39;, &#39;Chindia&#39;, etc.) &nbsp;
**continent** | str | This field is populated if the ETF provides targeted exposure to a specific continent or country within that Continent &nbsp;
**latin_america_sub_group** | str | For ETFs that are classified as &#39;Latin America&#39; in the &#39;continent&#39; field, this field provides further detail on the type of regional exposure &nbsp;
**europe_sub_group** | str | For ETFs that are classified as &#39;Europe&#39; in the &#39;continent&#39; field, this field provides further detail on the type of regional exposure &nbsp;
**asia_sub_group** | str | For ETFs that are classified as &#39;Asia&#39; in the &#39;continent&#39; field, this field provides further detail on the type of regional exposure &nbsp;
**specific_country** | str | This field is populated if the ETF provides targeted exposure to a specific country &nbsp;
**china_listing_location** | str | For ETFs that are classified as &#39;China&#39; in the &#39;country&#39; field, this field provides further detail on the type of exposure in the underlying securities &nbsp;
**us_state** | str | Takes the value of a US state if the ETF provides targeted exposure to the municipal bonds or equities of companies operating in a specific state in the US &nbsp;
**real_estate** | str | For ETFs that provide targeted real estate exposure, this field is populated if the ETF provides targeted exposure to a specific segment of the real estate market &nbsp;
**index_weighting_scheme** | str | For ETFs that track an underlying index, this field provides detail on the index weighting type &nbsp;
**market_cap_weighting_type** | str | For ETFs that take the value &#39;Market Cap Weighted&#39; in the &#39;index_weighting_scheme&#39; field, this field provides detail on the market cap weighting type &nbsp;
**fundamental_weighting_type** | str | For ETFs that take the value ‘Fundamental Weighted’ in the &#39;index_weighting_scheme&#39; field, this field provides detail on the fundamental weighting methodology &nbsp;
**dividend_weighting_type** | str | For ETFs that take the value &#39;Dividend Weighted&#39; in the &#39;index_weighting_scheme&#39; field, this field provides detail on the dividend weighting methodology &nbsp;
**bond_type** | str | For ETFs where &#39;asset_class_type&#39; is &#39;Bonds&#39;, this field provides detail on the type of bonds held in the ETF &nbsp;
**government_bond_types** | str | For bond ETFs that take the value &#39;Treasury &amp; Government&#39; in &#39;bond_type&#39;, this field provides detail on the exposure &nbsp;
**municipal_bond_region** | str | For bond ETFs that take the value &#39;Municipal&#39; in &#39;bond_type&#39;, this field provides additional detail on the geographic exposure &nbsp;
**municipal_vrdo** | bool | For bond ETFs that take the value &#39;Municipal&#39; in &#39;bond_type&#39;, this field identifies those ETFs that specifically provide exposure to Variable Rate Demand Obligations &nbsp;
**mortgage_bond_types** | str | For bond ETFs that take the value &#39;Mortgage&#39; in &#39;bond_type&#39;, this field provides additional detail on the type of underlying securities &nbsp;
**bond_tax_status** | str | For all US bond ETFs, this field provides additional detail on the tax treatment of the underlying securities &nbsp;
**credit_quality** | str | For all bond ETFs, this field helps to identify if the ETF provides targeted exposure to securities of a specific credit quality range &nbsp;
**average_maturity** | str | For all bond ETFs, this field helps to identify if the ETF provides targeted exposure to securities of a specific maturity range &nbsp;
**specific_maturity_year** | int | For all bond ETFs that take the value &#39;Specific Maturity Year&#39; in the &#39;average_maturity&#39; field, this field specifies the calendar year &nbsp;
**bond_currency_denomination** | str | For all bond ETFs, this field provides additional detail on the currency denomination of the underlying securities &nbsp;
**laddered** | bool | For bond ETFs, this field identifies those ETFs that specifically hold bonds in a laddered structure, where the bonds are scheduled to mature in an annual, sequential structure &nbsp;
**zero_coupon** | bool | For bond ETFs, this field identifies those ETFs that specifically hold zero coupon Treasury Bills &nbsp;
**floating_rate** | bool | For bond ETFs, this field identifies those ETFs that specifically hold floating rate bonds &nbsp;
**build_america_bonds** | bool | For municipal bond ETFs, this field identifies those ETFs that specifically hold Build America Bonds &nbsp;
**commodity_types** | str | For ETFs where &#39;asset_class_type&#39; is &#39;Commodities&#39;, this field provides detail on the type of commodities held in the ETF &nbsp;
**energy_type** | str | For ETFs where &#39;commodity_type&#39; is &#39;Energy&#39;, this field provides detail on the type of energy exposure provided by the ETF &nbsp;
**agricultural_type** | str | For ETFs where &#39;commodity_type&#39; is &#39;Agricultural&#39;, this field provides detail on the type of agricultural exposure provided by the ETF &nbsp;
**metal_type** | str | For ETFs where &#39;commodity_type&#39; is &#39;Gold &amp; Metals&#39;, this field provides detail on the type of exposure provided by the ETF &nbsp;
**inverse_leveraged** | str | This field is populated if the ETF provides inverse or leveraged exposure &nbsp;
**target_date_multi_asset_type** | str | For ETFs where &#39;asset_class_type&#39; is &#39;Target Date / MultiAsset&#39;, this field provides detail on the type of commodities held in the ETF &nbsp;
**currency_hedged** | bool | This field is populated if the ETF’s strategy involves hedging currency exposure &nbsp;
**currency_pair** | str | This field is populated if the ETF’s strategy involves providing exposure to the movements of a currency or involves hedging currency exposure &nbsp;
**social_environmental_type** | str | This field is populated if the ETF’s strategy involves providing exposure to a specific social or environmental theme &nbsp;
**clean_energy_type** | str | This field is populated if the ETF has a value of &#39;Clean Energy&#39; in the &#39;social_environmental_type&#39; field. &nbsp;
**dividend_type** | str | This field is populated if the ETF has an intended investment objective of holding dividend-oriented stocks as stated in the prospectus &nbsp;
**regular_dividend_payor_type** | str | This field is populated if the ETF has a value of &#39;Dividend – Regular Payors&#39; in the &#39;dividend_type&#39; field &nbsp;
**holds_ml_ps** | bool | If True, the ETF’s investment objective explicitly specifies that it holds MLPs as an intended part of its investment strategy &nbsp;
**holds_preferred_stock** | bool | If True, the ETF’s investment objective explicitly specifies that it holds preferred stock as an intended part of its investment strategy &nbsp;
**holds_closed_end_funds** | bool | IF True, if the ETF’s investment objective explicitly specifies that it holds closed end funds as an intended part of its investment strategy &nbsp;
**quant_strategies_type** | str | This field is populated if the ETF has either an index-linked or active strategy that is based on a proprietary quantitative strategy &nbsp;
**other_quant_models** | str | For ETFs where &#39;quant_strategies_type&#39; is &#39;Other Quant Model&#39;, this field provides the name of the specific proprietary quant model used as the underlying strategy for the ETF &nbsp;
**hedge_fund_type** | str | For ETFs where &#39;other_asset_types&#39; is &#39;Hedge Fund Replication&#39;, this field provides detail on the type of hedge fund replication strategy &nbsp;
**derivatives_based** | str | This field is populated if the ETF holds either listed or over-the-counter derivatives in its portfolio &nbsp;
**holds_ad_rs** | bool | If True, he ETF’s investment objective explicitly specifies that it holds American Depositary Receipts (ADRs) as an intended part of its investment strategy &nbsp;
**index_linked** | str | This field identifies whether an ETF is index linked or active &nbsp;
**includes_short_exposure** | bool | This field is populated if the ETF has short exposure in any of its holdings e.g. in a long/short or inverse ETF &nbsp;
**index_name** | str | This field identifies the name of the underlying index tracked by the ETF, if applicable &nbsp;
**parent_index** | str | This field identifies the name of the parent index, which represents the broader universe from which the index underlying the ETF is created, if applicable &nbsp;
**index_family** | str | This field identifies the index family to which the index underlying the ETF belongs. The index family is represented as categorized by the index provider &nbsp;
**broader_index_family** | str | This field identifies the broader index family to which the index underlying the ETF belongs. The broader index family is represented as categorized by the index provider &nbsp;
**index_provider** | str | This field identifies the Index provider for the index underlying the ETF, if applicable &nbsp;
**fund_family** | str | This field identifies the fund family to which the ETF belongs, as categorized by the ETF Sponsor &nbsp;
**index_ticker** | str | This field identifies the OpenFIGI ticker for the Index underlying the ETF &nbsp;
**etn_issuing_bank** | str | If the product is an Exchange Traded Note (ETN), this field identifies the issuing bank &nbsp;
**etn_maturity_date** | date | If the product is an ETN, this field identifies the maturity date for the ETN &nbsp;
**livestock** | str | For ETFs where &#39;commodity_type&#39; is &#39;Livestock&#39;, this field provides detail on the type of livestock exposure provided by the ETF &nbsp;
**dynamic_futures_roll** | bool | If the product holds futures contracts, this field identifies those products where the roll strategy is dynamic (rather than entirely rules based), so as to minimize roll costs &nbsp;
**index_provider_code** | str | This field provides the First Bridge code for each Index provider, corresponding to the index underlying the ETF if applicable &nbsp;
**single_category_designation** | str | This categorization is created for those users who want every ETF to be ‘forced’ into a single bucket, so that the assets for all categories will always sum to the total market &nbsp;
**registered_countries** | str | The list of countries where the ETF is legally registered for sale. This may differ from where the ETF is domiciled or traded, particularly in Europe &nbsp;
**issuing_entity_country_code** | str | The name of the legal entity that issued the Exchange Traded Product (ETP) &nbsp;
**ucits** | bool | If True, the Exchange Traded Product (ETP) is Undertakings for the Collective Investment in Transferable Securities (UCITS) compliant &nbsp;
**replication_structure** | str | The replication structure of the Exchange Traded Product (ETP) &nbsp;
**domicile** | str | 2 letter ISO country code for the country where the ETP is domiciled &nbsp;
**base_currency** | str | Base currency of the Exchange Traded Product (ETP) in which the net asset value (NAV) is calculated. Reported using the 3-digit ISO currency code &nbsp;
**listing_currency** | str | Listing currency of the Exchange Traded Product (ETP) in which it is traded. Reported using the 3-digit ISO currency code &nbsp;
**fund_listing_date** | date | The date on which the Exchange Traded Product (ETP) or share class of the ETP is listed on a specific exchange &nbsp;
**listing_country_code** | str | 2 letter ISO country code for the country where the Exchange Traded Product (ETP) is listed &nbsp;
**listing_region** | str | The region in which this specific ETF is listed &nbsp;
**smartvs_traditional_beta** | str | This field identifies whether an ETF provides &#39;Traditional&#39; beta exposure or &#39;Smart&#39; beta exposure. ETFs that are active (i.e. non-indexed), leveraged / inverse or have a proprietary quant model (i.e. that don’t provide indexed exposure to a targeted factor) are classified separately &nbsp;
**smartvs_traditional_beta_level2** | str | This field provides further detail within the traditional and smart beta categories &nbsp;
**income_category** | str | Identifies if an Exchange Traded Fund (ETF) falls into a category that is specifically designed to provide a high yield or income &nbsp;
**etp_structure_type** | str | Classifies Exchange Traded Products (ETPs) into very broad categories based on its legal structure &nbsp;
**month_end_assets** | float | Net assets in millions of dollars as of the most recent month end &nbsp;
**etf_portfolio_turnover** | float | The percentage of positions turned over in the last 12 months &nbsp;
**firstbridge_id** | str | The FirstBridge unique identifier for the Exchange Traded Fund (ETF) &nbsp;
**firstbridge_parent_id** | str | The FirstBridge unique identifier of the parent Exchange Traded Fund (ETF), if applicable &nbsp;
**number_of_holdings** | int | The number of holdings for this Exchange Traded Fund (ETF) &nbsp;

[//]: # (END_DEFINITION)



