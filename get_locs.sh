#!/bin/bash

# Export sequence name and alignment location for each alignment with
# quality >= 60
for f in *.sam; do
  echo "Reading ${f}"
  samtools view -q 60 $f |  gawk '{ print $1, $4}' >> loc.txt
  echo ""
done
