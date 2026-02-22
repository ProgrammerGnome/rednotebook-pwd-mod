# RedNotebook - modded version

RedNotebook is a modern desktop journal. It lets you format, tag and
search your entries. You can also add pictures, links and customizable
templates, spell check your notes, and export to plain text, HTML,
Latex or PDF.


## FORK FEATURES — Custom Enhancements

This fork introduces true cryptographic data protection, moving beyond the default plain-text storage of standard RedNotebook. It is built for users who require strict privacy and mathematical security for their journal entries, prioritizing data integrity over convenience.

* **AES-256-GCM Encryption:** All journal entries are encrypted on-the-fly before being written to the disk. The default readable YAML plain-text format has been completely replaced with authenticated ciphertext.
* **Scrypt Key Derivation:** A robust Key Derivation Function (KDF) generates the 256-bit encryption key from the user's password. It utilizes a dynamically generated, locally stored salt (`crypto.salt`) to neutralize rainbow table and dictionary attacks.
* **Startup GUI Authentication:** A GTK dialog intercepts the boot sequence, requiring the decryption password before any journal files are accessed or loaded into memory.
* **Zero-Knowledge Execution:** The password and the derived AES key exist strictly within volatile memory (RAM) during runtime. They are never written to disk, logged, or cached.
* **Tamper Detection & Fail-Safe:** Utilizing the authentication tag inherent to GCM, the application mathematically verifies data integrity. If an incorrect password is provided or if the files have been externally modified, the program forces an immediate halt (`sys.exit(1)`) to prevent data corruption.

> **⚠️ CRITICAL WARNING:** This system operates without a safety net. There is no "forgot password" backdoor or recovery mechanism. If the password is lost, all journal data becomes permanently mathematically inaccessible.


## Requirements

Needed for running RedNotebook:

  * GTK (3.24): https://www.gtk.org
  * GtkSourceView (3.0+): https://wiki.gnome.org/Projects/GtkSourceView
  * Python (3.8+): https://www.python.org
  * PyYAML (3.10+): https://pyyaml.org
  * Cryptography (46.0.5): https://pypi.org/project/cryptography
  * WebKitGTK (2.16+): https://webkitgtk.org (only on Linux and macOS)
  * PyEnchant for spell checking (1.6+): https://pypi.org/project/pyenchant/ (optional)

Needed for installing RedNotebook:

  * GNU gettext: https://www.gnu.org/software/gettext
  * Setuptools (60.0+): https://pypi.org/project/setuptools


## Run from source

Install all dependencies:

  * Linux/macOS: [run-tests.yml](.github/workflows/run-tests.yml)
  * Windows: [build-windows.yml](.github/workflows/build-windows.yml)

Start RedNotebook:

  * Linux/macOS: `python3 rednotebook/journal.py`
  * Windows: `py rednotebook/journal.py`

Enjoy!
