import argparse
import logging
import sys

import Config.config as config
import Config.variables as variables


logger = logging.getLogger(__name__)


def launch(args, others):
    print('Hello world : data_cleaning')


def parser(parent_parser):
    parser = parent_parser.add_parser('data_cleaning', help='data generation command help', aliases=['dc'])
    parser.add_argument('--data_source', default=config.__DEFAULT_DATA__, type=str, help='class to obtain data')
    parser.set_defaults(action=launch)
    return parser
