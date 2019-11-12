#!/bin/bash

# Perform alignment for each fastq.gz file in the folder. 
# It is required that mt_genome.fa be already indexed with:
# bwa index mt_genome.fa

for f in *.fastq.gz; do
  echo "Aligning ${f}"
  zcat $f | fq_filt.py | fq_trim.py subseq.txt | bwa mem -M -t 16 mt_genome.fa - > ${f%%.*}.sam
  echo ""
done
