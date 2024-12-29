def XML_to_string(data):
    data_single_line = ""
    in_tag = False

    for char in data:
        if char == "<":
            in_tag = True
            data_single_line += char
        elif char == ">":
            in_tag = False
            data_single_line += char
        elif not in_tag and char not in ["\n", "\t"]:
            data_single_line += char
        elif in_tag:
            data_single_line += char
    data_single_line = data_single_line.rstrip()
    data_single_line = data_single_line.replace("  ", "")
    return data_single_line




def parse_XML(data, result, count=0):
    is_tag = False
    is_closed_tag = False
    is_value = False
    tag = ""
    value = ""
    while count < len(data) - 1:
        item = data[count]
        if item == "<":
            if data[count + 1] != "/":
                is_tag = True
            if is_value:
                try:
                    value = int(value)
                except ValueError:
                    pass
                if isinstance(result, list):
                    result[-1][tag] = value
                else:
                    if result[tag] != {}:
                        temp = result
                        result = []
                        result.append(temp)
                        result.append({})
                        result[-1][tag] = value
                    else:
                        result[tag] = value
                value = ""
            if data[count + 1] == "/":
                is_closed_tag = True

        if item == ">":
            if is_closed_tag:
                count -= 1
                return result, count
            if tag not in result:
                if isinstance(result, list):
                    result[-1][tag] = {}
                elif isinstance(result, dict):
                    result[tag] = {}
            is_tag = False
            if data[count + 1] != "<":
                is_value = True
            elif data[count + 2] != "/":
                res, count = parse_XML(data, result[tag], count + 1)

                result[tag] = res

        if is_value and item != "<" and item != ">":
            value += item

        if is_tag and item != "<" and item != ">":
            tag += item
        count += 1
    return result, count

if __name__ == '__main__':
    data_XML = f"""
        <root>
        <user>
            <email>123@gmail.com</email>
            <name>name1</name>
        </user>
        <user>
            <email>321@gmail.com</email>
            <name>name2</name>
        </user>
        <value1>1</value1>
        <value2>2</value2>
        <meta>
            <date>today</date>
            <x>33</x>
        </meta>
        </root>
        """
    data_to = XML_to_string(data_XML)
    res, count = parse_XML(data_to, {})
    print(res)
