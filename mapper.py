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
 
import sys
import re
import string
 
def read_input(file):
    for line in file:
        # split the line into words
        yield line.split()
 
def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        for word in words:
	    lword = word.lower().strip(string.punctuation)
            print '%s%s%d' % (lword, separator, 1)
 
if __name__ == "__main__":
    main()
