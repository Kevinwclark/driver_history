import unittest
import driver_report as dr
import subprocess


filename = 'input.txt'


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
            self.assertIsInstance(dr.drivers[driver], dr.Driver)

    def test_driver_data_discard_fast(self):
        """Checks if data is discarded if average > 100"""
        driver = "Dan"
        start = "07:15"
        stop = "07:45"
        miles = "51"
        dr.initialize_driver(driver)
        self.assertIsInstance(dr.drivers[driver], dr.Driver)
        dr.driver_data(driver, start, stop, miles)
        self.assertEqual(dr.drivers[driver].miles, 0)
        self.assertEqual(dr.drivers[driver].hours, 0)

    def test_driver_data_discard_slow(self):
        """Checks if data is discarded if average < 5"""
        driver = "Dan"
        start = "07:15"
        stop = "07:45"
        miles = "2"
        dr.initialize_driver(driver)
        self.assertIsInstance(dr.drivers[driver], dr.Driver)
        dr.driver_data(driver, start, stop, miles)
        self.assertEqual(dr.drivers[driver].miles, 0)
        self.assertEqual(dr.drivers[driver].hours, 0)

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
        sample = ['Lauren', 'Dan', 'Kumi']
        dr.main(['input.txt'])
        drivers = dr.drivers
        sorted_drivers = sorted(
                drivers,
                key=lambda name: dr.drivers[name].miles,
                reverse=True
            )
        self.assertEqual(sorted_drivers, sample)

    def test_flake8(self):
        """Checking for PEP8/flake8 compliance"""
        result = subprocess.run(['flake8', "driver_report.py"])
        self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
