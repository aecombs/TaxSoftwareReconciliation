# Tax Software Reconciliation

This script is written in python and is used to reconcile data from **Lacerte**, as a source of truth, and the CRM extension **eWay**.

It checks agreement on three separate axes:
- That each Lacerte client exists in eWay with the exact same last name and first name(s)
- That each matching client has the same address (corresponding to each )
- That each matching client has the same preparer

## How to Use

To use this script, you'll need to replace the mock data in `eway_clients.csv` and `lacerte_clients.csv` with your actual client data.

You'll also need make changes to the `preparers` and `eway_statuses` dict in the `resources.py` file. The required changes are as follows:

#### Update the `preparers` dict to list each preparer's representative number as the key with the corresponding name as it appears in eWay as the value

Ex.:
```
preparers = {
  '0': 'Lorem Ipsum',
  '1': 'Dolor Sit',
  '2': 'Amet Consectetur',
  '3': 'Adipiscing Elit'
}
```

#### Update the `eway_statuses` dict to list your firm's eWay statuses and the preferred corresponding Lacerte status that it should match.

Ex.:
```
eway_statuses = {
  'Proforma\'d': ['Appt - In Person', 'Appt - Virtual', 'No Appt', 'No Mail'],
  'Final': ['Appt - In Person', 'Appt - Virtual', 'No Appt', 'No Mail'],
  'Amended': ['Appt - In Person', 'Appt - Virtual', 'No Appt', 'No Mail'],
  'Paper Return': ['Appt - In Person', 'No Appt', 'No Mail'],
  'Next Year': ['Appt - In Person', 'Appt - Virtual', 'No Appt', 'No Mail', 'Prospect'],
  'Planning': ['Financial Planning'],
  'Not Processed': ['Former', 'No Mail']
}
```

#### From Lacerte:
- Group select the clients whose data you want to reconcile
- Export that group into a Comma Delimited file with the following columns:
  - Preparer
  - Current Status
  - Client Full Name, last name first
  - Street Address
  - Apartment Number (_this feature isn't being used yet_)
  - City
  - State
  - Zip Code
- Manually edit the CSV to add the headers as follows: `Preparer, Status, Account Name, Street, Apt, City, State, Zip`
- Rename the file to `lacerte_clients.csv` and replace the existing mock CSV

#### From eWay:
- Display the columns:
  - Owner
  - Categories
  - Account Name
  - Street (Business)
  - City (Business)
  - State (Business)
  - ZIP/ Postal Code (Business)
- Select Export to Excel at the top
- After saving, open and save as a CSV (Comma delimited) (*.csv) (_Note: do NOT save as 'CSV UTF-8 (Comma delimited) (*.csv)'_)
- Manually edit the CSV to add the headers as follows: `Preparer, Status, Account Name, Street, Apt, City, State, Zip`
- Rename the file to `eway_clients.csv` and replace the existing mock CSV


### To Run
In terminal, navigate to the main directory of this project. Execute the script by using the command `python reconcilation.py`. The files `clients_not_in_eway.csv`, `nonmatching_addrs.csv`, `nonmatching_preparers.csv`, and `nonmatching_statuses.csv` will be generated in the `results` directory with the relevant information you'll need to manually resolve discrepencies.

To run tests, use the command `python -m unittest discover tests`.
