from lxml import etree

# Load and parse the XML Schema
with open('note.xsd', 'rb') as schema_file:
    schema_doc = etree.parse(schema_file)
    schema = etree.XMLSchema(schema_doc)

# Load and parse the XML file
with open('sample.xml', 'rb') as xml_file:
    xml_doc = etree.parse(xml_file)

# Validate the XML file against the schema
if schema.validate(xml_doc):
    print("XML is valid.")
else:
    print("XML is invalid.")
    # Print validation errors
    for error in schema.error_log:
        print(error.message)
