# pathcurse
Path segment finder

## What is this program?
Basically this program lists you the links related with 'a href=""' of the target website.
It may be reduce the time for gathering information from the website.

### Required libraries
```
bs4, for parsing and finding path segments
requests, for getting the data with HTTP request
argparse, for better usage
```
### Usage Example
```
python3 pathcurse.py --url https://google.com
```
#### *You have to use https:// or http://, in case of not using it program crashes (may be fixed)*
