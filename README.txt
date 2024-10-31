### Tax Software Reconciliation

This script is written in python and is used to reconcile data from Lacerte, as a source of truth, and the CRM extension eWay.

It checks agreement on three separate axes:
- That each Lacerte client exists in eWay with the exact same last name and first name(s)
- That each matching client has the same address (corresponding to each )
- That each matching client has the same preparer

## How to Use

To use this script, you'll need to replace the mock data in `eway_clients.csv` and `lacerte_clients.csv` with your actual client data.
You'll also need update the `preparers.py` file that includes a python dict named `preparers`. This dict will need to list each preparer's representative number as the key with the corresponding name as it appears in eWay as the value.

Here is an example:

> preparers = {
>   '0': 'Lorem Ipsum',
>   '1': 'Dolor Sit',
>   '2': 'Amet Consectetur',
>   '3': 'Adipiscing Elit'
> }

# From Lacerte:
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

# From eWay:
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

# To Run
From terminal, use the command `python3 main.py`. The files `clients_not_in_eway.csv`, `nonmatching_addrs.csv`, and `nonmatching_preparers.csv` should all be generated.