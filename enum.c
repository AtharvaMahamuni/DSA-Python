// #include <stdio.h>

// enum color
// {
//     red,
//     green,
//     blue
// };

// int main()
// {
//     // Initializing a variable that will hold the enums
//     //   enum color current_color = red;
//     printf("Value of red = %d \n", red);

//     // current_color = green;
//     // printf("Value of green = %d \n", current_color);

//     // current_color = blue;
//     // printf("Value of blue = %d \n", current_color);
//     return 0;
// }

// #include <stdio.h>

// // declaration on enum
// enum textEditor
// {
//     BOLD,
//     ITALIC,
//     UNDERLINE
// };

// int main()
// {
//     // Initializing enum variable
//     enum textEditor feature;
//     feature = BOLD;
//     printf("Selected feature is %d\n", feature);

//     feature = ITALIC;
//     printf("Selected feature is %d\n", feature);

//     return 0;
// }

// enum bike
// {
//     run,
//     stop
// };
// enum car
// {
//     run,
//     brake
// };

// int main(){return 0;}

// #define X 100L
// enum
// {
//     Y = 100L
// };

// int main()
// {
//     printf("%ld\n", X);
//     printf("%d\n", Y); /* Y has int type */
//     return 0;
// }

// #include<stdio.h>

// // declaration on enum
// enum car
// {
//     run = 1,
//     brake = 0,
//     stop = 0
// };

// int main()
// {
//     // Initializing enum variable
//     enum car perform = 0;
//     printf("Car is performing %d\n", perform);

//     perform = 5;
//     printf("Car is performing %d\n", perform);

//     return 0;
// }

#include <stdio.h>

// declaration on enum
enum textEditor
{
    BOLD = 1,
    ITALIC = 2,
    UNDERLINE = 3
};

int main()
{
    // Initializing enum variable
    enum textEditor feature = ITALIC;

    switch (feature)
    {
    case 1:
        printf("It is BOLD");
        break;

    case 2:
        printf("It is ITALIC");
        break;

    case 3:
        printf("It is UNDERLINE");
    }

    return 0;
}