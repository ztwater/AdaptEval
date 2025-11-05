>>> User().some_method()
<class 'balance_models.Balance'>
>>> Balance().some_method()
<class 'user_models.User'>
>>> Base.model_lookup_by_table_name("user")
<class 'user_models.User'>
>>> Base.model_lookup_by_table_name("balance")
<class 'balance_models.Balance'>
