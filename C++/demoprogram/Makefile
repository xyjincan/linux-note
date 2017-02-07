main: main.o mytool.o myfun.o
	gcc -o main main.o mytool.o myfun.o
main.o: main.c myfun.h mytool.h
	gcc -c main.c
mytool.o: mytool.c mytool.h
	gcc -c mytool.c
myfun.o: myfun.c myfun.h
	gcc -c myfun.c
clean:
	rm -f *.o main














#gcc hello.c -c hello.o #-c 生成目标代码
#gcc hello.o -o hello   #-o 对目标进行连接
#
