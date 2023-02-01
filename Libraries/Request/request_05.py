import html_to_json

html_string = """<head>
    <title>Test site</title>
    <meta charset="UTF-8"></head>"""
output_json = html_to_json.convert(html_string)
print(output_json)

output_json = html_to_json.convert(html_string,capture_element_values=False)
print(output_json)

output_json = html_to_json.convert(html_string,capture_element_values=False, capture_element_attributes=False)
print(output_json)
print(output_json['head'][0]['meta'])
