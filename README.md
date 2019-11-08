### Disabling the Fortran Control-C Handler

Flask applications run through ``flask`` are set up to automatically
close upon handling a ``ctrl-C`` event. Unfortunately, Intel Fortran
sets up its own handler when ``scipy.stats`` is imported internally by
``gensim``, leading to some ugly traceback:

```shell
forrtl: error (200): program aborting due to control-C event
Image              PC                Routine            Line        Source
libifcoremd.dll    00007FFCA1A93B58  Unknown               Unknown  Unknown
KERNELBASE.dll     00007FFCD3A24023  Unknown               Unknown  Unknown
KERNEL32.DLL       00007FFCD48E7974  Unknown               Unknown  Unknown
ntdll.dll          00007FFCD771A271  Unknown               Unknown  Unknown
forrtl: error (200): program aborting due to control-C event
Image              PC                Routine            Line        Source
libifcoremd.dll    00007FFCA1A93B58  Unknown               Unknown  Unknown
KERNELBASE.dll     00007FFCD3A24023  Unknown               Unknown  Unknown
KERNEL32.DLL       00007FFCD48E7974  Unknown               Unknown  Unknown
ntdll.dll          00007FFCD771A271  Unknown               Unknown  Unknown
```

This can't be disabled early enough in the process by setting environment
variables within the application itself, but it can be resolved by setting
an environment variable beforehand. When serving this application, first
set ``FOR_DISABLE_CONSOLE_CTRL_HANDLER`` to ``1``.

In DOS:

```dos
set FOR_DISABLE_CONSOLE_CTRL_HANDLER=1
```

In Bash:

```dos
export FOR_DISABLE_CONSOLE_CTRL_HANDLER=1
```
