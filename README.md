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
- Group select the clients whose data you want
- Export that group into a Comma Delimited file with the following columns:
  - Account Name
  - Preparer
  - Current Status
  - Client Full Name, last name first
  - Street Address
  - Apartment Number (_this feature isn't being used yet_)
  - City
  - State
  - Zip Code

#### From eWay:
- Display the columns:
  - Account Name
  - Owner
  - Categories
  - Street (Business)
  - City (Business)
  - State (Business)
  - ZIP/ Postal Code (Business)
- Select Export to Excel at the top
- After saving, open and save as a CSV

Rename both of these files approriately and replace the existing mock CSVs.

### To Run
In terminal, navigate to the  use the command `python3 reconcilation.py`. The files `clients_not_in_eway.csv`, `nonmatching_addrs.csv`, `nonmatching_preparers.csv`, and `nonmatching_statuses.csv` should all be generated in the `results` directory with the relevant information you'll need to resolve discrepencies.

To run tests, use the command `python3 -m unittest discover tests`.
