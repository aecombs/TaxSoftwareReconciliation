# classes

class Client:

	def __init__(self, account_name, preparer, status, street, apt, city, state,
							zip, t_email, s_email, t_cell, s_cell,
							t_home, s_home, t_work, s_work):
		names = account_name.split(',')
		self.account_name = account_name
		print(account_name)
		self.last_name = names[0].strip()
		self.first_names = names[1].strip().split(' ')

		# clean up items in first_names array
		unwanted_strs = ['and', 'AND', 'And', '&', '.', ',']
		for str in self.first_names:
				if str in unwanted_strs:
						self.first_names.remove(str)

		self.preparer = preparer
		self.status = status
		self.address = {
				'Street': street,
				'Apt': apt,
				'City': city,
				'State': state,
				'Zip': zip
		}

		self.taxpayerEmail = t_email
		self.spouseEmail = s_email
		# TODO: add non-matching phone number feature ... also, clean up data!
		# self.taxpayerCell = t_cell
		# self.spouseCell = s_cell
		# self.taxpayerHome = t_home
		# self.spouseHome = s_home
		# self.taxpayerWork = t_work
		# self.spouseWork = s_work

	def __str__(self):
		return f"{self.account_name}"


# functions

# Takes a CSV row (or dict) and returns a Client object with stringified and whitespace-stripped properties
def create_client(row):
	# Clean up the data
	account_name = row['Account Name'].title()

	# map preparer if it's a digit; this will only trigger if it's converting Lacerte clients
	preparer = str(row['Preparer']).strip().title()
	if preparer == 'Kathy Mcginnis':
		preparer = 'Kathy McGinnis'
	if preparer.isdigit():
		preparer = preparers[preparer]

	# map status if it's a digit; this will only trigger if it's converting Lacerte clients
	status = str(row['Status']).strip().title()
	if status.isdigit():
		status = lacerte_statuses[status]

	street = str(row['Street']).strip().title()
	# apt = str(row['Apt']).strip().title()  # can be empty
	city = str(row['City']).strip().title()
	state = str(row['State']).strip().upper()
	zipcode = str(row['Zip']).strip()

	t_email = str(row['Taxpayer Email']).strip().lower()
	s_email = str(row['Taxpayer Email']).strip().lower()

	# create and return Client object
	return Client(account_name, preparer, status, street, city, state, zipcode)


# Checks whether names match, regardless of formatting
def name_match(eway_client: Client, lacerte_client: Client):
	# if the account names match exactly, exit early with True result
	if eway_client.account_name == lacerte_client.account_name:
		return True
	
	# if the last names don't match, exit early with False result
	if eway_client.last_name != lacerte_client.last_name:
		return False

	# Check first names for matches
	# clean up names
	eway_names = eway_client.first_names
	lacerte_names = lacerte_client.first_names

	# track match count; each client may have anywhere between 1 and 4+ first names (S vs MFJ with initials and maiden names)
	first_name_matches = 0
	for name in eway_names:
		if name in lacerte_names:
				first_name_matches += 1

	# ideal case: if at least two names match, exit early with True result
	if first_name_matches >= 2 and len(eway_names) >= 2:
		return True
	else:
			# Single filer edge case. If this isn't a match, we've likely found a family member.
		return first_name_matches == 1 and len(eway_names) == 1

def addr_match(eway_client: Client, lacerte_client: Client):
	# TODO: match apt/unit
	# lacerteApt = lacerte_client.address['Apt']

	return eway_client.address['Street'] == lacerte_client.address[
		'Street'] and eway_client.address['City'] == lacerte_client.address[
		'City'] and eway_client.address['State'] == lacerte_client.address[
		'State'] and eway_client.address['Zip'] == lacerte_client.address['Zip']


# Checks whether the preparers match
def preparer_match(eway_client: Client, lacerte_client: Client):
	return eway_client.preparer == lacerte_client.preparer

def statusMatch(eway_client: Client, lacerte_client: Client):
	eway_status = eway_client.status
	lacerte_status = lacerte_client.status

	return eway_status in eway_statuses[lacerte_status]

def emailMatch(eway_client: Client, lacerte_client: Client):
	# taxpayer
	eway_taxpayer_email = eway_client.taxpayerEmail
	lacerte_taxpayer_email = lacerte_client.taxpayerEmail

	# spouse
	eway_spouse_email = eway_client.spouseEmail
	lacerte_spouse_email = lacerte_client.spouseEmail

	return (eway_taxpayer_email == lacerte_taxpayer_email and eway_spouse_email == lacerte_spouse_email)

# TODO: add non-matching phone number feature
# def phoneMatch(eway_client: Client, lacerte_client: Client):
# 	# taxpayer home phone
#   eway_taxpayer_home = eway_client.taxpayerHomePhone
#   lacerte_taxpayer_home = lacerte_client.taxpayerHomePhone

# 	# taxpayer mobile phone
#   eway_taxpayer_mobile = eway_client.taxpayerMobilePhone
#   lacerte_taxpayer_mobile = lacerte_client.taxpayerMobilePhone

# 	# taxpayer work phone
#   eway_taxpayer_work = eway_client.taxpayerWorkPhone
#   lacerte_taxpayer_work = lacerte_client.taxpayerWorkPhone



# 	# spouse home phone
#   eway_spouse_home = eway_client.spouseHomePhone
#   lacerte_spouse_home = lacerte_client.spouseHomePhone

# 	# spouse mobile phone
#   eway_spouse_mobile = eway_client.spouseMobilePhone
#   lacerte_spouse_mobile = lacerte_client.spouseMobilePhone

# 	# spouse work phone
#   eway_spouse_work = eway_client.spouseWorkPhone
#   lacerte_spouse_work = lacerte_client.spouseWorkPhone



# 	return (eway_taxpayer_email == lacerte_taxpayer_email and eway_spouse_email == lacerte_spouse_email)

def match_clients(eway_clients: dict, lacerte_clients: dict):
	clients_not_in_eway = lacerte_clients.copy()
	nonmatching_addrs = {}
	nonmatching_preparers = {}
	nonmatching_statuses = {}
	nonmatching_emails = {}
	# nonmatching_phone = {} # TODO: add non-matching phone number feature

	for lacerte_client in lacerte_clients:
		for eway_client in eway_clients:
		# check is there's a name match
			if name_match(eway_client, lacerte_client):
				if lacerte_client in clients_not_in_eway:
					clients_not_in_eway.pop(lacerte_client)
				# if the addresses don't match, add to dict
				if not addr_match(eway_client, lacerte_client):
					nonmatching_addrs[lacerte_client.account_name] = [eway_client.address, lacerte_client.address, lacerte_client.preparer]
				# if the preparers don't match, add to dict
				if not preparer_match(eway_client, lacerte_client):
					nonmatching_preparers[lacerte_client.account_name] = [eway_client.preparer, lacerte_client.preparer]
				# if the statuses don't correspond, add to dict
				if not statusMatch(eway_client, lacerte_client):
					nonmatching_statuses[lacerte_client.account_name] = [eway_client.status, lacerte_client.status, lacerte_client.preparer]
				if not emailMatch(eway_client, lacerte_client):
					nonmatching_emails[lacerte_client.account_name] = [
						eway_client.taxpayerEmail,
						lacerte_client.taxpayerEmail,
						eway_client.spouseEmail,
						lacerte_client.spouseEmail,
						lacerte_client.preparer
					]
			# if there isn't a name match, leave in clients_not_in_eway dict and move on
			else:
				continue

	return clients_not_in_eway, nonmatching_addrs, nonmatching_preparers, nonmatching_statuses, nonmatching_emails


# data

# Here's the part of the doc that holds important but conditional data. Some of this will need to be edited to match your firm's specific requirements and setup.

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
	'5': 'Jenny Wang',
	'6': 'Caitlin White',
	'7': 'Smita Patil',
	'8': 'Kathy McGinnis',
	'9': 'Ron Hogsett',
	'10': 'Self Prepared'
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
		'Tax Client - Appt (In-Person)', 'Tax Client - Appt (Teams)', 'Tax Client - No Appt', 'Tax Client - Mail', 'Tax Client - No Mail'
		],
	'Final': [
		'Tax Client - Appt (In-Person)', 'Tax Client - Appt (Teams)', 'Tax Client - No Appt', 'Tax Client - Mail', 'Tax Client - No Mail'
		],
	'Amended': [
		'Tax Client - Appt (In-Person)', 'Tax Client - Appt (Teams)', 'Tax Client - No Appt', 'Tax Client - Mail', 'Tax Client - No Mail'
		],
	'Paper Return': [
		'Tax Client - Appt (In-Person)', 'Tax Client - Appt (Teams)', 'Tax Client - No Appt', 'Tax Client - Mail', 'Tax Client - No Mail'
		],
	'Next Year': [
		'Tax Client - Appt (In-Person)', 'Tax Client - Appt (Teams)', 'Tax Client - No Appt', 'Tax Client - Mail', 'Tax Client - No Mail'
		],
	'Planning': [
		'Tax Client - Appt (In-Person)', 'Tax Client - Appt (Teams)', 'Tax Client - No Appt', 'Tax Client - Mail', 'Tax Client - No Mail'
		],
	'Not Processed': ['Former']
}

# ~~~~~~~~~~~~~~~~~ DO NOT EDIT BELOW THIS LINE ~~~~~~~~~~~~~~~~~

lacerte_statuses = {
	'1': 'Proforma\'d',
	'2': 'Info Pending',
	'3': 'Under Review',
	'4': 'On Extension',
	'5': 'Final',
	'6': 'Amended',
	'7': 'Paper Return',
	'8': 'Next Year',
	'9': 'Planning',
	'20': 'Not Processed'
}
