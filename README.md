# Telegram Picture Archiver
A simple script to download and save pictures in the specified chats as in the directory tree format below. It detects the last run date and only performs an incremental download by saving the pictures posted after the last time it was run. It also has some options you can specify according to your needs.

 * home_dir/
   * chat_1/
     * YYYY-MM-DD/
       * picture1.jpg
       * picture2.jpg
       * ...
	 * ...
   * chat_2
     * YYYY-MM-DD/
       * picture1.jpg
       * picture2.jpg
       * ...
	 * ...
   * ...
