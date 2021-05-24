#include <stdio.h>
#include <string.h>

int main()
{
   char T[500];
  
   fgets(T, sizeof(T), stdin);

   if(strlen(T)<=140)
      printf("TWEET\n");
   
   else
      printf("MUTE\n");


   return 0;
}
