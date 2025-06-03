# What is this?
## Discord bot to run simulations and calculations on the best odds and picks when it comes to sport's betting.
Start of the project will just focus primarily on NBA games utilizing WebScraping to gather data which will get sent to a database which then gets passed on to my main program to finally be displayed to my user via a discord bot, calculations will be made utilizing my own team power system

### Power System
So far the power system utilizes the following metrics
- ppg (points per game)
- injuries
- starters / benched players
- Status of the player 
### Future will include
- Managers/trainers
- Trades
- Previous games performance
- TBD
# 🐍 Python Project Learning Log

**Project Start Date:** *5/7/25*  
**Main Project:** Sports Betting Bot  
**Current Date:** 2025-06-03

---

## ✅ Key Milestones & Lessons Learned

### 🔹 Initial Setup & Main.py Integration
- Successfully connected `Main.py` with the `teams` module
- Fixed issues related to Python's `from` and `import` statements
- Understood the use of submodules and subpackages
- Learned how to import between files in the same package

---

### 🧠 Object-Oriented Programming (OOP)
- Learned to access instance variables using `self.variable`
- Understood that class methods must also use `self` to access other class attributes
- Learned how to instantiate classes and use class methods
- Realized that printing a class object directly shows a memory address, not its data
- To see actual data, print specific instance variables instead

---

### 🔧 Python Syntax & Structure
- `pass` can be used to skip a block (e.g., placeholder in `if` or function)
- Python methods don't need arguments for every variable if `self` can access them
- Parameters in method definitions should be lowercase (Python naming convention)
- Calling a method in the constructor runs it during instantiation

---

### 📦 Python Execution Behavior
- Running Python code generates a `__pycache__` folder with `.pyc` bytecode
- Python compiles `.py` to `.pyc` before interpreting — speeds up subsequent runs
- `.pyc` files shouldn't be committed to GitHub (`__pycache__/` goes in `.gitignore`)

---

### 🔍 Python vs Other Languages
- Python is **interpreted**, but also **compiles to bytecode** (.pyc)
- Compilation in Python is immediate and internal — part of the execution process
- Compared to C++:
  - Python is easier and safer, but slower
  - C++ is faster and gives full control over memory and types

---

### ⚙️ Under-the-Hood Python
- Learned about `dis` module to inspect bytecode
- Used `dis.dis()` to see compiled bytecode for functions and files
- Realized Python acts as a high-level wrapper for C/C++ in many ML frameworks

---

## 📝 Notes for Future Study
- Cement understanding of `from` and `import` with more complex packages
- Review Python’s memory model and garbage collection

---

**Next Task:** Work on the `player` class module

**Future Goals:**  
- Build core simulation logic  
- Connect Discord bot to the backend  
- Possibly add ML elements after a working prototype

---
