# Dinosaur

If you don't understand English, click [here](README-vn.md) / Nếu bạn không hiểu tiếng Anh, bấm vào [đây](README-vn.md)

A Chrome dinosaur game written entirely in Python.
<br>
<br>
![dino](https://user-images.githubusercontent.com/83117848/184065978-c6e65022-8df4-40f8-a4b6-ce53810f175d.gif)

```
Platform: PC
Python version: 3.10.5
Libraries:
    - read requirement.txt
```

## Update
Introduce major bug fixes that affect the gameplay, now you can freely play the game without the bug ruining your experience
(it's big laggy tho)

## Control

- Space: Jump
- Down arrow button: Duck
- P: Pause

Jumping while pressing down arrow will make the dino fall faster


## TODO
- [x] Add collision between dino and obstacles
- [x] Add paused screen
- [x] Add lost screen
- [ ] Add progress saver feature

## Build Instruction


ATTENTION: This instruction is designed specifically for Windows

Prerequisites:
- Install Python 3.10 at [python.org](https://www.python.org/)

To automatically build the game from source (**easiest method**), you can follow this instruction:

- Download the content of this repository
- Run `compile.bat` as Administrator to automatically package the game (package operations are listed in the file)
- Once it's done, Dinosaur.exe will appear in the root of this directory. Run it.

(if you want to recompile the game, please remember to delete the old executable first)
<br>

To manually build the game, follow this instruction:

- Download the content of this repository
- Open the console and change the directory path to the path of this directory, run the following command: `pip install -r requirement.txt`
- Continue and run this command: `python -m PyInstaller --onefile -w -i="./assets/img/icon/dino.ico" entry.py`
- Delete `./build` and `./entry.spec` if not necessary
- Move the executable from `./dist` to the root of this repo
- Run the executable

(Please note that the game will need some assets to function properly. You'll need the `assets` folder and `config.json` file to be in the same directory as the executable)

## Contributing
If you notice any performance issues or bugs, you can open an issue in the Issues tab.
## License

This project falls under the MIT License
