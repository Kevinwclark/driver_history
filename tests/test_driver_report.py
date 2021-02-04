import unittest
import driver_report as dr


filename = 'input.txt'
driver_set = {'Dan': {}, 'Lauren': {}, 'Kumi': {}}


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
        for index, driver in enumerate(dr.drivers):
            self.assertEqual(names[index], dr.drivers[driver].name)

    def test_driver_data_discard(self):
        """Checks if data is discarded"""
        self.fail('Driver data discard test not implemented')

    def test_driver_data_times(self):
        """Checks the driver times."""
        driver = "Dan"
        start = "07:15"
        stop = "07:45"
        miles = "17.3"
        dr.initialize_driver(driver)
        dr.driver_data(driver, start, stop, miles)
        self.assertEqual(dr.drivers[driver].hours, 0.5)

    def test_input_file(self):
        """Test end to end functionality"""
        self.fail('Input file test not implemented')


if __name__ == "__main__":
    unittest.main()
