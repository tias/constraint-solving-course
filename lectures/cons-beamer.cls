\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cons-beamer}[2025/06/22 Constraint Solving Beamer class]
\LoadClass[dvipsnames,aspectratio=169]{beamer}

% Whether to show additional flashcard slides in a specific syntax
\def\showcpmpy{}  % show CPMpy
%\def\showminizinc{}  % show MiniZinc -- UNTESTED/OUTDATED!!!

% Packages
%%%%%%%%%%
\RequirePackage{etex}  % see http://tex.stackexchange.com/questions/38607/no-room-for-a-new-dimen
\RequirePackage[normalem]{ulem}  % here, because it overrides \emph

\usepackage[boxed]{algorithm}   % drop [boxed] is no box around algorithm wanted
\usepackage[noend]{algorithmic} % drop [noend] if endif, endwhile, etc wanted
\renewcommand{\algorithmiccomment}[1]{\hfill // #1}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{array}
\usepackage[british]{babel}
\usepackage{booktabs}
\usepackage{comment} % Add the comment package
\usepackage{colortbl}  % provides \cellcolor
\usepackage[nocenter]{cwpuzzle}  % provides Sudoku -- from 'texlive-games'
\usepackage{graphicx}  % provides \includegraphics
\usepackage{listings} % For source code listing
\usepackage{logicpuzzle}  % provides kakuro
\definecolor{kakuro}{RGB}{155,206,167}
\kakurosetup{color=kakuro}
\usepackage{multicol}
\usepackage{multirow}
\usepackage{pgfplots} \pgfplotsset{compat=1.12}  % was 1.9, but gave errors?!
\usepackage{tikz}
\usetikzlibrary{arrows,automata,calc,trees,positioning,decorations.markings}
\usepackage{transparent}
\usepackage[dvipsnames]{xcolor}  % supersedes color
\usepackage{xspace}

\usepackage{hyperref}
\hypersetup{linkcolor=black}  % should always be last package


% Styling
%%%%%%%%%

\RequirePackage{helvet}
\RequirePackage{courier} % \texttt{...} gives thinner text and /\ displays OK

% Beamer themeing
\usetheme{boxes}
\usecolortheme{rose}  % colors the Examples

% Beamer hide navigation symbols
\setbeamertemplate{navigation symbols}{}

% Define colors
\definecolor{cons-darkblue}{RGB}{18,60,117}
\definecolor{cons-lightblue}{RGB}{106,194,238}


% Beamer custom title position and color
\setbeamercolor{frametitle}{fg=cons-darkblue}
\setbeamertemplate{frametitle}{
	\vskip0.5em
	%\hspace*{0.5em}
	{\usebeamerfont{frametitle}\usebeamercolor[fg]{frametitle}\insertframetitle\par}
	\vskip0.5em
}

% Beamer minimal line as footline
\setbeamertemplate{footline}{
	\vskip1em
	\nointerlineskip
	\begin{beamercolorbox}[wd=\paperwidth,ht=0.5em,dp=0pt,leftskip=0pt,rightskip=0pt]{}
		\color{cons-lightblue}\rule{\paperwidth}{0.5em}
	\end{beamercolorbox}
}

% Beamer remove dropshadow from blocks, but they are still rounded:
\setbeamertemplate{blocks}[rounded][shadow=false]
% Beamer remove gradient below header in blocks:
\makeatletter
\pgfdeclareverticalshading[lower.bg,upper.bg]{bmb@transition}{200cm}{color(0pt)=(lower.bg); color(4pt)=(lower.bg); color(4pt)=(upper.bg)}
\makeatother
% Beamer non-gradient bullets:
\setbeamertemplate{section in toc}{\inserttocsectionnumber.~\inserttocsection}%[circle]
\setbeamertemplate{subsection in toc}[circle]


% Beamer automatically show ToC before section/subsection
\AtBeginSection[]{
	\begin{frame}<beamer>{Outline}
		\tableofcontents[currentsection]
	\end{frame}
}
\AtBeginSubsection[]{
	\begin{frame}<beamer>{Outline}
		\tableofcontents[currentsection,currentsubsection]
	\end{frame}
}

\hypersetup{colorlinks=true,urlcolor=blue}

%% Colours
\newcommand<>{\blue}[1]{\textcolor#2{blue}{#1}}
\newcommand<>{\green}[1]{\textcolor#2{OliveGreen}{#1}}
\newcommand<>{\red}[1]{\textcolor#2{red}{#1}}
\definecolor{uured}{HTML}{9A0100}
\definecolor{uudarkblue}{HTML}{0A4267}
\definecolor{uulightblue}{HTML}{0C8FE6}
\definecolor{uulightyellow}{HTML}{EBE917}

% Symbols / commands
%%%%%%%%%%%%%%%%%%%%

%% Styles:
\newcommand{\defined}[1]{\textcolor{Orchid}{#1}}
\newcommand<>{\inference}[1]{\textcolor#2{LimeGreen}{#1}} % was OliveGreen
\newcommand<>{\relaxation}[1]{\textcolor#2{SkyBlue}{#1}}
\newcommand<>{\search}[1]{\textcolor#2{Orange}{#1}}
\newcommand<>{\conflict}[1]{\textcolor#2{red}{#1}}

\newcommand{\structured}[1]{\textbf{\textcolor{uured}{#1}}}
\newcommand{\important}[1]{\textcolor{red}{#1}}
\newcommand{\stressed}[1]{\textbf{\textit{#1}}}

%% Fancy characters:
\usepackage{pifont}
\newcommand{\handpoint}{\ding{43}}
\newcommand{\tick}{\ding{51}}
\newcommand{\notick}{\ding{55}}
\DeclareSymbolFont{extraup}{U}{zavm}{m}{n}

%% Tools and Languages:
\newcommand{\MiniZinc}{Mini\-Zinc\xspace}
\newcommand{\CPMpy}{CPMpy\xspace}

%% CP & Gecode & MiniCP & MiniZinc:
\newcommand{\AllDifferent}{\Constraint{AllDifferent}}  % MiniCP
\newcommand{\AnyCond}[1]{\text{Any}(#1)}  % Gecode
\newcommand{\BinPacking}{\Constraint{binpacking}}  % Gecode
\newcommand{\BoundedCond}[1]{\text{Bounded}(#1)}  % Gecode
\newcommand{\Channel}{\Constraint{channel}}  % Gecode
%\newcommand{\Circuit}{\Constraint{circuit}}  % Gecode
\newcommand{\Circuit}{\Constraint{Circuit}}  % MiniCP
\newcommand{\CondSet}[1]{\text{PropConds}(#1)}  % Gecode
\newcommand{\Conds}[2]{\text{Conds}(#1,#2)}  % Gecode
%\newcommand{\Constraint}[1]{\textsc{#1}}
\newcommand{\Constraint}[1]{\texttt{#1}}
%\newcommand{\Cumulative}{\Constraint{cumulative}}  % Gecode
\newcommand{\Cumulative}{\Constraint{Cumulative}}  % MiniCP
\newcommand{\DepProps}{\textit{DepProps}}  % Gecode
\newcommand{\DFE}{\text{DFE}}  % Gecode
\newcommand{\Disjunctive}{\Constraint{Disjunctive}}  % MiniCP
%\newcommand{\Distinct}{\Constraint{distinct}}  % Gecode
\newcommand{\Distinct}{\AllDifferent}  % MiniCP
\newcommand{\Domain}[1]{\textnormal{dom}(#1)}
%\newcommand{\Element}{\Constraint{element}}  % Gecode
\newcommand{\Element}{\Constraint{Element}}  % MiniCP
%\newcommand{\Extensional}{\Constraint{extensional}}  % Gecode
\newcommand{\Extensional}{\Table}  % MiniCP
\newcommand{\Failed}{\text{Failed}}  % Gecode
\newcommand{\FailedCond}[1]{\text{Failed}(#1)}  % Gecode
\newcommand{\FixedCond}[1]{\text{Fixed}(#1)}  % Gecode
\newcommand{\Fixpoint}{\text{AtFixpt}}  % Gecode
\newcommand{\GlobalCardinality}{\Constraint{count}}  % Gecode
\newcommand{\Linear}{\Constraint{linear}}  % Gecode
\newcommand{\MaxCond}[1]{\text{Max}(#1)}  % Gecode
\newcommand{\MinCond}[1]{\text{Min}(#1)}  % Gecode
\newcommand{\ModVars}{\textit{ModVars}}  % Gecode
\newcommand{\NoneCond}[1]{\text{None}(#1)}  % Gecode
\newcommand{\NValues}{\Constraint{nvalues}}  % Gecode
\newcommand{\Path}{\Constraint{path}}  % Gecode
\newcommand{\Precede}{\Constraint{precede}}  % Gecode
\newcommand{\Propagate}{\text{Propagate}}
%\newcommand{\Reifies}[2]{#1\Leftrightarrow#2}
\newcommand{\Reifies}[2]{#2\Leftrightarrow#1}  % layout as in MiniZinc
\newcommand{\Stores}{\mathbb{S}}
\newcommand{\Subsumed}{\text{Subsumed}}  % Gecode
\newcommand{\Sum}{\Constraint{Sum}}  % MiniCP
\newcommand{\Table}{\Constraint{Table}}  % MiniCP
\newcommand{\Unary}{\Constraint{unary}}  % Gecode
\newcommand{\Unknown}{\text{Unknown}}  % Gecode
\newcommand{\Variables}[1]{\text{var}(#1)}

%% Math support:
\newcommand{\cons}[2]{\textsc{#1}(#2)}
\newcommand{\AbsValue}[1]{\left\lvert#1\right\rvert}
\newcommand{\Cardinality}[1]{\left\lvert#1\right\rvert}
%\newcommand{\Cardinality}[1]{\##1}
\newcommand{\Ceiling}[1]{\left\lceil#1\right\rceil}
\newcommand{\Else}{\textbf{~else~}}
\newcommand{\EmptySet}{\varnothing}
\newcommand{\Floor}[1]{\left\lfloor#1\right\rfloor}
\newcommand{\GeqLex}{\geq_{\Lex}}
\newcommand{\If}{\textbf{if~}}
\newcommand{\Iff}{\Leftrightarrow}
\newcommand{\IfThenElse}[3]{\If#1\Then#2\Else#3}
\newcommand{\Implies}{\Rightarrow}
\newcommand{\Int}{\mathbb{Z}}
\newcommand{\Inter}{\cap}
\newcommand{\Iverson}[1]{{\textcolor{red}{\left[\textcolor{black}{#1}\right]}}}
\newcommand{\LeqLex}{\leq_{\Lex}}
\newcommand{\Lex}{\textnormal{lex}}
\newcommand{\LtLex}{<_{\Lex}}
\newcommand{\Nat}{\mathbb{N}}
\newcommand{\Oh}[1]{\mathcal{O}(#1)}
\newcommand{\Sequence}[1]{\left[#1\right]}
\newcommand{\Set}[1]{\left\{#1\right\}}
\newcommand{\SetComp}[2]{\Set{#1\SuchThat#2}}
\newcommand{\SuchThat}{\mid}
\newcommand{\Then}{\textbf{~then~}}
\newcommand{\Tuple}[1]{\left\langle#1\right\rangle}
\newcommand{\Union}{\cup}
\newcommand{\Where}{\textbf{~~where~~}}
\DeclareMathOperator*{\minimize}{minimize}
\DeclareMathOperator*{\maximize}{maximize}


%% Toggling flashcard slides on/off
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% both are used once L01, even without flashcard 
\input{listing_cpmpy}  
\input{listing_minizinc}

\ifdefined\showcpmpy
\newenvironment{flashcardcpmpy}{}{}
\else
\excludecomment{flashcardcpmpy}
\fi

\ifdefined\showminizinc
\newenvironment{flashcardminizinc}{}{}
\else
\excludecomment{flashcardminizinc}
\fi
