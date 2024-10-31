import data

class Client:

    def __init__(self, account_name, preparer, status, street, city, state,
                 zip):
        names = account_name.split(',')
        self.account_name = account_name
        self.last_name = names[0].strip()
        self.first_names = names[1].strip()
        
        self.preparer = preparer
        self.status = status
        self.address = {
            'Street': street,
            # 'Apt': apt,
            'City': city,
            'State': state,
            'Zip': zip
        }

        def __str__(self):
            return f"{self.account_name}"


# functions


# Takes a CSV row (or dict) and returns a Client object with stringified and whitespace-stripped properties
def createClient(row):
    # Clean up the data

    account_name = row['Account Name'].upper()

    # map preparer if it's a digit; this will only trigger if it's converting Lacerte clients
    preparer = str(row['Preparer']).strip().upper()
    if preparer.isdigit():
        preparer = data.preparers[preparer]

    # map status if it's a digit; this will only trigger if it's converting Lacerte clients
    status = str(row['Status']).strip().upper()
    if status.isdigit():
        status = lacerte_statuses[status]

    street = str(row['Street']).strip().upper()
    # apt = str(row['Apt']).strip().upper()  # can be empty
    city = str(row['City']).strip().upper()
    state = str(row['State']).strip().upper()
    zip = str(row['Zip']).strip()

    # create and return Client object
    return Client(account_name, preparer, status, street, city, state, zip)


# Checks whether names match, regardless of formatting
def nameMatch(ewayClient, lacerteClient):

    # if the account names match exactly, exit early with True result
    if ewayClient.account_name == lacerteClient.account_name:
        return True
    
    # if the last names don't match, exit early with False result
    if ewayClient.last_name != lacerteClient.last_name:
        return False

    # Check first names for matches
    # clean up names
    eway_split_names = ewayClient.first_names.split(' ')
    lacerte_split_names = lacerteClient.first_names.split(' ')

    # track match count; each client may have anywhere between 1 and 4+ first names (S vs MFJ with initials and maiden names)
    first_name_matches = 0
    for name in eway_split_names:
        if name != ('AND' or '&') and name in lacerte_split_names:
            first_name_matches += 1

    # ideal case: if at least two names match, exit early with True result
    if first_name_matches >= 2 and len(eway_split_names) >= 2:
        return True
    else:
        # Single filer edge case. If this isn't a match, we've likely found a family member.
        return first_name_matches == 1 and len(eway_split_names) == 1

def addrMatch(ewayClient, lacerteClient):
    # TODO: match apt/unit
    # lacerteApt = lacerteClient.address['Apt']

    return ewayClient.address['Street'] == lacerteClient.address[
        'Street'] and ewayClient.address['City'] == lacerteClient.address[
            'City'] and ewayClient.address['State'] == lacerteClient.address[
                'State'] and ewayClient.address['Zip'] == lacerteClient.address['Zip']


# Checks whether the preparers match
def preparerMatch(ewayClient, lacerteClient):
    return ewayClient.preparer == lacerteClient.preparer