# Duke_CBB520_HW3

## Authors
    - Marcelo Lerendegui
    - Kuei-Yueh Ko
    - Jianqiao Liu
    - Weihsien Lee

## Contents
**align.sh:**
    ascript that aligns all the fastq files and generates sam files

**command_out.txt:**
    output i got when i called allign.sh

**get_locs.sh:**
    reads all sam files and generates loc.txt, a text file
    with sequence names and alignment locations

**loc.txt:**
    output of get_locs.sh

**mt_genome.flat:**
    flat file where I took the region types and names for the
    reference genome

**mt_genome_regions.py:**
    module with dictionary with region info and some functions

**mt_gen_ref.py:**
    a script that reads loc.txt and generates loc_type.txt, a text
    file that has sequence name, location, type, name and
    complement strand.

**loc_type.txt:**
    output of mt_gen_ref.py

**hits.py:**
    script that reads loc_type.txt and plots the number of matches
    for each mt_genome position. each region type is plotted using
    different colors.

**get_stats.py:**
    a script that reads loc_type.txt and prints stats about aligns

**stats.txt:**
    output of get_stats.py

## Usage

#### First index the genome:

```sh
bwa index mt_genome.fa
```

#### Align all files:

```sh
./align.sh
```

#### Get hit locations:

```sh
./get_locs.sh
```

#### Add region information to each location:

```sh
python mt_gen_ref.py
```

#### Print statistics of the alignments:

```sh
python hits.py
python get_stats.py
```