# GIL Playground

A hands-on Python playground to explore the **Global Interpreter Lock (GIL)**.  
Run small, focused scripts to see when the GIL matters, when it doesn’t, and how to work around it.

---

## 📌 Planning on adding

- **Basics** – Simple examples to show GIL behavior.
- **Benchmarks** – CPU-bound vs I/O-bound performance.
- **Advanced** – NumPy, multiprocessing, and GIL internals.
- **Notes** – Links and explanations for deeper learning.

---

## 📂 Repo Structure

gil-playground/
│── basics/
│ ├── gil_basics_counter.py
│ ├── cpu_bound_threads.py
│ └── io_bound_threads.py
│── benchmarks/
│ ├── threading_vs_multiprocessing_cpu.py
│ └── mixed_io_cpu.py
│── advanced/
│ ├── numpy_gil_release_demo.py
│ └── notes_cpython_gil_internals.md
│── README.md
│── requirements.txt
└── Makefile
