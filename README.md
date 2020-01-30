<h1 align="center">Welcome to loop-calc 👋</h1>
<p>
  <img alt="PyPI" src="https://img.shields.io/pypi/v/loop-calc.svg">
  <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/loop-calc.svg">
  <img alt="PyPI - Wheel" src="https://img.shields.io/pypi/wheel/loop-calc.svg">
  <a href="https://github.com/fin-ger/loop-calc/blob/master/LICENSE">
    <img alt="PyPI - License" src="https://img.shields.io/pypi/l/loop-calc.svg">
  </a>
  <a href="https://liberapay.com/fin-ger">
    <img alt="Liberapay receiving" src="https://img.shields.io/liberapay/receives/fin-ger.svg">
  </a>
  <a href="http://makeapullrequest.com">
    <img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" target="_blank" />
  </a>
  <a href="http://spacemacs.org">
    <img src="https://cdn.rawgit.com/syl20bnr/spacemacs/442d025779da2f62fc86c2082703697714db6514/assets/spacemacs-badge.svg" />
  </a>
  <a href="https://offering.maintenance.rocks#https://github.com/fin-ger/loop-calc/blob/master/README.md#author"
     alt="Looking for Maintenance">
    <img src="https://maintenance.rocks/badge.svg">
  </a>
</p>

> This program evaluates loop programs as described in the lecture `Grundlagen der theoretischen Informatik 2`.

This software is written in python using pyparsing for language parsing.

## Install

```sh
$ pip install loop-calc
```

## Usage

To display all registers and steps of a loop program, run

```sh
$ loop-calc --debug ./path/to/program.loop var1 var2
```

You can view all available options with

```sh
$ loop-calc --help
```

Have a look at the `/examples` folder for a Fibonacci implementation in loop.

## Author

**Fin Christensen**

> [:octocat: `@fin-ger`](https://github.com/fin-ger)  
> [:elephant: `@fin_ger@weirder.earth`](https://weirder.earth/@fin_ger)  
> [:bird: `@fin_ger_github`](https://twitter.com/fin_ger_github)  

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/fin-ger/loop-calc/issues).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2019 [Fin Christensen](https://github.com/fin-ger).<br />
This project is [GPL-2.0](https://github.com/fin-ger/loop-calc/blob/master/LICENSE) licensed.
