# 🎼 Music Interval Flip Cards

### 🃏 A flip card game application that helps music learners to memorize musical intervals.

The User:
- Chooses an interval from a list, clicks **Begin**, and then is directed to another page to begin playing.
- Clicks **Start** to show the first card.
- Clicks on the card to show the corresponding interval on the back of the card.
- Then clicks **Next** to show the next card.

<br>

## 🕹️ Getting Started

- Follow [installation](#-installation) process to setup the repo.
- Run the following script in the terminal: <br>
Make sure your are in the "flip-card" folder (\<your-project-path>/**flip-card**)
```
flask --app flaskr run --debug
```
(This will run in debug mode inside the Docker dev container, with its local port 5000 forwarded to your local machine to be opened in your browser)
- To end the session, Press **Ctrl + C** in the terminal.  

<br>

## 🛠️ Tech Stack

- **Language:** Python / HTML / CSS / JavaScript
- **Framework:** Flask
- **Database:** SQLite
- **Other Tools:** Docker

<br>

## 📦 Installation
### Installing in GitHub Codespaces
- In the "music-interval-cards" repo, click the green **Code** button.
- Select **Codespaces**.
- Select create a new Codespace.

(The .devcontainer file should be automatically detected and build the dependencies.)

### Installing in your Local Development
(e.g. using VS Code)
- Install Docker Desktop
- Install Dev Containers extension in VS Code
- In the terminal, clone the repository:

In the terminal

```bash
git clone https://github.com/pl-codes/music-interval-cards.git
```
The .devcontainer file should be automatically detected and a request from VS Code to "open in Dev Containers" should be displayed. Click Ok.

If not:
- In VS Code, from the Command Palette, run "Dev Containers: Reopen in Container"