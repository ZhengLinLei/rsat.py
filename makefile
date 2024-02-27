CC = gcc
CFLAGS = -Wall -Wextra

all: main

main: main.o log
	$(CC) $(CFLAGS) -o main main.o

main.o: main.c
	$(CC) $(CFLAGS) -c main.c

log:
	@echo "Creating log folder"
	mkdir -p log

clean:
	rm -f main main.o
	rm -f log/*