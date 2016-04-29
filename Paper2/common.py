import argparse
import logging
import logging.config
from configparser import ConfigParser, ExtendedInterpolation
import os
import sys
import ast
import copy
from Config.configfile import defaultconfig
from Paper2.loader_class import LoaderClass

import Config.config as config
import Config.variables as variables

logger = logging.getLogger(__name__)


'''
TODO
-------
'''

# Configure common argument


def treat_common_args(args):
    if args.version:
        sys.exit(0)
    parser = ConfigParser(interpolation=ExtendedInterpolation())
    variables.config = copy.deepcopy(defaultconfig)
    variables.loader = LoaderClass()

    # Read actual config file
    parser.read(args.config)
    variables.configfile = parser
    arg = vars(args)
    update_conf(arg, "common")

    # logconf = variables.config["common"]['logconfigfile']
    if os.path.isfile(args.logconfigfile):
        logging.config.fileConfig(args.logconfigfile, disable_existing_loggers=False)


def describe(others):
    print('PAPER2 version', config.version)


def parser(argsparser):
    argsparser.add_argument('--logconfigfile', type=str, default="logger.conf", help='set log config file')
    argsparser.add_argument('--config', type=str, default="optibag.conf", help='config file')
    argsparser.add_argument('--version', action='store_true', default=False, help='display version')
    argsparser.set_defaults(action=describe)


def update_conf(cmdline, section):
    for var in variables.config[section]:
        try:
            conf = variables.configfile[section]
        except KeyError:
            conf = None
        if var in cmdline:
            ret = cmdline[var]
        elif conf is not None and var in conf:
            ret = ast.literal_eval(conf[var])
        else:
            continue

        if not isinstance(ret, type(variables.config[section][var])):
            logger.warning("type of param %s differ : (default) %s / (input) %s. Not changing value",
                           var,  type(variables.config[section][var]), type(ret))
        else:
            variables.config[section][var] = ret
