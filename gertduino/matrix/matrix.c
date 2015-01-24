/*
 * Gertboard 5x5 LED matrix demo
 * Written in C for speed
 *
 */


#define BCM2708_PERI_BASE        0x20000000
#define CLOCK_BASE               (BCM2708_PERI_BASE + 0x101000) /* Clocks */
#define GPIO_BASE                (BCM2708_PERI_BASE + 0x200000) /* GPIO   */
#define PWM_BASE                 (BCM2708_PERI_BASE + 0x20C000) /* PWM    */
#define SPI0_BASE                (BCM2708_PERI_BASE + 0x204000) /* SPI0 controller */
#define UART0_BASE               (BCM2708_PERI_BASE + 0x201000) /* Uart 0 */
#define UART1_BASE               (BCM2708_PERI_BASE + 0x215000) /* Uart 1 (not used) */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <dirent.h>
#include <fcntl.h>
#include <assert.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/stat.h>

#include <unistd.h>

#define PAGE_SIZE (4*1024)
#define BLOCK_SIZE (4*1024)

#define TRUE  1
#define FALSE 0

// GPIO setup macros. Always use INP_GPIO(x) before using OUT_GPIO(x) or SET_GPIO_ALT(x,y)
#define INP_GPIO(g) *(gpio+((g)/10)) &= ~(7<<(((g)%10)*3))
#define OUT_GPIO(g) *(gpio+((g)/10)) |=  (1<<(((g)%10)*3))
#define SET_GPIO_ALT(g,a) *(gpio+(((g)/10))) |= (((a)<=3?(a)+4:(a)==4?3:2)<<(((g)%10)*3))

#define GPIO_SET0   *(gpio+7)  // Set GPIO high bits 0-31
#define GPIO_SET1   *(gpio+8)  // Set GPIO high bits 32-53

#define GPIO_CLR0   *(gpio+10) // Set GPIO low bits 0-31
#define GPIO_CLR1   *(gpio+11) // Set GPIO low bits 32-53

#define GPIO_IN0    *(gpio+13) // Read GPIO status bits 0-31
#define GPIO_IN1    *(gpio+14) // Read GPIO status bits 32-53

#define GPIO_PULL   *(gpio+37) // Pull up/pull down
#define GPIO_PULLCLK0 *(gpio+38) // Pull up/pull down clock

int mem_fd;
char *gpio_mem, *gpio_map;
volatile unsigned *gpio;


// These are specific for the matrix program


/*
   Use GPIO 7,8,9,10,11 as LED row driver
   as these are all adjacent so easy to write
   Use GPIO 22,23,24,25,17 as ROWumn sink
   we have 25 bits as pattern which fits nice in a 32-bit integer

   row 0-4 are bits 0-4,
 */

#define COL_MASK  0x00000F80 // bits 7-11
#define ROW0      (1<<22)
#define ROW1      (1<<23)
#define ROW2      (1<<24)
#define ROW3      (1<<25)
#define ROW4      (1<<27)

int on_time = 1000;
int rep = 10;

#include "pattern1.h"

/*
int pattern[] =  {
   0x10000001,
   0x10000071,
   0x10000171,
   0x10007171,
   0x1F0F7171,

   0x11F0001F,
   0x100F83E0,
   0x10007C00,
   0x100F83E0,
   0x11F0001F,

   0x1118c631,
   0x10A5294A,
   0x10421084,
   0x10A5294A,
   0x1118c631


};
*/


// Need 10 outputs
void setup_gpio()
{
   /* open /dev/mem */
   if ((mem_fd = open("/dev/mem", O_RDWR|O_SYNC) ) < 0) {
      printf("Can't open /dev/mem\n");
      printf("Did you forgot to use 'sudo .. ?'\n");
      exit (-1);
   }

   /*
    * mmap GPIO
    */
   if ((gpio_mem = malloc(BLOCK_SIZE + (PAGE_SIZE-1))) == NULL) {
      printf("allocation error \n");
      exit (-1);
   }
   if ((unsigned long)gpio_mem % PAGE_SIZE)
     gpio_mem += PAGE_SIZE - ((unsigned long)gpio_mem % PAGE_SIZE);

   gpio_map = (unsigned char *)mmap(
      (caddr_t)gpio_mem,
      BLOCK_SIZE,
      PROT_READ|PROT_WRITE,
      MAP_SHARED|MAP_FIXED,
      mem_fd,
      GPIO_BASE
   );

   if ((long)gpio_map < 0) {
      printf("gpio mmap error %d\n", (int)gpio_map);
      exit (-1);
   }
   gpio = (volatile unsigned *)gpio_map;


   INP_GPIO(7);   OUT_GPIO(7);
   INP_GPIO(8);   OUT_GPIO(8);
   INP_GPIO(9);   OUT_GPIO(9);
   INP_GPIO(10);  OUT_GPIO(10);
   INP_GPIO(11);  OUT_GPIO(11);
   INP_GPIO(22);  OUT_GPIO(22);
   INP_GPIO(23);  OUT_GPIO(23);
   INP_GPIO(24);  OUT_GPIO(24);
   INP_GPIO(25);  OUT_GPIO(25);
   INP_GPIO(27);  OUT_GPIO(27);
}

void show_pattern(int p)
{
  // clear column
  GPIO_CLR0 = COL_MASK;
  // Set first column bit pattern, have to shift bits 0-4 to position 7-11
  GPIO_SET0 = (p<<7) & COL_MASK; // 5 bits
  // Active first row by pulling bit LOW
  GPIO_CLR0 = ROW0;
  usleep(on_time); // sleep
  // de-activate
  GPIO_SET0 = ROW0;

  // clear column
  GPIO_CLR0 = COL_MASK;
  // Set second column bit pattern, have to shift bits 5-9 to position 7-11
  GPIO_SET0 = (p << 2) & COL_MASK;
  // Active second row
  GPIO_CLR0 = ROW1;
  usleep(on_time); // sleep
  // de-activate
  GPIO_SET0 = ROW1;

  // clear column
  GPIO_CLR0 = COL_MASK;
  // Set third column bit pattern, have to shift bits 10-14 to position 7-11
  GPIO_SET0 = (p>>3) & COL_MASK;
  // Active third row
  GPIO_CLR0 = ROW2;
  usleep(on_time); // sleep
  // de-activate
  GPIO_SET0 = ROW2;

  // clear column
  GPIO_CLR0 = COL_MASK;
  // Set forth column bit pattern, have to shift bits 15-19 to position 7-11
  GPIO_SET0 = (p>>8) & COL_MASK;
  // Active forth row
  GPIO_CLR0 = ROW3;
  usleep(on_time); // sleep
  // de-activate
  GPIO_SET0 = ROW3;

  // clear column
  GPIO_CLR0 = COL_MASK;
  // Set fifth column bit pattern, have to shift bits 20-24 to position 7-11
  GPIO_SET0 = (p>>13) & COL_MASK;
  // Active last row
  GPIO_CLR0 = ROW4;
  usleep(on_time); // sleep
  // de-activate
  GPIO_SET0 = ROW4;
} // show_pattern

//
// Change keyboard behaviour
//
void immediate_key_action()
{ int flags;
   // switch I/O to non-blocking
   flags = fcntl(STDIN_FILENO, F_GETFL);
   fcntl(STDIN_FILENO, F_SETFL, flags | O_NONBLOCK);

   // Switch TTY input to non buffered
   system("stty -icanon");
}

void demo_mode()
{ int old_on_time;
  int p,key;
  old_on_time = on_time;
  on_time = 1000000; // very slow
  p =0;
  do {
    show_pattern(0x01F79C61);
    p++;
    if (p==5)
      p = 0;
    key=fgetc(stdin);
    switch (key)
    {
    case '0' : on_time = 1000; break;
    case '1' : on_time = 2000; break;
    case '2' : on_time = 4000; break;
    case '3' : on_time = 8000; break;
    case '4' : on_time = 10000; break;
    case '5' : on_time = 30000; break;
    case '6' : on_time = 60000; break;
    case '7' : on_time = 100000; break;
    case '8' : on_time = 200000; break;
    case '9' : on_time = 1000000; break;
    }
  } while (key!='q');
  on_time = old_on_time;
} // demo mode 

int main()
{ int key,p,r;
  setup_gpio();
  immediate_key_action();

  p=0;
  r = rep;
  do {
    show_pattern(pattern[p]);
    r--;
    if (r<=0)
    {
      p++;
      if (p>=sizeof(pattern)/4) // sizeof in bytes conv to int
        p = 0;
      // Use top 7 bits of pattern for 'speed'
      r = rep * (1+ ((pattern[p] >> 25) & 0x7F));
    }
    key=fgetc(stdin);
    switch (key)
    {
    case 'a' : rep = 1; break;
    case 'b' : rep = 2; break;
    case 'c' : rep = 4; break;
    case 'd' : rep = 6; break;
    case 'e' : rep = 8; break;
    case 'f' : rep = 10; break;
    case 'g' : rep = 15; break;
    case 'h' : rep = 20; break;
    case 'D' : demo_mode();
    case 'R' : on_time = 1000;   rep = 5; break; // normal run mode
    }
  } while (key!='q');

  system("stty sane");
}
