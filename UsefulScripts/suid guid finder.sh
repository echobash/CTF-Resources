
#We are using the find command again to find specific permission in this case 4000 (SUID) or 6000 (SGID) if using octal or u=s and g=s
#Specifying the file type with the argument -type f
#The last part is redirecting errors to /dev/null so that it doesn't pollute the terminal screen
#When you execute a binary with a SUID or SGID bit set, you will execute the program with the permissions of another user.

#Commands:
#SUID binaries 
`
find / -perm -u=s -type f 2>/dev/null
find / -perm -4000 -type f 2>/dev/null
#SGID binaries
find / -perm -g=s -type f 2>/dev/null
find / -perm -6000 -type f 2>/dev/null
`
