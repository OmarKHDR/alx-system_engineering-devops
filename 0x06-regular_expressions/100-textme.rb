#!/usr/bin/env ruby
# rrrr

puts ARGV[0].scan(/(?<=from:)[0-9A-Za-z+]*|(?<=to:)[0-9A-Za-z+]*|(?<=flags:)[0-9:-]*/).join(',')