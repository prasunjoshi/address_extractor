# Address Extractor

Input: string of address

Output: string of street and string of street-number as JSON object

In the solution we are using 2 step regular expressions based approach
- classifies the order of street name and house number using the first set of regular expression
- based on classfication, we can map the respected type with the other regular expression which separates street and house number.

1. The most simple cases, e.g.
   1. `"Winterallee 3"` -> `{"street": "Winterallee", "housenumber": "3"}`
   1. `"Musterstrasse 45"` -> `{"street": "Musterstrasse", "housenumber": "45"}`
   1. `"Blaufeldweg 123B"` -> `{"street": "Blaufeldweg", "housenumber": "123B"}`

2. More complicated cases
   1. `"Am Bächle 23"` -> `{"street": "Am Bächle", "housenumber": "23"}`
   1. `"Auf der Vogelwiese 23 b"` -> `{"street": "Auf der Vogelwiese", "housenumber": "23 b"}`

3. Other countries (complex cases)
   1. `"4, rue de la revolution"` -> `{"street": "rue de la revolution", "housenumber": "4"}`
   1. `"200 Broadway Av"` -> `{"street": "Broadway Av", "housenumber": "200"}`
   1. `"Calle Aduana, 29"` -> `{"street": "Calle Aduana", "housenumber": "29"}`
   1. `"Calle 39 No 1540"` -> `{"street": "Calle 39", "housenumber": "No 1540"}`

## Code Structure 
- `address.py`: The method `extract_address_details` has the desired logic to extract address
- `tests/test_address.py`: contains the test cases
- `requirements.txt`: No additional dependency is required, hence requirements.txt is empty

## Steps to Run
1. Add your desired testcases in the `tests/test_address.py`
2. Update project directory path in `tests/test_address.py`
    ```
    sys.path.append('/path/to/project')
    ```
3. Run the testcases    
    ```
    $ python3 tests/test_address.py
    ``` 

To extend/ cover more use-cases of this problem, we can extend this classification to multiple classes and map with respective regular expressions. This will ensure we are notoverfitting any data.