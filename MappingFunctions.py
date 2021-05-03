#...____MAPPING FUNCTIONS_____...
import math
import random
print("\n""..........MAPPING FUNCTIONS..........""\n"
      "_____________________________________________________________")
def DIRECT():
        print("\n"".............DIRECT MAPPING............")
        a="yes"
        while(a=="yes"):
            cache_blocks=int(input("\n""ENTER NO. OF BLOCKS IN CACHE : "))
            wordsperblock_cache=int(input("ENTER WORDS PER BLOCK IN CACHE : "))
            main_blocks=int(input("\n""ENTER NO. OF BLOCKS IN MAIN : "))
            wordsperblock_main=int(input("ENTER WORDS PER BLOCK IN MAIN : "))
            print("\n""ENTER THE BLOCK NO. TO BE MAPPED FROM MAIN TO CACHE [ 0 -",main_blocks-1,"] ")
            j=int(input("\n""ENTER : "))
            remainder=j%cache_blocks
            cache_words=wordsperblock_cache*cache_blocks
            main_words=wordsperblock_main*main_blocks
            print("\n""THE TOTAL NO. OF WORDS IN CACHE :",cache_words)
            print("\n""THE TOTAL NO. OF WORDS IN MAIN :",main_words)
            print("\n""THE [ BLOCK",j,"] OF MAIN MEMORY MAPS ONTO [ BLOCK",int(remainder),"] OF CACHE ")
            print("\n"".............THE MAIN MEMORY ADDRESS............. ")
            Word=math.log(wordsperblock_main)/math.log(2)
            Block=math.log(cache_blocks)/math.log(2)
            Tag=(math.log(main_blocks)/math.log(2))-Block
            print("\n""Word : ",Word)
            print("Block [Set] : ",Block)
            print("Tag : ",Tag)
            a=input("\n""DO YOU WANT TO CONTINUE DIRECT MAPPING 'yes or no' : ")
        print("\n""..............THANKYOU..............")
def ASSOCIATIVE():
        print("\n"".............ASSOCIATIVE............")
        b="yes"
        while(b=="yes"):
            cache_blocks=int(input("\n""ENTER NO OF BLOCKS IN CACHE : "))
            wordsperblock_cache=int(input("ENTER WORDS PER BLOCK IN CACHE : "))
            main_blocks=int(input("\n""ENTER NO OF BLOCKS IN MAIN : "))
            wordsperblock_main=int(input("ENTER WORDS PER BLOCK IN MAIN : "))
            print("\n""ENTER THE BLOCK NO. TO BE MAPPED FROM MAIN TO CACHE [ 0 -",main_blocks-1,"] ")
            j=int(input("\n""ENTER : "))
            remainder=random.randint(0,cache_blocks-1)
            cache_words=wordsperblock_cache*cache_blocks
            main_words=wordsperblock_main*main_blocks
            print("\n""THE TOTAL NO OF WORDS IN CACHE :",cache_words)
            print("\n""THE TOTAL NO OF WORDS IN MAIN :",main_words)
            print("\n""THE [ BLOCK",j,"] OF MAIN MEMORY MAPS ONTO [ BLOCK",int(remainder),"] OF CACHE ")
            print("\n"".............THE MAIN MEMORY ADDRESS............. ")
            Word=math.log(wordsperblock_main)/math.log(2)
            Tag=math.log(main_blocks)/math.log(2)
            print("\n""Word : ",Word)
            print("Tag : ",Tag)
            b=input("\n""DO YOU WANT TO CONTINUE ASSOCIATIVE MAPPING 'yes or no' : ")
        print("\n""..............THANKYOU..............")
def SET_ASSOCIATIVE():
        print("\n"".............SET_ASSOCIATIVE............")
        c="yes"
        while(c=="yes"):
            cache_blocks=int(input("\n""ENTER NO OF BLOCKS IN CACHE : "))
            wordsperblock_cache=int(input("ENTER WORDS PER BLOCK IN CACHE : "))
            blocksper_set=int(input("ENTER NO OF BLOCKS PER SET OF CACHE : "))
            main_blocks=int(input("\n""ENTER NO OF BLOCKS IN MAIN : "))
            wordsperblock_main=int(input("ENTER WORDS PER BLOCK IN MAIN : "))
            print("\n""ENTER THE BLOCK NO. TO BE MAPPED FROM MAIN TO CACHE [ 0 -",main_blocks-1,"] ")
            j=int(input("\n""ENTER : "))           
            cache_words=wordsperblock_cache*cache_blocks
            main_words=wordsperblock_main*main_blocks                        
            totalsets=cache_blocks/blocksper_set
            remainder=j%totalsets
            location=random.randint(0,blocksper_set-1)
            print("\n""THE TOTAL NO OF WORDS IN CACHE :",cache_words)
            print("\n""THE NO OF SETS IN CACHE:",totalsets)
            print("\n""THE TOTAL NO OF WORDS IN MAIN :",main_words)
            print("\n""THE [ BLOCK",j,"] OF MAIN MEMORY MAPS ONTO [ BLOCK",location,"] IN [ SET",int(remainder),"] OF CACHE ")
            print("\n"".............THE MAIN MEMORY ADDRESS............. ")
            Word=math.log(wordsperblock_main)/math.log(2)
            Block=math.log(totalsets)/math.log(2)
            Tag=(math.log(main_blocks)/math.log(2))-Block
            print("\n""Word : ",Word)
            print("Block [Set] : ",Block)
            print("Tag : ",Tag)
            c=input("\n""DO YOU WANT TO CONTINUE SET_ASSOCIATIVE MAPPING 'yes or no' : ")
        print("\n""..............THANKYOU..............")
d="yes"
while(d=="yes"):
    print("\n""1.DIRECT MAPPING""\n""2.ASSOCIATIVE MAPPING""\n""3.SET-ASSOCIATIVE MAPPING")
    choice=int(input("\n""Choose your service 1 , 2 or 3 : "))
    if choice==1:
        DIRECT()
    elif choice==2:
        ASSOCIATIVE()
    elif choice==3:
        SET_ASSOCIATIVE()    
    d=input("\n""DO YOU WANT TO CHOOSE ANOTHER MAPPING TECHNIQUE 'yes or no' : ")
print("\n""..............THANKYOU..............")    
