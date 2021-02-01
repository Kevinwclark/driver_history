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
        pass
        
        
        
        


if __name__ == "__main__":
    unittest.main()