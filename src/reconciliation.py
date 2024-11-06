import csv
import resources

eway_clients = []
lacerte_clients = []

clients_not_in_eway = {}
nonmatching_addrs = {}
nonmatching_preparers = {}
# partial_matches = {} # this would be to save any matches on last names but not first

# create eway client objects and put into eway array
with open('eway_clients.csv', newline='') as csvfile:
  # field_names = ["Account Name","Preparer","Status","Street","City","State", "Zip"]
  # reader = csv.DictReader(csvfile, fieldnames=field_names)
  reader = csv.DictReader(csvfile)

  for row in reader:
    client = resources.createClient(row)
    eway_clients.append(client)

# create lacerte client objects and put into lacerte array
with open('lacerte_clients.csv', newline='') as csvfile:
  # field_names = ["Account Name","Preparer","Status","Street","City","State", "Zip"]
  # clients = csv.DictReader(csvfile, fieldnames=field_names)
  clients = csv.DictReader(csvfile)

  for row in clients:
    client = resources.createClient(row)
    lacerte_clients.append(client)

# check lacerteClient to find a matching ewayClient.
for lacerteClient in lacerte_clients:
  for ewayClient in eway_clients:
    # check is there's a name match
    if resources.nameMatch(ewayClient, lacerteClient):
      # if the addresses don't match, add to dict
      if not resources.addrMatch(ewayClient, lacerteClient):
        nonmatching_addrs[lacerteClient.account_name] = [ewayClient.address, lacerteClient.address]
      # if the preparers don't match, add to dict
      if not resources.preparerMatch(ewayClient, lacerteClient):
        nonmatching_preparers[lacerteClient.account_name] = [ewayClient.preparer, lacerteClient.preparer]
    # if there isn't a name match, add to dict and move on
    else:
      # clients_not_in_eway[lacerteClient.account_name] = lacerteClient
      clients_not_in_eway[lacerteClient.account_name] = [lacerteClient.preparer, lacerteClient.status]
      continue

# write to csv files
with open('clients_not_in_eway.csv', 'w', newline='') as csvfile:
  field_names = ['Account Name', 'Preparer', 'Status']
  writer = csv.DictWriter(csvfile, fieldnames=field_names)
  writer.writeheader()
  for name in clients_not_in_eway:
    writer.writerow({
      'Account Name': name, 
      'Preparer': clients_not_in_eway[name][0],
      'Status': clients_not_in_eway[name][1]
    })

with open('nonmatching_addrs.csv', 'w', newline='') as csvfile:
  field_names = ['Lacerte Account Name', 'eWay Address', 'Lacerte Address']
  writer = csv.DictWriter(csvfile, fieldnames=field_names)
  writer.writeheader()
  for name in nonmatching_addrs:
    writer.writerow({
      'Lacerte Account Name': name, 
      'eWay Address': nonmatching_addrs[name][0],
      'Lacerte Address': nonmatching_addrs[name][1]
    })

with open('nonmatching_preparers.csv', 'w', newline='') as csvfile:
  field_names = ['Lacerte Account Name', 'eWay Preparer', 'Lacerte Preparer']
  writer = csv.DictWriter(csvfile, fieldnames=field_names)
  writer.writeheader()
  for name in nonmatching_preparers:
    writer.writerow({
      'Lacerte Account Name': name, 
      'eWay Preparer': nonmatching_preparers[name][0],
      'Lacerte Preparer': nonmatching_preparers[name][1]
    })

