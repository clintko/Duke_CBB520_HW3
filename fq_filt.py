#!/usr/bin/env python
import sys
import re
import argparse


def get_config():
    parser = argparse.ArgumentParser(
        description='Read a fastq file from standard input, filter by sequence quality and write to standard output.',
        epilog='cat SRR123.fastq | fq_filter.py - m 25 - l 50 | HQ_SRR123.fastq',
    )

    parser.add_argument(
        '-m',
        type=int,
        help='minimum score to be HQ',
        default=25,
        dest='min_score',
    )

    parser.add_argument(
        '-l',
        type=int,
        help='minimum length to be HQ',
        default=50,
        dest='min_length',
    )

    parser.add_argument(
        '-smin',
        type=int,
        help='score minimum possible value in ASCII table',
        default=33,
        dest='score_min',
    )

    parser.add_argument(
        '-smax',
        type=int,
        help='score maximum possible value in ASCII table',
        default=126,
        dest='score_max',
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


def generate_hq_restr_line(min_score: int = 25, min_length: int = 50, score_range: list = [33, 126]):
    """Generate a regex that checks if a sequence is a high quality(HQ) sequence based on it's scores.
    It looks for a number of consecutive reads with high score using regular expressions.

    :param min_score: minimum score to be considered HQ, defaults to 25
    :type min_score: int, optional
    :param min_length: minimum length of consecutive HQ scores to classify the sequence
        as HQ, defaults to 50
    :type min_length: int, optional
    :param score_range: [min, max] scores possible, defaults to [33, 126]
    :type score_range: list, optional
    :return: compiled regex
    :rtype: compiled regex
    """
    range_min = score_range[0]
    range_max = score_range[1]
    c_min_score = chr(min_score + range_min)
    c_max_score = chr(range_max)
    hq_str = r"[{}-{}]{{{}}}".format(c_min_score, c_max_score, min_length)
    return hq_str


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

    regex_hq = re.compile(
        generate_hq_restr_line(
            min_score=args.min_score,
            min_length=args.min_length,
            score_range=[args.score_min, args.score_max],
        ),
        re.MULTILINE
    )

    for seq_lines in sequence_gen(f_in):
        if regex_hq.search(seq_lines[3]) is not None:
            f_out.writelines(seq_lines)


if __name__ == "__main__":
    main()
