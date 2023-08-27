import lxml.etree as ET
from lxml.etree import XMLSyntaxError, DocumentInvalid

# Load XML and XSLT files
xml_tree = ET.parse("D:\christ\sem 1\web stack development\lab5(XML to html)\products.xml")
xslt_tree = ET.parse("D:\christ\sem 1\web stack development\lab5(XML to html)\ptransform.xsl")
transform = ET.XSLT(xslt_tree)

# Apply transformation
html_output = transform(xml_tree)

# Save transformed HTML to a file
output_file_path = r"D:\christ\sem 1\web stack development\lab5(XML to html)\transformed_output.html"
with open(output_file_path, "wb") as output_file:
    output_file.write(html_output)

# Validate transformed HTML against XSD schema
xsd = ET.XMLSchema(file="D:\christ\sem 1\web stack development\lab5(XML to html)\products.xsd")

try:
    html_tree = ET.parse(output_file_path)
    xsd.assertValid(html_tree)
    print("Validation successful. HTML adheres to schema rules.")
except (DocumentInvalid, XMLSyntaxError) as e:
    print("Validation failed. Errors:")
    print(e)
