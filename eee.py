from back.main import XML_to_string, parse_XML

# test_XML_to_string
test_data1 = """
<root>
<user><name>name1</name></user>
</root>
"""
expected_output5 = "<root><user><name>name1</name></user></root>"
output = XML_to_string(test_data1)
print("XML_to_string output:", output)
print("Expected output:", expected_output5)

# test_parse_XML_single_element
test_data2 = """
<root>
    <value1>1</value1>
    <value2>2</value2>
</root>
"""
data33 = XML_to_string(test_data2)
result, _ = parse_XML(data=data33)
expected_result = {
    'root': {
        'value1': 1,
        'value2': 2
    }
}
print("parse_XML_single_element result:222", result)
print("Expected result:", expected_result)

# test_parse_XML_multiple_elements
test_data3 = """
<root>
    <user><email>123@gmail.com</email><name>name1</name></user>
    <user><email>321@gmail.com</email><name>name2</name></user>
</root>
"""
data1 = XML_to_string(test_data3)
result1, _ = parse_XML(data=data1)
expected_result1 = {
    'root': {
        'user': [
            {'email': '123@gmail.com', 'name': 'name1'},
            {'email': '321@gmail.com', 'name': 'name2'}
        ]
    }
}
print("parse_XML_multiple_elements result 22:", result1)
print("Expected result:", expected_result1)

# test_parse_XML_with_meta
test_data4 = """
<root>
    <value1>1</value1>
    <meta>
        <date>today</date>
        <x>33</x>
    </meta>
</root>
"""
data2 = XML_to_string(test_data4)
result2, _ = parse_XML(data=data2)
expected_result2 = {
    'root': {
        'value1': 1,
        'meta': {'date': 'today', 'x': 33}
    }
}
print("parse_XML_with_meta result:", result2)
print("Expected result:", expected_result2)

# test_parse_XML_numeric_values
test_data5 = """
<root>
    <value1>1</value1>
    <value2>2</value2>
</root>
"""
data3 = XML_to_string(test_data5)
result3, _ = parse_XML(data=data3)
expected_result3 = {
    'root': {
        'value1': 1,
        'value2': 2
    }
}
print("parse_XML_numeric_values result:", result3)
print("Expected result:", expected_result3)
