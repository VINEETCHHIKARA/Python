def changeme( mylist ):
   "This changes a passed list into this function"
   mylist=4;
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = 30;
changeme( mylist );
print ("Values outside the function: ", mylist)
