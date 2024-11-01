import unittest
import mockdata
from reconciliation import resources

class TestResources(unittest.TestCase):
  #mock data?...

  def test_createClient(self):
    name = mockdata.mock_MFJ['Account Name']
    preparer = mockdata.mock_MFJ['Preparer']
    status = mockdata.mock_MFJ['Status']
    street = mockdata.mock_MFJ['Street']
    city = mockdata.mock_MFJ['City']
    state = mockdata.mock_MFJ['State']
    zip = mockdata.mock_MFJ['Zip']

    mock_client = resources.Client(name, preparer, status, street, city, state, zip)
    created_client = resources.createClient(name, preparer, status, street, city, state, zip)

    self.assertEqual(mock_client, created_client)

  # def test_nameMatch(self):

  # def test_addrMatch(self):

  # def test_preparerMatch(self):
    #setup
    # self.assertEqual()