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
		client = logic.create_client(row)
		eway_clients.append(client)

# create lacerte client objects and put into lacerte array
with open('lacerte_clients.csv', newline='') as csvfile:
	# field_names = ["Account Name","Preparer","Status","Street","City","State", "Zip"]
	# clients = csv.DictReader(csvfile, fieldnames=field_names)
	clients = csv.DictReader(csvfile)

	for row in clients:
		client = logic.create_client(row)
		lacerte_clients.append(client)

# check lacerteClient to find a matching ewayClient.
(clients_not_in_eway, nonmatching_addrs, nonmatching_preparers,
 nonmatching_statuses, nonmatching_emails) = logic.match_clients(eway_clients, lacerte_clients)

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
	field_names = ['Lacerte Preparer', 'Lacerte Account Name', 'eWay Address', 'Lacerte Address']
	writer = csv.DictWriter(csvfile, fieldnames=field_names)
	writer.writeheader()
	for name in nonmatching_addrs:
		writer.writerow({
			'Lacerte Preparer': nonmatching_addrs[name][2],
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
	field_names = ['Lacerte Preparer', 'Lacerte Account Name', 'eWay Status', 'Lacerte Status']
	writer = csv.DictWriter(csvfile, fieldnames=field_names)
	writer.writeheader()
	for name in nonmatching_statuses:
		writer.writerow({
			'Lacerte Preparer': nonmatching_statuses[name][2],
			'Lacerte Account Name': name,
			'eWay Status': nonmatching_statuses[name][0],
			'Lacerte Status': nonmatching_statuses[name][1]
		})

with open('results/nonmatching_emails.csv', 'w', newline='') as csvfile:
	field_names = ['Lacerte Preparer', 'Lacerte Account Name',
								 'eWay Taxpayer Email', 'Lacerte Taxpayer Email',
								 'eWay Spouse Email', 'Lacerte Spouse Email']
	writer = csv.DictWriter(csvfile, fieldnames=field_names)
	writer.writeheader()
	for name in nonmatching_emails:
		writer.writerow({
			'Lacerte Preparer': nonmatching_emails[name][4],
			'Lacerte Account Name': name,
			'eWay Taxpayer Email': nonmatching_emails[name][0],
			'Lacerte Taxpayer Email': nonmatching_emails[name][1],
			'eWay Spouse Email': nonmatching_emails[name][2],
			'Lacerte Spouse Email': nonmatching_emails[name][3]
		})


# TODO: add missing phone numbers feature
# with open('results/missing_phone.csv', 'w', newline='') as csvfile:
#   field_names = ['Lacerte Preparer', 'Lacerte Account Name',
#                  'eWay Cell Phone', 'Lacerte Cell Phone',
#                  'eWay Home Phone', 'Lacerte Home Phone',
#                  'eWay Work Phone', 'Lacerte Work Phone',
#                  'eWay Other Phone']
#   writer = csv.DictWriter(csvfile, fieldnames=field_names)
#   writer.writeheader()
#   for name in missing_phone:
#     writer.writerow({
#       'Lacerte Preparer': missing_phone[name][2],
#       'Lacerte Account Name': name,
#       'eWay Cell Phone': missing_phone[phone_numbers][0],
#       'Lacerte Cell Phone': missing_phone[phone_numbers][1],
#       'eWay Home Phone': missing_phone[phone_numbers][0],
#       'Lacerte Home Phone': missing_phone[phone_numbers][1],
#       'eWay Work Phone': missing_phone[phone_numbers][0],
#       'Lacerte Work Phone': missing_phone[phone_numbers][1],
#       'eWay Other Phone': missing_phone[phone_numbers][0],
#       'Lacerte Other Phone': missing_phone[phone_numbers][1]
#     })

# TODO: add non-matching phone number feature
# with open('results/nonmatching_phone.csv', 'w', newline='') as csvfile:
#   field_names = ['Lacerte Preparer', 'Lacerte Account Name',
#                  'eWay Cell Phone', 'Lacerte Cell Phone',
#                  'eWay Home Phone', 'Lacerte Home Phone',
#                  'eWay Work Phone', 'Lacerte Work Phone',
#                  'eWay Other Phone']
#   writer = csv.DictWriter(csvfile, fieldnames=field_names)
#   writer.writeheader()
#   for name in nonmatching_phone:
#     writer.writerow({
#       'Lacerte Preparer': nonmatching_phone[name][2],
#       'Lacerte Account Name': name,
#       'eWay Cell Phone': nonmatching_phone[phone_numbers][0],
#       'Lacerte Cell Phone': nonmatching_phone[phone_numbers][1],
#       'eWay Home Phone': nonmatching_phone[phone_numbers][0],
#       'Lacerte Home Phone': nonmatching_phone[phone_numbers][1],
#       'eWay Work Phone': nonmatching_phone[phone_numbers][0],
#       'Lacerte Work Phone': nonmatching_phone[phone_numbers][1],
#       'eWay Other Phone': nonmatching_phone[phone_numbers][0],
#       'Lacerte Other Phone': nonmatching_phone[phone_numbers][1]
#     })
