#!/usr/bin/env ruby
# rrrr

puts ARGV[0].scan(/(?<=from:)[1-9A-Za-z]*(?<=from:)[1-9A-Za-z]*(?<=flags:)[1-9:-]*/).join(',')