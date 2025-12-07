# Hardware-Reporter
PC Hardware Reporter to Discord Webhook – A lightweight Python script that collects your PC’s CPU, GPU, RAM, Disk, IP, and approximate location and sends a detailed report to a Discord webhook. Cross-platform (Windows, Linux, macOS) and optionally integrates with Electron for a GUI.

<p align="center">
  <img src="https://img.icons8.com/color/96/000000/computer.png"/>
</p>
<h1 align="center">🖥️ PC Hardware Reporter to Discord</h1>
<p align="center">A Python script that collects your PC hardware info and sends it to Discord via webhook.</p>

![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Issues](https://img.shields.io/github/issues/YOUR_USERNAME/YOUR_REPO)

---

## 📖 Table of Contents

- [⚡ Features](#-features)  
- [📦 Requirements](#-requirements)  
- [🛠️ Installation](#-installation)  
- [🚀 Usage](#-usage)  
- [🖥️ Optional Electron Integration](#-optional-electron-integration)  
- [🔐 Privacy & Security](#-privacy--security)  
- [👨‍💻 Contributing](#-contributing)  
- [📄 License](#-license)  
- [📸 Screenshots](#-screenshots)  

---

## ⚡ Features

- Cross-platform: **Windows, Linux, macOS**  
- Sends live reports to **Discord webhook**  
- CPU, GPU, RAM, Disk info  
- Local IP, Public IP, Approximate location  
- Timestamp included  
- Lightweight Python script  
- Optional **Electron GUI integration**  

---

## 📦 Requirements

| Module   | Purpose                                 |
|----------|----------------------------------------|
| psutil   | RAM, Disk usage                         |
| requests | Public IP & Discord webhook             |
| wmi      | CPU/GPU detection (Windows only)        |
| platform | CPU fallback info                        |
| socket   | Local IP                                |
| subprocess | Linux/macOS CPU & GPU commands        |
| datetime | Timestamp                               |

> ⚠ Note:  
> - `wmi` is required **only on Windows**  
> - Linux/macOS use built-in system commands  
> - Internet connection is required to fetch public IP and location  

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/shervinexe/Hardware-Reporter.git
cd pc-hardware-discord

