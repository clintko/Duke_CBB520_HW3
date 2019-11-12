regions = [
    {'name': 'tRNA-Phe', 'range': (1, 69), 'type': 'tRNA', 'comp': False},
    {'name': 's-rRNA', 'range': (70, 1023), 'type': 'rRNA', 'comp': False},
    {'name': 'tRNA-Val', 'range': (1024, 1090), 'type': 'tRNA', 'comp': False},
    {'name': 'l-rRNA', 'range': (1091, 2670), 'type': 'rRNA', 'comp': False},
    {'name': 'tRNA-Leu', 'range': (2671, 2744), 'type': 'tRNA', 'comp': False},
    {'name': 'ND1', 'range': (2747, 3702), 'type': 'gene_CDS', 'comp': False},
    {'name': 'tRNA-Ile', 'range': (3703, 3771), 'type': 'tRNA', 'comp': False},
    {'name': 'tRNA-Gln', 'range': (3768, 3842), 'type': 'tRNA', 'comp': True},
    {'name': 'tRNA-Met', 'range': (3844, 3913), 'type': 'tRNA', 'comp': False},
    {'name': 'ND2', 'range': (3914, 4955), 'type': 'gene_CDS', 'comp': False},
    {'name': 'tRNA-Trp', 'range': (4956, 5023), 'type': 'tRNA', 'comp': False},
    {'name': 'tRNA-Ala', 'range': (5037, 5105), 'type': 'tRNA', 'comp': True},
    {'name': 'tRNA-Asn', 'range': (5107, 5178), 'type': 'tRNA', 'comp': True},
    {'name': 'origin L-strand repl',
        'range': (5179, 5215), 'type': 'rep_origin', 'comp': False},
    {'name': 'tRNA-Cys', 'range': (5212, 5279), 'type': 'tRNA', 'comp': True},
    {'name': 'tRNA-Tyr', 'range': (5280, 5347), 'type': 'tRNA', 'comp': True},
    {'name': 'COX1', 'range': (5349, 6893), 'type': 'gene_CDS', 'comp': False},
    {'name': 'tRNA-Ser', 'range': (6891, 6961), 'type': 'tRNA', 'comp': True},
    {'name': 'tRNA-Asp', 'range': (6966, 7033), 'type': 'tRNA', 'comp': False},
    {'name': 'COX2', 'range': (7034, 7717), 'type': 'gene_CDS', 'comp': False},
    {'name': 'tRNA-Lys', 'range': (7735, 7801), 'type': 'tRNA', 'comp': False},
    {'name': 'ATP8', 'range': (7803, 8006), 'type': 'gene_CDS', 'comp': False},
    {'name': 'ATP6', 'range': (7964, 8644), 'type': 'gene_CDS', 'comp': False},
    {'name': 'COX3', 'range': (8644, 9427), 'type': 'gene_CDS', 'comp': False},
    {'name': 'tRNA-Gly', 'range': (9428, 9495), 'type': 'tRNA', 'comp': False},
    {'name': 'ND3', 'range': (9496, 9841), 'type': 'gene_CDS', 'comp': False},
    {'name': 'tRNA-Arg', 'range': (9842, 9910), 'type': 'tRNA', 'comp': False},
    {'name': 'ND4L', 'range': (9911, 10207),
     'type': 'gene_CDS', 'comp': False},
    {'name': 'ND4', 'range': (10201, 11578),
     'type': 'gene_CDS', 'comp': False},
    {'name': 'tRNA-His', 'range': (11579, 11647),
     'type': 'tRNA', 'comp': False},
    {'name': 'tRNA-Ser', 'range': (11648, 11707),
     'type': 'tRNA', 'comp': False},
    {'name': 'tRNA-Leu', 'range': (11708, 11777),
     'type': 'tRNA', 'comp': False},
    {'name': 'ND5', 'range': (11778, 13598),
     'type': 'gene_CDS', 'comp': False},
    {'name': 'ND6', 'range': (13582, 14109), 'type': 'gene_CDS', 'comp': True},
    {'name': 'tRNA-Glu', 'range': (14110, 14178),
     'type': 'tRNA', 'comp': True},
    {'name': 'CYTB', 'range': (14183, 15322),
     'type': 'gene_CDS', 'comp': False},
    {'name': 'tRNA-Thr', 'range': (15323, 15392),
     'type': 'tRNA', 'comp': False},
    {'name': 'tRNA-Pro', 'range': (15392, 15457),
     'type': 'tRNA', 'comp': True},
    {'name': 'control region', 'range': (
        15458, 16727), 'type': 'D-loop', 'comp': False},
]


def is_in_range(val, range):
    return val > range[0] and val < range[1]


def get_region(loc):
    for r in regions:
        if is_in_range(loc, r['range']):
            return r
