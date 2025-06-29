Constraint Solving
==================

An open-source course on constraint solving: modeling with decision variables and constraints, efficient modeling with viewpoints, symmetries and algorithm configuration, and how to model for specific solving technologies including CP, SMT, ILP, PB en SAT.

The course is modeling language agnostic in several ways:

  * It starts independent of solving technologies: modeling conceptually with Booleans and integers, and exposing high-level structure in the problem through the concept of global constraints from CP.
  * It uses mathematics as modeling language; this is followed by an optional slide that shows the equivalent expressions in the CPMpy library. These CPMpy slides can be disabled or replaced with your favorate modeling system with a latex command.
  * Later lectures explain for each of SMT, CP, ILP, PB en SAT the basics of how the solving technology works, and how to translate high-level models to that specific solver technology (this part has room to grow and mature).

The lectures are based on the nice <a href="https://github.com/Pierre-Flener/Pierre-Flener.github.io/tree/main/courses/M4CO/slides">slides of Pierre Flener</a>, about 50% is the same but more solver-agnostic in earlier lectures while focussing more on specific solver technologies in later lectures.

The slides are in Beamer (Latex), the practice labs in Jupyter Notebooks with CPMpy.

All course material is available under the open-source CC BY-NC-SA 4.0 license (see https://creativecommons.org/licenses/by-nc-sa/4.0). This means you can freely share and adapt it for non-commerical use, with attribution and under the same license.


Lectures
--------

The course is split up into 3 basic lectures and 5 advanced lectures. At KU Leuven, this is followed by research-based guest lectures on 'Advanced topics in CP research' (not included).

Each lecture is sized so it can be given in a 90 minute timeslot (except L07: 90 + 45 minutes and L08: 45 minutes)

**Basics:**

  * L01: Introduction ([PDF](https://github.com/tias/constraint-solving-course/blob/main/lectures/L01-Introduction.pdf), [Tex](https://github.com/tias/constraint-solving-course/blob/main/lectures/L01-Introduction.tex))
  * L02: Basic Modeling ([PDF](https://github.com/tias/constraint-solving-course/blob/main/lectures/L02-BasicModeling.pdf), [Tex](https://github.com/tias/constraint-solving-course/blob/main/lectures/L02-BasicModeling.tex))
  * L03: Solving, debugging and explanation techniques ([PDF](https://github.com/tias/constraint-solving-course/blob/main/lectures/L03-SolveDebugExplain.pdf), [Tex](https://github.com/tias/constraint-solving-course/blob/main/lectures/L03-SolveDebugExplain.tex))

**Advanced:**

  * L04: Modeling with global constraints ([PDF](https://github.com/tias/constraint-solving-course/blob/main/lectures/L04-GlobalCons.pdf), [Tex](https://github.com/tias/constraint-solving-course/blob/main/lectures/L04-GlobalCons.tex))
  * L05: Viewpoints and redundant constraints ([PDF](https://github.com/tias/constraint-solving-course/blob/main/lectures/L05-ViewpointsRedundancy.pdf), [Tex](https://github.com/tias/constraint-solving-course/blob/main/lectures/L05-ViewpointsRedundancy.tex))
  * L06: Symmetry and dominance ([PDF](https://github.com/tias/constraint-solving-course/blob/main/lectures/L06-SymmetryDominance.pdf), [Tex](https://github.com/tias/constraint-solving-course/blob/main/lectures/L06-SymmetryDominance.tex))
  * L07: Solving technologies and encodings ([PDF](https://github.com/tias/constraint-solving-course/blob/main/lectures/L07-SolvingEncoding.pdf), [Tex](https://github.com/tias/constraint-solving-course/blob/main/lectures/L07-SolvingEncoding.tex))
  * L08: CP Search Strategies and Algorithm Configuration ([PDF](https://github.com/tias/constraint-solving-course/blob/main/lectures/L08-SearchConfiguration.pdf), [Tex](https://github.com/tias/constraint-solving-course/blob/main/lectures/L08-SearchConfiguration.tex))


Practice labs
-------------

While the lectures are modeling language agnostic, the practice labs (also called exercises here) are in the Python-based CPMpy library. The exercises are in a Python Notebook, so the students can practice on their own laptop (or in Google Colab).

We provide notebooks without and with solutions. If you are a student, think about the learning opportunity you are denying yourself by looking at the solutions...

  * E0: Homework: testing the exercise setup [ipynb](https://github.com/tias/constraint-solving-course/blob/main/practice/E0_homework_setup.ipynb)
  * E1: Basic modeling [ipynb](https://github.com/tias/constraint-solving-course/blob/main/practice/E1_basic_modeling.ipynb)
  * E2: Debugging, solving, explaining and reification [ipynb](https://github.com/tias/constraint-solving-course/blob/main/practice/E2_debug_expl_reif.ipynb)
  * E3: Global constraints [ipynb](https://github.com/tias/constraint-solving-course/blob/main/practice/E3_global_constraints.ipynb)
  * E4: Advanced modeling 1: viewpoints [ipynb](https://github.com/tias/constraint-solving-course/blob/main/practice/E4_viewpoints.ipynb)
  * E5: Advanced modeling 2: symmetry [ipynb](https://github.com/tias/constraint-solving-course/blob/main/practice/E5_symmetry.ipynb)
  * E6: Solving technologies [ipynb](https://github.com/tias/constraint-solving-course/blob/main/practice/E6a_solving.ipynb) + algorithm configuration [ipynb](https://github.com/tias/constraint-solving-course/blob/main/practice/E6b_configuration.ipynb)


Roadmap
=======
The current repository is a snapshot of how the course was taught at KU Leuven in Fall 2024 (for the first time).

For Fall 2025, the major changes planned are:

  * Make a conceptual distinction between 'numeric integers' and 'categoric integers', to ease connecting to ILP/PB/SAT modelling
  * Move 'debugging and explanation techniques' to Advanced; potentially have just 2 Basic lectures
  * Extend L06 Solving technologies and encodings, to spread over 2 lectures and center around primitive/non-primitive constraint following ["Branch and Infer: A Unifying Framework for Integer and Finite Domain Constraint Programming", Bockmayr and Kasper, INFORMS]

Major slide changes will be pushed to a separate branch untill the Fall 2025 course is over. Until then, the main repository will only see slide-level changes or additions, including externally contributed additions.


Contact
=======
We would like this course, or parts of it, to be useful for lecturers teaching any flavor of constraint solving.

If you have different slides, or make slides based on ours; please send us a copy so we can learn from your approach and improve this material over time!

Also comments through Github issues, or pull requests that modify slides directly are welcome. This is an open-source course after all...


Tias Guns \<tias.guns@kuleuven.be\> <br />
Dimos Tsouros \<dimos.tsouros@kuleuven.be\>
