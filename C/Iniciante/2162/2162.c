#include <stdio.h>

int main()
{
  int n, i, padrao = 1;
  scanf("%d", &n);

  int alturas[n];

  for (i = 0; i < n; i++)
  {
    scanf("%d", &alturas[i]);
  }

  if (alturas[0] < alturas[1])
  {
    for (i = 0; i < n; i += 2)
    {
      if (i == n - 1)
      {
        if (alturas[i] >= alturas[i - 1])
        {
          padrao = 0;
          break;
        }
      }
      if (i < n - 1)
      {
        if (alturas[i] >= alturas[i + 1])
        {
          padrao = 0;
          break;
        }
      }
    }
  }
  else if (alturas[0] == alturas[1])
    padrao = 0;
  else
  {
    for (i = 0; i < n; i += 2)
    {
      if (i == n - 1)
      {
        if (alturas[i] <= alturas[i - 1])
        {
          padrao = 0;
          break;
        }
      }
      if (i < n - 1)
      {
        if (alturas[i] <= alturas[i + 1])
        {
          padrao = 0;
          break;
        }
      }
    }
  }

  printf("%d\n", padrao);

  return 0;
}