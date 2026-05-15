# 🎼🃏 Music Interval Flip Cards

### A flip card game application that helps music learners to memorize musical intervals.

The User:
- Chooses an interval from a list, clicks **Begin**, and then is directed to another page to begin playing.
- Clicks **Start** to show the first card.
- Clicks on the card to show the corresponding interval on the back of the card.
- Then clicks **Next** to show the next card.

<br>

## 🕹️ Getting Started

- Follow [installation](#-installation) process to setup the repo.
- Set up the users database. Run the following script in the terminal: <br>
```
flask --app flaskr create_db
```
(This will create a users database in the instance folder)
- Start the application. Run the following script in the terminal: <br>
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
Follow the instructions to install in either GitHub Codespaces, your local development using Docker, or your local development without a container (use this for testing!)
### Installing in GitHub Codespaces
- In the "music-interval-cards" repo, click the green **Code** button.
- Select **Codespaces**.
- Select create a new Codespace.

(The .devcontainer file should be automatically detected and build the dependencies.)

### Installing in your Local Development via the Docker container
(e.g. using VS Code)
- Install Docker Desktop
- Install Dev Containers extension in VS Code
- Using the terminal (bash), clone the repository:

```bash
git clone https://github.com/pl-codes/music-interval-cards.git
```
In VS Code open the music-interval-cards folder. The .devcontainer file should be automatically detected and a request from VS Code to "open in Dev Containers" should be displayed. Click Ok.

If not:
- In VS Code, open the Command Palette (Cmd/Ctrl+Shift+P), run "Dev Containers: Reopen in Container"
<br>

### Installing in your Local Development (no container, **use this method to run selenium automated tests**)

(e.g. using VS Code)
- Using the terminal (bash), clone the repository:
```bash
git clone https://github.com/pl-codes/music-interval-cards.git
```
*Ignore prompt to open in a container if asked*

<br>

- Move to the repo folder:
```bash
cd music-interval-cards
```
<br>

- Create a virtual environment:
```bash
python -m venv venv
```
<br>

- Activate the virtual environment:

For Linux/macOS
```bash
source venv/bin/activate
```
For Windows
```bash
source venv/Scripts/activate
```
<br>

- Install the packages:
```bash
pip install -r requirements.txt 
```