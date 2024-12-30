import sys
import time

# Function to print lyrics with a delay between each character
def lyrics(line, delay):
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

# Lyrics lines
l1 = "I'll imagine we fell in love"
l2 = "I'll nap under moonlight skies with you"
l3 = "I think I'll picture us, you with the waves"
l4 = "The oceans colors on your face"
l5 = "I'll leave my heart with your air"
l6 = "So let me fly with you"
l7 = "Will you be forever with me?"

# Print each line of lyrics with adjusted timing
lyrics(l1, 0.1)   # Print l1 with 0.1 second delay between characters
time.sleep(0.3)   # Wait for 0.3 seconds
lyrics(l2, 0.08)  # Print l2 with 0.08 second delay between characters
time.sleep(0.3)   # Wait for 0.3 seconds
lyrics(l3, 0.07)  # Print l3 with 0.07 second delay between characters
time.sleep(1.0)   # Wait for 1.0 seconds
lyrics(l4, 0.06)  # Print l4 with 0.06 second delay between characters
time.sleep(2.0)   # Wait for 2.0 seconds
lyrics(l5, 0.1)   # Print l5 with 0.1 second delay between characters
time.sleep(1.2)   # Wait for 1.2 seconds
lyrics(l6, 0.12)  # Print l6 with 0.12 second delay between characters
time.sleep(1.2)   # Wait for 1.2 seconds
lyrics(l7, 0.15)  # Print l7 with 0.15 second delay between characters
time.sleep(5.0)   # Wait for 5.0 seconds
