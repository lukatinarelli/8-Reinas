<p align="center">
   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Eight-queens-animation.gif/220px-Eight-queens-animation.gif" alt="8 queens animation"/>
</p>

<h1 align="center">♛ 8 Queens Solver — Backtracking Edition</h1>

<p align="center">
   <img src="https://img.shields.io/badge/STATUS-COMPLETED-green?style=for-the-badge">

   <a href="https://docs.python.org/3/">
      <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python"></a>
   
   <a href="https://en.wikipedia.org/wiki/Backtracking">
      <img src="https://img.shields.io/badge/Algorithm-Backtracking-orange?style=for-the-badge"></a>

   <a href="https://github.com/lukatinarelli/8-Queens-Backtracking/blob/main/LICENSE">
      <img src="https://img.shields.io/badge/License-CC0-lightgrey?style=for-the-badge"></a>
</p>

---

## 📜 Project Description

This project implements a solver for the classic **8 Queens puzzle**, using a **backtracking algorithm** to place eight queens on a chessboard so that none of them can attack each other.

Unlike standard versions of the puzzle, this implementation allows the user to:

- Specify the **initial position** of one queen
- Automatically compute a valid arrangement for the remaining seven
- Visualize the board in an ANSI-colored console output

The solver is lightweight, uses pure Python, and runs entirely in the terminal.

---

## ⚙️ Key Features

- **User-defined starting position:** Place the first queen anywhere on the board (e.g., A1, H8).  
- **Backtracking algorithm:** Automatically computes a valid arrangement for the remaining queens.  
- **ANSI-colored console output:** Clear and easy-to-read board visualization.  
- **Lightweight Python implementation:** No external libraries required.  
- **Interactive input:** Simple, terminal-based interface for specifying positions.

---

## 💻 Installation & Usage

### 📋 Requirements

- **Python 3.x** (Version 3.6 or higher recommended)
- Terminal that supports **ANSI colors**

No additional libraries are needed.

### 💻 Installation

1. Clone the repository:

```bash
git clone https://github.com/lukatinarelli/8-Queens-Backtracking.git
cd 8-Queens-Backtracking
```

2. (Optional) Make sure Python 3 is in your PATH.

### 🚀 Usage

Run the main script and follow the prompts:

```bash
python main.py
```

1. Enter the initial position of the first queen (e.g., A1, H8).

2. The program will automatically compute a valid solution and display the board with colored output.

### Example Output

```console
Enter the initial position of the first queen (e.g., A1):

Solution found:

    A B C D E F G H
  +----------------+
1 |♛ - - - - - - - |
2 |- - - - - ♛ - - |
3 |- - - - - - - ♛ |
4 |- ♛ - - - - - - |
5 |- - - ♛ - - - - |
6 |- - - - - - ♛ - |
7 |- - ♛ - - - - - |
8 |- - - - ♛ - - - |
  +----------------+
```

---

## 🔗 Useful Resources

- [8 Queens Problem - Wikipedia](https://en.wikipedia.org/wiki/Eight_queens_puzzle)  
- [Python 3 Documentation](https://docs.python.org/3/)  
- [Backtracking Algorithm](https://www.geeksforgeeks.org/backtracking-algorithms/)

---

## 📄 License

This project is licensed under the **[CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](LICENSE)**.  

You can freely:

- **Copy, modify, and distribute** the code  
- **Use it for any purpose**, including commercial use  
- **No attribution required** (although credit is appreciated)

> This project is released into the public domain for educational and personal use.
