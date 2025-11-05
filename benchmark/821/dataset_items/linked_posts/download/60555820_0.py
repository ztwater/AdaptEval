#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function, unicode_literals)
import sys, os, argparse
from bs4 import BeautifulSoup

# --- insert Stan's script here ---
# if sys.version_info >= (3,): 
#...
#...
# def download_file(url, dest=None): 
#...
#...

# --- new stuff ---
def collect_all_url(page_url, extensions):
    """
    Recovers all links in page_url checking for all the desired extensions
    """
    conn = urllib2.urlopen(page_url)
    html = conn.read()
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find_all('a')

    results = []    
    for tag in links:
        link = tag.get('href', None)
        if link is not None: 
            for e in extensions:
                if e in link:
                    # Fallback for badly defined links
                    # checks for missing scheme or netloc
                    if bool(urlparse.urlparse(link).scheme) and bool(urlparse.urlparse(link).netloc):
                        results.append(link)
                    else:
                        new_url=urlparse.urljoin(page_url,link)                        
                        results.append(new_url)
    return results

if __name__ == "__main__":  # Only run if this file is called directly
    # Command line arguments
    parser = argparse.ArgumentParser(
        description='Download all files from a webpage.')
    parser.add_argument(
        '-u', '--url', 
        help='Page url to request')
    parser.add_argument(
        '-e', '--ext', 
        nargs='+',
        help='Extension(s) to find')    
    parser.add_argument(
        '-d', '--dest', 
        default=None,
        help='Destination where to save the files')
    parser.add_argument(
        '-p', '--par', 
        action='store_true', default=False, 
        help="Turns on parallel download")
    args = parser.parse_args()

    # Recover files to download
    all_links = collect_all_url(args.url, args.ext)

    # Download
    if not args.par:
        for l in all_links:
            try:
                filename = download_file(l, args.dest)
                print(l)
            except Exception as e:
                print("Error while downloading: {}".format(e))
    else:
        from multiprocessing.pool import ThreadPool
        results = ThreadPool(10).imap_unordered(
            lambda x: download_file(x, args.dest), all_links)
        for p in results:
            print(p)
