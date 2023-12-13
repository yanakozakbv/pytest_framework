import argparse
import json
import xml.etree.ElementTree as ElementTree


class Human:
    def __init__ (self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def __get_property_names(self):
        return list(self.__dict__.keys())

    def convert_to_json(self):
        return json.dumps(self.__dict__)

    def convert_to_xml(self):
        root = ElementTree.Element(self.__class__.__name__)

        for key, value in self.__dict__.items():
            item = ElementTree.SubElement(root, key)
            item.text = self.name

        # Serialize object to XML
        return ElementTree.tostring(root, encoding='unicode')

    def parse(self):
        if args.parse == "json":
            return self.convert_to_json()
        else:  # default
            return self.convert_to_xml()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Argument parser')
    parser.add_argument("-parse")
    args = parser.parse_args()

    andrew = Human("John", 23, "male", 2000)

    print(andrew.parse())
