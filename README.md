# GitProject

GitProject is a Python-based tool for managing and synchronizing multiple Git repositories within a project. It allows users to easily update modules, check their status, and ensure that the project is in sync with its dependencies.

## Features

- **Status Check**: Quickly view the status of all modules, including whether they are up-to-date, ahead, behind, or have local modifications.
- **Module Update**: Automatically update all modules to their latest versions, and clone any missing modules.
- **Colored Output**: Easy-to-read status updates with colored output indicating the status of each module.

## Installation

Before using GitProject, ensure you have Python installed on your system. Then, install the required dependencies:

```bash
pip install gitpython termcolor
```
Configuration
-------------

Create a `.projectenv` JSON configuration file in your project directory with the following structure:

```
{
    "name": "Your Project Name",
    "modules": [
        {
            "name": "ModuleName",
            "path": "path/to/module",
            "url": "https://repository.url",
            "branch": "branch_name"  // optional, defaults to 'master'
        },
        // Add more modules as needed
    ]
}

```
Usage
-----

### Status Mode

To check the status of all configured modules:

`gitproject --status`

This will display the status of each module with colored indicators.

### Update Mode

To update all modules:

`gitproject --update`

This will update each module to the latest commit on the specified branch or clone it if it's not present.
