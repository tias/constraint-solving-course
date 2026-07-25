Constraint Solving
==================

An open-source course on constraint solving: modeling with decision variables and constraints, efficient modeling with viewpoints, symmetries and algorithm configuration, and how to model for specific solving technologies including CP, SMT, ILP, PB and SAT.

The course is modeling language agnostic in several ways:

  * It starts independent of solving technologies: modeling conceptually with Booleans and integers, and exposing high-level structure in the problem through the concept of global constraints from CP.
  * It uses mathematics as modeling language; this is followed by an optional slide that shows the equivalent expressions in the CPMpy library. These CPMpy slides can be disabled or replaced with your favorite modeling system with a latex command.
  * Later lectures explain for each of SMT, CP, ILP, PB and SAT the basics of how the solving technology works, and how to translate high-level models to that specific solver technology (this part has room to grow and mature).

The lectures are based on the nice <a href="https://github.com/Pierre-Flener/Pierre-Flener.github.io/tree/main/courses/M4CO/slides">slides of Pierre Flener</a>, about 50% is the same but more solver-agnostic in earlier lectures while focusing more on specific solver technologies in later lectures.

The slides are in Beamer (Latex), the practice labs in Jupyter Notebooks with CPMpy.

All course material is available under the open-source CC BY-NC-SA 4.0 license (see https://creativecommons.org/licenses/by-nc-sa/4.0). This means you can freely share and adapt it for non-commercial use, with attribution and under the same license.


Lectures
--------

The course is split up into 5 modeling lectures and 3 solving lectures. At KU Leuven, this is followed by research-based guest lectures on 'Advanced topics in CP research' (not included).

Each lecture is sized so it can be given in a 2 hour timeslot (except L07: 3 hours and L08: 1 hour)

**Modeling:**

  * L01: Introduction ([PDF](https://github.com/tias/constraint-solving-course/blob/main/lectures/L01-Introduction.pdf), [Tex](https://github.com/tias/constraint-solving-course/blob/main/lectures/L01-Introduction.tex))
  * L02: Basic Modeling ([PDF](https://github.com/tias/constraint-solving-course/blob/main/lectures/L02-BasicModeling.pdf), [Tex](https://github.com/tias/constraint-solving-course/blob/main/lectures/L02-BasicModeling.tex))
  * L03: Global Constraints ([PDF](https://github.com/tias/constraint-solving-course/blob/main/lectures/L03-GlobalCons.pdf), [Tex](https://github.com/tias/constraint-solving-course/blob/main/lectures/L03-GlobalCons.tex))
  * L04: Viewpoints and Redundancy ([PDF](https://github.com/tias/constraint-solving-course/blob/main/lectures/L04-ViewpointsRedundancy.pdf), [Tex](https://github.com/tias/constraint-solving-course/blob/main/lectures/L04-ViewpointsRedundancy.tex))
  * L05: Symmetry and Dominance ([PDF](https://github.com/tias/constraint-solving-course/blob/main/lectures/L05-SymmetryDominance.pdf), [Tex](https://github.com/tias/constraint-solving-course/blob/main/lectures/L05-SymmetryDominance.tex))

**Solving:**

  * L06: Solving Technologies and Encodings, Part 1 ([PDF](https://github.com/tias/constraint-solving-course/blob/main/lectures/L06-SolvingEncoding1.pdf), [Tex](https://github.com/tias/constraint-solving-course/blob/main/lectures/L06-SolvingEncoding1.tex))
  * L07: Solving Technologies and Encodings, Part 2 ([PDF](https://github.com/tias/constraint-solving-course/blob/main/lectures/L07-SolvingEncoding2.pdf), [Tex](https://github.com/tias/constraint-solving-course/blob/main/lectures/L07-SolvingEncoding2.tex))
  * L08: Portfolio Solvers, Algorithm Configuration and Parallelism ([PDF](https://github.com/tias/constraint-solving-course/blob/main/lectures/L08-SearchConfiguration.pdf), [Tex](https://github.com/tias/constraint-solving-course/blob/main/lectures/L08-SearchConfiguration.tex))


Practice labs
-------------

While the lectures are modeling language agnostic, the practice labs (also called exercises here) are in the Python-based CPMpy library. The exercises are in a Python Notebook, so the students can practice on their own laptop (or in Google Colab).

We provide notebooks without and with solutions. If you are a student, think about the learning opportunity you are denying yourself by looking at the solutions...

  * E0: Homework: testing the exercise setup [ipynb](https://github.com/tias/constraint-solving-course/blob/main/practice/E0_homework_setup.ipynb)
  * E1: Basic modeling [ipynb](https://github.com/tias/constraint-solving-course/blob/main/practice/E1_basic_modeling.ipynb)
  * E2: Reification and global constraints [ipynb](https://github.com/tias/constraint-solving-course/blob/main/practice/E2_reify_and_global_constraints.ipynb)
  * E3: Viewpoints [ipynb](https://github.com/tias/constraint-solving-course/blob/main/practice/E3_viewpoints.ipynb)
  * E4: Symmetry and dominance [ipynb](https://github.com/tias/constraint-solving-course/blob/main/practice/E4_symmetry_and_dominance.ipynb)
  * E5: Solving technologies and encodings [ipynb](https://github.com/tias/constraint-solving-course/blob/main/practice/E5_solving.ipynb)
  * E6: Low-level encodings and algorithm configuration [ipynb](https://github.com/tias/constraint-solving-course/blob/main/practice/E6_lowlevel_and_configuration.ipynb)


Roadmap
=======
The current repository is a snapshot of how the course was taught at KU Leuven in Fall 2025.

Contact
=======
We would like this course, or parts of it, to be useful for lecturers teaching any flavor of constraint solving.

If you have different slides, or make slides based on ours; please send us a copy so we can learn from your approach and improve this material over time!

Also comments through Github issues, or pull requests that modify slides directly are welcome. This is an open-source course after all...


Tias Guns \<tias.guns@kuleuven.be\>


Acknowledgments
===============
Past co-lecturers at KU Leuven:

  * Dimos Tsouros
  * Henk Bierlee

Reuse of slides from:

  * Pierre Flener (in L01..L07)
  * Guido Tack (in L01)
  * Chris Beck (in L01)
  * Barbara Smith (in L04)
  * Helene Verhaeghe (in L06)
  * Ambros Gleixner (in L07)
  * Jakob Nordstrom (in L07)
  * Lars Kotthoff (in L08)
  * Toby Davies (in L08)