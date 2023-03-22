import re

class Address():
    def __init__(self, address_string):
        self.address_string = address_string

    def extract_address_details(self):
        # Regular expression to match the house number first format
        hn_regex = r"^(?:\d+[a-zA-Z]?(?:[\s\\/,\\-]\d*[a-zA-Z]?)?)\s+(.*)$"
        # Regular expression to match the street name first format
        sn_regex = r"^(.*)\s+(?:\d+[a-zA-Z]?(?:[\s\\/,\\-]\d*[a-zA-Z]?)?)$"
        
        # Check if the address matches the house number first format
        if re.match(hn_regex, self.address_string):
            pattern = r'^(\d+|\w+,*) (.*)$'
            match = re.match(pattern, self.address_string)
            if match:
                address_dict = {
                    "street": match.group(2),
                    "housenumber": match.group(1).strip(', ')
                }
                return address_dict
            else:
                return "unparsable address"

        # Check if the address matches the street name first format
        elif re.match(sn_regex, self.address_string):
            regex = r'^(?P<street>[\w\s-]+,*)\s(,*)(?P<number>\d+\s*[a-zA-Z]?)$'
            match = re.search(regex, self.address_string)
            if match:
                address_dict = {
                    "street": match.group('street').strip(', '),
                    "housenumber": match.group('number').strip()
                }
                return address_dict
            else:
                return "unparsable address"
        # If the address doesn't match either format, return 'unparsable address' "
        else:
            return "unparsable address"