#!/bin/sh

for file in /data/Twitter\ dataset/geoTwitter20-*;
do nohup ./src/map.py --input_path="$file" --output_folder='outputs_new' > outputcheck/$(basename "$file"|cut -f 1 -d '.') &
done
