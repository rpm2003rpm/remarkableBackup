# remarkableBackup
## Instuctions
Scripts for back-up of remarkable files. 

In order to run, make the remarkableBackup script executable and then type the following command in a terminal:
```
  ./remarkableBackup <name_of_the_folder_that_will_hold_the_backup
```
All the pdfs will be downloaded following the remarkable folder structure.

## Notes 
* The script was tested with the software version 2.14.3.977. I can't guarantee that will work for other versions.
* Depending on the amount of files, it may take a while to download everything, so make sure turn the auto-sleep off (settings -> Battery -> Auto sleep).
* The host remarkable must be know by the system. You can edit the file /etc/hosts and add the correct address for your remarkable.
