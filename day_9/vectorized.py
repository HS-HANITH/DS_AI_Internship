import pandas as pd
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
cleaned_usernames = usernames.str.strip().str.lower()
contains_a = cleaned_usernames.str.contains('a')
print(cleaned_usernames)
print(contains_a)
