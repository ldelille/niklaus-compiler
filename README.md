# A compiler for the language Niklaus

Niklaus is a simplified **imperative langage** such as Pascal or C. 

Here is how you would write a program to compute the gcd of two numbers using Euclide algorithm: 

```
program PGCD;
var a, b;
{
    read a;
    read b;
    while(a <> b) {
        if(a > b) {
            a := a - b;
        } else {
            b := b - a;
        }
    }
    write a;
}
```

I wrote a compiler for this langage, the compiler generates assembly langage. The language is then assembled for a mini ARM processor. 

## The grammar

An ANTLR [grammar](https://github.com/ldelille/nilkaus-compiler/tree/master/grammar)  was written for the langage. 

After installing [antlr v4](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md) and  [antlr4-python3-runtime ](https://pypi.org/project/antlr4-python3-runtime/)

The grammar can be compiled: 

```bash
antlr4 -Dlanguage=Java Niklaus.g
antlr4 -visitor  -Dlanguage=Python3 Niklaus.g
javac Niklaus*.java
```

This commands will generate all necessary Python file to parse and visit the tree of a Niklaus program. 

## The compiler

The `NiklausCompiler.py` contains all the logic to generate assembly code for the mini ARM processor. 

To test it for the GDD program: 

```bash
python3 NiklausCompiler.py ../example/pgcd.niklaus
```

That will generate the `PGCD.arm` assembly code that can be assembled to be loaded on a mini ARM processor. The `lib.arm`
fiel contains pre-built assembly code for readInt, printInt, readChr, printStr functions. 

