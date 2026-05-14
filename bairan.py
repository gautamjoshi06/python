import time

# Lyrics with timing (seconds)
song = [
    ("[Music Intro 🎶]", 3),
Read Full Lyrics at iLyricsHub: https://www.ilyricshub.com/bairan-banjaare/.", 2.5),
    (".", 2.5),
    ("Dil mera ho gaya bairan...", 3),
    ("Tu hi meri duniya...", 2.5),
    ("Tu hi mera chain...", 3),
    ("[Music Beat 🎶]", 2),
]

# Play the song (print with delay)
for line, delay in song:
    print(line)
    time.sleep(delay)