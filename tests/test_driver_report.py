import unittest
import driver_report as dr


filename = 'input.txt'
driver_set = {'Dan': [], 'Lauren': [], 'Kumi': []}

class TestDriver(unittest.TestCase):

    def test_command_finder(self):
        driver = 0
        test = 0
        with open(filename, 'r') as f:
            x = f.read().splitlines()
            for line in x:
                y = line.split(' ')
                if y[0] == "Driver":
                    driver += 1
                elif y[0] == 'Trip':
                    test += 1
        self.assertEqual(driver, 3)
        self.assertEqual(test, 3)


    def test_initialize_driver(self):
        """Checks for Driver initialization"""
        names = ['Dan', 'Lauren', 'Kumi']
        for i in names:
            dr.initialize_driver(i)
        self.assertEqual(dr.d, driver_set)
    

    def test_initialize_driver_double(self):
        """Checks for Driver initialization and doesn't create two drivers"""
        names_double = ['Dan', 'Lauren', 'Kumi', 'Dan']
        for i in names_double:
            dr.initialize_driver(i)
        print('Why is this like this', dr.d)
        self.assertEqual(dr.d, driver_set)
        
    
    # def test_driver_data_times(self):
    #     """Checks the driver times."""
    #     driver = "Lauren"
    #     times = ["12:01", "13:16"]
    #     miles = "42.0"
    #     output = {"Lauren": [42, 34]}
    #     dr.driver_data(driver, times, miles)
    #     self.assertEqual(dr.d[], output)
        


if __name__ == "__main__":
    unittest.main()