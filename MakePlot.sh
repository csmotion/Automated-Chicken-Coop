#!/bin/sh
#GLUPLOT script to create graph in PNG format
/usr/bin/gnuplot << EOF
set datafile separator ","
set terminal png size 800,500
set terminal png
set output "/var/www/ChickenCoopTemps.png"

set title "Temps, Last 24 Hours"
set xlabel "Time"
set xtics rotate
set ylabel "Temp (C)"
set xdata time
set timefmt "%Y-%m-%d-%H-%M-%S"
set format x "%H:%M"
#set xrange [* : *]
#set yrange [* : *]
set linetype 1 lw 2 lc rgb "blue"
set linetype 2 lw 2 lc rgb "red"
set grid x y

plot "< tail -1440 /usr/ChickenCoop/Log.txt" using 1:2 with lines title "Temp 1", "< tail -1440 /usr/ChickenCoop/Log.txt" using 1:3 with lines title "Temp 2"
