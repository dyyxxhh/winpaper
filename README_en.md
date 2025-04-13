## winpaper
A simple and simple wallpaper switching tool

**Instructions for use**(Translated by ai)
1. Download the compiled exe (windows) from Releases or download winpaper.py from the repository to manually compile
  
2. Create cofig.txt (encoded as utf-8) in the same directory and the format is:
   
  Write image paths (can be absolute or relative)
  
  Even line writing sets the waiting time (s) after the picture is (if it is -1, the program will be exited)
  
  For example (cofig.txt):
  
      a.png
      1
      b.png
      2
      c.png
      3
      
The meaning of this example is to set a.png as the desktop background, then wait for one second and then set b.png as the desktop background, wait for two more seconds, then set c.png as the desktop background, wait for another 3 seconds, then set a.png as the background, wait for another second and then set b point png as the desktop background, wait for another two seconds, then set c point png as the desktop background, wait for another 3 seconds, then set a point png as the background, wait for another second (loop execution)

If you are in c.png at this time, the next 3 seconds will be changed to -1 seconds. Then you will directly exit the program after the first pass of setting c.png.
