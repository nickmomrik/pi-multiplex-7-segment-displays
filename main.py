#!/usr/bin/python

# Shared 7 Segment Display Pins (A, B, C, D, E, F, G, DP)
segment_pins = [ 18, 23, 24, 25, 8, 12, 16, 20 ]

# Individual 7 Segment Displays
digit_pins = [ 22, 5, 6, 13, 19, 26 ]

# Milliseconds between number increases
count_delay = 10

# Delay between switching on/off
display_delay = 0.0005

# Starting digits across the displays
digit_values = [ 9, 9, 9, 0, 0, 0 ]

############
# END CONFIG
############

from gpiozero import LED, Button
from time import clock, sleep

# Individual LED segments on/off values to show each number
numbers = {
  0: ( 1, 1, 1, 1, 1, 1, 0 ),
  1: ( 0, 1, 1, 0, 0, 0, 0 ),
  2: ( 1, 1, 0, 1, 1, 0, 1 ),
  3: ( 1, 1, 1, 1, 0, 0, 1 ),
  4: ( 0, 1, 1, 0, 0, 1, 1 ),
  5: ( 1, 0, 1, 1, 0, 1, 1 ),
  6: ( 1, 0, 1, 1, 1, 1, 1 ),
  7: ( 1, 1, 1, 0, 0, 0 ,0 ),
  8: ( 1, 1, 1, 1, 1, 1, 1 ),
  9: ( 1, 1, 1, 1, 0, 1, 1 )
}

def update_displays() :
  global digits, numbers, digit_values, segment_leds, display_delay

  for i in range( len( digits ) ) :
    for j in range( 7 ) :
      if ( numbers[ digit_values[i] ][j] ) :
        segment_leds[j].on()
      else :
        segment_leds[j].off()

	# Decimal point
    #if ( something ) :
    #  segment_leds[7].on()
    #else :
    #  segment_leds[7].off()

    digits[i].on()
    sleep( display_delay )
    digits[i].off()

def update_digits() :
  global digits_last_updated, digit_values, count_delay

  now = clock()

  if ( ( now - digits_last_updated ) * 1000 >= count_delay ) :
	digits_last_updated = now
	if ( 9 == digit_values[5] ) :
	  digit_values[5] = 0
	  if ( 9 == digit_values[4] ) :
		digit_values[4] = 0
		if ( 9 == digit_values[3] ) :
		  digit_values[3] = 0
		  if ( 9 == digit_values[2] ) :
			digit_values[2] = 0
			if ( 9 == digit_values[1] ) :
			  digit_values[1] = 0
			  if ( 9 == digit_values[0] ) :
				 digit_values[0] = 0
			  else :
			    digit_values[0] += 1
			else :
			  digit_values[1] += 1
		  else :
			digit_values[2] += 1
		else :
		  digit_values[3] += 1
	  else :
	    digit_values[4] += 1
	else :
	  digit_values[5] += 1

# Setup gpiozero
segment_leds = []
for i in range( len( segment_pins ) ) :
  segment_leds.append( LED( segment_pins[i] ) )

digits = []
for i in range( len( digit_pins ) ) :
  digits.append( LED( digit_pins[i] ) )

digits_last_updated = clock()

while ( True ) :
	update_digits()
  	update_displays()
