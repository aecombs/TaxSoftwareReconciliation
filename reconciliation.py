import csv
import logic

eway_clients = []
lacerte_clients = []

# create eway client objects and put into eway array
with open('eway_clients.csv', newline='') as csvfile:
  # field_names = ["Account Name","Preparer","Status","Street","City","State", "Zip"]
  # reader = csv.DictReader(csvfile, fieldnames=field_names)
  reader = csv.DictReader(csvfile)

  for row in reader:
    client = logic.createClient(row)
    eway_clients.append(client)

# create lacerte client objects and put into lacerte array
with open('lacerte_clients.csv', newline='') as csvfile:
  # field_names = ["Account Name","Preparer","Status","Street","City","State", "Zip"]
  # clients = csv.DictReader(csvfile, fieldnames=field_names)
  clients = csv.DictReader(csvfile)

  for row in clients:
    client = logic.createClient(row)
    lacerte_clients.append(client)

# check lacerteClient to find a matching ewayClient.
clients_not_in_eway, nonmatching_addrs, nonmatching_preparers, nonmatching_statuses = logic.matchClients(eway_clients, lacerte_clients)

# write to csv files
with open('results/clients_not_in_eway.csv', 'w', newline='') as csvfile:
  field_names = ['Account Name', 'Preparer', 'Status']
  writer = csv.DictWriter(csvfile, fieldnames=field_names)
  writer.writeheader()
  for client in clients_not_in_eway:
    writer.writerow({
      'Account Name': client.account_name,
      'Preparer': client.preparer,
      'Status': client.status
    })

with open('results/nonmatching_addrs.csv', 'w', newline='') as csvfile:
  field_names = ['Lacerte Account Name', 'eWay Address', 'Lacerte Address']
  writer = csv.DictWriter(csvfile, fieldnames=field_names)
  writer.writeheader()
  for name in nonmatching_addrs:
    writer.writerow({
      'Lacerte Account Name': name,
      'eWay Address': nonmatching_addrs[name][0],
      'Lacerte Address': nonmatching_addrs[name][1]
    })

with open('results/nonmatching_preparers.csv', 'w', newline='') as csvfile:
  field_names = ['Lacerte Account Name', 'eWay Preparer', 'Lacerte Preparer']
  writer = csv.DictWriter(csvfile, fieldnames=field_names)
  writer.writeheader()
  for name in nonmatching_preparers:
    writer.writerow({
      'Lacerte Account Name': name,
      'eWay Preparer': nonmatching_preparers[name][0],
      'Lacerte Preparer': nonmatching_preparers[name][1]
    })

with open('results/nonmatching_statuses.csv', 'w', newline='') as csvfile:
  field_names = ['Lacerte Account Name', 'eWay Status', 'Lacerte Status']
  writer = csv.DictWriter(csvfile, fieldnames=field_names)
  writer.writeheader()
  for name in nonmatching_statuses:
    writer.writerow({
      'Lacerte Account Name': name,
      'eWay Status': nonmatching_statuses[name][0],
      'Lacerte Status': nonmatching_statuses[name][1]
    })

