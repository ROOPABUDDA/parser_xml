import xml.etree.ElementTree as ET
import json
from lxml import etree
from lxml.etree import XMLSchema, parse

# Function to validate XML against schema
def validate_xml(xml_file, xsd_file):
    # Parse the XML schema file
    with open(xsd_file, 'r') as schema_file:
        schema_root = etree.parse(schema_file)
        schema = XMLSchema(schema_root)

    # Parse the XML file and validate it
    tree = etree.parse(xml_file)
    if not schema.validate(tree):
        print("XML Validation Failed:")
        print(schema.error_log)
        return False

    print("XML Validation Successful.")
    return True

def xml_to_json(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    books = []

    for book in root.findall("book"):
        book_data = {
            "id": book.get("id"),
            "title": book.findtext("title"),
            "author": book.findtext("author"),
            "year": int(book.findtext("year")),
            "topics": [t.text for t in book.find("topics").findall("topic")]
        }
        books.append(book_data)

    return books

if __name__ == "__main__":
    xml_file = "sample_data.xml"
    xsd_file = "library_schema.xsd"

    # Validate the XML file before processing
    if validate_xml(xml_file, xsd_file):
        books_json = xml_to_json(xml_file)

        with open("books.json", "w", encoding="utf-8") as f:
            json.dump(books_json, f, indent=4, ensure_ascii=False)

        print("Conversion complete. Output saved to books.json.")
    else:
        print("Exiting due to XML validation failure.")