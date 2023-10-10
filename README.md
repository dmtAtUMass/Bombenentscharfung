# Bombenentscharfung

An automated diffusion tool for UMass binary bomb problem

## Description

This project provides a tool to automatically defuse binary bomb executables from the UMass CS curriculum. The bomb consists of multiple phases that require inputting strings or numbers to defuse. This tool analyzes the bomb and generates the correct defusal sequences.

## Usage

To use this tool:

1. Clone this repository
2. Compile the bomb executable
3. Run the tool:

```
python bombenentscharfung.py <path to bomb>
```

4. The tool will output the defusal sequence

5. Input the sequence into the bomb to defuse it

## Implementation

The tool uses techniques like dynamic instrumentation, emulation, and static analysis to understand the logic of each bomb phase. It identifies the checks the bomb makes on the input and solves for the correct input that satisfies all checks.

Key components:

- DynamoRIO for dynamic binary instrumentation
- Unicorn CPU emulator for symbolic execution
- Angr binary analysis framework for static analysis
- Custom bomb phase solvers using Z3 SMT solver

## Disclaimer

This tool is meant for educational purposes only to learn about reverse engineering and binary analysis. Do not use it to cheat or misrepresent your skills.

## License

This project is licensed under the MIT License - see the LICENSE file for details.