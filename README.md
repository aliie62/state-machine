# About the project
This is a finite state machine with 26 states. It introduces both server and client code and the project structure is inherited from Flask projects.
<br/><br/>

## State Machine
 The state machine implemented in this project has 26 states, one per each alphebatic letter (A-Z). State **A** is the initial state and state **Z** is the terminator. These 3 possible transitions from each state, except for state **Z** which only has one transition to **A**.
<br/>
 The full scenario can be found here: [State Machine Structure](scenario.md)
<br/><br/>


## Design
It is currecntly deployed with a **TCP** server using socket programming.
<br/><br/>


# Getting Started
<br/>

## Built With
Built with Python 3.10.2 on top of a postgres database.
<br/>

## Installation
Download or clone the repository in your machine. In the Command Prompt in Windows or bash in Linux, go to folder that you cloned/copied the code. There us no need to any extra packages other than some of the built-in ones.
<br/>
You might want to set up a virtual environment before installing any packages. If so, you can run the code below:

```
pip3 install virtualenv
cd [PROJECT_FOLDER]
virtualenv venv --python=python3.10
```

MacOS/Linux:
```
source venv/bin/activate
```

Windows:
```
.\venv\Scripts\activate
```

Then install the requirements using command below:
```
pip install -r requirements.txt
```
<br/>


## Configuration
There are a few parameter to configure:
<br/>
- SM_DATABASE_URI environment variable to point to the desired SQLite database path.
- Server **host** and **port** variables in both [client.py](client.py) and [server.py](server.py) according to your server configuration. 

<br/>

## Usage
In the Command Prompt/bash run below command:

- Server:
```
python.exe server.py
```
- Client:
```
python.exe client.py
```
<br/><br/>


# Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.
<br/>
1. Fork the Project
2. Create your Feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request.
<br/><br/>

# License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
<br/><br/>

# Change Log
To learn more about the changes in this version, please refer to [Change Log](CHANGELOG.md)
<br/><br/>

# Contact
Ali Hosseini on https://twitter.com/a1iie62 or Ali.Hoss3ini@gmail.com
Project Link: https://github.com/aliie62/state-machine-tcp

