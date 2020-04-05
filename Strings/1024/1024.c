#include <ctype.h>
#include <stdio.h>
#include <string.h>
/* Obs.: O seguinte código funciona, mas ele está com um problema de
 * apresentação de solução imprimindo uma linha a mais do que deveria se
 * quiserem corrigir
*/

void
encrypt(char *buf, int len)
{
    int mid, i;
    char aux;

    mid = len/2;
    /* primeira passada */
    i = -1;
    while (buf[++i])
        if (isalpha(buf[i]))
            buf[i] += 3;
    /* segunda passada */
    for (i = 0; i <= mid;i++) {
        aux = buf[i];
        buf[i] = buf[len - i];
        buf[len - i] = aux;
    }
    /* terceira passada */
    for (i = mid+1; i <= len; i++)
        buf[i] -= 1;
}

void
run(char *buf, int n)
{
    int i, len;
    for (i = 0; i < n; i++) {
        fgets(buf, 1024, stdin);
        len = strlen(buf) - 1;
        buf[len+1] = '\0';
        encrypt(buf, len);
        printf("%s", buf);
    }
}

int
main(int argc, char *argv[])
{
    int n;
    char buf[1024];

    scanf("%d\n\n", &n);
    run(buf, n);

    return 0;
}
