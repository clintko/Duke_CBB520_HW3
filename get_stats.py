from mt_genome_regions import regions

DNA_stats_names = {}
DNA_stats_types = {}
RNA_stats_names = {}
RNA_stats_types = {}

with open('loc_type.txt') as f_in:
    lines = [line.strip().split(',') for line in f_in]

for (seq_name, loc, loc_type, loc_name, comp) in lines:
    if seq_name[0:3] == 'ERR':
        DNA_stats_names[loc_name] = DNA_stats_names.get(loc_name, 0) + 1
        DNA_stats_types[loc_type] = DNA_stats_types.get(loc_type, 0) + 1
    elif seq_name[0:3] == 'SRR':
        RNA_stats_names[loc_name] = RNA_stats_names.get(loc_name, 0) + 1
        RNA_stats_types[loc_type] = RNA_stats_types.get(loc_type, 0) + 1


n_aligned_reads_dna = sum([v for k, v in DNA_stats_names.items()])
n_aligned_reads_rna = sum([v for k, v in RNA_stats_names.items()])
n_aligned_reads = n_aligned_reads_dna + n_aligned_reads_rna


print("\nDNA Sequence files")
print("==================")

print("\nNumber of aligned reads: {}".format(n_aligned_reads_dna))

print("\nBy region name:")
for k, v in DNA_stats_names.items():
    print("    {}: {}".format(k, v))

print("\nBy region type:")
for k, v in DNA_stats_types.items():
    print("    {}: {}".format(k, v))


print("\nRNA Sequence files")
print("==================")

print("\nNumber of aligned reads: {}".format(n_aligned_reads_rna))

print("\nBy region name:")
for k, v in RNA_stats_names.items():
    print("    {}: {}".format(k, v))

print("\nBy region type:")
for k, v in RNA_stats_types.items():
    print("    {}: {}".format(k, v))
