#!/usr/bin/env python3
import os
import sys
import csv
import argparse
import datetime

def ts_input_filter(ts,operator,val,ts_format):
    '''
    Check if input timestamp is lower,greater,equal,or not equal to vs date
    '''
    vs_dt = convert2dt(ts=val,ts_format=ts_format)
    if vs_dt != False:
        if operator == "lt":
            if ts > vs_dt:
                return True
            else:
                return False
        if operator == "gt":
            if ts < vs_dt:
                return True
            else:
                return False
        if operator == "ne":
            if ts != vs_dt:
                return True
            else:
                return False
        if operator == "eq":
            if ts == vs_dt:
                return True
            else:
                return False


def convert2dt(ts,ts_format):
    '''
    Return Datetime object from timestamp if ts is valid vs ts_format, else False
    '''
    try:
        return datetime.datetime.strptime(ts, ts_format)
    except ValueError:
        if args.show_errors:
            sys.stderr.write('ERROR in ts "%s" or in ts format "%s"\n'%(ts,ts_format))
        if args.exit_on_error:
            sys.exit(-1)
    return False


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Do comparisons in timestamps from STDIN')
    
    parser.add_argument('--delimiter',                  type   = str,           required = False, default = ',')
    parser.add_argument('--column',                     type   = int,           required = False, default = 0)
    parser.add_argument('--timestamp_format',           type   = str,           required = False, default = '%Y.%m.%d %H:%M:%S')
    parser.add_argument('--show_errors',                action = 'store_true',  default  = False)
    parser.add_argument('--dont_show_output',           action = 'store_true',  default  = False)
    parser.add_argument('--exit_on_error',              action = 'store_true',  default  = False)
    parser.add_argument('--eq',                         type   = str,           required = False)
    parser.add_argument('--ne',                         type   = str,           required = False)
    parser.add_argument('--lt',                         type   = str,           required = False)
    parser.add_argument('--gt',                         type   = str,           required = False)

    args  = parser.parse_args()
    for row in csv.reader(iter(sys.stdin.readline, ''), delimiter=args.delimiter):
        try:
            timestamp = convert2dt(ts=row[args.column],ts_format=args.timestamp_format)
            if timestamp != False:
                pass_test = False
                if args.eq:
                    if ts_input_filter(ts=timestamp,operator="eq",val=args.eq,ts_format=args.timestamp_format):
                        pass_test = True
                    else:
                        pass_test = False
                if args.ne:
                    if ts_input_filter(ts=timestamp,operator="ne",val=args.ne,ts_format=args.timestamp_format):
                        pass_test = True
                    else:
                        pass_test = False
                if args.gt:
                    if ts_input_filter(ts=timestamp,operator="lt",val=args.gt,ts_format=args.timestamp_format):
                        pass_test = True
                    else:
                        pass_test = False
                if args.lt:
                    if ts_input_filter(ts=timestamp,operator="gt",val=args.lt,ts_format=args.timestamp_format):
                        pass_test = True
                    else:
                        pass_test = False
                if pass_test:
                    if args.dont_show_output == False:
                        print(args.delimiter.join(row))
        except Exception as ex:
            pass
