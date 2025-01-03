# Snake, Water, Gun Game

This repository contains a simple Python implementation of the classic "Snake, Water, Gun" game. Like "Rock, Paper, Scissors," this game involves players competing by choosing one of three options.

## How to Play

- **Snake** beats **Water** (Snake drinks Water).
- **Water** beats **Gun** (Water douses Gun).
- **Gun** beats **Snake** (Gun shoots Snake).
- If both the player and the computer choose the same option, it's a draw.

## Features

- Randomized computer choices for fairness.
- User-friendly input and output.
- Fun and engaging gameplay.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Running the Game

1. Clone this repository:

   ```bash
   git clone https://github.com/Bikram-Mahanta/Snake-water-game.git
   ```

2. Navigate to the project directory:

   ```bash
   cd <repository-directory>
   ```

3. Run the Python script:

   ```bash
   python main.py
   ```

4. Enter your choice when prompted:

   - `s` for Snake
   - `w` for Water
   - `g` for Gun

5. The program will display the choices and the results of the game.

## Example

```plaintext
Enter your number: s
You Choose Snake
Computer choose Gun
You Lose
```

## Code Overview

- The program uses the `random` module to generate the computer's choice.
- A dictionary maps user inputs (`s`, `w`, `g`) to their respective game entities.
- Another dictionary reverses the mapping for display purposes.
- Logical conditions determine the winner based on the rules.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- Inspired by the classic "Rock, Paper, Scissors" game.
- Built for fun and educational purposes.

