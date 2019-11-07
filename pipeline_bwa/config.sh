###
set -u

### Directories for Data and results
export DATA_BASE=$HOME/work/DATA/fastq_cbb520_hw3
export FASTQS_RAW=$DATA_BASE/assignment_3
export FASTQS_TRIMMED=$DATA_BASE/fastqs_trimmed
export FASTQS_FILTER=$DATA_BASE/fastqs_filter

### Genome: Canis Family Mitochondria
export FA_URL="ftp://ftp.ensembl.org/pub/release-98/fasta/canis_familiaris/dna/Canis_familiaris.CanFam3.1.dna.chromosome.MT.fa.gz"
export GTF_URL="ftp://ftp.ensembl.org/pub/release-98/gtf/canis_familiaris/Canis_familiaris.CanFam3.1.98.gtf.gz"
export GTF=$(basename ${GTF_URL%.gz})
export FA=$(basename ${FA_URL%.gz})

### Directories fo working directory
export CUROUT=$DATA_BASE/pipeline_bwa

### Output
export GENOME=$CUROUT/genome
export OUT_BWA=$CUROUT/out_bwa
export QUT_COUNT=$CUROUT/out_count
export OUT_QC_RAW=$CUROUT/out_qc_raw
export OUT_QC_TRIMMED=$CUROUT/out_qc_trimmed
export OUT_QC_FILTER=$CUROUT/out_qc_filter
export OUT_IGV=$CUROUT/out_igv
export OUT_FIG=$CUROUT/figure

### Arguments
export THREADS=6
export ADAPTERS=$CUROUT/adapters.fasta