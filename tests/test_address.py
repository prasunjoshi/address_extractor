import unittest
from address import Address

class TestAddress(unittest.TestCase):
    def test_extract_address_details(self):
        address_str_1 = "Winterallee 3"
        address_1 = Address(address_str_1)
        self.assertEqual(address_1.extract_address_details(), {"street": "Winterallee", "housenumber": "3"})

        address_str_2 = "Musterstrasse 45"
        address_2 = Address(address_str_2)
        self.assertEqual(address_2.extract_address_details(), {"street": "Musterstrasse", "housenumber": "45"})

        address_str_3 = "Blaufeldweg 123B"
        address_3 = Address(address_str_3)
        self.assertEqual(address_3.extract_address_details(), {"street": "Blaufeldweg", "housenumber": "123B"})

        address_str_4 = "Am Bächle 23"
        address_4 = Address(address_str_4)
        self.assertEqual(address_4.extract_address_details(), {"street": "Am Bächle", "housenumber": "23"})

        address_str_5 = "Auf der Vogelwiese 23 b"
        address_5 = Address(address_str_5)
        self.assertEqual(address_5.extract_address_details(), {"street": "Auf der Vogelwiese", "housenumber": "23 b"})

        address_str_6 = "4, rue de la revolution"
        address_6 = Address(address_str_6)
        self.assertEqual(address_6.extract_address_details(), {"street": "rue de la revolution", "housenumber": "4"})

        address_str_7 = "200 Broadway Av"
        address_7 = Address(address_str_7)
        self.assertEqual(address_7.extract_address_details(), {"street": "Broadway Av", "housenumber": "200"})

        address_str_8 = "Calle Aduana, 29"
        address_8 = Address(address_str_8)
        self.assertEqual(address_8.extract_address_details(), {"street": "Calle Aduana", "housenumber": "29"})

        address_str_9 = "Calle 39 No 1540"
        address_9 = Address(address_str_9)
        self.assertEqual(address_9.extract_address_details(), {"street": "Calle 39 No", "housenumber": "1540"})


if __name__ == '__main__':
    unittest.main()
