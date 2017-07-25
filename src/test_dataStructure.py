import pytest
from datetime import datetime
from src import DataStructure


class TestDataStructure(object):



    def test_data_structure(self):
        data = DataStructure.DataStructure()
        assert data.data_structure() == {'Customer': None, 'ImageUpload': [], 'Order': [], 'OrderId': [], 'SiteVisit': []}


    def test_get_customer(self):
        data = DataStructure.DataStructure()
        data.add_new_customer(*["99f55c7d8f43","2017-01-06T12:46:46.384Z","Smith","Middletown","AK"])
        assert data.get_customer("99f55c7d8f43")["Customer"].customer_id == '99f55c7d8f43'
        assert data.get_customer("99f55c7d8f43")["Customer"].last_name == 'Smith'
        assert isinstance(data.get_customer("99f55c7d8f43")["Customer"].event_time,datetime)


    def test_add_new_customer(self):
        data = DataStructure.DataStructure()

        # Insufficient details so customer is not added to database.
        data.add_new_customer(*["99f55c7d8f43"])
        assert data.get_customer("99f55c7d8f43")["Customer"] == None



    def test_update_customer(self):
        assert True == True

    def test_add_site_visit(self):
        assert True == True

    def test_add_image_upload(self):
        assert True == True

    def test_add_new_order(self):
        assert True == True

    def test_update_order(self):
        assert True == True
