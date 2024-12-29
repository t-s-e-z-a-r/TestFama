import unittest
from main import XML_to_string, parse_XML

class TestXMLParsing(unittest.TestCase):
    
    def test_XML_to_string(self):
        test_data1 = """
        <root>
        <user><name>name1</name></user>
        </root>
        """
        expected_output1 = "<root><user><name>name1</name></user></root>"
        result1 = XML_to_string(test_data1)
        self.assertEqual(result1, expected_output1)

    def test_parse_XML_single_element(self):
        test_data2 = """
        <root>
            <value1>1</value1>
            <value2>2</value2>
        </root>
        """
        data2 = XML_to_string(test_data2)
        result2, _ = parse_XML(data=data2, result={})
        expected_result2 = {
            'root': {
                'value1': 1,
                'value2': 2
            }
        }
        self.assertEqual(result2, expected_result2)

    def test_parse_XML_multiple_elements(self):
        test_data3 = """
        <root>
            <user><email>123@gmail.com</email><name>name1</name></user>
            <user><email>321@gmail.com</email><name>name2</name></user>
        </root>
        """
        data3 = XML_to_string(test_data3)
        result3, _ = parse_XML(data=data3, result={})
        expected_result3 = {
            'root': {
                'user': [
                    {'email': '123@gmail.com', 'name': 'name1'},
                    {'email': '321@gmail.com', 'name': 'name2'}
                ]
            }
        }
        self.assertEqual(result3, expected_result3)

    def test_parse_XML_with_meta(self):
        test_data4 = """
        <root>
            <value1>1</value1>
            <meta>
                <date>today</date>
                <x>33</x>
            </meta>
        </root>
        """
        data4 = XML_to_string(test_data4)
        result4, _ = parse_XML(data=data4, result={})
        expected_result4 = {
            'root': {
                'value1': 1,
                'meta': {'date': 'today', 'x': 33}
            }
        }
        self.assertEqual(result4, expected_result4)

    def test_parse_XML_numeric_values(self):
        test_data5 = """
        <root>
            <value1>1</value1>
            <value2>2</value2>
        </root>
        """
        data5 = XML_to_string(test_data5)
        result5, _ = parse_XML(data=data5, result={})
        expected_result5 = {
            'root': {
                'value1': 1,
                'value2': 2
            }
        }
        self.assertEqual(result5, expected_result5)
        
if __name__ == '__main__':
    unittest.main()
