#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2013 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 29 December 2013 13:02 PST (-0800)
"""

from __future__ import absolute_import

from phyluce.misc import fasta
from phyluce.common import FullPaths, is_dir


descr = ("Compute the length of a FASTA file or a directory of FASTAS")


def configure_parser(sub_parsers):
    sp = sub_parsers.add_parser(
        "fasta",
        description=descr,
        help=descr,
    )

    sp.add_argument(
        "--fastas",
        required=True,
        action=FullPaths,
        help="The directory containing the FASTA files to summarize."
    )
    sp.add_argument(
        "--output",
        type=str,
        help="The path to an output file to store results."
    )
    sp.add_argument(
        "--csv",
        action="store_true",
        default=False,
        help="Output to STDOUT/file in CSV format."
    )
    sp.add_argument(
        "--cores",
        type=int,
        default=1,
        help="Process alignments in parallel using --cores for alignment. "
             "This is the number of PHYSICAL CPUs."
    )
    sp.add_argument(
        "--verbosity",
        type=str,
        choices=["INFO", "WARN", "CRITICAL"],
        default="INFO",
        help="""The logging level to use."""
    )
    sp.add_argument(
        "--log-path",
        action=FullPaths,
        type=is_dir,
        default=None,
        help="""The path to a directory to hold logs."""
    )

    sp.set_defaults(func=fasta_lengths)


def fasta_lengths(args, parser):
    fasta.main(args, parser)