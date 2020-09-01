import unittest
from employee import Employee
import requests
from unittest.mock import patch



class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')


    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smoter', 60000)

    def tearDown(self):
        print('tearDown')        
        pass




    def test_email(self):
        print('test_email')

        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smoter@email.com') 

        self.emp_1.first = 'jhon'
        self.emp_2.first = 'jane'
        
        self.assertEqual(self.emp_1.email, 'jhon.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'jane.Smoter@email.com')         



    def test_fullname(self):
        print('test_fullname')

        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smoter') 

        self.emp_1.first = 'jhon'
        self.emp_2.first = 'jane'
        
        self.assertEqual(self.emp_1.fullname, 'jhon Schafer')
        self.assertEqual(self.emp_2.fullname, 'jane Smoter')         



    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)         


    # def test_monthly_schedule(self):
    #     with patch('employee.requests.get') as mocked_get:
    #         mocked_get.return_value.ok = True      
    #         mocked_get.return_value.text = 'success'

    #         schedule = self.emp_1.monthly_schedule('May')
    #         mocked_get.assert_called_with('http://company.com/Schafer/May')      
    #         self.assertEqual(schedule, 'Success')







if __name__ == '__main__':
    unittest.main()