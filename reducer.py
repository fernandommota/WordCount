#!/usr/bin/env python
############################################################################################
#  Examples code for First Hadoop with Amazon's Elastic MapReduce
#  Scott Hendrickson
#  http://drskippy.net
#   
#  Latest version at http://drskippy.net/projects/EMR-HadoopMeetup.zip
#
#  Example code for First Hadoop with AWS EMR by Scott Hendrickson is licensed under a 
#  Creative Commons Attribution-Noncommercial-Share Alike 3.0 United States License.
#  http://creativecommons.org/licenses/by-nc-sa/3.0/us/
#  Based on a work at drskippy.net.
#  Permissions beyond the scope of this license may be available at http://drskippy.net.
#
# from Michail Noll's tutial:
# http://www.michael-noll.com/wiki/Writing_An_Hadoop_MapReduce_Program_In_Python
############################################################################################
 
from itertools import groupby
from operator import itemgetter
import sys
 
def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)
 
def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["<current_word>", "<count>"] items
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            print "%s%s%d" % (current_word, separator, total_count)
        except ValueError:
            # count was not a number, so silently discard this item
            pass
 
if __name__ == "__main__":
    main()
