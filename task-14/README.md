# Bandit

This was a fun and interesting task which gave a good revision and learning about the linux terminal commands. 

1. **Level 0**: With the username: bandit0 and password: bandit0 I logged in to level 1 by running the command- ssh bandit0@bandit.labs.overthewire.org -p 2220

2. **Level 0-1**: Using the cat command I opened the readme file (cat readme) to get the password

3. **Level 1-2**: Using the cat ./ command I opened the dashed file (cat ./-) to get the password

4. **Level 2-3**: Using the cat command I opened the file 'spaces in this filename' by using inverted commas (cat 'spaces in this filename') to get the password

5. **Level 3-4**: Using the cd command I was directed to the inhere directory (+cd inhere). Using the ls -alps I found the hidden file (.hidden) and then I used the cat command to open the file (cat '.hidden')

6. **Level 4-5**: Using the cd command I was directed to the inhere directory (cd inhere). Using the find -type f | xargs file I found that -file07 had ASCII text and opened the file using cat command (cat ./-file07)

7. **Level 5-6**: Using the cd command I was directed to the inhere directory (cd inhere). Using the find command I used to find the location of the line (find -type f -size 1033c -readable ! -executable)I found that the folder maybehere07 had a .file2 which satisfies all the given conditions. 

8. **Level 6-7**: Using the find command I found the location of the files (find -user bandit7 -group bandit6 -size 33c) I found a list of files, and one of them had the password to the next level

9. **Level 7-8**: Using the grep command I found the password (grep "millionth" data.txt).

10. **Level 8-9**: Using the sort command (sort data.txt | uniq -u) I was able to find the password. 

11. **Level 9-10**: Using the strings and grep command (strings data.txt | grep "=") I was able to find the password
. 
11. **Level 10-11**: Using the base64 -d command (base64 -d data.txt) I was able to find the password. 
