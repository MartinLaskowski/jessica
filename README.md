# Project: Jessica

An experimental framework for optimizing equity SMAs (Separately Managed Accounts, aka standalone portfolios) for retail distribution.

### Goal: optimize representative clusters of SMAs subject to account minimums in the shortest time possible.
 
#### TO-DO:

- [ ] **Build optimization model portfolio**
  - [ ] modularize model components (variables, objectives and constraints)
  - [ ] build model-to-use-case matrix
  - [ ] build JIT model-assembler

- [ ] **Build test harness**
  - [ ] visualize execution waterfall

- [ ] **Test and tune Performance-Train components (and replace where needed)**
  - [ ] CPU
  - [ ] RAM
  - [ ] OS
  - [ ] env
  - [ ] UI
  - [ ] scripts
  - [ ] data
  - [ ] model
  - [ ] solvers


## Application Components

### **Performance Train**

|                       | Initial                                          | Next up                         |
| --------------------- | ------------------------------------------------ | ------------------------------- |
| CPU                   | M2                                               | Intel Xeon E-2488               |
| RAM                   | 8GB                                              | 128GB DDR 4 ECC                 |
| OS                    | macOS Sonoma 14.5                                | Linux Ubuntu Server             |
| Env                   | Docker Compose v2.27.0-desktop.2                 | --                              |
| Script (glue) langs   | Python                                           | [Dask](https://www.dask.org/)   |
| Database              | PostgreSQL + TimescaleDB                         | kdb+                            |
| Dataframes            | Pandas                                           | [Polars](https://pola.rs/)      |
| Model langs           | AMPL                                             | Pyomo, gurobipy                 |
| Solvers               | Gurobi (optionally + HiGHS for small problems)   | --                              |


### **Non-Performance Train**

|                        |                                                         |
| ---------------------- | ------------------------------------------------------- |
| UI                     | Grafana                                                 |
| DB Admin               | [CloudBeaver](https://github.com/dbeaver/cloudbeaver)   |


### Data

#### Data Sources
- Yahoo Finance API

#### Instruments Imported
- S&P 500
- Russell 2000
