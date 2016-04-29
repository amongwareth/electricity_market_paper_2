import argparse
import logging
import sys

import Config.config as config
import Config.variables as variables


logger = logging.getLogger(__name__)


def launch(args, others):
    print('Hello world : data_loader')


def parser(parent_parser):
    parser = parent_parser.add_parser('data_loader', help='data loader command help', aliases=['dl'])
    parser.set_defaults(action=launch)
    return parser
