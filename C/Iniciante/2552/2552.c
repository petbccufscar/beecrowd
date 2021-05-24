#include <stdio.h>
#include <stdlib.h>

int main()
{
    int N,M;
    int a[100][100], soma;
    int i, j;


    while(scanf("%d %d", &N, &M) != EOF)
    {
        for(i=0;i<N;i++)
        {
            for(j=0;j<M;j++)
                scanf("%d", &a[i][j]);
        }
        if(M==1)
        {
            if(N==1)
            {
                if(a[0][0]==1) 
                    printf("9");
                else 
                    printf("0");
            }
            else{
                
                for(i=0;i<N;i++)
                {
                    soma=0;

                    if(i!=N-1)
                    {
                        if(a[i][0]==1) 
                            printf("9");
                        else
                        {
                            if(a[i+1][0]==1)
                                soma+=1;
                                printf("%d", soma);
                        }

                    }
                    else{
                            if(a[i][0]==1) 
                                printf("9");
                            
                            else{
                                
                                if(a[i-1][0]==1)
                                soma+=1;
                        
                        printf("%d", soma);
                             }
                    }
                }
            }
        }

        else if(M==2)
        {
            if(N==1)
            {
                soma=0;

                if(a[0][0]==1)
                    printf("9");
                else
                {
                    if(a[0][1]==1)
                        printf("1");
                    else 
                        printf("0");
                }
                if(a[0][1]==1)
                    printf("9");
                else
                {
                    if(a[0][0]==1)
                        printf("1");
                    else 
                        printf("0");
                }
                printf("\n");
            }
            else{
                for(i=0;i<N;i++)
                {
                    for(j=0;j<M;j++)
                    {
                        soma=0;

                        if(a[i][j]==1) 
                            printf("9");
                        else
                        {
                            if(j==0)
                            {
                                if(i==0)
                                {
                                    if(a[i][j+1]==1) soma+=1;
                                    if(a[i+1][j]==1) soma+=1;
                                }
                                else if(i==N-1)
                                {
                                    if(a[i][j+1]==1) soma+=a[i][j+1];
                                    if(a[i-1][j]==1) soma+=a[i-1][j];
                                }
                                else{
                                    if(a[i][j+1]==1) soma+=1;
                                    if(a[i+1][j]==1) soma+=1;
                                    if(a[i-1][j]==1) soma+=a[i-1][j];

                                }
                            }
                            else{
                                    if(i==0)
                                {
                                    if(a[i][j-1]==1) soma+=1;
                                    if(a[i+1][j]==1) soma+=1;
                                }
                            else if(i==N-1)
                                {
                                    if(a[i][j-1]==1) soma+=1;
                                    if(a[i-1][j]==1) soma+=1;
                                }
                                else{
                                    if(a[i][j-11]==1) soma+=1;
                                    if(a[i+1][j]==1) soma+=1;
                                    if(a[i-1][j]==1) soma+=1;

                                }
                            }
                            printf("%d", soma);
                        }

                    }
                    printf("\n");
                }
            }
        }
        else{
        for(i=0;i<N;i++)
        {
            for(j=0;j<M;j++)
            {
                soma=0;
                if(a[i][j]==1)
                    printf("9");
                else{
                    if(j==0)
                    {
                        if(i==0)
                        {
                            if(a[i][j+1]==1) soma+=a[i][j+1];
                            if(a[i+1][j]==1) soma+=a[i+1][j];
                        }
                        else if(i==N-1)
                        {
                            if(a[i][j+1]==1) soma+=a[i][j+1];
                            if(a[i-1][j]==1) soma+=a[i-1][j];
                        }
                        else
                        {
                            if(a[i][j+1]==1) soma+=a[i][j+1];
                            if(a[i-1][j]==1) soma+=a[i-1][j];
                            if(a[i+1][j]==1) soma+=a[i+1][j];
                        }
                    }
                    else if(j<M-1)
                    {
                        if(i==0)
                        {
                            if(a[i][j+1]==1) soma+=a[i][j+1];
                            if(a[i+1][j]==1) soma+=a[i+1][j];
                            if(a[i][j-1]==1) soma+=a[i][j-1];
                        }
                        else if(i==N-1)
                        {
                            if(a[i][j+1]==1) soma+=a[i][j+1];
                            if(a[i-1][j]==1) soma+=a[i-1][j];
                            if(a[i][j-1]==1) soma+=a[i][j-1];
                        }
                        else
                        {
                            if(a[i][j+1]==1) soma+=a[i][j+1];
                            if(a[i+1][j]==1) soma+=a[i+1][j];
                            if(a[i][j-1]==1) soma+=a[i][j-1];
                            if(a[i-1][j]==1) soma+=a[i-1][j];
                        }
                    }
                    else{
                        if(i==0)
                        {
                            if(a[i][j-1]==1) soma+=a[i][j-1];
                            if(a[i+1][j]==1) soma+=a[i+1][j];
                        }
                        else if(i==N-1)
                        {
                            if(a[i][j-1]==1) soma+=a[i][j-1];
                            if(a[i-1][j]==1) soma+=1;
                        }
                        else
                        {
                            if(a[i][j-1]==1) soma+=1;
                            if(a[i-1][j]==1) soma+=1;
                            if(a[i+1][j]==1) soma+=1;
                        }
                    }
                    printf("%d", soma);
                }
            }
            printf("\n");
        }
    }
    }

    return 0;
}
