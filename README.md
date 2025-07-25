# squidInk
This will be a tool to generate info to display on esp32 based e-ink displays
running on zivyobraz.eu firmware.<br><br>
As this is my summer project and I'm still a student don't expect much lol.
## The idea
Inspired by the TRMNL I got myself a localy made smart e-ink display. While
it allows for some data visualization customizations, I couldn't figure 
out how to display the things I want to. However the base firmware 
allows for fetching images from a predefined URL. That gave me and idea.<br><br>
I could make a piece of software, that fetches the data I want, sorts 
it out in a HTML document (to make sorting and combining data from
multiple sources easier), converts the HTML file to an image and uploads
it to a URL, from which the ZivyObraz server downloads the image at 
given time intervals.
## Notes
I may be overcomplicating things, I'm not sure, lol. I'm using this as 
a python learning project
