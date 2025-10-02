#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
  const char *name;
  int x, y;
} City;

City cities[] = {
    {"Clean", 1336, 536}, {"Prosy", 977, 860},  {"Rabbi", 6, 758},    {"Addle", 222, 261},
    {"Smell", 1494, 836}, {"Quite", 905, 345},  {"Lives", 72, 714},   {"Cross", 23, 680},
    {"Synth", 1529, 785}, {"Tweak", 1046, 426}, {"Medic", 1485, 514}, {"Glade", 660, 476},
    {"Breve", 1586, 448}, {"Hotel", 1269, 576}, {"Toing", 398, 561},  {"Scorn", 617, 373},
    {"Tweet", 1253, 403}, {"Zilch", 1289, 29},  {"React", 296, 659},  {"Fiche", 787, 278},
};

void City_print(City *c)
{
  printf("%s(%d,%d)", c->name, c->x, c->y);
}
void City_printAll(City *p, int count)
{
  for (int i = 0; i < count; i++, p++) {
    City_print(p);
    putchar(' ');
  }
  putchar('\n');
}

City *city_ptrs[sizeof(cities) / sizeof(cities[0])];
void CityPtr_printAll(City **pp, int count) 
{
  for (int i = 0; i < count; i++, pp++) {
    City_print(*pp);
    putchar(' ');
  }
  putchar('\n');
}

int City_comparator_name_asc(const void *a, const void *b)
{
  City *p1 = (City *)a;
  City *p2 = (City *)b;

  return strcmp(p1->name, p2->name);

  // int ret = strcmp(p1->name, p2->name);
  // if (ret < 0) {
  //   return -1;
  // } else if (ret > 0) {
  //   return 1;
  // } else {
  //   return 0;
  // }
}

int City_comparator_y_asc(const void *a, const void *b)
{
  City *p1 = (City *)a;
  City *p2 = (City *)b;

  return p1->y - p2->y;
  // if (p1->y < p2->y) {
  //   return -1;
  // } else if (p1->y > p2->y) {
  //   return 1;
  // } else {
  //   return 0;
  // }
}

int CityPtr_comparator_x_asc(const void *a, const void *b)
{
  City *p1 = *(City **)a;
  City *p2 = *(City **)b;

  return p1->x - p2->x;
}

int main(void) 
{
  const int width = sizeof(cities[0]);
  const int count = sizeof(cities) / sizeof(cities[0]);
  City_printAll(cities, count);

  for (int i = 0; i < count; i++) {
    city_ptrs[i] = &cities[i];
  }
  qsort(city_ptrs, count, sizeof(City *), CityPtr_comparator_x_asc);
  CityPtr_printAll(city_ptrs, count);

  // sort here by name
  qsort(cities, count, width, City_comparator_name_asc);
  City_printAll(cities, sizeof(cities) / sizeof(cities[0]));

  // sort here by y coordinate
  qsort(cities, count, width, City_comparator_y_asc);
  City_printAll(cities, sizeof(cities) / sizeof(cities[0]));

  return 0;
}