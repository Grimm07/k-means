CC = gcc
CFLAGS = -g -Wall -Iinclude
CLINK = -lm -ldl -lsqlite3

main: main.o km.o
	$(CC) main.o km.o -o main $(CLINK)

main.o: src/main.c
	$(CC) $(CFLAGS) -c src/main.c -o main.o

km.o: src/km.c
	$(CC) $(CFLAGS) $(OPT) -c src/km.c -o km.o

clean:
	rm *.o *.exe main
