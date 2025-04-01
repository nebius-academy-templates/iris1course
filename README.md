# Iris for Friends

## How to Work With the Repository 
### Clone the Iris for Friends project into the *Dev/* folder.

You should get this structure:

```
Dev/
 └── iris1course/
     ├── iris_for_fiends/
     ├── html_templates/
     ├── .gitignore
     ├── LICENSE
     ├── requirements.txt
     └── README.md
```

### Create a virtual environment

1. Open Visual Studio Code, go to *"File" / "Open Folder,"* and open *Dev/iris1course/*.
2. Launch the terminal in VS Code and make sure you work from the *iris1course/* directory. If you use Windows, make sure Git Bash runs in the terminal, and not through PowerShell or anything else. Run this command:
- Linux/macOS
    
    ```bash
    python3 -m venv venv
    ```
    
- Windows
    
    ```python
    python -m venv venv
    ```

The virtual environment will be deployed in the *iris1course/* directory. The `venv` folder will appear there too and will store all the project dependencies. The file structure will look like this:

```

Dev/
└── iris1course/
    ├── iris_for_friends/
    ├── html_templates/
    ├── venv/   
    ├── .gitignore
    ├── LICENSE
    ├── requirements.txt
    └── README.md
```

### Activating the virtual environment
In the terminal, go to the root directory of the project *Dev/iris1course/* and run this command:
- Linux/macOS
    
    ```bash
    source venv/bin/activate
    ```
    
- Windows
    
    ```bash
    source venv/Scripts/activate
    ```

All commands in the terminal will now be preceded by the `(venv)` string.

💡 All the following console commands must be run with the working virtual environment.

Refresh pip:

```bash
python -m pip install --upgrade pip
```

### Install the dependencies from the *requirements.txt* file
Run the following command while you are in the *Dev/iris1course/* folder:

```bash
pip install -r requirements.txt
```

### Using migrations

    
In the directory with the manage.py file, run this command:

```bash
python manage.py migrate
```

### Running the project in dev mode

    
In the directory with the manage.py file, run the command:

```bash
python manage.py runserver
```

In response to the command, Django will report that the server is running and the project is available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/). 
