import pytz
import datetime
import os
import requests
import csv
import process_filing
import time
import traceback
import sys
from fec.models import *

from fec.utils import loader

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--repeat-interval',
            dest='repeat-interval',
            help='Number of minutes before rerunning the command. If not specified, just run once')
        parser.add_argument('--logfile',
            dest='logfile',
            help='File to log to, otherwise just log to console')
        parser.add_argument('--filing_dir',
            dest='filing_dir',
            help='where to save and read filings from')
    #default is to do just today and just committees we have in the DB

    def handle(self, *args, **options):

        if options['repeat-interval']:
            repeat_interval = int(options['repeat-interval'])
        else:
            repeat_interval = None
        if options['logfile']:
            logfile = options['logfile']
            log = open(logfile, 'a')
        else:
            logfile = None
            log = sys.stdout
        if options['filing_dir']:
            filing_dir = options['filing_dir']
        else:
            filing_dir = 'filings/'

        while True:
            loader.load_filings(log, filing_dir)

            if logfile:
                log.close()
            if repeat_interval:
                time.sleep(repeat_interval)
            else:
                break


