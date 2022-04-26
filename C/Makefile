
# For Macs that are messed up
CC = gcc-11 -g

# For Macs that arent messed up
# CC = gcc -g

CFLAGS = -Iinclude 
CLINK = -lm -fopenmp -lsqlite3

OPT =

main.exe: main.o km.o
	$(CC) main.o km.o -o main.exe $(CLINK)

main.o: main.c
	$(CC) $(CFLAGS) $(OPT) -c main.c -o main.o

km.o: src/km.c
	$(CC) $(OPT) -c src/km.c -o km.o

clean:
	rm *.o *.exe
