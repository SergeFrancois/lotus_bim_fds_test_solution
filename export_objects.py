import argparse
import csv
import ifcopenshell
import ifcopenshell.geom
import ifcopenshell.util.element
import ifcopenshell.util.placement


def main():
    parser = argparse.ArgumentParser(description='Export objects from IFC to CSV')
    parser.add_argument('input_file_path', type=str, help='Input IFC file path')
    parser.add_argument('output_file_path', type=str, help='Output CSV file path')
    parser.add_argument('families', nargs='+', help='Object families for export')
    args = parser.parse_args()
    objects = []
    families = tuple(f.lower() for f in args.families)
    model = ifcopenshell.open(args.input_file_path)
    for storey in model.by_type("IfcBuildingStorey"):
        elements = ifcopenshell.util.element.get_decomposition(storey)
        for element in elements:
            if element.Name and ':' in element.Name:
                family, type, *_ = element.Name.split(':')
                family2 = family.lower()
                if any(f in family2 for f in families):
                    matrix = ifcopenshell.util.placement.get_local_placement(element.ObjectPlacement)
                    x, y, z = matrix[:,3][:3]
                    objects.append({'family': family, 'type': type, 'x': x, 'y': y, 'z': z})
    with open(args.output_file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file,
                                fieldnames=('family', 'type', 'x', 'y', 'z'),
                                quoting=csv.QUOTE_MINIMAL)
        # writer.writeheader()
        writer.writerow({'family': 'Family', 'type': 'Type', 'x': 'X', 'y': 'Y', 'z': 'Z'})
        for obj in objects:
            writer.writerow(obj)


if __name__ == '__main__':
    main()