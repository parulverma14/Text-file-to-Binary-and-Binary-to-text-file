import pickle#-------------IT IS USED TO STORE OBJECTS (LISTS , DICTONARY ETC)
#---Sample file present in our computer(if not it will be created

x=open("C:\\Users\\ss\\Desktop\\Q2SAMPLE FILE.txt","w+")
content_samplefile="A binary file is a computer file that is not a text file. The term binary file is often used as a term meaning non-text file."
x.write(content_samplefile)
x.close()
x=open("C:\\Users\\ss\\Desktop\\Q2SAMPLE FILE.txt")
y=x.read()
br_list=y.split()  #------Creating a list so as to convert in binary form using PICKLE METHOD------
#Creating another sample file to store data converted to binary---

bi_file=open("C:\\Users\\ss\\Desktop\\samplefilebinary.txt","wb+")
pickle.dump(br_list,bi_file)
bi_file.close()

#-----Depickle------

bi_file=open("C:\\Users\\ss\\Desktop\\samplefilebinary.txt","rb")
br_list=pickle.load(bi_file)

bi_file.close()
original_content=' '.join(br_list)
print(original_content)



