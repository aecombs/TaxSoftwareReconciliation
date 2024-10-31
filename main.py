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
  field_names = ["Account Name","Preparer","Status","Street","City","State", "Zip"]
  reader = csv.DictReader(csvfile, fieldnames=field_names)

  for row in reader:
    client = resources.createClient(row)
    eway_clients.append(client)

# create lacerte client objects and put into lacerte array
with open('lacerte_clients.csv', newline='') as csvfile:
  field_names = ["Account Name","Preparer","Status","Street","City","State", "Zip"]
  clients = csv.DictReader(csvfile, fieldnames=field_names)

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
  writer = csv.DictWriter(csvfile, fieldnames=field_names)
  headers = ['Account Name', 'Preparer', 'Status']
  writer.writeheader()
  for name in clients_not_in_eway:
    writer.writerow({name: clients_not_in_eway[name]})

with open('nonmatching_addrs.csv', 'w', newline='') as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames=field_names)
  headers = ['Lacerte Account Name', 'eWay Address', 'Lacerte Address']
  writer.writeheader()
  for name in nonmatching_addrs:
    writer.writerow({name: nonmatching_addrs[name]})

with open('nonmatching_preparers.csv', 'w', newline='') as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames=field_names)
  headers = ['Lacerte Account Name', 'eWay Preparer', 'Lacerte Preparer']
  writer.writeheader()
  for name in nonmatching_preparers:
    writer.writerow({name: nonmatching_addrs[name]})
