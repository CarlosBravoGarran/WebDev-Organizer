# Web File Organizer

## Description
WebDev-Organizer is a tool designed to help web developers automatically organize their project files and directories. This Python script categorizes files by type and extension or by section of work, moving them to specific directories to improve management and accessibility.

## Features
- **Automatic Organization**: Classifies files by extension or section.
- **Support for Multiple File Types**: Handles JavaScript, CSS, images, fonts, and HTML documents.
- **Empty Directories Removal**: Cleans up directory structures by removing empty folders after reorganization.
- **Interactive User Interface**: Allows choosing between organization modes through a console menu.

## Prerequisites
Ensure you have Python 3.x installed on your device.

## Installation
Clone this repository to your local device using one of the following methods:
```bash
git clone https://github.com/CarlosBravoGarran/WebDev-Organizer.git  # HTTPS
git clone git@github.com:CarlosBravoGarran/WebDev-Organizer.git      # SSH
```

## Usage
To run the script, navigate to the repository directory and execute:
```bash
python file_organize.py <source_directory>
```
Where `<source_directory>` is the path to the directory containing your project files.

### Organization Methods
1. **By Extension**: Organizes files based on file extension.
2. **By Section**: Organizes files based on a user-determined function
   - For this, files of the same section must have the same name (home.html, home.css, home.js).

## Example of Use

Suppose you have a project directory with the following structure:

  ```
  my_project/
  ├── index.html
  ├── contact.html
  ├── about.html
  ├── contact.css
  ├── home.js
  ├── about.css
  ├── home.css
  └── logo.png
  ```

To automatically organize these files using the **Web File Organizer**, follow these steps:

1. Open a terminal or command line.
2. Navigate to the directory where you downloaded or cloned the repository.
3. Run the script by providing the path to your project directory:

   ```bash
   python file_organize.py /path/to/my_project
   ```

   An interactive menu will appear allowing you to select the organization method:

   ```
   Select an organization method:
   1. By extension
   2. By function
   Enter your choice (1 or 2): 
   ```

4. If you choose **1. By Extension**, the script will move the files to directories based on their extension, resulting in an organized structure like this:

   ```
   my_project/
   ├── images/
   │   └── logo.png
   ├── scripts/
   │   └── home.js
   ├── styles/
   │   ├── contact.css
   │   ├── home.css
   │   └── about.css
   ├── html/
   │   ├── contact.html
   │   └── about.html
   └── index.html
   ```

5. If you choose **2. By Section**, and your section files are correctly named, the script will organize them into directories based on their section or function.
  
  ```
     my_project/
     ├── images/
     │   └── logo.png
     ├── home/
     │   ├── home.css
     │   └── home.js
     ├── about/
     │   ├── about.html
     │   └── about.css
     ├── html/
     │   ├── contact.html
     │   └── contact.css
     └── index.html
  ```
