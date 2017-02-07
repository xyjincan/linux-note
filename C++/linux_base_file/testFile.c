#include <unistd.h>
#include <sys/file.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(void)
{
    int i = 20;
    
        char* s = "parent";
    
        int pid = fork();
        

        if(pid==0){
            s = "child";
        }

        int file = open("hello",O_RDWR | O_CREAT, 0666);
        printf("open file:%d \n",file);
        
        
        
        
        sleep(3);
        
        
        printf("begin:\n");
    
    while(1) //进入循环,加锁时间为20秒,打印倒计时
    {   
        
        flock
        int re = (file,LOCK_EX);
        //int re = flock(file,LOCK_EX | LOCK_NB);
        
        printf("%s : %d  file locked:%d \n",s,i--,re);
        //printf("file lock:%d\n", re);
        sleep(1);
        if (i == 0)
            break;
    }
    
    return 0;
	
}
 
 
