import argparse
import logging
import sys

import Config.config as config
import Config.variables as variables


logger = logging.getLogger(__name__)


def launch(args, others):
    print('Hello world : data_analysis')


def parser(parent_parser):
    parser = parent_parser.add_parser('data_analysis', help='data analysis command help', aliases=['da'])
    parser.set_defaults(action=launch)
    return parser
