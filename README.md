# Various Python Scripts

![](https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue.svg)

A set of handy scripts. Written in Python 3 with 💜

Send requests via Twitter: [@Phixyn](https://twitter.com/Phixyn).

## CSV To JSON

Reads CSV data from a file, converts it to JSON format and saves it to a new file.

**Example usages:**

```sh
./CSV_To_JSON.py Input.csv Output.json "Column 1" "Column 2" "Column 3"
./CSV_To_JSON.py -i 2 -mk "April Sales" Input.csv Output.json "Column 1" "Column 2" "Column 3"
./CSV_To_JSON.py --transpose Needs_Transposing.csv Output.json "Column 1" "Column 2" "Column 3"
```

## CSV Transpose

Transposes the contents of a CSV file and saves the output to a new file.

**Example usages:**

```sh
./CSV_Transpose.py Input.csv Output.csv
./CSV_Transpose.py --add-quotes Input.csv Output.csv
```

## URL Markify

> Usage: ./url_markify.py

Generates a nicely formatted website link in Markdown syntax. For example:

`[Phixyn - Blog](https://phixyn.com/blog)`

This script requires third-party modules listed in `requirements.txt`. These can be quickly installed using `pip install -r requirements.txt` globally or in a virtual environment.

## Markdown File Generator

> Usage: ./generate_md_wiki_file.py

Generates a Markdown file for use with Simiki or similar wikis, based on a template. Handles YAML metadata generation.

This is mostly for personal use, but feel free to use if you want a pretty Markdown file with some YAML metadata!

Here's an example of what gets generated: [https://github.com/Phixyn/mwiki/blob/master/template.md](https://github.com/Phixyn/mwiki/blob/master/template.md)

## Python Twitch URL Grabber [broken]

Grabs HLS stream links from live Twitch.tv channels, so that they can be opened with a media player such as VLC.

* [SCRUM Board on Taiga.io](https://tree.taiga.io/project/phixyn-twitch-url-grabber/)
