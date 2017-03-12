# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > pwd - show current working directory path  
pwd - creating a directory  
rmdir - deleting a directory  
touch - creating a file using `touch` command  
rm - deleting a file  
mv - renaming a file  
ls -a - listing hidden files  
cp file.txt randomdirectory/ copying a file from one directory to another  
sudo - become super user  
chown - change ownership  
chmod - change permission  
man - manual page  

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 'ls' - lists files and directories except hidden files  
'ls -a' - list all files + hidden files. (does not show permissions though, ls -la would)  
'ls -l' - lists all files except hidden files. Shows owners and permissions  
'ls - lh' - lists all files except hidden files. Shows bite size of files  
'ls -lah' - shows all files including hidden files with bite size  
'ls -t' - sorts directories by last modified date  
'ls -glp' - lists files, except directories are color coordinated.  


---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -la, ls -Gl, ls -u, ls -R, ls -GR

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs takes the output of a command and uses the result as an argument for another action. For example, if i want to delete all txt files in a particular directory I would use  find *.txt | xargs rm
 

