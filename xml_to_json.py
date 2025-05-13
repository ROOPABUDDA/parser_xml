import json
import xml.etree.ElementTree as ET

def xml_to_dict(elem):
    result = {}

    # Include element attributes if any
    if elem.attrib:
        result["@attributes"] = elem.attrib

    # Handle child elements
    children = list(elem)
    if children:
        child_dict = {}
        for child in children:
            child_result = xml_to_dict(child)
            tag = child.tag
            # Handle multiple children with the same tag
            if tag in child_dict:
                if not isinstance(child_dict[tag], list):
                    child_dict[tag] = [child_dict[tag]]
                child_dict[tag].append(child_result)
            else:
                child_dict[tag] = child_result
        result.update(child_dict)
    else:
        result = elem.text.strip() if elem.text else ""

    return result

# Parse the XML file
tree = ET.parse("sample_data.xml")
root = tree.getroot()

# Convert to dictionary
json_dict = {root.tag: xml_to_dict(root)}

# Convert to JSON string
json_output = json.dumps(json_dict, indent=2)

# Print or save
print(json_output)
# Optionally save to file
with open("output.json", "w") as f:
    f.write(json_output)
