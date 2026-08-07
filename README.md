# FinanceSmart Hackathon

**Time:** 1:30 – 3:00 PM  
**Task:** Build the budgeting tracker app as a team.

- You are expected to come up with a name for your team that you put in the "CONTRIBUTIONS.md" file.
- You are expected to plan the solution before developing it. Pen and paper is fine — if you plan electronically, add links to your designs or docs in `GROUP_LINKS.txt`.
- Keep a log of each member's work and contributions in the "CONTRIBUTIONS.md" file.

**Suggested schedule**

| Time | Activity |
|---|---|
| 1:30 – 1:45 | Read the brief, set up the repo |
| 1:45 – 2:45 | Plan and build |
| 2:45 – 3:00 | Final touches, clean up, make sure code is pushed and contributions are noted |

---

## Disclaimer

> By downloading files from capitalone.co.uk, you agree that Capital One is not liable for any issues that may arise from the use of these files. You acknowledge that although Capital One has taken reasonable precautions to ensure no viruses are present in the downloadable files contained herein, Capital One does not accept responsibility for any loss or damage sustained as a result of computer viruses and you must ensure that the email (and attachments) are virus free and take responsibility for the protection of your equipment through the use of up-to-date virus protection.
>
> The software contained in the downloadable files are provided by the copyright holders and contributors and any express or implied warranties, including, but not limited to, the implied warranties of fitness for a particular purpose are disclaimed. In no event shall Capital One (Europe) PLC. be liable for any direct, indirect, incidental, special, exemplary, or consequential damages however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.

This is a coding practice session aimed to provide a hands-on learning experience. Working simplicity is better than non-working complexity. Even if your implementation is not finished, being able to explain what you would have done next will also be taken into account when marking.

If you finish early, consider these extensions:
- **Testing**: consider more complex test cases as well as edge cases
- **Input validation and Error Messages**: consider how you can improve the user's experience with useful error messages on inputs on the frontend and backend
- **Database**: consider how you can persist data in a database instead of a .csv file to handle larger amounts of data and quick data querying

**NO AI tools please.**

---

## The Brief

### Budgeting Tracker
Help a young adult understand and track their monthly financial spending. Given their income and expenditure, show them where their money is going and help them identify areas where they can save.  
📁 `budgeting/`

Read `brief.md` inside the folder for the detailed brief.

Any external links that you would like us to consider when assigning marks<> such as planning boards, should go into the `GROUP_LINKS.txt` file.

---

## Getting Started — Fork & Clone

**1. Fork the repo**  
One person in the team forks the repo on GitHub by clicking **Fork** (top right). The rest of the team then clone that person's fork — everyone in the team works from the same copy.

**2. Clone the fork**
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

**3. Make sure you commit and push your work regularly**
```bash
git add .
git commit -m "your message"
git push
```

---

## Setup — What You Need Installed

| Tool | Purpose | Install |
|---|---|---|
| Python 3.11+ | Backend runtime | python.org |
| Git | Version control | git-scm.com |
| GitHub Account | Host your code | github.com |
| IDE (VS Code recommended) | Editor | code.visualstudio.com |
| Browser (Chrome recommended) | Frontend | google.com/chrome |

Verify your setup:
```bash
python3 --version   # should be 3.11+
git --version
```

### 1. Python 3.11+
*Licence: Copyright © 2001-2024 Python Software Foundation. Licensed under the PSF License — https://docs.python.org/3/license.html*

**Windows:**
1. Go to https://www.python.org/downloads/
2. Click "Download Python 3.x.x"
3. Run the installer
4. **IMPORTANT:** On the first screen, tick **"Add Python to PATH"** before clicking Install
5. Click "Install Now"

**Mac:**
1. Go to https://www.python.org/downloads/
2. Click "Download Python 3.x.x"
3. Open the downloaded .pkg file and follow the installer steps

### 2. Git
*Licence: Copyright © 2005-2024 Linus Torvalds and others. Licensed under GPL-2.0 — https://www.gnu.org/licenses/old-licenses/gpl-2.0.html*

**Windows:**
1. Go to https://git-scm.com/downloads and click "Windows"
2. Run the installer — the default options are fine
3. This also installs "Git Bash", a terminal you can use for git commands

**Mac:**
- Easiest: open Terminal, type `git --version` — macOS will prompt you to install it automatically
- Or download from https://git-scm.com/downloads and run the installer

### 3. GitHub Account
*Terms: Copyright © GitHub, Inc. — https://docs.github.com/en/site-policy/github-terms/github-terms-of-service*

1. Go to https://github.com
2. Click "Sign up" and follow the steps
3. Choose the free plan and verify your email

If you already have a GitHub account, you're good to go.

### 4. VS Code (recommended IDE)
*Licence: Copyright © Microsoft Corporation. Licensed under the MIT Licence — https://github.com/microsoft/vscode/blob/main/LICENSE.txt*

**Windows:**
1. Go to https://code.visualstudio.com
2. Click "Download for Windows"
3. Run the installer — tick "Add to PATH" when prompted

**Mac:**
1. Go to https://code.visualstudio.com
2. Click "Download for Mac"
3. Open the downloaded .zip — this extracts VS Code.app
4. Drag VS Code.app to your Applications folder
5. Open it from Applications (or Spotlight: Cmd+Space, type "VS Code")

### 5. Google Chrome (recommended browser)
*Terms: Copyright © Google LLC — https://www.google.com/chrome/terms/*

1. Go to https://www.google.com/chrome
2. Click "Download Chrome" and run the installer

Any modern browser will work (Firefox, Edge, Safari).

### 6. Python Packages (Flask, pytest)

We use three Python packages: Flask (web framework), Flask-CORS (allows the frontend to talk to the backend), and pytest (testing).

*Licences: Flask — BSD 3-Clause (https://flask.palletsprojects.com/en/stable/license/), Flask-CORS — MIT (https://github.com/corydolphin/flask-cors/blob/main/LICENSE), pytest — MIT (https://docs.pytest.org/en/stable/license.html)*

**OPTION A — Install globally (recommended before the event)**

Windows:
```bash
python -m pip install flask flask-cors pytest
```
Mac:
```bash
python3 -m pip install flask flask-cors pytest
```

**OPTION B — Install in a virtual environment (do this on the day, not before)**

A virtual environment isolates packages for this project so they don't affect your existing Python setup. However it is tied to the folder it's created in — so this only makes sense once you have the repo cloned in front of you on the day.

Windows:
```bash
python -m venv venv
venv\Scripts\activate
python -m pip install flask flask-cors pytest
```
Mac:
```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install flask flask-cors pytest
```
You'll know it's active when you see `(venv)` at the start of your terminal prompt. Run the activate command each time you open a new terminal. To deactivate: `deactivate`

> If you don't do this ahead of time, you can run the same commands on the day once you have cloned the repo. We can help you with that!

---

## How to Run

**1. Install dependencies**
```bash
cd budgeting/backend
python3 -m pip install -r requirements.txt
```

**2. Start the backend**
```bash
python3 app.py
```

**3. Start the frontend server** (run from inside the `budgeting/` folder)
```bash
python3 -m http.server 8080
```

**4. Open in browser**
```
http://localhost:8080/frontend/login.html
```

**Run tests**
```bash
cd budgeting/backend
pytest tests/ -v
```

---

## Marking

**Total: 30 marks**

| Category | Marks | Notes |
|---|---|---|
| Design | 10 | See breakdown below |
| Implementation | 10 | See breakdown below |
| Communication | 5 | To be assessed through observations during planning and implementation |
| Teamwork | 5 | To be assessed through observations and member contributions noted in the "CONTRIBUTIONS" file |

### Design (10)
| Sub-category | Marks |
|---|---|
| **Accessibility and ethics** - Our motto is "Change Banking for Good" so keep the best interest of customers in mind when planning your app, especially those that are more vulnerable | 3 |
| **Planning** - We expect to see Wiremocks and/or plans for your app. Pen & paper is fine, just make sure to hand it in at the end. If you have done your planning electronically then add a link that assessors can access to the GROUP_LINKS.txt file | 5 |
| **Testing** - Think about how to test your app when planning, especially the key test cases you think you will need and what the expected results of them are | 2 |

### Implementation (10)
| Sub-category | Marks |
|---|---|
| **Functionality** - Your solution will be capped at 4 marks if it does not achieve the basic functionality outlined in the project's brief even if you do the extensions | 4 |
| **Testing** - writing tests may get you 1 point but you won't achieve full marks unless you write good tests | 2 |
| **Database / Persistence** - Implement a database instead of using the CSV file to store data | 2 |
| **User Experience** - Add input validation and useful error messages to tell users what they are doing wrong. This section also involves how your app looks and feels to a user. &#x2728; Creativity will be rewarded! &#x2728; | 2 |
