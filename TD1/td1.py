"""TD 1"""
import argparse
from typing import Any, Dict, List

from tabulate import tabulate
from yaml import YAMLError
from yaml import safe_load as yaml_safe_load


def load_yaml_file(path: str) -> Dict[str, Any]:
    """Load YAML file."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml_safe_load(f)


def check_yaml(yaml_path: str) -> bool:
    """Check if yaml file exists, is readable and is valid"""

    try:
        load_yaml_file(yaml_path)
    except YAMLError:
        print("Invalid YAML file")
        return False
    except IOError as e:
        print(f"Can't open file : {e.strerror}")
        return False

    return True


def print_tabular_enhanced(data: Dict[str, Any]) -> None:
    """Print data in tabular format."""
    if "zone_dns" not in data:
        print("Can't find 'zone_dns' key in YAML file!")
        return

    dns_entries: List[Dict[str, Any]] = data["zone_dns"]
    if not (isinstance(dns_entries, list) and isinstance(dns_entries[0], dict)):
        print(
            "'zone_dns' key must be an array (list) of associative arrays (map/dict)!"
        )
        return

    # headers = list(
    #     set([entry for i in range(len(dns_entries)) for entry in dns_entries[i].keys()])
    # )
    headers: List[str] = []
    for i in range(len(dns_entries)):
        for header in dns_entries[i]:
            if header not in headers:
                headers.append(header)
    if "nom" in headers:
        headers.insert(0, headers.pop(headers.index("nom")))

    # table: Dict[str, List[Any]] = {k: [entry.get(k, "") for entry in dns_entries] for k in headers}
    table: Dict[str, List[Any]] = {header: [] for header in headers}
    for entry in dns_entries:
        for header in headers:
            table[header].append(entry.get(header, ""))

    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))


def print_tabular(data: Dict[str, Any]) -> None:
    """Print data in tabular format."""
    if "zone_dns" not in data:
        print("Can't find 'zone_dns' key in YAML file!")
        return

    dns_entries: List[Dict[str, Any]] = data["zone_dns"]
    if not (isinstance(dns_entries, list) and isinstance(dns_entries[0], dict)):
        print(
            "'zone_dns' key must be an array (list) of associative arrays (map/dict)!"
        )
        return

    headers = list(dns_entries[0].keys())
    if "nom" in headers:
        headers.insert(0, headers.pop(headers.index("nom")))

    table: Dict[str, List[Any]] = {k: [] for k in headers}
    for entry in dns_entries:
        for header in headers:
            table[header].append(entry[header])

    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))


def print_zone(data: Dict[str, Any]) -> None:
    """Print dns zone name"""
    if "zone" not in data:
        print("Can't find 'zone' key in YAML file!")
        return

    print(f'DNS zone name: {data["zone"]}')


def main(args: argparse.Namespace) -> None:
    """Main function"""
    if args.check:
        if check_yaml(args.file):
            print("Well done! YAML file is valid!")
        else:
            print("Try again!")
        return

    data = load_yaml_file(args.file)
    if args.zone:
        print_zone(data)
    if args.print:
        print_tabular(data)
    if args.print_enhanced:
        print_tabular_enhanced(data)


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser(
        prog="TD1",
        description="Parsing fichier YAML",
    )
    parser.add_argument(
        "-f", "--file", action="store", help="YAML file path.", required=True, type=str
    )
    parser.add_argument(
        "-c",
        "--check",
        action="store_true",
        help="Check if YAML file is readable and valid.",
        required=False,
        default=False,
    )
    parser.add_argument(
        "-p",
        "--print",
        action="store_true",
        help="Print DNS entries in your YAML file in tabular format.",
        required=False,
        default=False,
    )
    parser.add_argument(
        "-e",
        "--print_enhanced",
        action="store_true",
        help="Print DNS entries in your YAML file in tabular format even if each "
        "row does not have the same number of colums.",
        required=False,
        default=False,
    )
    parser.add_argument(
        "-z",
        "--zone",
        action="store_true",
        help="Print DNS zone name from your YAML file.",
        required=False,
        default=False,
    )
    args = parser.parse_args()

    main(args)
