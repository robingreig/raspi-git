// matrix_pattern.cpp : Defines the entry point for the console application.
// seperated

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <malloc.h>

#define MAX_SET 128

FILE *infile,*outfile;

int do_set(char line[1024]);
int match_set(char *line,int *value);


typedef struct {
  char name[33];
  int value;
} set_type;

set_type set[MAX_SET];
int set_count = 0;
int line_number = 0;
char *this_program;

int main(int argc, char *argv[])
{ int line_number,error;
  int row,col;
  int extra,scan_status;
  int pattern,pattern_count;
  char line[1024]; // if that does not fit the text we are in trouble anyway 

  this_program = argv[0];

  if (argc!=3)
  { fprintf(stderr,"Usage %s <inputfile> <outputfile>\n",this_program);
    fprintf(stderr,"%s is a program to convert a text file to 5x5 matrix values\n",this_program);
    fprintf(stderr,"The text file has 5x5 patterns seperated by empty lines\n");
    fprintf(stderr,"The following indicate a LED which is on: x,X,#\n");
    fprintf(stderr,"The following indicate a LED which is off: .,<space>,<comma>\n");
    fprintf(stderr,"Lines starting with / are ignored\n");
    return 1;
  }
  infile=fopen(argv[1],"r");
  if (!infile)
  {
    fprintf(stderr,"Error in %s: Could not open '%s' for reading\n",this_program,argv[1]);
    return 1;
  }
  outfile=fopen(argv[2],"w");
  if (!outfile)
  {
    fprintf(stderr,"Error in %s: Could not open '%s' for writing\n",this_program,argv[2]);
    return 1;
  }


  fprintf(outfile,"// Pattern generated from %s\n",argv[1]);
  fprintf(outfile,"int pattern[] = {\n");
  line_number = 0;
  row = 0;
  error = 0;
  pattern_count = 0;

  while (fgets(line,1024,infile) && !error)
  { line_number++;
    if (line[0]=='/')
      continue;
    if (!strncmp(line,"set",3))
    { error = do_set(line);
      continue;
    }
    
    if (row==0)
    { // start of new pattern
      pattern = 0;
    }

    if (row==5)
    { // must be empty line
      if (line[0]!=0x0a && line[0]!=0x0d)
      { error = 1;
        fprintf(stderr,"%s: error in line %d of %s, Expected empty line\n",
                  this_program,line_number,argv[1]);
      }
      row = 0;
    }
    else
    { // process one row 
      for (col=0; col<5; col++)
      { // is character a 'bit-set' one?
        if (line[col]=='x' || line[col]=='X' || line[col]=='#' )
          pattern = pattern | (0x01 << (row*5+col));
        else
        { // must be bit clear. If not error
          if (line[col]!=' ' && line[col]!='.' && line[col]!=',' )
          { error = 1;
            fprintf(stderr,"%s: error in line %d of %s, Illegal pattern character\n",
                      this_program,line_number,argv[1]);
          } // bit clear? 
        } // bit set 
      } // process 5 chars
      row++;
    } // process row 
    if (row==5)
    { // finish row 

      // Here I scan for a number or variable at the end of row 5 
      // That can be used as a 'time' for the pattern 
      if (isdigit(line[5]))
        scan_status = sscanf(line+5,"%d",&extra);
      else
        if (isalpha(line[5]))
        { error = match_set(line+5,&extra);
          scan_status = !error;
        }

      if (scan_status==1)
      { // Have 32-25=7 bits left
        if (extra<0 || extra>127)
        { error = 1;
          fprintf(stderr,"%s: error in line %d of %s, Illegal extra value\n",
                    this_program,line_number,argv[1]);
        } 
        else
          pattern = pattern | (extra << 25);
      }

      if (pattern_count==0)
        fprintf(outfile,"0x%08X",pattern);
      else
        fprintf(outfile,",\n0x%08X",pattern);
       pattern_count++;
    }
  }
  fprintf(outfile,"\n};\n // End of pattern array\n");
  fclose(infile);
  fclose(outfile);
	return error ? 1 : 0;
} // main 

//
// Read 'set' from input file
// Syntax set <name>=<dec value>
// name must start with character followed by characters,
// numbers or _ and max 32 long. 
//
// return 0 on OK, 1 on error
//
int do_set(char line[1024])
{ int l;
  int n;
  char name[33];
  int  value;

  if (set_count==128)
  { fprintf(stderr,"%s, line %d: Error : max set count reached\n",
                 this_program,line_number);
    return 1;
  }

  l = 3;
  // skip spaces
  while (line[l]==' ')
    l++;

  // get name 
  n=0;
  while (line[l] && line[l]!='=' && line[l]!=' ' && n<32)
    name[n++]=line[l++];
  name[n]=0;

  // Has this name been used already ?
  for (n=0; n<set_count; n++)
    if (!strcmp(name,set[n].name))
    { fprintf(stderr,"%s, line %d: Error : Set name already used\n",
                   this_program,line_number);
      return 1;
    }
 
  // is the name legal?
  n = 0;
  while (name[n])
  {
    if ( (n==0 && !isalpha(name[n])) ||
         (n>0  && !isalnum(name[n]) && name[n]!='_') )
    { fprintf(stderr,"%s, line %d: Error : Illegal set name character\n",
                   this_program,line_number);
      return 1;
    }
    n++;
  }

  // skip spaces
  while (line[l]==' ')
    l++;

  if (line[l]!='=')
  { fprintf(stderr,"%s, line %d: Error set expecting '='\n",
                 this_program,line_number);
    return 1;
  }
  l++; // skip '='

  // skip spaces
  while (line[l]==' ')
    l++;

  // get number
  n = sscanf(line+l,"%d",&value);
  if (n!=1)
  { fprintf(stderr,"%s, line %d: Error set value syntax error\n",
                 this_program,line_number);
    return 1;
  }

  strcpy(set[set_count].name,name);
  set[set_count].value = value;
  set_count++;

  return 0;
} // do_set 

int match_set(char *line,int *value)
{ char name[33];
  int  l,n;
  // get name 
  l=0; n=0;
  while (line[l] && line[l]!=' ' && line[l]!=0x0a && line[l]!=0x0d && n<32)
    name[n++]=line[l++];
  name[n]=0;

  // Find name in set 
  for (n=0; n<set_count; n++)
    if (!strcmp(name,set[n].name))
    { // Have a match
      *value = set[n].value;
      return 0;
    }
  fprintf(stderr,"%s, line %d: Error name '%s' found\n",
               this_program,line_number,name);
  return 1;

} // match_set
