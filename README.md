# Telegram Image Archiver
A simple script to download and archive images in the specified chats as in the directory tree format below. It detects the last run date and only performs an incremental download by saving the images posted after the last time it was run. It also has some options you can specify according to your needs.

 * home_dir/
   * chat_1/
     * YYYY-MM-DD/
       * image1.jpg
       * image2.jpg
       * ...
	 * ...
   * chat_2
     * YYYY-MM-DD/
       * image1.jpg
       * image2.jpg
       * ...
	 * ...
   * ...
   
## Requirement:
In the script, [Telethon](https://docs.telethon.dev/en/latest/index.html) library is used To interact with Telegram’s API. To install Telethon:
```
pip3 install telethon 
```

## How to run:
First, make sure you specified the API ID, API key and options accordingly. After that, to run Telegram Image Archiver:
```
python3 TIA.py 
```
