import json

# input and output filenames
input_file = "docs/nba_api_docs/nba_api.json"
output_file = "docs/nba_api_docs/nba_api_clean.json"

# read json file
with open(input_file, "r") as f:
    data = json.load(f)

# filter out entries where status is "invalid" or "deprecated"
filtered_data = {
    key: value
    for key, value in data.items()
    if value.get("status") not in ("invalid", "deprecated")
}

# write to new file
with open(output_file, "w") as f:
    json.dump(filtered_data, f, indent=4)

print(f"Filtered JSON written to {output_file}")
