# GO basics

Why is Go complilation notably faster than most other compiled languages, even when building from scratch ?

There are main three reasons:

- all imports must be explicitly listed at the beginning of each source file, so the compiler does not have to read and process an entire file to determin its dependencies.
- the dependencies of a package form a directed acyclic graph, and because there are no cycles, packages can be compiled separately and perhaps in parallel.
- the object file for a compiled Go package records exports information not just for the package itself, but for its dependencies too. When compiling a package, the compiler must read one object file for each import but need not look beyond these files.
