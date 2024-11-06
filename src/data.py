
# This is the file that holds important but conditional data. Some of this will need to be edited to match your firm's specific requirements and setup.

# ~~~~~~~~~~~~~~~~~ EDIT BELOW THIS LINE ~~~~~~~~~~~~~~~~~

# Update the `preparers` dict with your firm's preparers.

# Ex.:
# preparers = {
#   '0': 'Lorem Ipsum',
#   '1': 'Dolor Sit',
#   '2': 'Amet Consectetur',
#   '3': 'Adipiscing Elit'
# }

preparers = {
    '0': '',
    '1': 'Andy Andrikopoulos',
    '2': 'Tim Chiochios',
    '3': '',
    '4': 'Kathryn Kauffman',
    '5': '',
    '6': 'Caitlin White',
    '7': 'Jenny Wang',
    '8': 'Kathy McGinnis',
    '9': '',
    '11': 'Dennis Daly',
    '12': 'Merry C Davis'
}

# ~~~~~~~~~~~~~~~~~

# Update the `eway_statuses` dict with your firm's eWay statuses and the desired corresponding Lacerte status.

# Ex.:
# eway_statuses = {
    # 'Proforma\'d': ['Appt - In Person', 'Appt - Virtual', 'No Appt', 'No Mail'],
    # 'Final': ['Appt - In Person', 'Appt - Virtual', 'No Appt', 'No Mail'],
    # 'Amended': ['Appt - In Person', 'Appt - Virtual', 'No Appt', 'No Mail'],
    # 'Paper Return': ['Appt - In Person', 'No Appt', 'No Mail'],
    # 'Next Year': ['Appt - In Person', 'Appt - Virtual', 'No Appt', 'No Mail', 'Prospect'],
    # 'Planning': ['Financial Planning'],
    # 'Not Processed': ['Former', 'No Mail']
# }

eway_statuses = {
    'Proforma\'d': [
      'Tax Client - Appt (In Person)', 'Tax Client - Appt (Teams)', 'No Appt', 'Mail', 'No Mail'
      ],
    'Final': [
      'Tax Client - Appt (In Person)', 'Tax Client - Appt (Teams)', 'No Appt', 'Mail', 'No Mail'
      ],
    'Amended': [
      'Tax Client - Appt (In Person)', 'Tax Client - Appt (Teams)', 'No Appt', 'Mail', 'No Mail'
      ],
    'Paper Return': [
      'Tax Client - Appt (In Person)', 'Tax Client - Appt (Teams)', 'No Appt', 'Mail', 'No Mail'
      ],
    'Next Year': [
      'Tax Client - Appt (In Person)', 'Tax Client - Appt (Teams)', 'No Appt', 'Mail', 'No Mail'
      ],
    'Planning': [
      'Tax Client - Appt (In Person)', 'Tax Client - Appt (Teams)', 'No Appt', 'Mail', 'No Mail'
      ],
    'Not Processed': ['Former']
}

# eway_statuses = {
#     'Proforma\'d': [],
#     'Final': [],
#     'Amended': [],
#     'Paper Return': [],
#     'Next Year': [],
#     'Planning': [],
#     'Not Processed': []
# }

# ~~~~~~~~~~~~~~~~~ DO NOT EDIT BELOW THIS LINE ~~~~~~~~~~~~~~~~~

lacerte_statuses = {
    '1': 'Proforma\'d',
    '5': 'Final',
    '6': 'Amended',
    '7': 'Paper Return',
    '8': 'Next Year',
    '9': 'Planning',
    '20': 'Not Processed'
    # TODO: Will update these with corresponding values:
    # 'Info Pending',
    # 'Under Review',
    # 'On Extension',
}