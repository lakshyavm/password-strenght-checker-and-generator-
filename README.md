# Password Vault & Strength Analyzer (Python, No External Libraries)

## Overview

This is a simple, human-friendly, *console-based Password Vault and Password Strength Analyzer* written in pure Python (no advanced libraries required). It helps users securely store, manage, and analyze passwords according to modern security standards.

*Main features:*
- *Add new credentials* (username + password)
- *View* all saved credentials
- *Delete* credentials  
- *Analyze* password strength according to industry best practices (min 12 chars, mixed case, digit, and symbol, not a dictionary word or common pattern)
- *Generate* a strong, standards-compliant password for any user

## Usage

1. *Run the script:*  
   Open your terminal and run:
   
   python password_vault.py
   
2. *Choose an Option:*  
   The menu will display these choices:
   - Add new credential (with an option to auto-generate a strong password)
   - View all credentials
   - Delete a credential
   - Check password strength
   - Generate a strong password only
   - Exit the program

3. *Store or review your credentials.*  
   Your passwords are never shown unless you select 'View'.

4. *Generate a password:*  
   The program can create complex, random passwords meeting all standards with a single choice.

## Why use this?

- *No advanced setup.* Pure Python, cross-platform—run on any machine with Python 3.x.
- *Modern password standards:*  Requires minimum 12-character passwords with uppercase, lowercase, number, and special character, and blocks common/personal patterns.
- *Educational:*  Learn how basic password vaults and generators work, and see the importance of password complexity.

## ⚠ Limitations

- Passwords and credentials are stored only *in memory* (not on disk), so nothing is saved after you close the program.
- This is a teaching and demo project! *Never use for real password management*. For production, use professional managers with secure encryption and persistent storage.

## Example Screenshot


----- Secure Password Vault -----
1. Add new credential
2. View all credentials
3. Delete a credential
4. Check password strength
5. Generate a strong password
6. Exit
Pick an option (1-6): 


## Contributing

Pull requests and improvements welcome! Please open an issue for bugs or suggestions.

## License

MIT License (see LICENSE file)

*Enjoy strong, safe passwords!*

