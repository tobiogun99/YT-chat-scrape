import urllib.request
import re

search = input().replace(" ","+") + "audio+only"
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search)
video_ID = re.findall(r"watch\?v=(\S{11})", html.read().decode())

print("https://www.youtube.com/watch?v="+video_ID[0])
