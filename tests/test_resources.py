import unittest
from src import logic

MFJ_name = "Gonzalez, Daniel And Danielle"
MFJ_e_preparer = 'Caitlin White'
MFJ_status_str = 'Final'
MFJ_street = '18 John Wall Plaza'
MFJ_city = 'Columbus'
MFJ_state = 'OH'
MFJ_zipcode = '27364'

mock_client = logic.Client(MFJ_name, MFJ_e_preparer, MFJ_status_str, MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode)


class TestResources(unittest.TestCase):
  
  def test_createClient(self):

    row = {
      'Account Name': MFJ_name,
      'Preparer': '6',
      'Status': '5',
      'Street': MFJ_street,
      'City': MFJ_city,
      'State': MFJ_state,
      'Zip': MFJ_zipcode
    }

    created_client = logic.createClient(row)

    self.assertEqual(mock_client.last_name, created_client.last_name)
    self.assertEqual(mock_client.first_names, created_client.first_names)
    self.assertEqual(mock_client.preparer, created_client.preparer)
    self.assertEqual(mock_client.status, created_client.status)
    self.assertEqual(mock_client.address['Street'], created_client.address['Street'])
    self.assertEqual(mock_client.address['City'], created_client.address['City'])
    self.assertEqual(mock_client.address['State'], created_client.address['State'])
    self.assertEqual(mock_client.address['Zip'], created_client.address['Zip'])

  def test_nameMatch(self):

    name_formatting_client = logic.Client(
      "Gonzalez,   Daniel D. & Danielle F. ", MFJ_e_preparer, MFJ_status_str, MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode
    )
    
    non_matching_S_client = logic.Client(
      "Scott, Zoey", MFJ_e_preparer, MFJ_status_str, MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode
    )

    non_matching_S2_client = logic.Client(
      "Scott, Janet S.", MFJ_e_preparer, MFJ_status_str, MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode
    )

    nearmatch_s_client = logic.Client(
      "Gonzalez, Daniel", MFJ_e_preparer, MFJ_status_str, MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode
    )
    nearmatch_married_client = logic.Client(
      "Gonzalez, Daniel and Gabriella", MFJ_e_preparer, MFJ_status_str, MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode
    )
    name_nonmatching_client = logic.Client(
      "Gonzalez, Dania and Dani", MFJ_e_preparer, MFJ_status_str, MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode
    )

    self.assertTrue(logic.nameMatch(mock_client, name_formatting_client))

    self.assertFalse(logic.nameMatch(mock_client, non_matching_S_client))
    self.assertFalse(logic.nameMatch(non_matching_S_client, non_matching_S2_client))
    self.assertFalse(logic.nameMatch(mock_client, nearmatch_s_client))
    self.assertFalse(logic.nameMatch(mock_client, nearmatch_married_client))
    self.assertFalse(logic.nameMatch(mock_client, name_nonmatching_client))

  def test_addrMatch(self):

    matching_addr_client = logic.Client(
      'bogus, name', '5', '20', MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode
    )
    nonmatching_addr_client = logic.Client(
      MFJ_name, MFJ_e_preparer, MFJ_status_str, '42 Wallaby Way', 'Sydney', 'AU', '87198'
    )
    
    self.assertTrue(logic.addrMatch(mock_client, matching_addr_client))

    self.assertFalse(logic.addrMatch(mock_client, nonmatching_addr_client))

  def test_preparerMatch(self):

    matching_preparer_client = logic.Client(
      'bogus, name', MFJ_e_preparer, 'these', 'attrs', 'don\'t', 'match', 'anything'
    )
    nonmatching_preparer_client = logic.Client(
      MFJ_name, 'Kathy McGinnis', MFJ_status_str, MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode
    )

    self.assertTrue(logic.preparerMatch(mock_client, matching_preparer_client))

    self.assertFalse(logic.preparerMatch(mock_client, nonmatching_preparer_client))

  def test_statusMatch(self):

    lacerteStatuses = [
      'Proforma\'d', 'Final', 'Amended', 'Paper Return', 'Next Year', 'Planning', 'Not Processed'
      ]
    eWayStatuses = [
      'Tax Client - Appt (In Person)', 'Tax Client - Appt (Teams)', 'No Appt', 'Mail', 'No Mail', 'Former'
      ]
    
    lacerte_status_0 = logic.Client(MFJ_name, MFJ_e_preparer, lacerteStatuses[0], MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode)
    lacerte_status_1 = logic.Client(MFJ_name, MFJ_e_preparer, lacerteStatuses[1], MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode)
    lacerte_status_2 = logic.Client(MFJ_name, MFJ_e_preparer, lacerteStatuses[2], MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode)
    lacerte_status_3 = logic.Client(MFJ_name, MFJ_e_preparer, lacerteStatuses[3], MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode)
    lacerte_status_4 = logic.Client(MFJ_name, MFJ_e_preparer, lacerteStatuses[4], MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode)
    lacerte_status_5 = logic.Client(MFJ_name, MFJ_e_preparer, lacerteStatuses[5], MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode)
    lacerte_status_6 = logic.Client(MFJ_name, MFJ_e_preparer, lacerteStatuses[6], MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode)

    eway_status_0 = logic.Client(MFJ_name, MFJ_e_preparer, eWayStatuses[0], MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode)
    eway_status_1 = logic.Client(MFJ_name, MFJ_e_preparer, eWayStatuses[1], MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode)
    eway_status_2 = logic.Client(MFJ_name, MFJ_e_preparer, eWayStatuses[2], MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode)
    eway_status_3 = logic.Client(MFJ_name, MFJ_e_preparer, eWayStatuses[3], MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode)
    eway_status_4 = logic.Client(MFJ_name, MFJ_e_preparer, eWayStatuses[4], MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode)
    eway_status_5 = logic.Client(MFJ_name, MFJ_e_preparer, eWayStatuses[5], MFJ_street, MFJ_city, MFJ_state, MFJ_zipcode)

    # Proforma'd
    self.assertTrue(logic.statusMatch(eway_status_0, lacerte_status_0))
    self.assertTrue(logic.statusMatch(eway_status_1, lacerte_status_0))
    self.assertTrue(logic.statusMatch(eway_status_2, lacerte_status_0))
    self.assertTrue(logic.statusMatch(eway_status_3, lacerte_status_0))
    self.assertTrue(logic.statusMatch(eway_status_4, lacerte_status_0))
    self.assertFalse(logic.statusMatch(eway_status_5, lacerte_status_0))

    # Final
    self.assertTrue(logic.statusMatch(eway_status_0, lacerte_status_1))
    self.assertTrue(logic.statusMatch(eway_status_1, lacerte_status_1))
    self.assertTrue(logic.statusMatch(eway_status_2, lacerte_status_1))
    self.assertTrue(logic.statusMatch(eway_status_3, lacerte_status_1))
    self.assertTrue(logic.statusMatch(eway_status_4, lacerte_status_1))
    self.assertFalse(logic.statusMatch(eway_status_5, lacerte_status_1))

    # Amended
    self.assertTrue(logic.statusMatch(eway_status_0, lacerte_status_2))
    self.assertTrue(logic.statusMatch(eway_status_1, lacerte_status_2))
    self.assertTrue(logic.statusMatch(eway_status_2, lacerte_status_2))
    self.assertTrue(logic.statusMatch(eway_status_3, lacerte_status_2))
    self.assertTrue(logic.statusMatch(eway_status_4, lacerte_status_2))
    self.assertFalse(logic.statusMatch(eway_status_5, lacerte_status_2))

    # Paper Return
    self.assertTrue(logic.statusMatch(eway_status_0, lacerte_status_3))
    self.assertTrue(logic.statusMatch(eway_status_1, lacerte_status_3))
    self.assertTrue(logic.statusMatch(eway_status_2, lacerte_status_3))
    self.assertTrue(logic.statusMatch(eway_status_3, lacerte_status_3))
    self.assertTrue(logic.statusMatch(eway_status_4, lacerte_status_3))
    self.assertFalse(logic.statusMatch(eway_status_5, lacerte_status_3))

    # Next Year
    self.assertTrue(logic.statusMatch(eway_status_0, lacerte_status_4))
    self.assertTrue(logic.statusMatch(eway_status_1, lacerte_status_4))
    self.assertTrue(logic.statusMatch(eway_status_2, lacerte_status_4))
    self.assertTrue(logic.statusMatch(eway_status_3, lacerte_status_4))
    self.assertTrue(logic.statusMatch(eway_status_4, lacerte_status_4))
    self.assertFalse(logic.statusMatch(eway_status_5, lacerte_status_4))

    # Planning
    self.assertTrue(logic.statusMatch(eway_status_0, lacerte_status_5))
    self.assertTrue(logic.statusMatch(eway_status_1, lacerte_status_5))
    self.assertTrue(logic.statusMatch(eway_status_2, lacerte_status_5))
    self.assertTrue(logic.statusMatch(eway_status_3, lacerte_status_5))
    self.assertTrue(logic.statusMatch(eway_status_4, lacerte_status_5))
    self.assertFalse(logic.statusMatch(eway_status_5, lacerte_status_5))

    # Not Processed
    self.assertFalse(logic.statusMatch(eway_status_0, lacerte_status_6))
    self.assertFalse(logic.statusMatch(eway_status_1, lacerte_status_6))
    self.assertFalse(logic.statusMatch(eway_status_2, lacerte_status_6))
    self.assertFalse(logic.statusMatch(eway_status_3, lacerte_status_6))
    self.assertFalse(logic.statusMatch(eway_status_4, lacerte_status_6))
    self.assertTrue(logic.statusMatch(eway_status_5, lacerte_status_6))