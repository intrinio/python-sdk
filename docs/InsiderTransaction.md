

[//]: # (CLASS:InsiderTransaction)

[//]: # (KIND:object)

### InsiderTransaction

#### Properties

[//]: # (START_DEFINITION)

Name | Type | Description
------------ | ------------- | -------------
**director** | bool | (true/false) A boolean indicating whether or not the owner is a director in the company &nbsp;
**officer** | bool | (true/false) A boolean indicating whether or not the owner is a officer in the company &nbsp;
**ten_percent_owner** | bool | (true/false) A boolean indicating whether or not the owner has a ten percent or greater interest in the company &nbsp;
**other_relation** | bool | (true/false) A boolean indicating whether or not the owner has another relationship with the company beside, direct, officer, or significant owner in the company &nbsp;
**officer_title** | str | The officer title of the owner in the company &nbsp;
**derivative_transaction** | bool | (true) A boolean indicating the transaction is a derivative transaction, which may or may not become common stock due to various possible exercise or conversion requirements &nbsp;
**ticker** | str | The ticker symbol for the company’s common stock &nbsp;
**security_title** | str | The name of the derivative security transacted &nbsp;
**conversion_exercise_price** | float | The conversion or exercise price of the derivative security transacted &nbsp;
**transaction_date** | date | The date of the transaction &nbsp;
**deemed_execution_date** | date | The date of the transaction had it not a directly identifiable date &nbsp;
**transaction_type_code** | str | A symbol representing the transaction type; P &#x3D; Purchase | S &#x3D; Sale | A  &#x3D; Award | M &#x3D; Conversion to Common | C &#x3D; Conversion | X &#x3D; Exercise of Derivative More Transaction Codes &nbsp;
**acquisition_disposition_code** | str | A symbol representing whether or not the derivative securities are Acquired or Disposed; A &#x3D; Acquisition | D &#x3D; Disposition &nbsp;
**amount_of_shares** | float | The number of derivative securities involved in the subject transaction &nbsp;
**exercise_date** | date | The exercise date of the derivative securities &nbsp;
**expiration_date** | date | The expiration date of the derivative securities &nbsp;
**underlying_security_title** | str | The name of the underlying non-derivative security related to this derivative transaction &nbsp;
**underlying_shares** | float | The number of non-derivative shares involved in the subject transaction &nbsp;
**transaction_price** | float | The price of the derivative securities &nbsp;
**total_shares_owned** | float | The total number of derivative securities owned following the subject transaction &nbsp;
**ownership_type_code** | str | A symbol representing the ownership of the securities transacted; D &#x3D; Direct Ownership | I &#x3D; Indirect Ownership &nbsp;
**company** | [**CompanySummary**](CompanySummary.md) | The company associated with the filing &nbsp;
**owner** | [**OwnerSummary**](OwnerSummary.md) | The owner associated with the filing &nbsp;

[//]: # (END_DEFINITION)


[//]: # (CONTAINED_CLASS:CompanySummary)


[//]: # (CONTAINED_CLASS:OwnerSummary)



