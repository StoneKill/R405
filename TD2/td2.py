"""TD2"""
import argparse
import re
from typing import List

REGEX_IPV4 = r"^.*((?:\d{1,3}\.){3}\d{1,3})\/(\d{1,2}).*$"
REGEX_IPV6 = (
    r".*\s("
    r"((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:)))(%.+)?s*(\/([0-9]|[1-9][0-9]|1[0-1][0-9]|12[0-8]))?"
    r")\s.*"
)


def prefix_list6(lines: List[str]) -> List[str]:
    """ipv6 prefix-list"""

    prefix_list: List[str] = []
    index = 10

    for line in lines:
        if m := re.match(REGEX_IPV6, line):
            prefix_list.append(f"ipv6 prefix-list PL6-RIPE seq {index} permit {m.group(1)} le 48")
            index += 10

    return prefix_list


def prefix_list4(lines: List[str]) -> List[str]:
    """ip prefix-list"""

    prefix_list: List[str] = []
    index = 10

    for line in lines:
        if m := re.match(REGEX_IPV4, line):
            prefix_list.append(f"ip prefix-list PL4-RIPE seq {index} permit {m.group(1)} le 24")
            index += 10

    return prefix_list


def main(args: argparse.Namespace) -> None:
    """main function"""

    with open(args.file, "r", encoding="utf-8") as f:
        ripe_alloc_list: List[str] = f.readlines()

    if args.ipv4:
        for line in prefix_list4(ripe_alloc_list):
            print(line)
    if args.ipv6:
        for line in prefix_list6(ripe_alloc_list):
            print(line)


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser(
        prog="TD2",
        description="TD regex",
    )
    parser.add_argument(
        "-f", "--file", action="store", help="YAML file path.", required=True, type=str
    )
    parser.add_argument(
        "-4",
        "--ipv4",
        action="store_true",
        help="Generate IPv4 prefix-list",
        required=False,
        default=False,
    )
    parser.add_argument(
        "-6",
        "--ipv6",
        action="store_true",
        help="Generate IPv6 prefix-list",
        required=False,
        default=False,
    )
    args = parser.parse_args()

    main(args)
