# OPS
OPS is a python tool designed to scan for open Redirect vulnerabilities, used also to bypass filters.

# Screenshots
![image](https://user-images.githubusercontent.com/65312444/116719737-f0995280-a9ca-11eb-9dcc-c59fa1d0b2a8.png)
![image](https://user-images.githubusercontent.com/65312444/116719809-060e7c80-a9cb-11eb-8a63-6e387cd5b487.png)


# Setup  
```
sudo chmod +x setup.sh  
sudo ./setup.sh  
./ops.py  
```
After running setup.sh you can execute ops using the terminal

# Requirement 
```
python3  
python packages :  
  - requests  
  - os  
  - optparse  
  - colorama
```
# Usage 
Short Form    | Long Form     | Description
------------- | ------------- |-------------
-u            | --url         | Target URL
-w            | --wordlist    | Using a custom payloads wordlist
-q            | --quiet       | Enable quiet mode
-t            | --Timeout     | Time of waiting for a request
-h            | --help        | show the help message and exit

## Credits
Special thanks to :

* [f0rkr](https://github.com/f0rkr)
* [yeez123](https://github.com/yezz123)

# issues
Bug reports are welcome! Please report all bugs on the issue tracker.
Thank you.
