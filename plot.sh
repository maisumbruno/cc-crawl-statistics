#!/bin/bash

set -e

LATEST_CRAWL=$(basename $(ls stats/CC-MAIN-201*.gz | tail -n 1) .gz)

# filter data to speed-up reading while plotting
zgrep -h '^\["size'       stats/CC-MAIN-*.gz >stats/size.json
zgrep -h '^\["histogram"' stats/CC-MAIN-*.gz >stats/histogram.json
zgrep -h '^\["tld"'       stats/CC-MAIN-*.gz >stats/tld.json
zgrep -h '^\["mimetype"'  stats/CC-MAIN-*.gz >stats/mimetype.json

python3 plot/crawl_size.py <stats/size.json

python3 plot/overlap.py    <stats/size.json

python3 plot/histogram.py  <stats/histogram.json

(cat stats/crawler/CC-MAIN-*.json; grep -E '"CC-MAIN-201(6-[^0][0-9]|[789]-)' stats/size.json) \
	| python3 plot/crawler_metrics.py

python3 plot/tld.py CC-MAIN-2014-10 CC-MAIN-2015-11 CC-MAIN-2016-07 CC-MAIN-2017-04 $LATEST_CRAWL <stats/tld.json

python3 plot/mimetype.py <stats/mimetype.json
