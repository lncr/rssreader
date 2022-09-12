import requests
import feedparser
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('source', type=str,
                    help='Receives RSS url and prints results in human-readable format')

args = parser.parse_args()

url = args.source
d = feedparser.parse(url)

print(d['entries'][0])