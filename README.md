# Wyrdl

A Python-based Wordle Clone for the Terminal.

## How to Create a Wordlist

To create the `wordlist.txt` file, follow these steps:

1. Make sure you have Python installed on your system. You can verify it by running the following command in the terminal:

```shell
python --version
```

2. Download or clone the repository to your local machine.

3. Open a terminal or command prompt and navigate to the project directory.

4. Run the following command:

```shell
python create_wordlist.py <file_path> wordlist.txt
```

Replace `<file_path>` with the path to the file that contains the words you want to extract and save in the `wordlist.txt` file.

5. After executing the command, the script will process the file and create the `wordlist.txt` file in the same directory.

## Installation

To install the required `rich` module, follow these steps:

1. Set up a virtual environment:

```shell
python -m venv venv
source venv/bin/activate
```

2. Install the dependencies using pip:

```shell
python -m pip install -r requirements.txt
```

## How to Play

1. Run:

```shell
python wyrdl.py
```

## View Original Project

Visit the original project [here](https://realpython.com/python-wordle-clone/).

Or scan the QRCode.

[![QR Code](qrcode.png "Scan or Click Here")](https://realpython.com/python-wordle-clone/)
