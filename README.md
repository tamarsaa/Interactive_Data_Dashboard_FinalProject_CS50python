# Interactive Data Dashboard

#### https://youtu.be/RdP_P7Ka9P0

### Introduction
This project is an interactive data dashboard built using Dash, Plotly, and Pandas. The application allows users to upload CSV files, visualize the data in a table, and create bar charts based on selected columns. The dashboard also features an undo button to reset the data to its original state. This tool aims to simplify data analysis tasks and make it accessible even to those without technical expertise.

### Motivation
As someone interested in making data analysis accessible to everyone, I developed this tool to help users gain insights from their data without needing extensive technical knowledge. This project was a valuable learning experience, allowing me to delve into Dash app development and data handling. By working on this project, I aimed to bridge the gap between raw data and meaningful visualizations, providing users with a straightforward interface to interact with their data.

### Project Structure

- **project.py**: Contains the main application logic.
  - main(): Starts the Dash server.
  - create_dash_app(): Sets up the app layout and stylesheets.
  - register_callbacks(app): Registers the data handling and chart update callbacks.
  - update_output(contents, filename, n_clicks, current_data): Handles file upload and data updates.
  - update_bar_chart(x_col, y_col, table_data): Updates the bar chart based on user selections.

- **test_project.py**: Contains pytest tests for core functions.
  - test_create_dash_app(): Tests app creation.
  - test_update_output(): Tests file upload handling.
  - test_update_output_with_data(): Tests with sample data.
  - test_update_bar_chart(): Tests bar chart updates.
  - test_update_bar_chart_with_data(): Tests with sample table data.

### Problems and Solutions

1. **Testing Callback Functions**:
   - **Problem**: Callback functions are not directly callable.
   - **Solution**: Exported these functions for testing and used pytest-dash for Selenium setup, which required careful configuration and troubleshooting.

2. **Data Upload Handling**:
   - **Problem**: Decoding and handling CSV content.
   - **Solution**: Implemented base64 decoding and error handling to ensure robustness and user-friendly error messages.

3. **Plotly Bar Chart**:
   - **Problem**: Ensuring chart updates with user input.
   - **Solution**: Verified DataFrame creation and column selection to dynamically generate accurate and visually appealing charts.

### Personal Experience
Testing the Dash app with pytest was challenging due to the Selenium setup required in a third-party environment. Overcoming these hurdles taught me a lot about integrating and testing web applications. With the help of Duck AI, I managed to troubleshoot the issues effectively. I am proud of creating a tool that simplifies data visualization and enhances accessibility. This project also helped me understand the nuances of user interface design and the importance of creating intuitive tools.

### Dependencies
To run this project, you need:
- dash
- pandas
- plotly
- pytest
- selenium

Install them using:
# pip install -r requirements.txt


### How to Run

1. Clone the repository.
2. Install the dependencies.
3. Run the application using the command:
   # python project.py


### How to Test

1. Set Up Virtual Environment:
I highly recommend setting up a virtual environment (venv) for testing. This makes sure that the testing environment is isolated, so dependencies like Selenium can be managed properly without messing with your global Python environment. Using a virtual environment also helps in smoothly running tests with pytest and ensures that the correct web driver for Dash applications is used, without needing to install a bunch of other dependencies.
2. To create and activate a virtual environment:
  # python -m venv venv
  # source venv/bin/activate
  On Windows use:
  # venv\Scripts\activate

3. Install Dependencies:
 -Make sure all the dependencies are installed within your virtual environment:
  # pip install -r requirements.txt

4. Run tests:
  # pytest test_project.py

### Future Improvements
Looking ahead, I plan to add more visualization options and enhance user interaction features based on feedback. Integrating more sophisticated error handling and user guidance are also on my list. I also aim to explore additional chart types, such as line and scatter plots, to provide users with a wider range of data visualization tools. Enhancing the dashboard's aesthetics with custom themes and improving performance with larger datasets are other potential areas for development.
