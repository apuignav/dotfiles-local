#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# @file   brew_formulae.py
# @author Albert Puig (albert.puig@cern.ch)
# @date   30.06.2015
# =============================================================================
"""Brew formulae and catch critical errors."""

from __future__ import print_function

import subprocess
import sys
import argparse


class BrewError(Exception):
    """Error executing brew."""


def brew(formulae_file, cask=False):
    """Brew the formulae in the provided file.

    If the formula is required, BrewError is raised, otherwise
    a list is printed at the end of the execution.

    """
    if not cask:
        command = 'brew install {0} || brew upgrade {0}'
    else:
        command = 'brew cask install --appdir=/Applications {0}'
    bad_formulae = []
    with open(formulae_file) as file_:
        formulae = file_.readlines()
    for formula in formulae:
        if not formula:
            continue
        try:
            cmd = command.format(formula).split()
            subprocess.check_call(cmd)
        except subprocess.CalledProcessError:
            if formula in REQUIRED_FORMULAE:
                raise BrewError("Cannot brew %s" % formula)
            else:
                bad_formulae.append(formula)
    if bad_formulae:
        print("Unable to brew:", ', '.join(bad_formulae), file=sys.stderr)


REQUIRED_FORMULAE = ['python']

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--cask', action='store_true', help='Use brew cask')
    parser.add_argument('formulae_file', action='store', type=str, help='Formula list to brew')
    args = parser.parse_args()
    brew(args.formulae_file, args.cask)

# EOF
