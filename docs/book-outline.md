# Practical Scientific Programming on the TI-84 Plus CE Python Edition

## Audience

This book is intended for science and engineering students, STEM instructors, and hobbyists interested in practical scientific programming on the TI-84 Plus CE Python calculator. It is designed for readers who already possess basic algebra skills and a willingness to experiment with Python programming, but who may not have prior software development experience.

The material is especially appropriate for chemistry, physics, and engineering applications where small scientific utilities, formatted data displays, and menu-driven programs can enhance problem solving and laboratory work. The focus is not on teaching Python syntax alone, but on building usable scientific applications within the limitations of the TI-84 Python environment.

---

## Description

Most TI-84 Python books concentrate on introductory programming exercises, graphing demonstrations, or calculator automation techniques. While useful, these approaches often overlook an important challenge of handheld scientific computing: presenting information clearly on a highly constrained display. This book introduces a lightweight display framework that simplifies pagination, menus, tables, formatted numerical output, and reusable user-interface patterns for the TI-84 Plus CE Python platform.

Using this display library as a foundation, the book develops a collection of practical scientific applications drawn from chemistry, physics, and engineering problem solving. Topics include unit conversions, significant figures, ideal gas calculations, spectroscopy utilities, kinetics calculations, and formatted scientific data presentation. The emphasis throughout is on writing readable, maintainable, and scientifically useful programs that extend the calculator beyond its built-in capabilities.


---

## Scope and Expectations

This book focuses on practical scientific programming using the TI-84 Plus CE Python environment. The emphasis is on building reusable scientific utilities, formatted displays, menu-driven applications, and computational tools for chemistry, physics, and engineering applications. While the TI-84 calculator already contains a powerful built-in graphing system, this book does not attempt to replace or duplicate the calculator’s native graphing capabilities through Python.

Although TI-84 Python provides basic graphics and drawing functionality, the MicroPython environment is intentionally limited compared to desktop scientific Python environments such as NumPy, Matplotlib, or Jupyter notebooks. Readers should view the TI-84 Python platform as a compact embedded scientific computing environment rather than a full-featured desktop programming system. The goal of this book is to teach structured scientific programming, reusable software design, and practical problem-solving techniques within the constraints of handheld calculator hardware.

The TI-84 Plus CE Python environment operates under significant practical constraints, including limited storage capacity, modest processing speed, small-screen formatting limitations, manual data-entry requirements, and the absence of modern desktop-style CSV or spreadsheet pipelines. These limitations are discussed openly throughout the book and are treated as important design considerations rather than defects. Real-world scientific and engineering systems frequently operate under constrained conditions involving limited memory, restricted interfaces, embedded hardware, low-power processors, or simplified user interaction models. Learning to design readable, reliable, and reusable scientific software within such constraints develops valuable problem-solving skills that extend beyond calculator programming alone. The TI-84 platform therefore serves not only as an educational calculator, but also as an accessible introduction to constrained scientific computing and practical software engineering tradeoffs.

The TI-84 Python environment is best viewed as a compact embedded scientific computing platform rather than a full desktop Python system.  Students learn:
- efficient formatting
- constrained-system thinking
- modular design
- compact scientific workflows
- algorithmic clarity

instead of immediately depending on:
- massive libraries
- large datasets
- heavy abstraction layers

## Physical Chemistry Perspective

Many of the scientific examples in this book are inspired by topics commonly found in physical chemistry, including thermodynamics, gases, equilibrium, kinetics, spectroscopy, molecular motion, and introductory statistical reasoning. These topics are often presented in advanced textbooks with substantial calculus and mathematical formalism. In this book, they are adapted into compact computational examples suitable for the TI-84 Plus CE Python environment.

The goal is not to replace a full physical chemistry course or textbook. Instead, the examples provide an accessible bridge between community-college-level chemistry and physics topics and the more quantitative perspective students may encounter later in upper-division university coursework. By using Python to model, calculate, format, and interpret scientific relationships, students gain early familiarity with physical chemistry ideas while also developing practical scientific programming habits.

## Laboratory Data and Scientific Workflows

A major emphasis of this book is the processing and presentation of experimental scientific data. Many examples are designed around realistic laboratory workflows commonly encountered in chemistry and physics courses, including data collected from LabQuest systems, spreadsheets, spectroscopy experiments, gas-law measurements, kinetics studies, and other laboratory activities. Rather than focusing exclusively on isolated formula calculations, the book demonstrates how the TI-84 Plus CE Python environment can be used to organize, format, analyze, and summarize experimental results in a structured and reusable manner.

The TI-84 Python platform should not be viewed as a replacement for desktop scientific environments such as Excel, MATLAB, NumPy, or Jupyter notebooks. Instead, the calculator is treated as a compact embedded scientific computing platform suitable for small datasets, portable calculations, laboratory checks, educational demonstrations, and lightweight scientific utilities. The examples in this book emphasize practical scientific problem solving within the memory, display, and input limitations of handheld calculator hardware.

Several chapters demonstrate how experimental data originating from spreadsheets or laboratory acquisition systems may be adapted into TI-84 Python programs using lists, compact tables, formatted numerical displays, and reusable analysis functions. Topics include significant figures, error analysis, regression utilities, spectroscopy calculations, kinetics data reduction, thermodynamic computations, and scientific table formatting. The overall goal is to help students and instructors build practical scientific tools that complement — rather than replace — larger desktop scientific computing systems.

## Example Scientific Applications

The examples and projects developed throughout this book emphasize practical scientific computing tasks commonly encountered in chemistry, physics, engineering, and laboratory courses. Rather than focusing exclusively on isolated mathematical exercises, the programs are designed to support realistic scientific workflows involving data analysis, numerical calculations, formatted output, and reusable computational utilities.

### Linear Regression and Calibration Utilities

Several applications demonstrate the use of linear regression techniques for scientific calibration and data analysis. Example projects include Beer-Lambert calibration curves, kinetics trend analysis, gas-law relationships, and experimental curve fitting. The TI-84 calculator already provides built-in statistical tools, but Python programs can automate repetitive workflows, improve formatting, and organize scientific output more effectively.

### Error Analysis and Experimental Uncertainty

The book includes utilities for handling common forms of experimental uncertainty and data analysis. Applications include average and standard deviation calculations, percent error and percent difference analysis, confidence intervals, significant-figure handling, and basic uncertainty propagation methods frequently encountered in laboratory courses.

### Scientific Table Formatting and Data Presentation

A major emphasis of the display library is the clear presentation of scientific information on small displays. Example utilities demonstrate aligned columns, formatted numerical output, scientific notation handling, unit labeling, paginated tables, and structured experimental summaries suitable for laboratory and educational use.

### Spectroscopy and Analytical Chemistry Utilities

Several examples focus on compact spectroscopy and analytical chemistry applications appropriate for the TI-84 Python environment. Projects include absorbance calculations, concentration determination, calibration interpolation, repeated-measurement averaging, and lightweight spectroscopy data analysis utilities.

### Chemical Kinetics and Reaction Analysis

The TI-84 platform is well suited for small computational kinetics utilities. Example projects include rate-law calculators, Arrhenius equation applications, half-life calculations, integrated rate-law analysis, slope estimation, and compact reaction-analysis tools commonly encountered in introductory physical chemistry and laboratory settings.

### Thermodynamics and Scientific Reference Utilities

Additional examples demonstrate the use of thermodynamic tables, equilibrium calculations, Gibbs free energy estimations, heat-capacity calculations, and reusable scientific reference utilities. These applications emphasize structured program organization, reusable computation modules, and clear scientific presentation within the constraints of handheld scientific computing hardware.

# Tentative Chapter List

## Part I — TI-84 Python Foundations

1. Introduction to TI-84 Python Scientific Programming  
   - Purpose and scope of the book  
   - Scientific computing on constrained hardware  
   - Python versus TI-Basic  
   - Relationship to desktop scientific Python  

2. Calculator Limitations and Design Constraints  
   - Memory and storage limitations  
   - Small-screen formatting constraints  
   - Manual data-entry realities  
   - Performance considerations  
   - Constrained scientific computing concepts  

3. Installing and Using the Display Library  
   - Installing programs on the TI-84 Plus CE Python  
   - Library organization and structure  
   - Basic display workflows  
   - Testing example programs  

4. Formatting Text for Small Displays  
   - Screen layout strategies  
   - Readable scientific output  
   - Multi-line formatting techniques  
   - Compact information presentation  

5. Pagination and Multi-Screen Output  
   - Handling large outputs  
   - Page navigation concepts  
   - Structured display flow  
   - Scientific report formatting  

6. Menus, User Input, and Program Navigation  
   - Menu-driven applications  
   - User prompts and validation  
   - Lightweight scientific interfaces  
   - Program organization strategies  

7. Scientific Computation Fundamentals  
   - Scientific notation  
   - Significant figures  
   - Units and unit conversions  
   - Numerical formatting  
   - Estimation and computational reasoning  

8. Displaying Tables and Structured Scientific Data  
   - Aligned columns and tables  
   - Experimental data presentation  
   - Scientific summaries  
   - Lightweight reporting utilities  

9. TI-84 MicroPython Libraries and Scientific Utilities  
   - Overview of TI-84 Python modules  
   - Using ti_system  
   - Using ti_draw and graphics functions  
   - Using ti_plotlib for plotting  
   - Working with lists and numerical data  
   - Integrating built-in modules with display.py  
   - Limitations compared to desktop Python  

10. Organizing, Debugging, and Testing Scientific Programs  
    - Modular scientific programs  
    - Reusable utilities  
    - Separating computation from presentation  
    - Debugging techniques on constrained hardware  
    - Testing scientific calculations  

---

## Part II — Scientific Computing Applications

11. Physics, Chemistry, and Computational Connections  
    - Using computation to connect scientific disciplines  
    - Vectors and molecular dipole moments  
    - Waves and spectroscopy  
    - Energy and thermodynamics  
    - Diffusion and molecular motion  
    - Statistics and molecular behavior  
    - Scientific modeling concepts  

12. Representative Scientific Applications  
    - Motion and energy utilities  
    - Gas-law and thermodynamics calculations  
    - Spectroscopy and Beer-Lambert examples  
    - Equilibrium and acid-base calculations  
    - Kinetics and reaction analysis  
    - Regression and error-analysis utilities  

13. Laboratory Data Processing and Scientific Presentation  
    - Experimental data tables  
    - Spreadsheet and LabQuest-derived datasets  
    - Calibration curves and regression  
    - Error analysis workflows  
    - Structured laboratory summaries  
    - Portable scientific computation workflows  

---

## Part III — Advanced Projects and Future Directions

14. Building Reusable Scientific Applications  
    - Menu-driven scientific tools  
    - Multi-module applications  
    - Reusable scientific architectures  
    - Lightweight scientific software engineering  

15. Advanced Scientific Computing Projects  
    - Integrated chemistry and physics utilities  
    - Thermodynamics applications  
    - Spectroscopy tools  
    - Data-analysis utilities  
    - Student-designed scientific applications  

16. Future Directions in Scientific Computing  
    - Transitioning to desktop Python  
    - NumPy and Jupyter concepts  
    - Raspberry Pi and MicroPython systems  
    - Embedded scientific instrumentation  
    - Physical chemistry and computational science pathways  
    - Constrained scientific computing systems  

---

# Possible Scientific Exploration Topics

The following topics are suggested throughout the book as possible extensions and student-designed scientific applications:

- Vector analysis and molecular dipole moments  
- Gravity, sedimentation, and centrifugation  
- Gas pressure and atmospheric modeling  
- Waves, optics, and spectroscopy  
- Diffusion and molecular motion  
- Chemical kinetics and exponential decay  
- Thermodynamics and energy transfer  
- Statistical methods and molecular behavior  
- Error analysis and experimental uncertainty  
- Calibration curves and regression analysis  
- Spectroscopy and analytical chemistry utilities  
- Laboratory data reduction and presentation  
- Electrostatics and intermolecular interactions  
- Numerical approximation and lightweight simulation methods  

