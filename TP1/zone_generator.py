#!/usr/bin/env python3

import argparse

import jinja2
import yaml


def main() -> None:
    """
    Main function
    """
    
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--template', help='Zone template file', default='template.j2')
    parser.add_argument('--data', help='Zone data file in YAML format', default='data.yaml')
    parser.add_argument('--out', help='Zone output file', default=None)
    args = parser.parse_args()

    # Load YAML file
    with open(args.data, 'r') as file:
        data = yaml.load(file, Loader=yaml.Loader)

    # Load and render template
    with open(args.template, 'r') as file:
        template = jinja2.Template(file.read())
        render = template.render(data)

    # Rendered template output to file or stdout
    if args.out:
        with open(args.out, 'w') as file:
            file.write(render)
    else:
        print(render)

if __name__ == '__main__':
    main()
