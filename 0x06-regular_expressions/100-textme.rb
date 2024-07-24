#!/usr/bin/env ruby
# rrrr

puts [ARGV[0].scan(/(?<=from:)[1-9A-Za-z]*/),ARGV[0].scan(/(?<=from:)[1-9A-Za-z]*/),ARGV[0].scan(/(?<=flags:)[1-9:-]*/)].join(',')