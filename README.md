# Telegram Username Checker

In order to run this tool you need have up to date versions of python and pip installed first. This uses telethon to interact with the telegram api and allows you to check usernames, however you need to obtain an api `id` and `hash` to be able to call the username checks. On first run of the program you will first be prompted with a login (telephone) and then code sent to your telegram account. Once logged in a session file is created and you will be able to run the checker.

Obtain api `id` and `hash` here: https://core.telegram.org/api/obtaining_api_id

If you have a question about the rate limit read here https://github.com/jnoc/telegram-username-checker/issues/2#issuecomment-653112868
## Installation

1. Download the zip or clone the repository with Git to your machine.
2. Install the dependencies using `setup.bat` (for windows) or the following command inside Command Prompt (Windows) or Terminal (Mac). If you use Python.exe, it will not work.

```
python -m pip install configparser telethon
```

3. Edit the `config.ini` indisde a text editor. It explains what to do inside of it.
4. You have 2 options from here;
> A). You can directly run the python file by double clicking it

> B). Open the Command Prompt or Terminal. Navigate to the file:

```
cd *path to the folder*
```

> Run the script via command line 

```
python check.py
```

## Disclaimer
I do not condone breaking TOS of the Telegram api with this tool.
