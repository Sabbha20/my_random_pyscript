import os

def replace_string_in_xml(xml_file, old_string, new_string):
    with open(xml_file, 'r') as file:
        xml_content = file.read()

    updated_content = xml_content.replace(old_string, new_string)

    with open(xml_file, 'w') as file:
        file.write(updated_content)

def process_xml_files(directory, old_string, new_string):
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            xml_file = os.path.join(directory, filename)
            replace_string_in_xml(xml_file, old_string, new_string)

# Replace 'ElementValue' in all XML files within the 'xml_files' directory with 'NewValue'
directory_path = r'/Users/sabbha/Desktop/WorkSpace/RandomPyPrjs/YOLO-OCR/images_labeled/'
element_to_replace = r'/home/srikanth/Desktop/windows_projects/django/data_cars/d/'
new_value = r'/Users/sabbha/Desktop/WorkSpace/RandomPyPrjs/YOLO-OCR/images_labeled/'

process_xml_files(directory_path, element_to_replace, new_value)
