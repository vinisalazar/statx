#!/usr/bin/env python
'''
  basic t test
'''

import argparse
import logging
import sys

import scipy.stats

def anova(values1, values2, values3):
  logging.info('starting: %i values vs %i values vs %i values', len(values1), len(values2), len(values3))
  logging.debug('group 1: %s; group 2: %s; group 3: %s', ' '.join(values1), ' '.join(values2), ' '.join(values3))

  if len(values1) == 0 or len(values2) == 0 or len(values3) == 0:
    logging.fatal('at least one empty group')
    return

  num1 = [float(x) for x in values1]
  num2 = [float(x) for x in values2]
  num3 = [float(x) for x in values3]

  sys.stdout.write('statistic\tp-value\n')

  if all([num1[0] == x for x in num1 + num2 + num3]):
    logging.info('all values equal')
    sys.stdout.write('0\t1\n')
    return

  result = scipy.stats.f_oneway(num1, num2, num3)
  logging.debug(result)

  sys.stdout.write('{}\t{}\n'.format(result.statistic, result.pvalue))

  logging.info('done')

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Perform an ANOVA test')
  parser.add_argument('--values1', required=True, nargs='+', help='group 1')
  parser.add_argument('--values2', required=True, nargs='+', help='group 2')
  parser.add_argument('--values3', required=False, nargs='+', help='group 3')
  parser.add_argument('--verbose', action='store_true', help='more logging')
  args = parser.parse_args()
  if args.verbose:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
  else:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

  anova(args.values1, args.values2, args.values3)

