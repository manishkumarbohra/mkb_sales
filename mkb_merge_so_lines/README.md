# Merge Duplicate Sales Order Lines

This module adds a button on the Sales Order form to automatically merge duplicate sales order lines into a single line.

---

## Features

- Adds a **Merge Duplicate SO Lines** button in the Sales Order form header.
- Automatically merges duplicate lines that have:
  - The same **Product**
  - The same **Unit Price**
  - The same **Taxes**
- The quantities of duplicate lines are summed into a single line.
- Available only when the Sales Order is in **Draft** state.

---

## Compatibility

- Odoo: 19.0

---

## Dependencies

- `sale`
- `sale_management`

---

## Installation

1. Copy this module into your Odoo `addons` directory.
2. Update the Apps list from **Apps ▸ Update Apps List**.
3. Search for **Merge Duplicate Sales Order Lines** and install it.

---

## Usage

1. Navigate to **Sales ▸ Orders**.
2. Open any Sales Order in **Draft** state.
3. Click the **Merge Duplicate SO Lines** button in the form header.
4. Duplicate lines will be merged automatically, and quantities will be updated.

> **Notes**  
> - Only duplicates (same product, price, and taxes) are merged.  
> - The action is available only in Draft quotations.  
> - If no duplicates are found, the order remains unchanged.  

---

## Access Rights

- Available to any user with access to Sales Orders (`sale_user` or higher).  

---

## Known Limitations

- Does not consider differences in **UoM** (Unit of Measure). If the same product is entered with different UoMs, lines will not merge.  
- Custom workflows or third-party modules may override default line handling.  

---

## Changelog

### v1.0.0
- Initial release: Added button to merge duplicate Sales Order lines.  

---

## Author

- **Manish Kumar Bohra**

## Developer

- **Manish Kumar Bohra** — <manishkumarbohra@outlook.com>
