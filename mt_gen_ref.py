from mt_genome_regions import regions, is_in_range

with open('loc.txt') as f_in:
    lines = [line.strip().split(' ') for line in f_in]

with open('loc_type.txt', 'wt') as f_out:
    for (name, loc) in lines:
        for r in regions:
            if is_in_range(int(loc), r['range']):
                f_out.write(
                    "{},{},{},{},{}\n".format(
                        name,
                        loc,
                        r['type'],
                        r['name'],
                        r['comp']
                    )
                )
