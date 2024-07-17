#!/bin/bash

common_prefix="windreport1"

output_file="winmergedup.csv"

cat "${common_prefix}".csv_* >> "$output_file"

echo "CSV files merged and saved to $output_file"
