#!/usr/bin/env python3
"""Generates a Markdown file for use with Simiki or similar wikis,
based on a template. Handles YAML metadata generation.

Mostly for personal use, but feel free to use if you want a pretty
Markdown file with some YAML metadata!

To-Do:
- Allow users to customize template and metadata tags
"""


__author__ = "Phixyn"
__version__ = "1.0.0"


from collections import OrderedDict

import os
import sys
import time


def make_yaml_list(list_string):
    """Takes a comma-separated string and converts it into a YAML list.

    Args:
        list_string (str): A comma-separated string. Extra spacing is
            stripped after splitting.

    Returns:
        A string containing a YAML list.

    Examples:
        If `list_string` is "cats, dogs, foxes", it becomes:
          - cats
          - dogs
          - foxes

        This is returned as: "\n  - cats\n  - dogs\n  - foxes".
    """
    # This is where the YAML list item goes okay, don't judge my naming pls
    temp_list = []
    for metadata in list_string.split(","):
        temp_list.append(f"\n  - {metadata.strip()}")
    return "".join(temp_list)


def build_yaml_metadata():
    """Generates the document's YAML metadata based on the user's input.

    Returns:
        An OrderedDict containing the complete YAML metadata.
    """
    yaml_dict = OrderedDict()

    print("[INFO] To build your document's metadata, fill these in.")
    print("[INFO] Leave blank to keep defaults or exclude metadata:\n")
    yaml_dict["title"] = input("> Title (default: New Page): ") or "New Page"
    yaml_dict["description"] = input("> Description (default: None): ")

    # Date will be populated just before write to file, that way we get a
    # more accurate timestamp of when the file was created. However, we still
    # need an entry for it in the ordered dict, to ensure the right order.
    yaml_dict["date"] = ""

    category_input = input("> Category (specify multiple with commas): ")
    if category_input:
        if "," not in category_input:
            yaml_dict["category"] = category_input.strip()
        else:
            yaml_dict["categories"] = make_yaml_list(category_input)

    tags_input = input("> Tags (comma separated): ")
    if tags_input:
        if "," not in tags_input:
            yaml_dict["tag"] = f"\n  - {tags_input.strip()}"
        else:
            yaml_dict["tag"] = make_yaml_list(tags_input)

    yaml_dict["layout"] = input("> Layout (default: page): ") or "page"

    return yaml_dict


if __name__ == "__main__":
    print("[INFO] Welcome to fancy Markdown file generator!")
    print("[INFO] To generate your Markdown file, fill these in.")
    print("[INFO] Leave blank to keep defaults:\n")
    filename = input("> Filename (default: new-page.md): ") or "new-page.md"
    directory = input("> Directory (absolute, default: current directory): ") or os.getcwd()
    
    file_path = os.path.join(directory, filename)
    print(f"\n[DEBUG] Writing to: '{file_path}'.")
    # Try to create document folder if it doesn't exist
    if not os.path.isdir(directory):
        print("[DEBUG] Directory not found, attempting to create it...")
        os.mkdir(directory)
        print("[DEBUG] Directory created.")

    if os.path.isfile(file_path):
        print("[INFO] File exists and will be overwritten!")
        should_overwrite = input("Continue? (y/N): ") or None
        if not should_overwrite or should_overwrite.lower() != "y":
            print("[INFO] Not overwriting existing file.")
            print("[INFO] Did not create file, try a different name or folder.")
            sys.exit(1)
        else:
            print("[INFO] Overwriting existing file.")

    print("[INFO] Building YAML metadata...")
    metadata = build_yaml_metadata()

    print("\n[INFO] Writing to file...")
    with open(file_path, "w", encoding="utf-8") as md_file:
        # **Excessive use of print statements intensifies**
        print("[DEBUG] File is open for writing.")
        # Example format: date: 2020-01-20 20:20
        metadata["date"] = time.strftime("%Y-%m-%d %H:%M")
        # Make a YAML string. If metadata values are empty strings or None,
        # they won't appear in this string.
        # TODO: Try to get rid of join() and make a string directly from dict
        metadata_string = "".join([f"\n{k}: {v}" for k, v in metadata.items() if v])
        # md_file.write(template_string)
        md_file.write(f"""---{metadata_string}
---

# {metadata["title"]}

- [Section 1](#section-1)

- - -

## Section 1

Start here.""")
        print("[DEBUG] Wrote to file.")

    print(f"[DEBUG] Did close file: {md_file.closed}.")
    print(f"[INFO] Markdown file generated at '{file_path}'.")