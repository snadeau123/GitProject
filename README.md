# GitProject

GitProject, a Python tool, enhances the management and synchronization of multiple Git repositories in projects with actively developed modules. It automates the update process, replacing the manual efforts required by traditional Git submodules. This automation ensures that projects consistently integrate the latest changes, making it ideal for projects evolving rapidly or decomposing into independently developed components.

## Features

- **Status Check**: Quickly view the status of all modules, including whether they are up-to-date, ahead, behind, or have local modifications.
- **Module Update**: Automatically update all modules to their latest versions, and clone any missing modules, with minimal manual intervention.
- **Colored Output**: Easy-to-read status updates with colored output indicating the status of each module, enhancing the overall user experience.


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


### GitIgnore Update

To update the `.gitignore` file with the paths of all modules:

`gitproject --gitignore`

This will add the paths of the modules to the `.gitignore` file, ensuring they are not tracked by the main project's Git repository.



