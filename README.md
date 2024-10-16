# NehaAuchar

This is a demo project to demonstrate the implementation of the Selenium with Python.

## Description

This project includes automated tests for a banking application using Selenium WebDriver. The tests are written in Python and use the Behave framework for BDD (Behavior-Driven Development).

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/NehaAuchar/demo-project.git
    cd demo-project
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

## Usage

3. **Run the tests**:
    ```sh
    behave

[//]: # (   To generate html report)
    behave -f behave_html_formatter:HTMLFormatter -o behave_report.html 
    Or

[//]: # (    To generate json report)
    behave --format=json --outfile=test_report.json 
   


2. **View the test results**:
   The test results will be displayed in the terminal.


