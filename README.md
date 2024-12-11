# SKII Programming Language

Welcome to the SKII Programming Language repository! SKII is a skiing-inspired programming language designed to help users progress from beginner to advanced coding concepts using ski-related terminology. The language is divided into three levels: **GREEN**, **BLUE**, and **BLACK DIAMOND**.

## Introduction
SKII is designed to make programming more approachable for beginners while still offering powerful tools for experienced programmers. The language uses ski-related terminology and offers three levels of difficulty:
- **GREEN** for beginners
- **BLUE** for intermediate users
- **BLACK DIAMOND** for advanced users

## Grammar Overview

### GREEN Level Grammar
The **GREEN** level introduces the most basic concepts. You can declare variables, print values, and perform basic arithmetic.

#### Syntax Rules:
- **Program Structure**: A SKII program consists of blocks, where each block is either a `GreenBlock`, `BlueBlock`, or `BlackDiamondBlock`.
- **GreenBlock**: Contains commands that are specific to the GREEN level, such as variable declarations and print statements.
- **Expression Types**: Supports basic operations like addition, subtraction, multiplication, and division.

#### GreenBlock Example:
```ski
SKII GREEN {
    lodge speed as 10;
    snow(traverse speed to 20);
}
lodge: Declares a variable.
snow: Prints the result.
traverse: Adds two values.
GreenCommands:

VariableDeclaration: Declares a variable using lodge.
PrintStatement: Prints the result using snow.
Operations:
traverse: Addition
descend: Subtraction
lift: Multiplication
carve: Division
BLUE Level Grammar
The BLUE level introduces more complex concepts such as loops, conditionals, and data structures like lists and dictionaries.

Syntax Rules:
WhileLoop: A basic while loop is denoted by slope.
ForLoop: A for loop is defined using apres.
IfStatement: Conditionals are represented by trail (if) and yew (else).
Data Structures: Lists are declared with mogul and dictionaries with glacier.
BlueBlock Example:
ski
Copy code
SKII BLUE {
    slope(descend base 0 from summit 100) {
        snow(lodge speed as 10);
    }
    apres step 0 to summit 100 by 10 {
        snow(traverse speed to step);
    }
}
slope: A while loop.
apres: A for loop with a start, end, and step.
snow: Prints the result.
BlueBlockCommands:

WhileLoop: A while loop using slope.
ForLoop: A for loop using apres.
IfStatement: A conditional using trail and yew.
ListDeclaration: Declares a list using mogul.
DictionaryDeclaration: Declares a dictionary using glacier.
BLACK DIAMOND Level Grammar
The BLACK DIAMOND level is for advanced users and includes features like classes, recursion, error handling, and more complex loops and control structures.

Syntax Rules:
Class Definition: Defined using steez to declare a class.
Methods: Methods are declared with ~frontside (public) and backside~ (private).
Error Handling: Use crevasse and rescue for try-catch blocks.
Recursion: Use avalanche for recursive functions.
Advanced Control Structures: More advanced loops like pow for nested loops.
BlackDiamondBlock Example:
ski
Copy code
SKII BLACK DIAMOND {
    steez Snowboard {
        ~frontside speed() {
            snow(lodge speed as 20);
        }
    }
}
steez: Defines a class.
~frontside: Defines a public method.
BlackDiamondBlockCommands:

ClassDefinition: Defines a class with steez.
MethodDefinitions: Includes both public (~frontside) and private (backside~) methods.
ErrorHandling: Uses crevasse and rescue for exception handling.
Recursion: Uses avalanche to define recursive functions.
AdvancedControlStructure: Uses pow for advanced looping structures.
Examples
GREEN Level Example
ski
Copy code
SKII GREEN {
    lodge speed as 10;
    snow(traverse speed to 20);
}
BLUE Level Example
ski
Copy code
SKII BLUE {
    slope(descend base 0 from summit 100) {
        snow(lodge speed as 10);
    }
    apres step 0 to summit 100 by 10 {
        snow(traverse speed to step);
    }
}
BLACK DIAMOND Level Example
ski
Copy code
SKII BLACK DIAMOND {
    steez Snowboard {
        ~frontside speed() {
            snow(lodge speed as 20);
        }
    }
}

Contribute
If you'd like to contribute to the development of SKII, feel free to fork the repository, make your changes, and submit a pull request. We welcome improvements, bug fixes, and new features!
LETS HIT THE SLOPESSS
