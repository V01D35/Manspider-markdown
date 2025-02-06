import os
import pathlib
import datetime
import argparse

def search_files(directory):
    """Searches the specified directory and retrieves file information."""
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            path = pathlib.Path(root) / filename
            size_kb = round(path.stat().st_size / 1024, 2)
            last_modified = datetime.datetime.fromtimestamp(path.stat().st_mtime).strftime("%d-%m-%Y %H:%M:%S")
            extension = path.suffix if path.suffix else "N/A"
            reason = determine_selection_reason(filename, extension)
            files.append([filename, extension, size_kb, last_modified, str(path), reason])
    return files

def determine_selection_reason(filename, extension):
    """Determines why a file was selected."""
    sensitive_keywords = {
        "password": "Passwords",
        "login": "Login credentials",
        "ssh": "SSH Keys",
        "idcard": "Personal Identification",
        "passport": "Personal Identification",
        "backup": "Backup Files",
        "certificate": "Certificates and Keys",
        "pentest": "Pentest Reports",
        "email": "Email Data",
        "confidential": "Confidential Documents",
    }
    
    for word, category in sensitive_keywords.items():
        if word in filename.lower():
            return category
    
    sensitive_extensions = {
        ".kdbx": "Password Manager Files",
        ".msg": "Email Files",
        ".pdf": "Documents",
        ".docx": "Documents",
        ".xlsx": "Excel Files",
    }
    return sensitive_extensions.get(extension.lower(), "Other Files")

def generate_markdown(file_data, output_file, output_dir, directory):
    """Generates a Markdown table with the search results."""
    if not file_data:
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, output_file)
        with open(output_path, "w") as f:
            f.write("# Search Results\n\nNo files found in the specified directory.\n")
        print(f"No files found. Markdown file created at: {output_path}")
        return

    headers = ["Filename", "Extension", "Size (KB)", "Last Modified", "Path", "Reason Found"]
    data = [headers] + file_data
    column_widths = [max(len(str(row[i])) for row in data) for i in range(len(headers))]

    def format_row(values):
        return "| " + " | ".join(f"{str(values[i]).ljust(column_widths[i])}" for i in range(len(values))) + " |"

    md_content = f"# Search Results\n\n**Searched Directory:** `{directory}`\n\n## Found Files\n\n"
    md_content += format_row(headers) + "\n"
    md_content += "|-" + "-|-".join("-" * column_widths[i] for i in range(len(headers))) + "-|\n"
    for row in file_data:
        md_content += format_row(row) + "\n"

    os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists
    output_path = os.path.join(output_dir, output_file)

    with open(output_path, "w") as f:
        f.write(md_content)
    print(f"Markdown file saved at '{output_path}'")

def main():
    parser = argparse.ArgumentParser(description="Search a directory and generate a Markdown file with found files.")
    parser.add_argument("directory", help="Path to the directory to search")
    parser.add_argument("-o", "--output", default="search_results.md", help="Name of the output file (default: search_results.md)")
    parser.add_argument("-d", "--output-dir", default=".", help="Directory to save the output file (default: current directory)")
    args = parser.parse_args()

    files = search_files(args.directory)
    generate_markdown(files, args.output, args.output_dir, args.directory)

if __name__ == "__main__":
    main()
