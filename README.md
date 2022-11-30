# powercut_bot ⚡

 Power Cut Scheduler

 ## Token 

 In the root directory of the project 
  1. Create a new `.env` file
  2. Add the blow code with your `TOKEN`

 ```.env
    TOKEN = TOKEN_OF_YOUR_THE_BOT
```



***

### To run virtual environment on VSCode


```bash
# macOS/Linux
# You may need to run sudo apt-get install python3-venv first
python3 -m venv .venv

# Windows
# You can also use py -3 -m venv .venv
python -m venv .venv
```

### On VSCode

```bash
1. `ctrl` + `shift` + `p` and select Python Interpreter
2. Select the `enter interpreter path`
3. Browse and select `.venv/Scripts/python.exe`
```
If you want to manually specify a default interpreter that will be used once you first open your workspace, you can create or modify an entry for `python.defaultInterpreterPath` setting in your workspace `settings.json` with the full path to the Python executable. 

In `settings.json`

```json
{
  "python.defaultInterpreterPath": "YOUR_PATH/.venv/Scripts/python.exe"
}

```


