#!/usr/bin/env python
import sys
import re
import argparse


def get_config():
    parser = argparse.ArgumentParser(
        description='Read a fastq file from standard input, trim sequences that have specific subsequences and write to standard output.',
        epilog='cat SRR123.fastq | fq_trim.py | TRM_SRR123.fastq',
    )

    parser.add_argument(
        'subseq_file',
        type=str,
        help='name of the file that contains the subsequences to remove',
    )

    parser.add_argument(
        '-f',
        type=str,
        help='input filename',
        dest='f_in',
    )

    parser.add_argument(
        '-o',
        type=str,
        help='output filename',
        dest='f_out',
    )

    parsed, unknown = parser.parse_known_args()

    if unknown:
        print('Unknown arguments:', unknown)

    return parsed


def sequence_gen(f_in):
    """Yield sequence reads from file

    :param f_in: open fileIO
    :type f_in: fileIO
    """
    lines = [f_in.readline() for i in range(4)]
    while not any(l == '' for l in lines):
        yield lines
        lines = [f_in.readline() for i in range(4)]


def main():
    args = get_config()
    f_in = open(args.f_in, 'rt') if args.f_in is not None else sys.stdin
    f_out = open(args.f_out, 'wt') if args.f_out is not None else sys.stdout

    with open(args.subseq_file) as f:
        subsequences = [line.rstrip() for line in f]

    for seq_lines in sequence_gen(f_in):
        if not any(subseq in seq_lines[1] for subseq in subsequences):
            f_out.writelines(seq_lines)


if __name__ == "__main__":
    main()
