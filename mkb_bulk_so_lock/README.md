# Bulk Lock Sales Orders

Lock multiple confirmed Sales Orders in one go from the Sales Orders list view.

---

## Features

- Adds an **Action ▸ Lock Sales Orders** option in the Sales Orders list view.
- Select several confirmed orders at once and lock them in bulk.
- Respects standard Odoo access rights and workflow.

---

## Compatibility

- Odoo: 19.0

---

## Dependencies

- `sale`
- `sale_management`

---

## Installation

1. Copy this module into your Odoo `addons` path.
2. Update the app list: **Apps ▸ Update Apps List**.
3. Install **Bulk Lock Sales Orders**.

---

## Usage

1. Go to **Sales ▸ Orders**.
2. Switch to the **list** (tree) view.
3. Select the confirmed Sales Orders you want to lock.
4. Click **Action ▸ Lock Sales Orders**.
5. The selected Sales Orders will be locked immediately.

> Notes:
> - Only orders in the **Confirmed** state will be locked.
> - Orders already locked remain unchanged.
> - Standard Odoo permissions apply.

---

## Access Rights

- Users need Sales Orders access rights (`sale_user` or above).
- The bulk action is only available for users allowed to lock orders individually.

---

## Known Limitations

- Quotations or already locked orders are skipped.
- Custom workflows or third-party modules may alter behavior.

---

## Support & Issues

If you encounter problems or want enhancements, please open an issue or contact the developer.

---

## Author

- **Manish Kumar Bohra**

## Developer

- **Manish Kumar Bohra** — <manishkumarbohra@outlook.com>

---
