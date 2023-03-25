# Customer Invoicing System Automation

This project is designed to automate the process of adding customer invoices to the government system. The system uses Selenium, an open-source web automation tool, to extract data from an XML file and input it into the government's invoicing system.

The project was initially created for my aunt who is a tax consultant and is now being used by her to streamline her invoicing process.

## Project Structure

The project consists of three main components:

1. **anasayfa.py**: This file just main page.

2. **genelayarlar.py**: This file contains all the necessary settings for the automation process. This includes login credentials, URLs, and other configuration options.

3. **mypage.py**: This is a sample XML file that contains the invoice data. The automation process reads the data from this file and enters it into the government system.

## How to Use

To use this automation tool, follow these steps:

1. Clone the project from GitHub
2. Install the necessary dependencies by running `pip install -r requirements.txt`
3. Modify the settings in `genelayarlar.py` file according to your needs
4. Place the XML file containing the invoice data in the project directory
5. Run the `main.py` file

The automation process will start and automatically add the customer invoices to the government system.

## Disclaimer

This project is intended for educational purposes only. It is not intended for any illegal activities or purposes. The user of this automation tool is responsible for complying with all laws and regulations governing the use of the government system. 

## Screenshots

Screenshots of the project can be found in the `preview` directory. These screenshots show the automation process in action, including navigating to the government system, entering data, and submitting the invoice.

## Conclusion

This automation tool simplifies the process of adding customer invoices to the government system. It saves time and effort, and can be easily customized to meet the specific needs of the user.
