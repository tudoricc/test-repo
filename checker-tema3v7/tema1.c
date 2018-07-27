#include <stdio.h>
#include "/Users/tvasile/Documents/tudor/checker-tema3v7/bmp_header.h"
#include <stdlib.h>
typedef struct bmp_infoheader bmp_infoheader;
void LoadBitmapFile(char *filename, struct bmp_infoheader *bitmapInfoHeader)
{
    FILE *filePtr; //our file pointer
    bmp_infoheader bitmapFileHeader; //our bitmap file header
    unsigned char *bitmapImage;  //store image data
    int imageIdx=0;  //image index counter
    unsigned char tempRGB;  //our swap variable

    //open filename in read binary mode
    filePtr = fopen(filename,"rb");
    if (filePtr == NULL)
        return NULL;
    printf("GETS HERE\n" );
    //read the bitmap file header
    fread(&bitmapFileHeader, sizeof(bmp_infoheader),1,filePtr);
    printf("What asbout here\n" );
    printf("%s\n", bitmapFileHeader.biSize);
    //printf("%s\n", bitmapFileHeader.width);
    //printf("%s\n", bitmapFileHeader.height);
}


int main() {
  //LoadBitmapFile(char *filename, bmp_infoheader *bitmapInfoHeader)
  char *file_name = "/Users/tvasile/Documents/tudor/checker-tema3v7/input/input_files/input1.txt" ;
  //myPipe = malloc(sizeof(struct PipeShm));

  struct bmp_infoheader *bitmapInfoHeader  = malloc(sizeof *bitmapInfoHeader);
  LoadBitmapFile(file_name , bitmapInfoHeader);
  return 0;
}
