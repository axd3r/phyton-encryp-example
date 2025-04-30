
# PBKDF2-SHA256 Hash Generator

This project provides a simple tool to generate a secure password hash using the **PBKDF2-SHA256** algorithm. This algorithm is widely used for password protection and is the same one used by Django for password storage.

## Author
[Joaquin Orihuela](https://www.linkedin.com/in/joaquin-orihuela-liberato-405019304/)

## Requirements

- Python 3.x
- Python dependencies (see below)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/axd3r/phyton-encryp-example.git
   ```

2. Navigate to the project directory:

   ```bash
   cd phyton-encryp-example
   ```

3. Create and activate a virtual environment to manage dependencies (optional but recommended):

   - On Unix/macOS systems:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - On Windows systems:

     ```bash
     python -m venv venv
     .env\Scripts\ctivate
     ```

4. Install the project dependencies (if any):

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To generate a password hash, simply run the `generate_hash.py` script:

```bash
python generate_hash.py
```

The program will ask you to input a password, and it will generate a hash in the format:

```
pbkdf2_sha256$<iterations>$<salt_base64>$<hash_base64>
```

This is the format used by Django to store passwords.

### Example

If you enter a password like `my_secret_password`, the result could look like this:

```
pbkdf2_sha256$320000$4e5f3ae718a8691e8ab63efb$2dedc8049c6757a152940bc94cc57987d39109e62cbf30d14596ba03a95c923a
```

This hash can be used directly in applications like Django to authenticate users.

## Notes

- This generator uses a default iteration count of 320,000, which is secure and provides a good balance between security and performance.
- You can modify the iteration count if you wish, but it's recommended not to use a too-low number.

## License

This project is licensed under the **Python Software Foundation License**.

## Contributions

If you have any improvements or fixes, please create a **pull request**.
