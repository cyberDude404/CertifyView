# CertifyView

CertifyView is a Python-based program that provides the following features:
- Fetches and displays SSL certificate details for any website.
- Generates dynamic ASCII art with a colorful output.
- Handles graceful exits with a thank-you message when interrupted.

## Features
- **SSL Certificate Info**: Displays IP, Issuer, and Validity Dates of the SSL certificate.
- **ASCII Art**: Generates dynamic ASCII art that adapts. to terminal width.
- **Colorful Output**: Uses the `Colorama` library for enhanced visual representation.
- **Graceful Exit**: Handles `Ctrl+C` interruptions and exits cleanly with a thank-you message.

---

## Getting Started

### Prerequisites
To run this program, you need:
- Python 3.6 or higher installed on your system.
- The following Python libraries:
  - `pyfiglet`
  - `colorama`

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/cyberDude404/CertifyView.git
   cd CertifyView
   ```

2. **Install Dependencies**:
   Ensure you have `pip` installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the program by executing the following command:
   ```bash
   python certifyview.py
   ```
2. Enter a website address (e.g., `www.example.com`).
3. View the colorful SSL certificate information.
4. Press `Ctrl+C` to exit the program gracefully.

---


## Notes
- Ensure you have an active internet connection to fetch SSL certificate details.
- The program is tested on both Linux and Windows platforms.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing
Contributions are welcome! Feel free to open issues or create pull requests to improve this project.

---

## Author
Developed by [cyberDude](https://github.com/cyberDude404).

