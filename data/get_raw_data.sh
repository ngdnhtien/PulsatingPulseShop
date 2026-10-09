#!/bin/sh
# Fetch the raw single-shot arrays (1.5 GB) from the GitHub release and unzip them into the repository.
set -e
cd "$(dirname "$0")/.."
for part in PulsatingPulseShop_raw_data.zip PulsatingPulseShop_raw_data_2.zip; do
  curl -L -o "$part" "https://github.com/ngdnhtien/PulsatingPulseShop/releases/download/v1.0-data/$part"
  unzip -o "$part"
  rm "$part"
done
echo "raw data in place: $(find data -name iq_data.npy | wc -l) iq_data.npy files"
