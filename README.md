# Various Python Scripts

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

## Python Twitch URL Grabber [broken]

Grabs HLS stream links from live Twitch.tv channels, so that they can be opened with a media player such as VLC.

* [SCRUM Board on Taiga.io](https://tree.taiga.io/project/phixyn-twitch-url-grabber/)
