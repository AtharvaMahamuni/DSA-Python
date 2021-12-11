# What is Enum in C  

### Introduction
Imagine a scenario where we are designing a text editor and want to have a features like bold, italic and underline.  
  
Now what are different ways with which you can use them in your program?  
One way is to use string literals like "BOLD", "ITALIC" or "UNDERLINE" but the problem arises when you want to use them in a switch/case statements.  
Now another way is to map them with certain numbers like 0, 1 or 2 but having string "BOLD" is more meaningful instead of having any random number 0 in the code.   



Enumerator(enum) is one of the special user-defined datatype in C programming language which is used to create and store the integer constants.  

Enum is used to make C code easy to read and maintain.  

The ***enum*** keyword is used to create the list of integer constants and it is declared as follows:

```
enum name{item1, item2, item3, ...}  
```  
