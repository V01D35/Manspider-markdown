# MANSPIDER File Searcher

## Description
This script searches a specified directory for MANSPIDER files and generates a Markdown report listing the found files, their details, and why they might be of interest based on predefined criteria. It is designed to be used for security assessments, penetration testing, or forensic analysis.

## Features
- Recursively scans a directory for files
- Identifies files based on names, extensions, and keywords
- Generates a formatted Markdown report
- Allows users to specify both the search directory and output file location

## Installation
No installation required, but ensure you have Python installed.

### Requirements
- Python 3.x

## Usage
Run the script from the command line:

```sh
python manspider_markdown.py /path/to/search -o report.md -d /path/to/output
```

### Arguments
```sh
- `directory` (required) - The directory to search  
- `-o, --output` (optional) - The name of the output Markdown file (default: `search_results.md`)  
- `-d, --destination` (optional) - The directory where the output file should be saved (default: current working directory)  
```

### Example
```sh
python manspider_markdown.py /home/user/documents -o findings.md -d /home/user/reports
```
This will search /home/user/documents, generate findings.md, and save it in /home/user/reports.

