# Dependencies




Python 2.x must be installed on your system. For instructions on installing python please visit https://www.python.org

### In Ubuntu(or other Debian base systems)
```
sudo apt-get install ffmpeg python-numpy python-matplotlib gnuplot gnuplot-x11 python-pip

sudo pip install pydub
```
In order to run the youtube mp3 extraction script file the following additional dependency is required
```
sudo apt-get install youtube-dl
```

### In Manjaro(or other Arch base systems)
```
sudo pacman -S ffmpeg python-numpy python-matplotlib gnuplot python-pip

sudo pip install pydub
```
In order to run the youtube mp3 extraction script file the following additional dependency is required
```
sudo pacman -S youtube-dl
```



# Execution




{input_file_path}	:	Path to the input mp3 audio file

{output_file_path}	:	Path to the output plot file (default: 'spectrum.plot')


### From terminal:
```
python v1.py {input_file_path} {output_file_path}

gnuplot -p -e "plot '{output_file_path}' w filledcurves x1"
```
